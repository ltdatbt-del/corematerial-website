"""Gộp bản PREVIEW đa trang thành 1 trang (định tuyến bằng #hash) để xem trước dạng artifact.
Chạy sau: PREVIEW=1 python3 tools/build_site.py
Kết quả: /home/claude/pv/index.html + img/, media/ (đường dẫn tương đối)."""
import re, glob, os, shutil

ROOT = os.path.join(os.path.dirname(__file__), '..', 'public')
OUT = '/home/claude/pv'
PAGES = ['', 'gioi-thieu', 'vat-lieu', 'may-moc', 'may-moc/phun-grc', 'may-moc/phun-vua-to-tuong',
         'may-moc/robot-xep-pallet', 'ung-dung', 'lien-he', 'hop-tac-dau-tu']


def key(p):
    return p.replace('/', '-') if p else 'trang-chu'


def fix_links(h):
    # liên hệ có chọn sẵn nhóm
    from urllib.parse import unquote_plus
    h = re.sub(r'href="/lien-he/\?nhom=([^"#]+)(?:#form)?"', lambda m: 'href="#form" data-nhom="%s"' % unquote_plus(m.group(1)), h)
    def repl(m):
        path, frag = m.group(1).strip('/'), m.group(2)
        if path in PAGES:
            return 'href="#%s"' % (frag or key(path))
        return m.group(0)
    h = re.sub(r'href="/([^"#?]*)(?:#([^"]*))?"', repl, h)
    h = re.sub(r'(src|poster|content)="/(img|media)/', r'\1="\2/', h)
    return h


idx = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
sections, scripts, titles = [], [], {}
for p in PAGES:
    s = open(os.path.join(ROOT, p, 'index.html'), encoding='utf-8').read()
    titles[key(p)] = re.search(r'<title>(.*?)</title>', s).group(1)
    main = re.search(r'<main>(.*)</main>', s, re.S).group(1)
    sections.append('<section class="pv-page" data-page="%s" hidden>%s</section>' % (key(p), main))
    for sc in re.findall(r'<script(?![^>]*ld\+json)(?![^>]*src=)[^>]*>.*?</script>', s, re.S):
        if p == 'lien-he' and sc not in scripts:
            scripts.append(sc.replace("new URLSearchParams(location.search).get('nhom')", "null")
                             .replace("fetch('/api/lien-he'", "fetch('https://www.corematerial.vn/api/lien-he'"))

css = open(os.path.join(ROOT, 'assets', 'site.css'), encoding='utf-8').read()
body = idx.replace(re.search(r'<main>.*</main>', idx, re.S).group(0), '<main>%s</main>' % ''.join(sections))
body = re.sub(r'<link rel="stylesheet" href="/assets/site.css"[^>]*>', '<style>%s</style>' % css, body)
body = re.sub(r'<script[^>]*challenges\.cloudflare[^>]*></script>', '', body)
banner = ('<div style="background:#D4A835;color:#111;font:600 13px/1.4 Inter,sans-serif;padding:8px 16px;text-align:center">'
          'BẢN XEM TRƯỚC — chưa xuất bản. Khung vàng sọc = vị trí chờ nội dung thật. Form ở bản này không gửi được (môi trường xem trước).</div>')
body = body.replace('<header class="site">', banner + '<header class="site">', 1)
router = '''<script>
(function(){
 const pages=[...document.querySelectorAll('.pv-page')],T=%s;
 function go(){let h=decodeURIComponent(location.hash.slice(1))||'trang-chu';
  let pg=pages.find(s=>s.dataset.page===h),el=null;
  if(!pg){el=document.getElementById(h);pg=el?el.closest('.pv-page'):pages[0];}
  pages.forEach(s=>s.hidden=s!==pg);document.title=T[pg.dataset.page]||document.title;
  document.querySelectorAll('header .menu a').forEach(a=>{const k=a.getAttribute('href').slice(1);a.classList.toggle('on',k===pg.dataset.page||pg.dataset.page.startsWith(k+'-'))});
  const m=document.getElementById('menu');if(m)m.classList.remove('open');
  if(el)setTimeout(()=>el.scrollIntoView(),0);else window.scrollTo(0,0);}
 document.addEventListener('click',e=>{const a=e.target.closest('a[data-nhom]');if(!a)return;
  setTimeout(()=>{document.querySelectorAll('input[name=nhom]').forEach(i=>{if(i.value===a.dataset.nhom){i.checked=true;i.dispatchEvent(new Event('change'))}})},50)});
 addEventListener('hashchange',go);go();
})();
</script>''' % __import__('json').dumps(titles, ensure_ascii=False)
body = re.sub(r'<script(?![^>]*ld\+json)(?![^>]*src=)[^>]*>.*?</script>', '', body, flags=re.S)
body = fix_links(body).replace('</body>', ''.join(scripts) + router + '</body>')

shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(OUT)
open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write(body)
used = set(re.findall(r'(?:src|poster|href)="((?:img|media)/[^"]+)"', body)) | set(re.findall(r'url\(["\']?/?((?:img|media)/[^"\')]+)', body))
for u in sorted(used):
    os.makedirs(os.path.dirname(os.path.join(OUT, u)), exist_ok=True)
    shutil.copy(os.path.join(ROOT, u), os.path.join(OUT, u))
print('bundle ok', len(body) // 1024, 'KB,', len(used), 'files')
