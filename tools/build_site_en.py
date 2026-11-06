# -*- coding: utf-8 -*-
"""Build the ENGLISH site into public/en/ from the same template as build_site.py.
  python3 tools/build_site.py && python3 tools/build_site_en.py
Text for products/equipment lives in tools/site_data_en.py; the UI strings below
replace the Vietnamese strings of the template (exact-match; the build fails loudly
if a string is no longer found, so template edits are not silently left untranslated).
"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "build_site.py"), encoding="utf-8").read()
src = src.split("# =================== 404 ===================")[0]

R = [
 # --- setup ---
 ('from site_data import *\nfrom site_data_en import PATHS as _EN_PATHS\nLANG, ALT_LANG, ALT_LABEL = "vi", "en", "EN"\nALT_MAP = _EN_PATHS',
  'from site_data_en import *\nLANG, ALT_LANG, ALT_LABEL = "en", "vi", "VI"\nALT_MAP = {v: k for k, v in PATHS.items()}'),
 # --- URLs ---
 ('def contact_href(group): return "/lien-he/?nhom="', 'def contact_href(group): return "/en/contact/?nhom="'),
 ('"/may-moc/phun-grc/"', '"/en/equipment/grc-spraying/"'), ('"/may-moc/phun-vua-to-tuong/"', '"/en/equipment/wall-plastering-machine/"'),
 ('#cat-kho', '#dry-sand'), ('#xi-mang-trang', '#white-cement'), ('#trang-tri', '#decorative'),
 ('/gioi-thieu/', '/en/about/'), ('/vat-lieu/', '/en/materials/'), ('/may-moc/', '/en/equipment/'),
 ('/ung-dung/', '/en/applications/'), ('/lien-he/', '/en/contact/'), ('/hop-tac-dau-tu/', '/en/investment/'),
 ('href="/" class="logo"', 'href="/en/" class="logo"'), ('[("/", "Trang chủ")', '[("/en/", "Home")'),
 ('write("/", page("/",', 'write("/en/", page("/en/",'),
 # --- chrome ---
 ('MENU = [("/en/about/", "Giới thiệu"), ("/en/materials/", "Nguyên liệu & Vật liệu"), ("/en/equipment/", "Máy móc & Tự động hóa"), ("/en/applications/", "Ứng dụng & Video"), ("/en/contact/", "Liên hệ")]',
  'MENU = [("/en/about/", "About"), ("/en/materials/", "Materials"), ("/en/equipment/", "Equipment & Automation"), ("/en/applications/", "Applications & Video"), ("/en/contact/", "Contact")]'),
 ('DEFAULT_DESC = "Core Material JSC kết nối nguồn cung nguyên liệu, thiết bị và giải pháp công nghệ cho ngành vật liệu xây dựng: cát khô, xi măng trắng, phụ gia, vật liệu trang trí, thiết bị phun GRC, máy phun vữa và tự động hóa nhà máy."',
  'DEFAULT_DESC = "Core Material JSC connects supply of raw materials, equipment and technology solutions for the construction-materials industry in Vietnam: dry sand, white cement, admixtures, decorative materials, GRC spraying, mortar spraying machines and factory automation."'),
 ('BẢN XEM TRƯỚC – Chờ bổ sung:', 'PREVIEW – pending:'),
 ('"legalName":COMPANY["legal"].title().replace("Cổ Phần","Cổ phần")', '"legalName":COMPANY["legal"].title()'),
 ('"streetAddress":"114bis Trần Quốc Toản, P. Xuân Hòa","addressLocality":"TP. Hồ Chí Minh"', '"streetAddress":"114bis Tran Quoc Toan St., Xuan Hoa Ward","addressLocality":"Ho Chi Minh City"'),
 ('aria-label="Core Material JSC – Trang chủ"', 'aria-label="Core Material JSC – Home"'),
 ('>Liên hệ tư vấn</a>\n  <button class="burger" aria-label="Mở menu"', '>Contact us</a>\n  <button class="burger" aria-label="Open menu"'),
 (' Gọi {COMPANY["hotline"]}</a>\n</body>', ' Call {COMPANY["hotline"]}</a>\n</body>'),
 ('<p>{e(COMPANY["legal"])}<br>MST: {COMPANY["tax"]}</p>', '<p>{e(COMPANY["legal"])}<br>Tax code: {COMPANY["tax"]}</p>'),
 ('<h6>Nguyên liệu & Vật liệu</h6>', '<h6>Materials</h6>'), ('<h6>Máy móc & Tự động hóa</h6>', '<h6>Equipment & Automation</h6>'), ('<h6>Công ty</h6>', '<h6>Company</h6>'),
 ('>Giới thiệu</a></li><li><a href="/en/applications/">Ứng dụng & Video</a></li><li><a href="/en/investment/">Hợp tác đầu tư</a></li><li><a href="https://corematerial.info">Kiến thức vật liệu (Insights)</a></li><li><a href="/en/contact/">Liên hệ</a>',
  '>About</a></li><li><a href="/en/applications/">Applications & Video</a></li><li><a href="/en/investment/">Investment partnership</a></li><li><a href="https://corematerial.info">Insights (Vietnamese)</a></li><li><a href="/en/contact/">Contact</a>'),
 ('Bảo lưu mọi quyền.', 'All rights reserved.'),
 ('def cta(text="Cần tư vấn vật liệu hoặc thiết bị?", sub="Đội ngũ Core Material tiếp nhận nhu cầu và phản hồi qua điện thoại hoặc email.", link="/en/contact/", label="Liên hệ tư vấn")',
  'def cta(text="Need advice on materials or equipment?", sub="The Core Material team will review your request and reply by phone or email.", link="/en/contact/", label="Contact us")'),
 ('style="color:#fff" href="tel:{TEL}">Gọi {COMPANY["hotline"]}</a>', 'style="color:#fff" href="tel:{TEL}">Call {COMPANY["hotline"]}</a>'),
 ('more="Xem chi tiết"', 'more="Learn more"'),
 # --- home ---
 ('"Nguyên liệu", MATERIALS[0]["short"], "Cát silica sấy khô, sàng phân cỡ cho vữa khô, keo dán gạch và bê tông trang trí."',
  '"Raw material", MATERIALS[0]["short"], "Kiln-dried, graded silica sand for dry-mix mortar, tile adhesive and decorative concrete."'),
 ('"Nguyên liệu", "Xi măng trắng", "Cung cấp xi măng trắng cho sản xuất vật liệu và thi công, có COA theo lô."',
  '"Raw material", "White cement", "White cement for material production and construction, with COA per lot."'),
 ('"Vật liệu trang trí", "Đá mài, hạt thủy tinh & bột màu", "Vật liệu cho terrazzo, bê tông nghệ thuật và hoàn thiện kiến trúc."',
  '"Decorative materials", "Terrazzo chips, glass granules & pigments", "Materials for terrazzo, architectural concrete and finishes."'),
 ('<h1>Vật liệu. Thiết bị.<br><em>Giải pháp công nghệ.</em></h1>', '<h1>Materials. Equipment.<br><em>Technology solutions.</em></h1>'),
 ('<p class="sub">Core Material kết nối nguồn cung nguyên liệu, thiết bị và giải pháp công nghệ cho ngành vật liệu xây dựng — từ sản xuất tại nhà máy đến thi công tại công trình.</p>',
  '<p class="sub">Core Material connects supply of raw materials, equipment and technology solutions for the construction-materials industry — from factory production to on-site construction.</p>'),
 ('class="btn btn-gold">Khám phá vật liệu {ARROW}</a><a href="/en/equipment/" class="btn btn-line">Khám phá thiết bị {ARROW}</a>',
  'class="btn btn-gold">Explore materials {ARROW}</a><a href="/en/equipment/" class="btn btn-line">Explore equipment {ARROW}</a>'),
 ('alt="Mẫu cát silica phân cỡ Core Material"><figcaption><b>Vật liệu</b> · Cát silica phân cỡ', 'alt="Core Material graded silica sand sample"><figcaption><b>Materials</b> · Graded silica sand'),
 ('alt="Máy phun vữa tô tường"><figcaption><b>Thiết bị</b> · Máy phun vữa', 'alt="Wall plastering machine"><figcaption><b>Equipment</b> · Mortar spraying'),
 ('alt="Thiết bị phun GRC"><figcaption><b>Công nghệ</b> · Phun GRC', 'alt="GRC spraying equipment"><figcaption><b>Technology</b> · GRC spraying'),
 ('aria-label="Giá trị cốt lõi"', 'aria-label="Core values"'),
 ('<span class="tag">Hai nhóm kinh doanh</span>\n <h2>Một đầu mối cho vật liệu và thiết bị</h2>\n <p class="lead">Từ nguyên liệu đầu vào cho nhà máy đến thiết bị cơ giới hóa và tự động hóa, Core Material giúp khách hàng chọn đúng giải pháp và kết nối nguồn cung phù hợp.</p>',
  '<span class="tag">Two business lines</span>\n <h2>One partner for materials and equipment</h2>\n <p class="lead">From raw materials for your plant to mechanisation and automation equipment, Core Material helps you choose the right solution and connects you with suitable supply.</p>'),
 ('<h3>Nguyên liệu & Vật liệu</h3><p>Cát khô, xi măng trắng, phụ gia VAE/RDP và vật liệu trang trí cho nhà sản xuất và nhà thầu.</p><ul><li>Cát khô</li><li>Xi măng trắng</li><li>VAE / RDP</li><li>Đá mài & hạt màu</li></ul><span class="more">Khám phá vật liệu {ARROW}',
  '<h3>Raw materials & Materials</h3><p>Dry sand, white cement, VAE/RDP admixtures and decorative materials for manufacturers and contractors.</p><ul><li>Dry sand</li><li>White cement</li><li>VAE / RDP</li><li>Terrazzo chips & granules</li></ul><span class="more">Explore materials {ARROW}'),
 ('<h3>Máy móc & Tự động hóa</h3><p>{e(TECH_INTRO)}</p><ul><li>Phun GRC/GFRC</li><li>Phun vữa tô tường</li><li>Robot xếp pallet</li></ul><span class="more">Khám phá thiết bị {ARROW}',
  '<h3>Equipment & Automation</h3><p>{e(TECH_INTRO)}</p><ul><li>GRC/GFRC spraying</li><li>Wall plastering</li><li>Palletizing robot</li></ul><span class="more">Explore equipment {ARROW}'),
 ('<span class="tag">Sản phẩm & thiết bị trọng tâm</span>\n <h2>Danh mục nổi bật</h2>', '<span class="tag">Key products & equipment</span>\n <h2>Featured</h2>'),
 ('<span class="tag">Ứng dụng & video</span>\n <h2>Thiết bị trong thực tế</h2>\n <p class="lead">Một số video thực tế về thiết bị phun GRC và máy phun vữa. Video và hình ảnh công trình tại Việt Nam sẽ được cập nhật thêm.</p>',
  '<span class="tag">Applications & video</span>\n <h2>Equipment in action</h2>\n <p class="lead">Videos of GRC spraying equipment and mortar spraying machines. Videos and photos of projects in Vietnam will be added.</p>'),
 ('>Xem thêm ứng dụng {ARROW}', '>More applications {ARROW}'),
 ('<span class="tag">Giá trị cốt lõi</span>\n <h2>Building Values', '<span class="tag">Core values</span>\n <h2>Building Values'),
 ('<span class="tag">Cách Core đồng hành</span>\n <h2>Quy trình tư vấn và triển khai</h2>\n <p class="lead">Áp dụng cho các dự án thiết bị và giải pháp công nghệ.</p>',
  '<span class="tag">How we work</span>\n <h2>Consulting and implementation process</h2>\n <p class="lead">For equipment and technology-solution projects.</p>'),
 ('"Core Material JSC — Vật liệu, thiết bị & giải pháp công nghệ cho ngành vật liệu xây dựng"', '"Core Material JSC — Materials, equipment & technology for the construction-materials industry"'),
 # --- about ---
 ('(None, "Giới thiệu")], "Về Core Material JSC", "Kết nối nguyên liệu, thiết bị và giải pháp công nghệ cho ngành vật liệu xây dựng.")',
  '(None, "About")], "About Core Material JSC", "Connecting raw materials, equipment and technology solutions for the construction-materials industry.")'),
 ('<p class="lead" style="max-width:none">Core Material JSC ({e(COMPANY["legal"].title().replace("Cổ Phần","Cổ phần"))}) tập trung vào thương mại nguyên liệu, vật liệu và thiết bị cho ngành vật liệu xây dựng. Chúng tôi làm việc cùng mạng lưới nhà cung cấp và đối tác kỹ thuật để giúp khách hàng chọn đúng vật liệu, đúng thiết bị cho nhu cầu sản xuất và thi công.</p>',
  '<p class="lead" style="max-width:none">Core Material JSC ({e(COMPANY["legal"].title())}) focuses on trading raw materials, materials and equipment for the construction-materials industry. We work with a network of suppliers and technical partners to help customers choose the right materials and equipment for production and construction.</p>'),
 ('<span class="tag">Lĩnh vực hoạt động</span><h2>Ba hướng phát triển</h2>', '<span class="tag">Business areas</span><h2>Three directions</h2>'),
 ('<h3>Thương mại nguyên liệu</h3><p>Cát khô, xi măng trắng, nguyên liệu vật liệu xây dựng và hóa chất chọn lọc. Ưu tiên chất lượng ổn định, truy xuất được nguồn gốc theo lô.</p>',
  '<h3>Raw-material trading</h3><p>Dry sand, white cement, construction raw materials and selected chemicals — with consistent quality and lot traceability.</p>'),
 ('<h3>Thiết bị & giải pháp công nghệ</h3><p>Thiết bị phun GRC/GFRC, máy phun vữa, thiết bị xử lý nguyên liệu và tự động hóa — triển khai cùng các nhà cung cấp và đối tác kỹ thuật.</p>',
  '<h3>Equipment & technology solutions</h3><p>GRC/GFRC spraying equipment, mortar spraying machines, material-processing equipment and automation — delivered with suppliers and technical partners.</p>'),
 ('CORE MATERIALS · ĐỊNH HƯỚNG</span><h3>Sản phẩm mang thương hiệu Core</h3><p>Phát triển dần các sản phẩm mang nhãn Core như cát phân cấp và vật liệu trang trí, với tiêu chuẩn chất lượng và truy xuất lô rõ ràng.</p>',
  'CORE MATERIALS · ROADMAP</span><h3>Core-branded products</h3><p>Gradually developing Core-branded products such as graded sand and decorative materials, with clear quality standards and lot traceability.</p>'),
 ('<span class="tag">Giá trị cốt lõi</span><h2>INTEGRITY', '<span class="tag">Core values</span><h2>INTEGRITY'),
 ('<span class="tag">Đồng hành cùng khách hàng</span><h2>Quy trình tư vấn và triển khai</h2>', '<span class="tag">Working with customers</span><h2>Consulting and implementation process</h2>'),
 ('<span class="tag">Thông tin doanh nghiệp</span><h2>Pháp nhân</h2>', '<span class="tag">Company information</span><h2>Legal entity</h2>'),
 ('<tr><th>Tên doanh nghiệp</th><td>{e(COMPANY["legal"])}</td></tr><tr><th>Tên thương hiệu</th>', '<tr><th>Company name</th><td>{e(COMPANY["legal"])}<br><small>{e(LEGAL_VN)}</small></td></tr><tr><th>Brand</th>'),
 ('<tr><th>Mã số thuế</th>', '<tr><th>Tax code</th>'), ('<tr><th>Địa chỉ</th>', '<tr><th>Address</th>'),
 ('Thông tin về dự án đầu tư và hợp tác: xem trang <a class="more" style="font-size:14px" href="/en/investment/">Hợp tác đầu tư</a>.',
  'For investment and partnership projects, see <a class="more" style="font-size:14px" href="/en/investment/">Investment partnership</a>.'),
 ('"Giới thiệu | Core Material JSC", "Core Material JSC kết nối nguyên liệu, thiết bị và giải pháp công nghệ cho ngành vật liệu xây dựng tại Việt Nam."',
  '"About | Core Material JSC", "Core Material JSC connects raw materials, equipment and technology solutions for the construction-materials industry in Vietnam."'),
 # --- materials ---
 ('alt="Cát {e(n)} {e(r)}"', 'alt="Sand {e(n)} {e(r)}"'),
 ('slot("Ảnh sản phẩm thật")', 'slot("Real product photo")'),
 ('<div><span class="tag">Nguyên liệu & Vật liệu</span><h2>', '<div><span class="tag">Materials</span><h2>'),
 ('>Yêu cầu báo giá {ARROW}', '>Request a quote {ARROW}'),
 ('(None, "Nguyên liệu & Vật liệu")], "Nguyên liệu & Vật liệu", "Nguyên liệu cho nhà máy vật liệu xây dựng và vật liệu hoàn thiện cho công trình: cát khô, xi măng trắng, phụ gia và vật liệu trang trí.")',
  '(None, "Materials")], "Raw materials & Materials", "Raw materials for construction-material plants and finishing materials for projects: dry sand, white cement, admixtures and decorative materials.")'),
 ('cta("Cần mẫu hoặc báo giá vật liệu?", "Cho chúng tôi biết loại vật liệu, quy cách và sản lượng dự kiến.", "/en/contact/#form", "Gửi yêu cầu")',
  'cta("Need samples or a quote?", "Tell us the material, specification and expected volume.", "/en/contact/#form", "Send a request")'),
 ('"Nguyên liệu & Vật liệu: cát khô, xi măng trắng, VAE/RDP, vật liệu trang trí | Core Material JSC", "Cát silica sấy khô phân cỡ, xi măng trắng, phụ gia VAE/RDP, đá mài, hạt thủy tinh và bột màu cho sản xuất vật liệu và thi công."',
  '"Materials: dry sand, white cement, VAE/RDP, decorative materials | Core Material JSC", "Kiln-dried graded silica sand, white cement, VAE/RDP admixtures, terrazzo chips, glass granules and pigments for material production and construction."'),
 # --- equipment ---
 ('(None, "Máy móc & Tự động hóa")], "Core Technology — Máy móc & Tự động hóa", TECH_INTRO)', '(None, "Equipment & Automation")], "Core Technology — Equipment & Automation", TECH_INTRO)'),
 ('<span class="tag">Nhóm thiết bị trọng tâm</span><h2>Ba nhóm thiết bị</h2>', '<span class="tag">Key equipment</span><h2>Three equipment groups</h2>'),
 ('<b>Phun GRC khác phun vữa tô tường thế nào?</b> Thiết bị phun GRC/GFRC dùng để sản xuất cấu kiện bê tông cốt sợi thủy tinh tại xưởng. Máy phun vữa tô tường dùng tại công trình để cơ giới hóa công tác trát tường.',
  '<b>GRC spraying vs. wall plastering?</b> GRC/GFRC spraying equipment is used to produce glass-fibre reinforced concrete elements in the workshop. Wall plastering machines are used on site to mechanise plastering.'),
 ('<span class="tag">Quy trình</span><h2>Tư vấn và triển khai thiết bị</h2>', '<span class="tag">Process</span><h2>Equipment consulting and implementation</h2>'),
 ('cta("Trao đổi nhu cầu thiết bị", "Mô tả ứng dụng, năng suất mong muốn và địa điểm lắp đặt — chúng tôi sẽ cùng nhà cung cấp đề xuất cấu hình phù hợp.", "/en/contact/#form", "Trao đổi nhu cầu thiết bị")',
  'cta("Discuss your equipment needs", "Describe the application, target output and installation site — we will propose a suitable configuration with our suppliers.", "/en/contact/#form", "Discuss equipment needs")'),
 ('"Máy móc & Tự động hóa: phun GRC, máy phun vữa, robot xếp pallet | Core Material JSC", "Thiết bị phun GRC/GFRC, máy phun vữa tô tường, robot bốc xếp & xếp pallet cho ngành vật liệu xây dựng — tư vấn, cung cấp qua mạng lưới nhà cung cấp."',
  '"Equipment & Automation: GRC spraying, mortar spraying, palletizing robots | Core Material JSC", "GRC/GFRC spraying equipment, wall plastering machines, bag handling & palletizing robots for the construction-materials industry — consulting and supply through our supplier network."'),
 ('slot("Ảnh thiết bị thật có quyền sử dụng")', 'slot("Licensed real equipment photo")'),
 ('"Chờ catalogue / tài liệu xác nhận"', '"Pending catalogue / confirmed data"'),
 ("'<div class=\"note\">Thông số kỹ thuật, cấu hình và catalogue được cung cấp theo nhu cầu cụ thể. Vui lòng liên hệ để nhận tài liệu.</div>'",
  "'<div class=\"note\">Specifications, configurations and catalogues are provided per specific requirement. Please contact us for documents.</div>'"),
 ('<b>Lưu ý:</b>', '<b>Note:</b>'),
 ('<span class="tag">Giải pháp đồng bộ</span><h2>Không chỉ là cái máy</h2><p class="lead">Máy phun vữa phát huy hiệu quả khi đi cùng vữa phù hợp, đội ngũ được đào tạo và quy trình vận hành chuẩn.</p>',
  '<span class="tag">Complete solution</span><h2>More than a machine</h2><p class="lead">A mortar spraying machine delivers results when combined with the right mortar, a trained crew and a standard operating routine.</p>'),
 ('<span class="tag">Video</span><h2>Thiết bị hoạt động</h2>', '<span class="tag">Video</span><h2>Equipment in operation</h2>'),
 ('slot("Video thiết bị hoạt động")', 'slot("Equipment operation video")'),
 ('("/en/equipment/", "Máy móc & Tự động hóa"), (None, q["name"])', '("/en/equipment/", "Equipment & Automation"), (None, q["name"])'),
 ('<h3 style="font-size:18px;margin:22px 0 6px">Thông số kỹ thuật</h3>', '<h3 style="font-size:18px;margin:22px 0 6px">Specifications</h3>'),
 ('>Trao đổi nhu cầu thiết bị {ARROW}</a><a class="btn btn-line" href="/en/equipment/">← Tất cả thiết bị</a>', '>Discuss equipment needs {ARROW}</a><a class="btn btn-line" href="/en/equipment/">← All equipment</a>'),
 ('<span class="tag">Quy trình</span><h2>Tư vấn và triển khai</h2>', '<span class="tag">Process</span><h2>Consulting and implementation</h2>'),
 # --- applications ---
 ('("Nhà máy vữa khô, keo dán gạch", "Cát khô phân cỡ, xi măng trắng, phụ gia VAE/RDP; tự động hóa bốc xếp và xếp pallet.", "/en/materials/")',
  '("Dry-mortar & tile-adhesive plants", "Graded dry sand, white cement, VAE/RDP admixtures; automated bag handling and palletizing.", "/en/materials/")'),
 ('("Xưởng sản xuất cấu kiện GRC/GFRC", "Thiết bị phun GRC và vật liệu nền cho cấu kiện kiến trúc.",', '("GRC/GFRC precast workshops", "GRC spraying equipment and base materials for architectural elements.",'),
 ('("Nhà thầu hoàn thiện", "Máy phun vữa tô tường giúp cơ giới hóa công tác trát, tăng tiến độ.",', '("Finishing contractors", "Wall plastering machines mechanise plastering and speed up progress.",'),
 ('("Terrazzo & trang trí kiến trúc", "Đá mài, hạt thủy tinh, bột màu và xi măng trắng.",', '("Terrazzo & architectural decoration", "Terrazzo chips, glass granules, pigments and white cement.",'),
 ('(None, "Ứng dụng & Video")], "Ứng dụng & Video", "Vật liệu và thiết bị theo từng lĩnh vực ứng dụng, kèm video thực tế.")', '(None, "Applications & Video")], "Applications & Video", "Materials and equipment by application, with real videos.")'),
 ('<span class="tag">Lĩnh vực ứng dụng</span><h2>Giải pháp theo nhu cầu</h2>', '<span class="tag">Applications</span><h2>Solutions by need</h2>'),
 ('<span class="k">Ứng dụng</span>', '<span class="k">Application</span>'), ('>Xem giải pháp {ARROW}', '>See solution {ARROW}'),
 ('<h2>Video thực tế</h2><p class="lead">Video từ nhà cung cấp thiết bị. Video công trình tại Việt Nam sẽ được cập nhật.</p>', '<h2>Videos</h2><p class="lead">Videos from equipment suppliers. Project videos from Vietnam will be added.</p>'),
 ('slot("Video / ảnh dự án tại Việt Nam (khi có quyền sử dụng)")', 'slot("Project video / photos in Vietnam (when licensed)")'),
 ('"Ứng dụng & Video | Core Material JSC", "Ứng dụng vật liệu và thiết bị cho nhà máy vữa khô, xưởng GRC, nhà thầu hoàn thiện và trang trí kiến trúc — kèm video thực tế."',
  '"Applications & Video | Core Material JSC", "Materials and equipment for dry-mortar plants, GRC workshops, finishing contractors and architectural decoration — with real videos."'),
 # --- investment ---
 ('(None, "Hợp tác đầu tư")], "Hợp tác đầu tư", "Core Material JSC chào đón trao đổi với các đối tác quan tâm đến chuỗi cung ứng vật liệu xây dựng tại phía Nam.")',
  '(None, "Investment partnership")], "Investment partnership", "Core Material JSC welcomes discussions with partners interested in the construction-materials supply chain in Southern Vietnam.")'),
 ('Chúng tôi đang nghiên cứu các phương án hợp tác cho nguồn cát và chế biến cát khô, cũng như các dự án vật liệu xây dựng khác. Các phương án đầu tư được đánh giá theo nhu cầu thị trường, hiệu quả và điều kiện thực tế, và chỉ triển khai khi được Hội đồng quản trị phê duyệt.',
  'We are studying partnership options for sand sources and dry-sand processing, as well as other construction-material projects. Investment options are assessed against market demand, returns and actual conditions, and are only implemented after Board approval.'),
 ('>Đối tác chúng tôi mong muốn trao đổi</h3>', '>Partners we would like to talk to</h3>'),
 ('Đơn vị sở hữu hoặc khai thác nguồn cát hợp pháp, bãi, phương tiện vận chuyển', 'Owners or operators of licensed sand sources, yards and transport'),
 ('Đối tác tài chính quan tâm lĩnh vực vật liệu xây dựng', 'Financial partners interested in construction materials'),
 ('Nhà máy có năng lực gia công, đóng gói vật liệu', 'Plants with toll-processing and packing capacity'),
 ('Thông tin chi tiết về phương án hợp tác được trao đổi trực tiếp sau khi hai bên ký thỏa thuận bảo mật.', 'Details of partnership options are shared directly after both parties sign a non-disclosure agreement.'),
 ('contact_href("Hợp tác đầu tư")}">Đăng ký trao đổi {ARROW}', 'contact_href("Investment partnership")}">Get in touch {ARROW}'),
 ('"Hợp tác đầu tư | Core Material JSC", "Core Material JSC chào đón trao đổi hợp tác về nguồn cát, chế biến cát khô và các dự án vật liệu xây dựng."',
  '"Investment partnership | Core Material JSC", "Core Material JSC welcomes partnership discussions on sand sources, dry-sand processing and construction-material projects."'),
 # --- contact ---
 ('kind = "mat" if grp.startswith("Nguyên") else ("eq" if grp.startswith("Máy") else "other")', 'kind = "mat" if grp.startswith("Raw") else ("eq" if grp.startswith("Equipment") else "other")'),
 ('data-language="vi"', 'data-language="en"'),
 ('(None, "Liên hệ")], "Liên hệ tư vấn", "Gửi nhu cầu vật liệu hoặc thiết bị — Core Material sẽ phản hồi qua điện thoại hoặc email.")', '(None, "Contact")], "Contact us", "Send us your material or equipment needs — Core Material will reply by phone or email.")'),
 ('<span class="tag">Thông tin liên hệ</span><h2>Trao đổi trực tiếp</h2>\n  <p class="lead">Anh/chị có thể gọi hotline, gửi email hoặc điền form bên cạnh.</p>',
  '<span class="tag">Contact information</span><h2>Talk to us</h2>\n  <p class="lead">Call our hotline, send an email or fill in the form. We reply in English or Vietnamese.</p>'),
 ('<small>Văn phòng</small>', '<small>Office</small>'), ('<small>Doanh nghiệp</small>{e(COMPANY["legal"])} · MST', '<small>Company</small>{e(COMPANY["legal"])} · Tax code'),
 ('<legend>Nhóm quan tâm <span class="req">*</span></legend>', '<legend>Interested in <span class="req">*</span></legend>'),
 ('<label for="ten">Họ tên <span', '<label for="ten">Full name <span'), ('<label for="cty">Công ty</label>', '<label for="cty">Company</label>'),
 ('<label for="sdt">Điện thoại <span', '<label for="sdt">Phone <span'),
 ('<label for="sanluong">Sản lượng vật liệu dự kiến / tháng</label>', '<label for="sanluong">Expected volume / month</label>'),
 ('<option value="">— Chọn —</option><option>Dưới 10 tấn</option><option>10 – 100 tấn</option><option>100 – 500 tấn</option><option>Trên 500 tấn</option><option>Chưa xác định</option>',
  '<option value="">— Select —</option><option>Under 10 t</option><option>10 – 100 t</option><option>100 – 500 t</option><option>Over 500 t</option><option>Not decided</option>'),
 ('<label for="ungdung">Ứng dụng thiết bị</label><input id="ungdung" name="ungdung" maxlength="200" placeholder="VD: sản xuất tấm GRC, tô tường chung cư, xếp pallet bao 40 kg…">',
  '<label for="ungdung">Application</label><input id="ungdung" name="ungdung" maxlength="200" placeholder="e.g. GRC panel production, apartment plastering, palletizing 40 kg bags…">'),
 ('<label for="nangsuat">Năng suất mong muốn</label><input id="nangsuat" name="nangsuat" maxlength="100" placeholder="VD: m²/ngày, bao/giờ…">',
  '<label for="nangsuat">Target output</label><input id="nangsuat" name="nangsuat" maxlength="100" placeholder="e.g. m²/day, bags/hour…">'),
 ('<label for="diadiem">Địa điểm lắp đặt / thi công</label>', '<label for="diadiem">Installation / project location</label>'),
 ('id="lbl-nd">Nội dung / mô tả nhu cầu</label><textarea id="noidung" name="noidung" maxlength="3000" placeholder="Quy cách, cỡ hạt, điều kiện mặt bằng, thời gian dự kiến…">',
  'id="lbl-nd">Message / description</label><textarea id="noidung" name="noidung" maxlength="3000" placeholder="Specification, grain size, site conditions, expected timing…">'),
 ('id="send">Gửi yêu cầu {ARROW}', 'id="send">Send request {ARROW}'),
 ("const fallback='Vui lòng gọi <a href=\"tel:{TEL}\"><b>{COMPANY[\"hotline\"]}</b></a> hoặc email <a href=\"mailto:{COMPANY[\"email\"]}\"><b>{COMPANY[\"email\"]}</b></a> để được hỗ trợ ngay.';",
  "const fallback='Please call <a href=\"tel:{TEL}\"><b>{COMPANY[\"hotline\"]}</b></a> or email <a href=\"mailto:{COMPANY[\"email\"]}\"><b>{COMPANY[\"email\"]}</b></a> for immediate help.';"),
 ("d.t=Date.now()-t0;", "d.t=Date.now()-t0;d.lang='en';"),
 ("'Vui lòng chọn ít nhất một nhóm quan tâm.'", "'Please select at least one interest.'"),
 ("'Vui lòng nhập họ tên và số điện thoại hợp lệ.'", "'Please enter your name and a valid phone number.'"),
 ("'Đang gửi yêu cầu…'", "'Sending…'"),
 ("'<b>Core Material đã nhận được yêu cầu của anh/chị.</b> Chúng tôi sẽ liên hệ lại sớm. Mã yêu cầu: '", "'<b>Thank you — Core Material has received your request.</b> We will contact you shortly. Reference: '"),
 ("'<b>Form trực tuyến đang được hoàn thiện, yêu cầu CHƯA được gửi.</b> '", "'<b>The online form is not available yet — your request was NOT sent.</b> '"),
 ("'Không xác minh được chống spam. Vui lòng thử lại. '", "'Spam check failed. Please try again. '"),
 ("'<b>Chưa gửi được yêu cầu.</b> '", "'<b>Your request could not be sent.</b> '"),
 ("'<b>Chưa gửi được yêu cầu (lỗi kết nối).</b> '", "'<b>Your request could not be sent (connection error).</b> '"),
 ('"Liên hệ tư vấn | Core Material JSC", "Liên hệ Core Material JSC: tư vấn vật liệu (cát khô, xi măng trắng, VAE/RDP) và thiết bị (phun GRC, phun vữa, robot xếp pallet)."',
  '"Contact | Core Material JSC", "Contact Core Material JSC for materials (dry sand, white cement, VAE/RDP) and equipment (GRC spraying, mortar spraying, palletizing robots)."'),
]

for a, b in R:
    if a not in src:
        sys.exit("build_site_en: template string not found (update build_site_en.py):\n  " + a[:120])
    src = src.replace(a, b)

exec(compile(src, "build_site_en(generated)", "exec"))

# Fail if Vietnamese text leaked into the English pages (address/legal VN name are allowed).
VN = re.compile(r"[ăâđêôơưĂÂĐÊÔƠƯàáảãạằắẳẵặầấẩẫậèéẻẽẹềếểễệìíỉĩịòóỏõọồốổỗộờớởỡợùúủũụừứửữựỳýỷỹỵ]")
bad = []
for d, _, fs in os.walk(os.path.join(ROOT, "en")):
    for f in fs:
        t = open(os.path.join(d, f), encoding="utf-8").read()
        t = t.replace(LEGAL_VN, "")
        t = re.sub(r'<script type="application/ld\+json">.*?</script>', "", t, flags=re.S)
        for m in VN.finditer(t):
            bad.append((os.path.relpath(os.path.join(d, f), ROOT), t[max(0, m.start()-40):m.end()+40].replace("\n", " ")))
            break
if bad:
    for b in bad: print("VN text in", b)
    sys.exit(1)
print("Built EN", "PREVIEW" if PREVIEW else "PRODUCTION", len(PATHS), "pages")
