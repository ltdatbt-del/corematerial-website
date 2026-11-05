# -*- coding: utf-8 -*-
"""Sinh trang tĩnh cho corematerial.info vào public/info/.
Chạy:  python3 tools/build_info.py
"""
import os, sys, html, json
sys.path.insert(0, os.path.dirname(__file__))
from info_articles import ARTICLES, CATEGORIES, LIBRARY

ROOT = os.path.join(os.path.dirname(__file__), "..", "public", "info")
SITE = "https://corematerial.info"
MARK = '''<svg viewBox="44 22 487 568" aria-hidden="true"><g stroke-linejoin="round" stroke-width="14"><polygon points="305,37 388,88 160,228 160,384 388,524 305,575 59,428 59,184" fill="{c}" stroke="{c}"/><polygon points="300,206 432,124 516,166 516,246 432,288" fill="#D4A835" stroke="#D4A835"/><polygon points="300,412 432,330 516,372 516,452 432,494" fill="#D4A835" stroke="#D4A835"/></g></svg>'''
e = html.escape

def head(title, desc, rel, path, og_type="website", extra=""):
    return f'''<!DOCTYPE html>
<html lang="vi"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{SITE}/{path}">
<meta property="og:type" content="{og_type}"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{SITE}/{path}">
<link rel="icon" type="image/svg+xml" href="{rel}img/core-mark.svg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&family=Noto+Serif:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{rel}assets/style.css">{extra}
</head><body>
<div class="topbar"><div class="wrap"><span>Tri thức vật liệu xây dựng · Công nghệ · Ứng dụng</span><span class="hide-s">Một kênh của <a href="https://www.corematerial.vn">Core Material JSC</a></span></div></div>
<header class="mast"><div class="wrap">
  <a class="brand" href="{rel}index.html">{MARK.format(c="#111")}<span><b>Core Material</b><small>INSIGHTS</small></span></a>
  <nav class="cats" id="cats">{''.join(f'<a href="{rel}chuyen-muc/{k}.html">{e(v[0])}</a>' for k,v in CATEGORIES.items())}<a href="{rel}index.html#thu-vien">Thư viện vật liệu</a></nav>
  <button class="burger" aria-label="Menu" onclick="document.getElementById('cats').classList.toggle('open')">☰</button>
</div></header>
'''

def foot(rel):
    return f'''<footer><div class="wrap"><div class="fgrid">
<div><a class="brand" href="{rel}index.html">{MARK.format(c="#fff")}<span><b>Core Material</b><small>INSIGHTS</small></span></a>
<p style="margin-top:14px;max-width:380px">Kênh chia sẻ kiến thức về vật liệu xây dựng, hóa chất chuyên dụng, máy móc và khoa học công nghệ – do Core Material JSC biên soạn.</p></div>
<div><h4>Chuyên mục</h4><ul>{''.join(f'<li><a href="{rel}chuyen-muc/{k}.html">{e(v[0])}</a></li>' for k,v in CATEGORIES.items())}</ul></div>
<div><h4>Core Material JSC</h4><ul><li><a href="https://www.corematerial.vn">www.corematerial.vn</a></li><li><a href="https://www.corematerial.vn/#san-pham">Sản phẩm</a></li><li><a href="https://www.corematerial.vn/#lien-he">Liên hệ báo giá</a></li><li>Hotline 0938.903.557</li></ul></div>
</div><div class="fbot"><span>© 2026 Core Material JSC. Nội dung mang tính tham khảo kỹ thuật.</span><span>INTEGRITY · INNOVATION · PARTNERSHIP</span></div></div></footer>
</body></html>'''

def ph(a, rel, cls="ph"):
    if a.get("img"):
        return f'<div class="{cls}" style="background-image:url({rel}img/{a["img"]})"></div>'
    return f'<div class="{cls} hex"><div class="hexdeco">{MARK.format(c="#fff")}</div></div>'

def card(a, rel):
    c = CATEGORIES[a["cat"]][0]
    return f'''<a class="card" href="{rel}bai-viet/{a["slug"]}.html">{ph(a,rel)}<div class="tx"><span class="kicker">{e(c)}</span><h3>{e(a["title"])}</h3><p>{e(a["excerpt"])}</p><div class="meta">{a["date"]} · {a["read"]} phút đọc</div></div></a>'''

def write(path, s):
    full = os.path.join(ROOT, path); os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(s)

# ---------- trang bài viết
for a in ARTICLES:
    rel = "../"; cname = CATEGORIES[a["cat"]][0]
    ld = {"@context":"https://schema.org","@type":"Article","headline":a["title"],"description":a["excerpt"],
          "datePublished":"-".join(reversed(a["date"].split("/"))),"inLanguage":"vi",
          "author":{"@type":"Organization","name":"Core Material JSC"},
          "publisher":{"@type":"Organization","name":"Core Material JSC","url":"https://www.corematerial.vn"},
          "mainEntityOfPage":f"{SITE}/bai-viet/{a['slug']}.html"}
    extra = f'\n<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>'
    img = f'<div class="art-img"><img src="../img/{a["img"]}" alt=""></div>' if a.get("img") else ""
    src = ""
    if a["sources"]:
        items = "".join(f'<li>{f"<a href={chr(34)}{u}{chr(34)} rel={chr(34)}noopener{chr(34)}>{e(t)}</a>" if u else e(t)}</li>' for t,u in a["sources"])
        src = f'<div class="sources"><h3>Nguồn tham khảo</h3><ul>{items}</ul></div>'
    rel_arts = [x for x in ARTICLES if x is not a and x["cat"] == a["cat"]] + [x for x in ARTICLES if x is not a and x["cat"] != a["cat"]]
    page = head(f'{a["title"]} | Core Material Insights', a["excerpt"], rel, f'bai-viet/{a["slug"]}.html', "article", extra) + f'''
<article>
<div class="narrow art-head">
  <div class="crumb"><a href="../index.html">Insights</a> / <a href="../chuyen-muc/{a["cat"]}.html">{e(cname)}</a></div>
  <span class="kicker">{e(cname)}</span>
  <h1>{e(a["title"])}</h1>
  <p class="lede">{e(a["excerpt"])}</p>
  <div class="byline"><span>Biên soạn: <b>Ban Kỹ thuật Core Material</b></span><span>{a["date"]}</span><span>{a["read"]} phút đọc</span></div>
</div>
<div class="narrow">{img}<div class="prose">{a["body"]}</div>{src}</div>
</article>
<div class="wrap related"><div class="sec-h"><h2>Bài viết liên quan</h2></div><div class="grid3">{"".join(card(x, rel) for x in rel_arts[:3])}</div></div>
''' + foot(rel)
    write(f'bai-viet/{a["slug"]}.html', page)

# ---------- trang chuyên mục
for k,(name,desc) in CATEGORIES.items():
    rel = "../"; arts = [a for a in ARTICLES if a["cat"] == k]
    body = "".join(card(a, rel) for a in arts) or '<p style="color:#6B6B6B">Bài viết đang được biên soạn.</p>'
    page = head(f'{name} | Core Material Insights', desc, rel, f'chuyen-muc/{k}.html') + f'''
<section><div class="wrap"><div class="crumb"><a href="../index.html">Insights</a> / {e(name)}</div>
<div class="sec-h"><h2>{e(name)}</h2><p>{e(desc)}</p></div><div class="grid3">{body}</div></div></section>
''' + foot(rel)
    write(f'chuyen-muc/{k}.html', page)

# ---------- trang chủ
rel = ""; f0 = ARTICLES[0]; others = ARTICLES[1:]
feat_bg = f' style="background-image:url(img/{f0["img"]})"' if f0.get("img") else ""
cats_html = "".join(f'<a class="catbox" href="chuyen-muc/{k}.html"><div class="n">0{i+1}</div><h3>{e(v[0])}</h3><p>{e(v[1])}</p></a>' for i,(k,v) in enumerate(CATEGORIES.items()))
lib_html = "".join(f'<div><b>{e(n)}</b><span>{e(d)}</span></div>' for n,d in LIBRARY)
side = "".join(f'<a class="mini" href="bai-viet/{a["slug"]}.html"><span class="kicker">{e(CATEGORIES[a["cat"]][0])}</span><h3>{e(a["title"])}</h3><div class="meta">{a["read"]} phút đọc</div></a>' for a in others[:4])
ld = {"@context":"https://schema.org","@type":"WebSite","name":"Core Material Insights","url":SITE+"/","inLanguage":"vi",
      "publisher":{"@type":"Organization","name":"Core Material JSC","url":"https://www.corematerial.vn"}}
page = head("Core Material Insights — Tri thức vật liệu xây dựng, máy móc & KHCN",
            "Kiến thức về vật liệu xây dựng, hóa chất chuyên dụng (VAE, RDP), cát khô, xi măng trắng, terrazzo, máy móc sản xuất và xu hướng nghiên cứu mới.",
            rel, "", extra=f'\n<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>') + f'''
<section class="hero"><div class="wrap">
  <span class="kicker">Core Material Insights</span>
  <h2 style="font-size:clamp(28px,4vw,46px);font-weight:800;letter-spacing:-.02em;margin:8px 0 28px;max-width:880px;line-height:1.12">Tri thức vật liệu cho những công trình bền vững.</h2>
  <div class="hero-grid">
    <a class="feature" href="bai-viet/{f0["slug"]}.html"><div class="ph"{feat_bg}></div><div class="tx"><span class="kicker">{e(CATEGORIES[f0["cat"]][0])} · Bài nổi bật</span><h1>{e(f0["title"])}</h1><p>{e(f0["excerpt"])}</p></div></a>
    <div class="side"><h2>Mới cập nhật</h2>{side}</div>
  </div>
</div></section>
<section style="padding-top:20px"><div class="wrap"><div class="sec-h"><h2>Chuyên mục</h2><p>Từ đặc tính vật liệu đến dây chuyền sản xuất và chính sách ngành.</p></div><div class="catgrid">{cats_html}</div></div></section>
<section><div class="wrap"><div class="sec-h"><h2>Tất cả bài viết</h2><p>Được biên soạn bởi đội ngũ kỹ thuật Core Material, có trích dẫn nguồn khi sử dụng số liệu nghiên cứu.</p></div><div class="grid3">{"".join(card(a, rel) for a in ARTICLES)}</div></div></section>
<section id="thu-vien"><div class="wrap"><div class="sec-h"><h2>Thư viện vật liệu</h2><p>Giải thích ngắn gọn các vật liệu và phụ gia thường gặp trong vữa khô, keo dán gạch và vật liệu trang trí.</p></div><div class="lib">{lib_html}</div></div></section>
<section><div class="wrap"><div class="cta"><div><h2>Cần tư vấn vật liệu cho dự án hoặc nhà máy?</h2><p>Đội ngũ kỹ thuật Core Material hỗ trợ chọn vật liệu, thử nghiệm cấp phối và báo giá.</p></div><a class="btn" href="https://www.corematerial.vn/#lien-he">Liên hệ Core Material →</a></div></div></section>
''' + foot(rel)
write("index.html", page)

# ---------- sitemap + robots
urls = [SITE+"/"] + [f"{SITE}/chuyen-muc/{k}.html" for k in CATEGORIES] + [f"{SITE}/bai-viet/{a['slug']}.html" for a in ARTICLES]
write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"<url><loc>{u}</loc></url>\n" for u in urls) + "</urlset>\n")
write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
print("Đã sinh", len(ARTICLES), "bài,", len(CATEGORIES), "chuyên mục.")
