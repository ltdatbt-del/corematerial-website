# -*- coding: utf-8 -*-
"""Sinh website chính www.corematerial.vn vào public/.
  python3 tools/build_site.py            -> bản công khai
  PREVIEW=1 python3 tools/build_site.py  -> bản xem trước (hiện ô chờ ảnh/thông số)
"""
import os, sys, html, json
sys.path.insert(0, os.path.dirname(__file__))
from site_data import *

PREVIEW = os.environ.get("PREVIEW") == "1"
ROOT = os.path.join(os.path.dirname(__file__), "..", "public")
SITE = COMPANY["site"]
e = html.escape

MARK_SYMBOL = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true"><symbol id="cm" viewBox="44 22 487 568"><g stroke-linejoin="round" stroke-width="14"><polygon points="305,37 388,88 160,228 160,384 388,524 305,575 59,428 59,184" fill="currentColor" stroke="currentColor"/><polygon points="300,206 432,124 516,166 516,246 432,288" fill="#D4A835" stroke="#D4A835"/><polygon points="300,412 432,330 516,372 516,452 432,494" fill="#D4A835" stroke="#D4A835"/></g></symbol></svg>'''
ARROW = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 8h10M9 4l4 4-4 4"/></svg>'
IC = {
 "phone": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>',
 "mail": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm0 4-8 5-8-5V6l8 5 8-5z"/></svg>',
 "pin": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a7 7 0 0 0-7 7c0 5.25 7 13 7 13s7-7.75 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z"/></svg>',
 "doc": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8zm-1 7V3.5L18.5 9zM8 13h8v2H8zm0 4h8v2H8z"/></svg>',
}
MENU = [("/gioi-thieu/", "Giới thiệu"), ("/vat-lieu/", "Nguyên liệu & Vật liệu"), ("/may-moc/", "Máy móc & Tự động hóa"), ("/ung-dung/", "Ứng dụng & Video"), ("/lien-he/", "Liên hệ")]
TEL = "+84" + COMPANY["hotline"].replace(".", "")[1:]
DEFAULT_DESC = "Core Material JSC kết nối nguồn cung nguyên liệu, thiết bị và giải pháp công nghệ cho ngành vật liệu xây dựng: cát khô, xi măng trắng, phụ gia, vật liệu trang trí, thiết bị phun GRC, máy phun vữa và tự động hóa nhà máy."

def slot(text, cls=""):
    return f'<div class="ph-box {cls}">BẢN XEM TRƯỚC – Chờ bổ sung:<br>{e(text)}</div>' if PREVIEW else ""

def page(path, title, desc, body, active=None, og_img="/img/og-image.jpg", extra_head=""):
    canon = SITE + path
    nav = "".join(f'<a href="{u}"{" class=on" if active==u else ""}>{e(t)}</a>' for u,t in MENU)
    org = {"@context":"https://schema.org","@type":"Organization","name":COMPANY["brand"],"legalName":COMPANY["legal"].title().replace("Cổ Phần","Cổ phần"),
           "url":SITE,"logo":SITE+"/img/core-mark.svg","slogan":COMPANY["slogan"],"taxID":COMPANY["tax"],"telephone":TEL,"email":COMPANY["email"],
           "address":{"@type":"PostalAddress","streetAddress":"114bis Trần Quốc Toản, P. Xuân Hòa","addressLocality":"TP. Hồ Chí Minh","addressCountry":"VN"}}
    robots = '<meta name="robots" content="noindex, nofollow">' if PREVIEW else ""
    return f'''<!DOCTYPE html>
<html lang="vi"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">{robots}
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Core Material JSC"><meta property="og:locale" content="vi_VN">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE}{og_img}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/svg+xml" href="/img/core-mark.svg"><meta name="theme-color" content="#111111">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
<script type="application/ld+json">{json.dumps(org, ensure_ascii=False)}</script>{extra_head}
</head><body>
{MARK_SYMBOL}
<header class="site"><div class="wrap nav">
  <a href="/" class="logo" aria-label="Core Material JSC – Trang chủ"><svg class="mk"><use href="#cm"/></svg><span class="wm"><b>Core Material <span>JSC.</span></b><small>Building Values, Enriching Life</small></span></a>
  <nav class="menu" id="menu">{nav}</nav>
  <a href="/lien-he/" class="btn btn-dark">Liên hệ tư vấn</a>
  <button class="burger" aria-label="Mở menu" aria-controls="menu" onclick="document.getElementById('menu').classList.toggle('open')"><span></span><span></span><span></span></button>
</div></header>
<main>
{body}
</main>
{footer()}
<a class="float-call" href="tel:{TEL}">{IC["phone"].replace('<svg','<svg width=16 height=16')} Gọi {COMPANY["hotline"]}</a>
</body></html>'''

def footer():
    mats = "".join(f'<li><a href="/vat-lieu/#{m["id"]}">{e(m["short"])}</a></li>' for m in MATERIALS)
    eqs = "".join(f'<li><a href="/may-moc/{q["id"]}/">{e(q["name"])}</a></li>' for q in EQUIPMENT)
    return f'''<footer><div class="wrap">
<div class="foot">
 <div><div class="logo"><svg class="mk" style="color:#fff;width:32px;height:38px"><use href="#cm"/></svg><span class="wm"><b>Core Material <span>JSC.</span></b><small>Building Values, Enriching Life</small></span></div>
  <p>{e(COMPANY["legal"])}<br>MST: {COMPANY["tax"]}</p>
  <p style="margin-top:10px">{e(COMPANY["address"])}<br><a href="tel:{TEL}">{COMPANY["hotline"]}</a> · <a href="mailto:{COMPANY["email"]}">{COMPANY["email"]}</a></p></div>
 <div><h6>Nguyên liệu & Vật liệu</h6><ul>{mats}</ul></div>
 <div><h6>Máy móc & Tự động hóa</h6><ul>{eqs}</ul></div>
 <div><h6>Công ty</h6><ul><li><a href="/gioi-thieu/">Giới thiệu</a></li><li><a href="/ung-dung/">Ứng dụng & Video</a></li><li><a href="/hop-tac-dau-tu/">Hợp tác đầu tư</a></li><li><a href="https://corematerial.info">Kiến thức vật liệu (Insights)</a></li><li><a href="/lien-he/">Liên hệ</a></li></ul></div>
</div>
<div class="copy"><span>© 2026 {e(COMPANY["brand"])}. Bảo lưu mọi quyền.</span><span class="v">INTEGRITY · INNOVATION · PARTNERSHIP</span></div>
</div></footer>'''

def phead(crumbs, title, sub):
    c = " / ".join(f'<a href="{u}">{e(t)}</a>' if u else e(t) for u,t in crumbs)
    return f'<section class="phead"><div class="wrap"><div class="crumb">{c}</div><span class="tag">{e(crumbs[-1][1])}</span><h1>{e(title)}</h1><p>{e(sub)}</p></div></section>'

def cta(text="Cần tư vấn vật liệu hoặc thiết bị?", sub="Đội ngũ Core Material tiếp nhận nhu cầu và phản hồi qua điện thoại hoặc email.", link="/lien-he/", label="Liên hệ tư vấn"):
    return f'<section style="padding-top:0"><div class="wrap"><div class="cta"><div><h2>{e(text)}</h2><p>{e(sub)}</p></div><div style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn btn-gold" href="{link}">{e(label)} {ARROW}</a><a class="btn btn-line" style="color:#fff" href="tel:{TEL}">Gọi {COMPANY["hotline"]}</a></div></div></div></section>'

def hexph():
    return '<div class="ph hex"><svg style="color:#fff"><use href="#cm"/></svg></div>'

def card(href, img, k, title, text, more="Xem chi tiết", pledge=None):
    ph = f'<div class="ph" style="background-image:url({img})" role="img" aria-label="{e(title)}"></div>' if img else hexph()
    pl = f'<span class="pledge">{" · ".join(p for p,_ in pledge)}</span>' if pledge else ""
    return f'<a class="card" href="{href}">{ph}<div class="tx"><span class="k">{e(k)}</span><h3>{e(title)}</h3><p>{e(text)}</p>{pl}<span class="more">{e(more)} {ARROW}</span></div></a>'

def vcard(v):
    src, poster, t, s = v
    return f'<div class="vcard"><video controls preload="none" playsinline poster="/{poster}"><source src="/{src}" type="video/mp4"></video><div class="tx"><h4>{e(t)}</h4><p>{e(s)}</p></div></div>'

def steps(cls=""):
    st = "".join(f'<div class="step"><div class="n">{i}</div><h4>{e(t)}</h4><p>{e(d)}</p></div>' for i,(t,d) in enumerate(PROCESS,1))
    return f'<div class="steps">{st}</div><p class="scope">{e(SCOPE_NOTE)}</p>'

def write(path, s):
    full = os.path.join(ROOT, path.strip("/"), "index.html") if path.endswith("/") else os.path.join(ROOT, path.strip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True); open(full, "w", encoding="utf-8").write(s)

def contact_href(group): return "/lien-he/?nhom=" + group.replace(" ", "+") + "#form"

# =================== TRANG CHỦ ===================
featured = [
  card("/vat-lieu/#cat-kho", "/"+MATERIALS[0]["img"], "Nguyên liệu", MATERIALS[0]["short"], "Cát silica sấy khô, sàng phân cỡ cho vữa khô, keo dán gạch và bê tông trang trí.", pledge=MATERIALS[0]["pledge"]),
  card("/vat-lieu/#xi-mang-trang", "/"+MATERIALS[1]["img"], "Nguyên liệu", "Xi măng trắng", "Cung cấp xi măng trắng cho sản xuất vật liệu và thi công, có COA theo lô.", pledge=MATERIALS[1]["pledge"]),
  card("/vat-lieu/#trang-tri", "/img/da-ho-phach.jpg", "Vật liệu trang trí", "Đá mài, hạt thủy tinh & bột màu", "Vật liệu cho terrazzo, bê tông nghệ thuật và hoàn thiện kiến trúc."),
] + [card(f"/may-moc/{q['id']}/", ("/"+q["img"]) if q["img"] else None, q["k"], q["name"], q["short"]) for q in EQUIPMENT]

home = f'''
<section class="hero"><div class="wrap">
 <div class="hero-in">
  <div>
   <span class="tag">Core Material JSC</span>
   <h1>Vật liệu. Thiết bị.<br><em>Giải pháp công nghệ.</em></h1>
   <p class="sub">Core Material kết nối nguồn cung nguyên liệu, thiết bị và giải pháp công nghệ cho ngành vật liệu xây dựng — từ sản xuất tại nhà máy đến thi công tại công trình.</p>
   <div class="hero-cta"><a href="/vat-lieu/" class="btn btn-gold">Khám phá vật liệu {ARROW}</a><a href="/may-moc/" class="btn btn-line">Khám phá thiết bị {ARROW}</a></div>
  </div>
  <div class="hero-media">
   <figure><img src="/img/san-pham/cat-hero.jpg" alt="Mẫu cát silica phân cỡ Core Material"><figcaption><b>Vật liệu</b> · Cát silica phân cỡ</figcaption></figure>
   <figure><img src="/img/thiet-bi/may-phun-vua-2.jpg" alt="Máy phun vữa tô tường"><figcaption><b>Thiết bị</b> · Máy phun vữa</figcaption></figure>
   <figure><img src="/media/video-phun-grc-poster.jpg" alt="Thiết bị phun GRC"><figcaption><b>Công nghệ</b> · Phun GRC</figcaption></figure>
  </div>
 </div>
 <div class="values" aria-label="Giá trị cốt lõi"><span>INTEGRITY</span><i></i><span>INNOVATION</span><i></i><span>PARTNERSHIP</span></div>
</div></section>

<section><div class="wrap">
 <span class="tag">Hai nhóm kinh doanh</span>
 <h2>Một đầu mối cho vật liệu và thiết bị</h2>
 <p class="lead">Từ nguyên liệu đầu vào cho nhà máy đến thiết bị cơ giới hóa và tự động hóa, Core Material giúp khách hàng chọn đúng giải pháp và kết nối nguồn cung phù hợp.</p>
 <div class="lines">
  <a class="line-card" href="/vat-lieu/"><img src="/img/san-pham/cat-so-3.jpg" alt=""><div class="tx"><span class="k">CORE TRADING · CORE MATERIALS</span><h3>Nguyên liệu & Vật liệu</h3><p>Cát khô, xi măng trắng, phụ gia VAE/RDP và vật liệu trang trí cho nhà sản xuất và nhà thầu.</p><ul><li>Cát khô</li><li>Xi măng trắng</li><li>VAE / RDP</li><li>Đá mài & hạt màu</li></ul><span class="more">Khám phá vật liệu {ARROW}</span></div></a>
  <a class="line-card" href="/may-moc/"><img src="/img/thiet-bi/may-phun-vua-5.jpg" alt=""><div class="tx"><span class="k">CORE TECHNOLOGY</span><h3>Máy móc & Tự động hóa</h3><p>{e(TECH_INTRO)}</p><ul><li>Phun GRC/GFRC</li><li>Phun vữa tô tường</li><li>Robot xếp pallet</li></ul><span class="more">Khám phá thiết bị {ARROW}</span></div></a>
 </div>
</div></section>

<section class="alt"><div class="wrap">
 <span class="tag">Sản phẩm & thiết bị trọng tâm</span>
 <h2>Danh mục nổi bật</h2>
 <div class="grid" style="margin-top:36px">{"".join(featured)}</div>
</div></section>

<section class="dark"><div class="wrap">
 <span class="tag">Ứng dụng & video</span>
 <h2>Thiết bị trong thực tế</h2>
 <p class="lead">Một số video thực tế về thiết bị phun GRC và máy phun vữa. Video và hình ảnh công trình tại Việt Nam sẽ được cập nhật thêm.</p>
 <div class="vgrid">{"".join(vcard(v) for v in EQUIPMENT[0]["videos"] + EQUIPMENT[1]["videos"])}</div>
 <p style="margin-top:26px"><a class="more" href="/ung-dung/">Xem thêm ứng dụng {ARROW}</a></p>
</div></section>

<section><div class="wrap">
 <span class="tag">Giá trị cốt lõi</span>
 <h2>Building Values, Enriching Life</h2>
 <div class="cv-grid">{"".join(f'<div class="cv-item"><span class="en">{a}</span><h3>{e(b)}</h3><p>{e(c)}</p></div>' for a,b,c in VALUES)}</div>
</div></section>

<section class="alt"><div class="wrap">
 <span class="tag">Cách Core đồng hành</span>
 <h2>Quy trình tư vấn và triển khai</h2>
 <p class="lead">Áp dụng cho các dự án thiết bị và giải pháp công nghệ.</p>
 {steps()}
</div></section>
''' + cta()
write("/", page("/", "Core Material JSC — Vật liệu, thiết bị & giải pháp công nghệ cho ngành vật liệu xây dựng", DEFAULT_DESC, home))

# =================== GIỚI THIỆU ===================
about = phead([("/", "Trang chủ"), (None, "Giới thiệu")], "Về Core Material JSC", "Kết nối nguyên liệu, thiết bị và giải pháp công nghệ cho ngành vật liệu xây dựng.") + f'''
<section><div class="wrap" style="max-width:900px">
 <p class="lead" style="max-width:none">Core Material JSC ({e(COMPANY["legal"].title().replace("Cổ Phần","Cổ phần"))}) tập trung vào thương mại nguyên liệu, vật liệu và thiết bị cho ngành vật liệu xây dựng. Chúng tôi làm việc cùng mạng lưới nhà cung cấp và đối tác kỹ thuật để giúp khách hàng chọn đúng vật liệu, đúng thiết bị cho nhu cầu sản xuất và thi công.</p>
</div></section>
<section class="alt"><div class="wrap">
 <span class="tag">Lĩnh vực hoạt động</span><h2>Ba hướng phát triển</h2>
 <div class="grid" style="margin-top:36px">
  <div class="card"><div class="tx"><span class="k">CORE TRADING</span><h3>Thương mại nguyên liệu</h3><p>Cát khô, xi măng trắng, nguyên liệu vật liệu xây dựng và hóa chất chọn lọc. Ưu tiên chất lượng ổn định, truy xuất được nguồn gốc theo lô.</p></div></div>
  <div class="card"><div class="tx"><span class="k">CORE TECHNOLOGY</span><h3>Thiết bị & giải pháp công nghệ</h3><p>Thiết bị phun GRC/GFRC, máy phun vữa, thiết bị xử lý nguyên liệu và tự động hóa — triển khai cùng các nhà cung cấp và đối tác kỹ thuật.</p></div></div>
  <div class="card"><div class="tx"><span class="k">CORE MATERIALS · ĐỊNH HƯỚNG</span><h3>Sản phẩm mang thương hiệu Core</h3><p>Phát triển dần các sản phẩm mang nhãn Core như cát phân cấp và vật liệu trang trí, với tiêu chuẩn chất lượng và truy xuất lô rõ ràng.</p></div></div>
 </div>
</div></section>
<section><div class="wrap">
 <span class="tag">Giá trị cốt lõi</span><h2>INTEGRITY · INNOVATION · PARTNERSHIP</h2>
 <div class="cv-grid">{"".join(f'<div class="cv-item"><span class="en">{a}</span><h3>{e(b)}</h3><p>{e(c)}</p></div>' for a,b,c in VALUES)}</div>
</div></section>
<section class="alt"><div class="wrap"><span class="tag">Đồng hành cùng khách hàng</span><h2>Quy trình tư vấn và triển khai</h2>{steps()}</div></section>
<section><div class="wrap" style="max-width:900px"><span class="tag">Thông tin doanh nghiệp</span><h2>Pháp nhân</h2>
 <table class="spec"><tr><th>Tên doanh nghiệp</th><td>{e(COMPANY["legal"])}</td></tr><tr><th>Tên thương hiệu</th><td>{e(COMPANY["brand"])}</td></tr><tr><th>Mã số thuế</th><td>{COMPANY["tax"]}</td></tr><tr><th>Địa chỉ</th><td>{e(COMPANY["address"])}</td></tr><tr><th>Hotline</th><td>{COMPANY["hotline"]}</td></tr><tr><th>Email</th><td>{COMPANY["email"]}</td></tr></table>
 <p style="color:var(--ink-3);font-size:14px">Thông tin về dự án đầu tư và hợp tác: xem trang <a class="more" style="font-size:14px" href="/hop-tac-dau-tu/">Hợp tác đầu tư</a>.</p>
</div></section>''' + cta()
write("/gioi-thieu/", page("/gioi-thieu/", "Giới thiệu | Core Material JSC", "Core Material JSC kết nối nguyên liệu, thiết bị và giải pháp công nghệ cho ngành vật liệu xây dựng tại Việt Nam.", about, "/gioi-thieu/"))

# =================== VẬT LIỆU ===================
blocks = []
for i, m in enumerate(MATERIALS):
    media = (f'<figure style="margin:0"><img src="/{m.get("img_full") or m["img"]}" alt="{e(m.get("img_caption") or m["name"])}" loading="lazy">' + (f'<figcaption style="font-size:12px;color:var(--ink-3);margin-top:6px">{e(m["img_caption"])}</figcaption>' if m.get("img_caption") else "") + '</figure>') if m.get("img") else (slot("Ảnh sản phẩm thật") or '<div class="ph hex" style="aspect-ratio:4/3;border-radius:3px"><svg style="color:#fff;width:90px;height:105px"><use href="#cm"/></svg></div>')
    pl = ""
    if m.get("pledge"):
        pl = '<div class="pl">' + "".join(f'<span>{a}<small>{e(b)}</small></span>' for a,b in m["pledge"]) + '</div>'
    grades = ""
    if m.get("grades"):
        grades = '<div class="grades">' + "".join(f'<figure><img src="/{im}" alt="Cát {e(n)} {e(r)}" loading="lazy"><figcaption><b>{e(n)}</b>{e(r)}</figcaption></figure>' for n,r,im in m["grades"]) + f'</div><p style="font-size:13px;color:var(--ink-3)">{e(m["grades_note"])}</p>'
    gal = ""
    if m.get("gallery"):
        gal = '<div class="gal" style="margin-top:16px">' + "".join(f'<figure><img src="/{im}" alt="{e(c)}" loading="lazy"><figcaption>{e(c)}</figcaption></figure>' for im,c in m["gallery"]) + '</div>'
    slots = "".join(slot(s) for s in m.get("slots", []))
    blocks.append(f'''<div class="pblock{" rev" if i%2 else ""}" id="{m["id"]}">
 <div class="pmedia">{media}{slots and '<div style="margin-top:10px;display:grid;gap:10px">'+slots+'</div>'}</div>
 <div><span class="tag">Nguyên liệu & Vật liệu</span><h2>{e(m["name"])}</h2>{pl}<p>{e(m["intro"])}</p>
  <ul class="chk">{"".join(f"<li>{e(p)}</li>" for p in m["points"])}</ul>{grades}
  <a class="btn btn-dark" href="{contact_href(m["form"])}">Yêu cầu báo giá {ARROW}</a>
 </div></div>{gal and '<div style="padding-bottom:40px">'+gal+'</div>'}''')
chips = '<div class="chips" style="margin-top:22px">' + "".join(f'<a href="#{m["id"]}">{e(m["short"])}</a>' for m in MATERIALS) + '</div>'
mat = phead([("/", "Trang chủ"), (None, "Nguyên liệu & Vật liệu")], "Nguyên liệu & Vật liệu", "Nguyên liệu cho nhà máy vật liệu xây dựng và vật liệu hoàn thiện cho công trình: cát khô, xi măng trắng, phụ gia và vật liệu trang trí.") + f'<section style="padding-top:40px"><div class="wrap">{chips}{"".join(blocks)}</div></section>' + cta("Cần mẫu hoặc báo giá vật liệu?", "Cho chúng tôi biết loại vật liệu, quy cách và sản lượng dự kiến.", "/lien-he/#form", "Gửi yêu cầu")
write("/vat-lieu/", page("/vat-lieu/", "Nguyên liệu & Vật liệu: cát khô, xi măng trắng, VAE/RDP, vật liệu trang trí | Core Material JSC", "Cát silica sấy khô phân cỡ, xi măng trắng, phụ gia VAE/RDP, đá mài, hạt thủy tinh và bột màu cho sản xuất vật liệu và thi công.", mat, "/vat-lieu/", "/img/san-pham/cat-hero.jpg"))

# =================== MÁY MÓC ===================
mm = phead([("/", "Trang chủ"), (None, "Máy móc & Tự động hóa")], "Core Technology — Máy móc & Tự động hóa", TECH_INTRO) + f'''
<section><div class="wrap">
 <span class="tag">Nhóm thiết bị trọng tâm</span><h2>Ba nhóm thiết bị</h2>
 <div class="grid" style="margin-top:36px">{"".join(card(f"/may-moc/{q['id']}/", ('/'+q['img']) if q['img'] else None, q['k'], q['name'], q['short']) for q in EQUIPMENT)}</div>
 <div class="note" style="margin-top:28px"><b>Phun GRC khác phun vữa tô tường thế nào?</b> Thiết bị phun GRC/GFRC dùng để sản xuất cấu kiện bê tông cốt sợi thủy tinh tại xưởng. Máy phun vữa tô tường dùng tại công trình để cơ giới hóa công tác trát tường.</div>
</div></section>
<section class="dark"><div class="wrap"><span class="tag">Quy trình</span><h2>Tư vấn và triển khai thiết bị</h2>{steps()}</div></section>
''' + cta("Trao đổi nhu cầu thiết bị", "Mô tả ứng dụng, năng suất mong muốn và địa điểm lắp đặt — chúng tôi sẽ cùng nhà cung cấp đề xuất cấu hình phù hợp.", "/lien-he/#form", "Trao đổi nhu cầu thiết bị")
write("/may-moc/", page("/may-moc/", "Máy móc & Tự động hóa: phun GRC, máy phun vữa, robot xếp pallet | Core Material JSC", "Thiết bị phun GRC/GFRC, máy phun vữa tô tường, robot bốc xếp & xếp pallet cho ngành vật liệu xây dựng — tư vấn, cung cấp qua mạng lưới nhà cung cấp.", mm, "/may-moc/", "/img/thiet-bi/may-phun-vua-2.jpg"))

for q in EQUIPMENT:
    media = f'<img src="/{q["img"]}" alt="{e(q["name"])}">' if q["img"] else (slot("Ảnh thiết bị thật có quyền sử dụng") or '<div class="ph hex" style="aspect-ratio:4/3;border-radius:3px"><svg style="color:#fff;width:90px;height:105px"><use href="#cm"/></svg></div>')
    thumbs = ('<div class="thumbs">' + "".join(f'<img src="/{g}" alt="" loading="lazy">' for g in q.get("gallery", [])) + '</div>') if q.get("gallery") else ""
    secs = "".join(f'<h3 style="font-size:18px;margin:22px 0 6px">{e(t)}</h3><ul class="chk">{"".join(f"<li>{e(x)}</li>" for x in xs)}</ul>' for t,xs in q["sections"])
    known = [(k,v) for k,v in q["spec"] if v]
    if PREVIEW:
        spec = '<table class="spec">' + "".join(f'<tr><th>{e(k)}</th><td class="{"" if v else "tbd"}">{e(v) if v else "Chờ catalogue / tài liệu xác nhận"}</td></tr>' for k,v in q["spec"]) + '</table>'
    elif known:
        spec = '<table class="spec">' + "".join(f'<tr><th>{e(k)}</th><td>{e(v)}</td></tr>' for k,v in known) + '</table>'
    else:
        spec = '<div class="note">Thông số kỹ thuật, cấu hình và catalogue được cung cấp theo nhu cầu cụ thể. Vui lòng liên hệ để nhận tài liệu.</div>'
    diff = f'<div class="note"><b>Lưu ý:</b> {e(q["diff"])}</div>' if q.get("diff") else ""
    pkg = ""
    if q.get("package"):
        pkg = f'<section class="alt"><div class="wrap"><span class="tag">Giải pháp đồng bộ</span><h2>Không chỉ là cái máy</h2><p class="lead">Máy phun vữa phát huy hiệu quả khi đi cùng vữa phù hợp, đội ngũ được đào tạo và quy trình vận hành chuẩn.</p><div class="grid g4" style="margin-top:32px">' + "".join(f'<div class="card"><div class="tx"><span class="k">0{i}</span><h3>{e(t)}</h3><p>{e(d)}</p></div></div>' for i,(t,d) in enumerate(q["package"],1)) + f'</div><p class="scope" style="color:var(--ink-3)">{e(SCOPE_NOTE)}</p></div></section>'
    vids = ""
    if q["videos"]:
        vids = f'<section class="dark"><div class="wrap"><span class="tag">Video</span><h2>Thiết bị hoạt động</h2><div class="vgrid">{"".join(vcard(v) for v in q["videos"])}</div></div></section>'
    elif PREVIEW:
        vids = f'<section><div class="wrap">{slot("Video thiết bị hoạt động")}</div></section>'
    slots = "".join(slot(s) for s in q.get("slots", []))
    body = phead([("/", "Trang chủ"), ("/may-moc/", "Máy móc & Tự động hóa"), (None, q["name"])], q["name"], q["short"]) + f'''
<section><div class="wrap"><div class="pblock" style="padding-top:0;border:0">
 <div class="pmedia">{media}{thumbs}{slots and '<div style="margin-top:10px;display:grid;gap:10px">'+slots+'</div>'}</div>
 <div><span class="tag">{e(q["k"])}</span>{"".join(f"<p>{e(p)}</p>" for p in q["intro"])}{diff}{secs}
  <h3 style="font-size:18px;margin:22px 0 6px">Thông số kỹ thuật</h3>{spec}
  <div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:8px"><a class="btn btn-dark" href="{contact_href(q["form"])}">Trao đổi nhu cầu thiết bị {ARROW}</a><a class="btn btn-line" href="/may-moc/">← Tất cả thiết bị</a></div>
 </div></div></div></section>{pkg}{vids}
<section class="paper"><div class="wrap"><span class="tag">Quy trình</span><h2>Tư vấn và triển khai</h2>{steps()}</div></section>'''
    write(f"/may-moc/{q['id']}/", page(f"/may-moc/{q['id']}/", f"{q['name']} | Core Material JSC", q["short"], body, "/may-moc/", ("/"+q["img"]) if q["img"] else "/img/og-image.jpg"))

# =================== ỨNG DỤNG & VIDEO ===================
apps = [("Nhà máy vữa khô, keo dán gạch", "Cát khô phân cỡ, xi măng trắng, phụ gia VAE/RDP; tự động hóa bốc xếp và xếp pallet.", "/vat-lieu/"),
        ("Xưởng sản xuất cấu kiện GRC/GFRC", "Thiết bị phun GRC và vật liệu nền cho cấu kiện kiến trúc.", "/may-moc/phun-grc/"),
        ("Nhà thầu hoàn thiện", "Máy phun vữa tô tường giúp cơ giới hóa công tác trát, tăng tiến độ.", "/may-moc/phun-vua-to-tuong/"),
        ("Terrazzo & trang trí kiến trúc", "Đá mài, hạt thủy tinh, bột màu và xi măng trắng.", "/vat-lieu/#trang-tri")]
allv = [v for q in EQUIPMENT for v in q["videos"]]
ud = phead([("/", "Trang chủ"), (None, "Ứng dụng & Video")], "Ứng dụng & Video", "Vật liệu và thiết bị theo từng lĩnh vực ứng dụng, kèm video thực tế.") + f'''
<section><div class="wrap"><span class="tag">Lĩnh vực ứng dụng</span><h2>Giải pháp theo nhu cầu</h2>
 <div class="grid g4" style="margin-top:32px">{"".join(f'<a class="card" href="{u}"><div class="tx"><span class="k">Ứng dụng</span><h3>{e(t)}</h3><p>{e(d)}</p><span class="more">Xem giải pháp {ARROW}</span></div></a>' for t,d,u in apps)}</div></div></section>
<section class="dark"><div class="wrap"><span class="tag">Video</span><h2>Video thực tế</h2><p class="lead">Video từ nhà cung cấp thiết bị. Video công trình tại Việt Nam sẽ được cập nhật.</p><div class="vgrid">{"".join(vcard(v) for v in allv)}</div>{slot("Video / ảnh dự án tại Việt Nam (khi có quyền sử dụng)")}</div></section>''' + cta()
write("/ung-dung/", page("/ung-dung/", "Ứng dụng & Video | Core Material JSC", "Ứng dụng vật liệu và thiết bị cho nhà máy vữa khô, xưởng GRC, nhà thầu hoàn thiện và trang trí kiến trúc — kèm video thực tế.", ud, "/ung-dung/", "/media/video-phun-grc-poster.jpg"))

# =================== HỢP TÁC ĐẦU TƯ ===================
inv = phead([("/", "Trang chủ"), (None, "Hợp tác đầu tư")], "Hợp tác đầu tư", "Core Material JSC chào đón trao đổi với các đối tác quan tâm đến chuỗi cung ứng vật liệu xây dựng tại phía Nam.") + f'''
<section><div class="wrap" style="max-width:900px">
 <p class="lead" style="max-width:none">Chúng tôi đang nghiên cứu các phương án hợp tác cho nguồn cát và chế biến cát khô, cũng như các dự án vật liệu xây dựng khác. Các phương án đầu tư được đánh giá theo nhu cầu thị trường, hiệu quả và điều kiện thực tế, và chỉ triển khai khi được Hội đồng quản trị phê duyệt.</p>
 <h3 style="font-size:20px;margin:30px 0 8px">Đối tác chúng tôi mong muốn trao đổi</h3>
 <ul class="chk" style="list-style:none"><li style="padding:7px 0">Đơn vị sở hữu hoặc khai thác nguồn cát hợp pháp, bãi, phương tiện vận chuyển</li><li style="padding:7px 0">Đối tác tài chính quan tâm lĩnh vực vật liệu xây dựng</li><li style="padding:7px 0">Nhà máy có năng lực gia công, đóng gói vật liệu</li></ul>
 <div class="note">Thông tin chi tiết về phương án hợp tác được trao đổi trực tiếp sau khi hai bên ký thỏa thuận bảo mật.</div>
 <a class="btn btn-dark" href="{contact_href("Hợp tác đầu tư")}">Đăng ký trao đổi {ARROW}</a>
</div></section>'''
write("/hop-tac-dau-tu/", page("/hop-tac-dau-tu/", "Hợp tác đầu tư | Core Material JSC", "Core Material JSC chào đón trao đổi hợp tác về nguồn cát, chế biến cát khô và các dự án vật liệu xây dựng.", inv))

# =================== LIÊN HỆ ===================
opts = ""
for grp, items in FORM_GROUPS:
    kind = "mat" if grp.startswith("Nguyên") else ("eq" if grp.startswith("Máy") else "other")
    opts += f'<span class="grp-t">{e(grp)}</span>' + "".join(f'<label><input type="checkbox" name="nhom" value="{e(i)}" data-kind="{kind}"><span>{e(i)}</span></label>' for i in items)
TS_KEY = os.environ.get("TURNSTILE_SITEKEY", "")
ts_head = '\n<script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async defer></script>' if TS_KEY else ""
ts_widget = f'<div class="cf-turnstile f" data-sitekey="{TS_KEY}" data-language="vi"></div>' if TS_KEY else ""
lh = phead([("/", "Trang chủ"), (None, "Liên hệ")], "Liên hệ tư vấn", "Gửi nhu cầu vật liệu hoặc thiết bị — Core Material sẽ phản hồi qua điện thoại hoặc email.") + f'''
<section><div class="wrap contact-in">
 <div>
  <span class="tag">Thông tin liên hệ</span><h2>Trao đổi trực tiếp</h2>
  <p class="lead">Anh/chị có thể gọi hotline, gửi email hoặc điền form bên cạnh.</p>
  <div class="info">
   <div><span class="ic">{IC["phone"]}</span><span><small>Hotline</small><a href="tel:{TEL}">{COMPANY["hotline"]}</a></span></div>
   <div><span class="ic">{IC["mail"]}</span><span><small>Email</small><a href="mailto:{COMPANY["email"]}">{COMPANY["email"]}</a></span></div>
   <div><span class="ic">{IC["pin"]}</span><span><small>Văn phòng</small>{e(COMPANY["address"])}</span></div>
   <div><span class="ic">{IC["doc"]}</span><span><small>Doanh nghiệp</small>{e(COMPANY["legal"])} · MST {COMPANY["tax"]}</span></div>
  </div>
 </div>
 <form id="form" class="lead-form" novalidate>
  <fieldset><legend>Nhóm quan tâm <span class="req">*</span></legend><div class="opts">{opts}</div></fieldset>
  <div class="row"><div class="f"><label for="ten">Họ tên <span class="req">*</span></label><input id="ten" name="ten" autocomplete="name" required maxlength="100"></div>
   <div class="f"><label for="cty">Công ty</label><input id="cty" name="cty" autocomplete="organization" maxlength="150"></div></div>
  <div class="row"><div class="f"><label for="sdt">Điện thoại <span class="req">*</span></label><input id="sdt" name="sdt" type="tel" autocomplete="tel" required maxlength="20"></div>
   <div class="f"><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email" maxlength="150"></div></div>
  <div class="cond" id="c-mat"><div class="f"><label for="sanluong">Sản lượng vật liệu dự kiến / tháng</label>
   <select id="sanluong" name="sanluong"><option value="">— Chọn —</option><option>Dưới 10 tấn</option><option>10 – 100 tấn</option><option>100 – 500 tấn</option><option>Trên 500 tấn</option><option>Chưa xác định</option></select></div></div>
  <div class="cond" id="c-eq">
   <div class="f"><label for="ungdung">Ứng dụng thiết bị</label><input id="ungdung" name="ungdung" maxlength="200" placeholder="VD: sản xuất tấm GRC, tô tường chung cư, xếp pallet bao 40 kg…"></div>
   <div class="row"><div class="f"><label for="nangsuat">Năng suất mong muốn</label><input id="nangsuat" name="nangsuat" maxlength="100" placeholder="VD: m²/ngày, bao/giờ…"></div>
    <div class="f"><label for="diadiem">Địa điểm lắp đặt / thi công</label><input id="diadiem" name="diadiem" maxlength="150"></div></div>
  </div>
  <div class="f"><label for="noidung" id="lbl-nd">Nội dung / mô tả nhu cầu</label><textarea id="noidung" name="noidung" maxlength="3000" placeholder="Quy cách, cỡ hạt, điều kiện mặt bằng, thời gian dự kiến…"></textarea></div>
  <div class="hp" aria-hidden="true"><label>Website<input name="website" tabindex="-1" autocomplete="off"></label></div>
  {ts_widget}
  <button class="btn btn-dark" type="submit" id="send">Gửi yêu cầu {ARROW}</button>
  <div class="status" id="status" role="status" aria-live="polite"></div>
 </form>
</div></section>
<script>
(function(){{
 const f=document.getElementById('form'),st=document.getElementById('status'),btn=document.getElementById('send');
 const t0=Date.now();
 function sync(){{const k=[...f.querySelectorAll('input[name=nhom]:checked')].map(i=>i.dataset.kind);
  document.getElementById('c-mat').classList.toggle('show',k.includes('mat'));document.getElementById('c-eq').classList.toggle('show',k.includes('eq'));}}
 f.querySelectorAll('input[name=nhom]').forEach(i=>i.addEventListener('change',sync));
 const pre=new URLSearchParams(location.search).get('nhom');
 if(pre)f.querySelectorAll('input[name=nhom]').forEach(i=>{{if(i.value===pre)i.checked=true}});sync();
 function show(cls,html){{st.className='status '+cls;st.innerHTML=html}}
 const fallback='Vui lòng gọi <a href="tel:{TEL}"><b>{COMPANY["hotline"]}</b></a> hoặc email <a href="mailto:{COMPANY["email"]}"><b>{COMPANY["email"]}</b></a> để được hỗ trợ ngay.';
 f.addEventListener('submit',async ev=>{{
  ev.preventDefault();
  const d=Object.fromEntries(new FormData(f).entries());d.nhom=[...f.querySelectorAll('input[name=nhom]:checked')].map(i=>i.value);d.t=Date.now()-t0;
  if(!d.nhom.length)return show('err','Vui lòng chọn ít nhất một nhóm quan tâm.');
  if(!d.ten.trim()||!/^[0-9+().\\s-]{{8,20}}$/.test(d.sdt.trim()))return show('err','Vui lòng nhập họ tên và số điện thoại hợp lệ.');
  btn.disabled=true;show('busy','Đang gửi yêu cầu…');
  try{{const r=await fetch('/api/lien-he',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify(d)}});
   const j=await r.json().catch(()=>({{}}));
   if(r.ok&&j.ok){{show('ok','<b>Core Material đã nhận được yêu cầu của anh/chị.</b> Chúng tôi sẽ liên hệ lại sớm. Mã yêu cầu: '+(j.id||''));f.reset();sync();if(window.turnstile)turnstile.reset();}}
   else if(j.error==='not_configured'){{show('err','<b>Form trực tuyến đang được hoàn thiện, yêu cầu CHƯA được gửi.</b> '+fallback);}}
   else if(j.error==='captcha'){{show('err','Không xác minh được chống spam. Vui lòng thử lại. '+fallback);if(window.turnstile)turnstile.reset();}}
   else{{show('err','<b>Chưa gửi được yêu cầu.</b> '+fallback);}}
  }}catch(_){{show('err','<b>Chưa gửi được yêu cầu (lỗi kết nối).</b> '+fallback);}}
  btn.disabled=false;
 }});
}})();
</script>'''
write("/lien-he/", page("/lien-he/", "Liên hệ tư vấn | Core Material JSC", "Liên hệ Core Material JSC: tư vấn vật liệu (cát khô, xi măng trắng, VAE/RDP) và thiết bị (phun GRC, phun vữa, robot xếp pallet).", lh, "/lien-he/", extra_head=ts_head))

# =================== 404 ===================
nf = '<section class="phead" style="padding:120px 0"><div class="wrap"><span class="tag">404</span><h1>Không tìm thấy trang</h1><p>Trang anh/chị tìm có thể đã được di chuyển.</p><p style="margin-top:24px"><a class="btn btn-gold" href="/">Về trang chủ</a> <a class="btn btn-line" style="color:#fff" href="/lien-he/">Liên hệ</a></p></div></section>'
write("/404.html", page("/404.html", "Không tìm thấy trang | Core Material JSC", DEFAULT_DESC, nf))

# =================== sitemap/robots ===================
urls = ["/", "/gioi-thieu/", "/vat-lieu/", "/may-moc/"] + [f"/may-moc/{q['id']}/" for q in EQUIPMENT] + ["/ung-dung/", "/lien-he/", "/hop-tac-dau-tu/"]
open(os.path.join(ROOT, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"<url><loc>{SITE}{u}</loc></url>\n" for u in urls) + "</urlset>\n")
open(os.path.join(ROOT, "robots.txt"), "w").write(("User-agent: *\nDisallow: /\n" if PREVIEW else f"User-agent: *\nAllow: /\nDisallow: /email/\nSitemap: {SITE}/sitemap.xml\n"))
print("Built", "PREVIEW" if PREVIEW else "PRODUCTION", len(urls), "pages")
