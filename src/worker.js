// Core Material JSC — Worker định tuyến + API form liên hệ
//  - corematerial.info (và www) -> public/info/ (site Insights)
//  - corematerial.vn -> 301 về www.corematerial.vn (địa chỉ chính)
//  - POST /api/lien-he -> nhận yêu cầu tư vấn
//
// Cấu hình form (Cloudflare dashboard > Worker > Settings), đều TÙY CHỌN:
//  - KV binding  LEADS          : lưu mọi yêu cầu (khuyến nghị bật)
//  - Email binding MAILER       : gửi email báo (cần Email Routing + địa chỉ nhận đã xác minh)
//      biến MAIL_FROM (vd form@corematerial.vn), MAIL_TO (vd info@corematerial.vn)
//  - Secret TURNSTILE_SECRET    : chống spam Cloudflare Turnstile (đi kèm site key trong trang)
// Nếu chưa có KV lẫn MAILER, API trả "not_configured" và trang KHÔNG báo gửi thành công.

const MAIN_HOST = "www.corematerial.vn";

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const host = url.hostname.toLowerCase();

    if (host === "www.corematerial.info") {
      url.hostname = "corematerial.info";
      return Response.redirect(url.toString(), 301);
    }
    if (host === "corematerial.vn") {
      url.hostname = MAIN_HOST;
      return Response.redirect(url.toString(), 301);
    }
    const isInfo = host === "corematerial.info";

    if (!isInfo && url.pathname === "/api/lien-he") {
      if (request.method !== "POST") return json({ ok: false, error: "method" }, 405);
      return handleLead(request, env);
    }

    let path = url.pathname;
    if (isInfo) {
      path = "/info" + path;
    } else if (path === "/info" || path.startsWith("/info/")) {
      const target = new URL(path.replace(/^\/info/, "") || "/", "https://corematerial.info");
      target.search = url.search;
      return Response.redirect(target.toString(), 301);
    }

    if (path.endsWith("/")) path += "index.html";
    let res = await asset(env, request, url, path);

    if (res.status === 404 && !/\.[a-z0-9]+$/i.test(path)) {
      // /vat-lieu -> /vat-lieu/ ; /bai-viet/x -> x.html
      const dir = await asset(env, request, url, path + "/index.html");
      if (dir.ok) { url.pathname = url.pathname + "/"; return Response.redirect(url.toString(), 301); }
      const alt = await asset(env, request, url, path + ".html");
      if (alt.ok) res = alt;
    }
    if (res.status === 404) {
      const nf = await asset(env, request, url, isInfo ? "/info/index.html" : "/404.html");
      if (nf.ok) return new Response(nf.body, { status: 404, headers: nf.headers });
    }
    return res;
  },
};

function asset(env, request, url, path) {
  const u = new URL(url); u.pathname = path; u.search = "";
  return env.ASSETS.fetch(new Request(u, { method: "GET", headers: request.headers }));
}

function json(obj, status = 200) {
  return new Response(JSON.stringify(obj), { status, headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store" } });
}

const clip = (v, n) => String(v ?? "").replace(/[\u0000-\u0008\u000B\u000C\u000E-\u001F]/g, "").trim().slice(0, n);

async function handleLead(request, env) {
  const len = Number(request.headers.get("content-length") || 0);
  if (len > 20000) return json({ ok: false, error: "too_large" }, 413);
  let d;
  try { d = await request.json(); } catch { return json({ ok: false, error: "bad_request" }, 400); }

  // Bẫy bot: ô ẩn có dữ liệu hoặc gửi quá nhanh -> giả vờ thành công, không lưu
  if (clip(d.website, 200) || Number(d.t) < 2500) return json({ ok: true, id: "OK" });

  const lead = {
    nhom: (Array.isArray(d.nhom) ? d.nhom : []).map((x) => clip(x, 60)).slice(0, 12),
    ten: clip(d.ten, 100), cty: clip(d.cty, 150), sdt: clip(d.sdt, 20), email: clip(d.email, 150),
    sanluong: clip(d.sanluong, 50), ungdung: clip(d.ungdung, 200), nangsuat: clip(d.nangsuat, 100),
    diadiem: clip(d.diadiem, 150), noidung: clip(d.noidung, 3000),
  };
  if (!lead.nhom.length || !lead.ten || !/^[0-9+().\s-]{8,20}$/.test(lead.sdt)) return json({ ok: false, error: "invalid" }, 400);

  if (!env.LEADS && !env.MAILER) return json({ ok: false, error: "not_configured" }, 503);

  if (env.TURNSTILE_SECRET) {
    const fd = new FormData();
    fd.append("secret", env.TURNSTILE_SECRET);
    fd.append("response", clip(d["cf-turnstile-response"], 2048));
    fd.append("remoteip", request.headers.get("CF-Connecting-IP") || "");
    const v = await fetch("https://challenges.cloudflare.com/turnstile/v0/siteverify", { method: "POST", body: fd }).then((r) => r.json()).catch(() => ({}));
    if (!v.success) return json({ ok: false, error: "captcha" }, 400);
  }

  const now = new Date();
  const id = "CM" + now.toISOString().slice(2, 10).replace(/-/g, "") + "-" + crypto.randomUUID().slice(0, 6).toUpperCase();
  const record = { id, at: now.toISOString(), ip: request.headers.get("CF-Connecting-IP") || "", ua: clip(request.headers.get("user-agent"), 200), ...lead };

  let stored = false, mailed = false;
  if (env.LEADS) {
    try { await env.LEADS.put(`lead:${record.at}:${id}`, JSON.stringify(record)); stored = true; } catch (e) { console.error("KV", e); }
  }
  if (env.MAILER && env.MAIL_FROM && env.MAIL_TO) {
    try { await sendMail(env, record); mailed = true; } catch (e) { console.error("MAIL", e); }
  }
  if (!stored && !mailed) return json({ ok: false, error: "delivery_failed" }, 502);
  return json({ ok: true, id, stored, mailed });
}

async function sendMail(env, r) {
  const { EmailMessage } = await import("cloudflare:email");
  const lines = [
    `Mã yêu cầu: ${r.id}`, `Thời gian: ${r.at}`, "",
    `Nhóm quan tâm: ${r.nhom.join(", ")}`, `Họ tên: ${r.ten}`, `Công ty: ${r.cty}`, `Điện thoại: ${r.sdt}`, `Email: ${r.email}`,
    r.sanluong && `Sản lượng/tháng: ${r.sanluong}`, r.ungdung && `Ứng dụng thiết bị: ${r.ungdung}`,
    r.nangsuat && `Năng suất mong muốn: ${r.nangsuat}`, r.diadiem && `Địa điểm: ${r.diadiem}`,
    "", "Nội dung:", r.noidung || "(không có)",
  ].filter((x) => x !== false && x !== undefined && x !== "").join("\r\n");
  const b64 = (s) => btoa(String.fromCharCode(...new TextEncoder().encode(s)));
  const subject = `=?UTF-8?B?${b64(`[Website] Yêu cầu tư vấn – ${r.ten} – ${r.nhom.join(", ")}`.slice(0, 180))}?=`;
  const body = b64(lines).replace(/.{1,76}/g, "$&\r\n");
  const raw = [
    `From: Website Core Material <${env.MAIL_FROM}>`, `To: <${env.MAIL_TO}>`,
    r.email ? `Reply-To: <${r.email.replace(/[<>\r\n]/g, "")}>` : null,
    `Subject: ${subject}`, `Message-ID: <${r.id}@corematerial.vn>`, `Date: ${new Date(r.at).toUTCString()}`,
    "MIME-Version: 1.0", "Content-Type: text/plain; charset=UTF-8", "Content-Transfer-Encoding: base64", "", body,
  ].filter(Boolean).join("\r\n");
  await env.MAILER.send(new EmailMessage(env.MAIL_FROM, env.MAIL_TO, raw));
}
