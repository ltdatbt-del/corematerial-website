# -*- coding: utf-8 -*-
"""Nội dung bài viết cho corematerial.info.
Thêm bài mới: thêm một dict vào ARTICLES rồi chạy  python3 tools/build_info.py
"""

CATEGORIES = {
    "vat-lieu":   ("Vật liệu",             "Đặc tính, tiêu chuẩn và cách chọn vật liệu nền cho vữa khô, keo dán gạch, terrazzo."),
    "nghien-cuu": ("Nghiên cứu & Xu hướng", "Những hướng nghiên cứu mới về vật liệu xây dựng carbon thấp và kinh tế tuần hoàn."),
    "may-moc":    ("Máy móc & Công nghệ",  "Nguyên lý, vận hành và lựa chọn thiết bị sản xuất vật liệu."),
    "khcn":       ("KHCN & Chính sách",    "Khoa học công nghệ, chính sách và thị trường vật liệu tại Việt Nam."),
}

ARTICLES = [
# ---------------------------------------------------------------- 1
{
"slug": "cat-kho-cong-nghiep-do-am-mo-dun-do-lon",
"cat": "vat-lieu",
"date": "05/11/2026",
"read": 7,
"img": "cat-xam.jpg",
"title": "Cát khô công nghiệp cho vữa khô: độ ẩm, mô đun độ lớn và vì sao chúng quyết định chất lượng",
"excerpt": "Cát chiếm phần lớn khối lượng một bao vữa khô hay keo dán gạch. Hai chỉ số đơn giản – độ ẩm và mô đun độ lớn – quyết định bao vữa có vón cục, có dễ thi công và có đạt cường độ hay không.",
"body": """
<p>Trong một bao vữa khô trộn sẵn hay keo dán gạch, cát thường chiếm phần lớn khối lượng. Xi măng, phụ gia polymer, cellulose ether… chỉ chiếm phần nhỏ nhưng rất nhạy cảm. Vì vậy chất lượng cát không chỉ là chuyện “cát sạch hay bẩn” mà là bài toán kiểm soát <b>độ ẩm</b>, <b>cấp phối hạt</b> và <b>tạp chất</b>.</p>

<h2>1. Độ ẩm: kẻ thù thầm lặng của vữa khô</h2>
<p>Cát dùng cho vữa trộn ướt tại công trường có thể ẩm vài phần trăm mà không sao. Nhưng với sản phẩm <b>trộn khô đóng bao</b>, nước trong cát sẽ bắt đầu phản ứng với xi măng ngay trong bao: vữa vón cục, đóng tảng, giảm thời gian lưu kho và giảm cường độ khi thi công. Phụ gia bột như RDP hay cellulose ether cũng có thể bị hút ẩm, mất tác dụng.</p>
<p>Thực tế sản xuất, các nhà máy vữa khô thường yêu cầu cát có độ ẩm <b>dưới 0,5%</b>. Để đạt được, cát phải đi qua lò sấy (thường là lồng sấy quay), sau đó được làm nguội và lưu trong silo hoặc bao Jumbo có lót chống ẩm.</p>
<div class="note"><b>Mẹo kiểm tra nhanh:</b> cân một mẫu cát, sấy ở khoảng 105–110 °C đến khối lượng không đổi rồi cân lại. Phần chênh lệch chia cho khối lượng sau sấy chính là độ ẩm. Phòng QC nên làm việc này cho từng lô nhập.</div>

<h2>2. Mô đun độ lớn (FM): một con số tóm tắt cả đường cấp phối</h2>
<p>Mô đun độ lớn được tính bằng tổng phần trăm lượng sót tích lũy trên bộ sàng tiêu chuẩn chia cho 100. FM càng nhỏ, cát càng mịn. Trong vữa khô, người ta thường tách cát thành nhiều cỡ để phối trộn theo công thức:</p>
<ul>
<li><b>Cát mịn (FM khoảng 1,5):</b> cho vữa tô hoàn thiện, bột trét gốc xi măng, keo dán gạch – cần bề mặt mịn, dễ cán.</li>
<li><b>Cát trung (FM khoảng 2,0–2,5):</b> cho vữa xây, vữa tô lót, vữa tự san phẳng lớp dày – cần khung hạt chắc, ít co ngót.</li>
</ul>
<p>Điều quan trọng không chỉ là con số FM mà là <b>sự ổn định giữa các lô</b>. Cát có FM dao động sẽ làm lượng nước trộn, độ dẻo và độ bám dính của vữa thay đổi – khách hàng sẽ cảm nhận ngay ngoài công trường.</p>

<h2>3. Tạp chất: bùn, sét và muối</h2>
<p>Hàm lượng bùn, bụi, sét cao làm tăng lượng nước yêu cầu, giảm bám dính và gây nứt chân chim. Cát nhiễm muối (cát biển, cát cửa sông chưa rửa) có nguy cơ gây ăn mòn cốt thép và loang muối trên bề mặt. Với cốt liệu cho bê tông và vữa, các chỉ tiêu này được quy định trong <b>TCVN 7570:2006</b>; nhà sản xuất vữa khô thường đặt ngưỡng nội bộ khắt khe hơn.</p>

<h2>4. Quy trình chuẩn của một dây chuyền cát khô</h2>
<ol>
<li>Tiếp nhận cát ướt, lọc tạp chất thô (rác, sỏi lớn).</li>
<li>Sấy trong lồng sấy quay đến độ ẩm mục tiêu.</li>
<li>Lọc bụi bằng hệ thống túi lọc xung để giữ môi trường và thu hồi hạt mịn.</li>
<li>Sàng rung phân loại thành các cỡ hạt theo đơn hàng.</li>
<li>Đóng bao Jumbo hoặc bao nhỏ, lưu kho khô ráo; ghi nhãn lô để truy xuất.</li>
</ol>

<h2>Kết luận</h2>
<p>Với nhà máy vữa khô, chi phí cho cát khô đạt chuẩn thường nhỏ hơn rất nhiều so với chi phí khiếu nại, đổi trả do vữa vón cục hay kém bám dính. Một nguồn cát khô ổn định về độ ẩm và cấp phối là nền móng cho mọi công thức tốt.</p>
""",
"sources": [
    ("TCVN 7570:2006 – Cốt liệu cho bê tông và vữa – Yêu cầu kỹ thuật", None),
],
},
# ---------------------------------------------------------------- 2
{
"slug": "vae-va-rdp-khac-nhau-the-nao",
"cat": "vat-lieu",
"date": "05/11/2026",
"read": 6,
"img": None,
"title": "VAE và RDP: hai dạng của cùng một “chất keo” – khi nào dùng loại nào?",
"excerpt": "VAE dạng lỏng và RDP dạng bột đều giúp vữa bám dính, dẻo dai và chống thấm tốt hơn. Hiểu đúng bản chất giúp nhà sản xuất chọn đúng loại, đúng liều và tránh lãng phí.",
"body": """
<p>Trong ngành hóa chất xây dựng, hai cái tên <b>VAE</b> và <b>RDP</b> xuất hiện gần như trong mọi công thức keo dán gạch, chống thấm, bột trét hay vữa cải tiến. Chúng có quan hệ rất gần nhau nhưng được dùng ở hai “thế giới” khác nhau: hệ lỏng và hệ khô.</p>

<h2>VAE là gì?</h2>
<p>VAE (Vinyl Acetate – Ethylene) là nhũ tương copolymer dạng <b>lỏng</b>, màu trắng sữa. Khi nước bay hơi, các hạt polymer liên kết lại thành màng dẻo, bám dính tốt. VAE được dùng trực tiếp trong:</p>
<ul>
<li>Chống thấm gốc xi măng – polymer hai thành phần (phần lỏng là VAE).</li>
<li>Keo dán, sơn lót, phụ gia trộn vữa tại công trường.</li>
<li>Làm nguyên liệu để sản xuất RDP.</li>
</ul>

<h2>RDP là gì?</h2>
<p>RDP (Redispersible Polymer Powder – bột polymer tái phân tán) thực chất thường được làm từ chính nhũ tương polymer như VAE, đem <b>sấy phun</b> thành bột cùng chất keo bảo vệ và chất chống vón. Điểm đặc biệt: khi trộn vữa với nước, bột RDP <b>tái phân tán</b> trở lại thành nhũ tương, rồi tạo màng polymer bên trong vữa.</p>
<p>Nhờ ở dạng bột, RDP có thể trộn sẵn vào sản phẩm khô đóng bao – điều mà VAE lỏng không làm được. Đây là “chìa khóa” của các sản phẩm như:</p>
<ul>
<li>Keo dán gạch, đặc biệt các loại có yêu cầu bám dính cao và biến dạng (theo phân loại C1, C2 của EN 12004).</li>
<li>Bột trét tường, vữa tô mỏng, vữa tự san phẳng.</li>
<li>Vữa dán và vữa trát cho hệ cách nhiệt ngoài (ETICS).</li>
</ul>

<h2>So sánh nhanh</h2>
<table>
<tr><th></th><th>VAE</th><th>RDP</th></tr>
<tr><td>Dạng</td><td>Nhũ tương lỏng</td><td>Bột khô</td></tr>
<tr><td>Dùng cho</td><td>Hệ 2 thành phần, trộn tại chỗ</td><td>Sản phẩm trộn khô 1 thành phần</td></tr>
<tr><td>Bảo quản</td><td>Tránh đông lạnh, nhiệt độ cao</td><td>Tránh ẩm, chống vón</td></tr>
<tr><td>Ưu điểm</td><td>Giá trên đơn vị polymer thường thấp hơn</td><td>Tiện lợi, đồng đều, dễ đóng bao</td></tr>
</table>

<h2>Chọn RDP: nhìn vào đâu?</h2>
<ul>
<li><b>Nhiệt độ chuyển thủy tinh (Tg):</b> Tg thấp cho màng mềm, dẻo – hợp keo dán gạch biến dạng; Tg cao hơn cho màng cứng – hợp vữa cần cường độ bề mặt.</li>
<li><b>Nhiệt độ tạo màng tối thiểu (MFFT):</b> quyết định khả năng tạo màng khi thi công ở nhiệt độ thấp.</li>
<li><b>Hàm lượng tro:</b> phản ánh lượng chất độn khoáng; tro quá cao nghĩa là ít polymer thực.</li>
<li><b>Tính kỵ nước:</b> một số loại RDP có thêm thành phần kỵ nước cho vữa ngoài trời, chống thấm.</li>
</ul>
<div class="note"><b>Lưu ý:</b> liều lượng RDP phụ thuộc rất lớn vào công thức (loại xi măng, cát, cellulose ether…). Cách làm đúng là thử nghiệm trong phòng Lab trước khi chốt công thức sản xuất, thay vì sao chép tỷ lệ từ sản phẩm khác.</div>

<h2>Kết luận</h2>
<p>VAE và RDP không cạnh tranh mà bổ sung cho nhau: VAE cho hệ lỏng và hai thành phần, RDP cho sản phẩm trộn khô. Chọn đúng loại, đúng thông số và thử nghiệm kỹ là cách tối ưu chất lượng mà không đội giá thành.</p>
""",
"sources": [
    ("EN 12004 – Adhesives for ceramic tiles (phân loại C1, C2, S1, S2)", None),
],
},
# ---------------------------------------------------------------- 3
{
"slug": "xi-mang-carbon-thap-lc3",
"cat": "nghien-cuu",
"date": "05/11/2026",
"read": 6,
"img": None,
"title": "LC3 – xi măng đá vôi & đất sét nung: hướng đi giảm khoảng 40% CO₂ cho ngành xi măng",
"excerpt": "Thay một nửa clinker bằng đất sét nung và đá vôi, LC3 hứa hẹn cắt giảm đáng kể phát thải mà vẫn giữ tính năng cơ học. Đây là một trong những hướng nghiên cứu được quan tâm nhất hiện nay.",
"body": """
<p>Sản xuất clinker – thành phần chính của xi măng poóc lăng – cần nung đá vôi ở nhiệt độ rất cao, giải phóng lượng lớn CO₂ cả từ nhiên liệu lẫn từ phản ứng phân hủy đá vôi. Vì vậy, giảm tỷ lệ clinker trong xi măng là con đường thực tế nhất để giảm phát thải trên quy mô lớn.</p>

<h2>LC3 là gì?</h2>
<p>LC3 (Limestone Calcined Clay Cement) là xi măng hỗn hợp ba thành phần: clinker, <b>đất sét nung</b> và <b>đá vôi</b> (cộng một ít thạch cao). Một tỷ lệ tham khảo thường được nhắc đến là khoảng 50% clinker, 30% đất sét nung, 15% đá vôi và 5% thạch cao.</p>
<p>Đất sét chỉ cần nung ở khoảng 650–950 °C – thấp hơn nhiều so với lò clinker – và không có phản ứng phân hủy đá vôi, nên lượng CO₂ phát sinh thấp hơn hẳn.</p>

<h2>Vì sao ba thành phần lại “hợp nhau”?</h2>
<p>Điểm hay của LC3 nằm ở hiệu ứng cộng hưởng: nhôm hoạt tính trong đất sét nung phản ứng với cacbonat trong đá vôi, cộng với phản ứng puzolan của đất sét và hiệu ứng lấp đầy của bột đá vôi. Các nghiên cứu cho thấy hệ ba thành phần này phản ứng hiệu quả hơn so với chỉ trộn đất sét nung với xi măng.</p>

<h2>Kết quả nghiên cứu nói gì?</h2>
<ul>
<li>Nhóm nghiên cứu tại EPFL (Thụy Sĩ) – nơi khởi xướng LC3 – cho biết LC3 đạt tính năng cơ học tương đương xi măng poóc lăng, bền hơn trước xâm thực clorua, hạn chế phản ứng kiềm – silic và giảm khoảng 40% phát thải CO₂.</li>
<li>Một số nghiên cứu thí nghiệm gần đây báo cáo mức giảm phát thải có thể lên đến khoảng 50% tùy công thức.</li>
<li>Đất sét nung đã bắt đầu được thương mại hóa như một nguyên liệu cho ngành xi măng tại nhiều thị trường.</li>
</ul>

<h2>Ý nghĩa với vữa khô và xi măng trắng</h2>
<p>Tư duy của LC3 – <b>thay clinker bằng vật liệu khoáng có phát thải thấp</b> – cũng là tư duy của các nhà sản xuất vữa khô và xi măng trắng phối trộn: dùng xỉ lò cao, bột đá, đất sét nung… để vừa giảm giá vốn, vừa giảm dấu chân carbon. Thách thức nằm ở việc kiểm soát chất lượng nguyên liệu đầu vào và tối ưu cấp phối trong phòng Lab.</p>
<div class="note"><b>Góc nhìn Core Material:</b> xu hướng giảm clinker cũng là hướng mà nhiều nhà sản xuất vữa khô và xi măng hỗn hợp đang theo đuổi. Việc áp dụng cần dựa trên thử nghiệm cụ thể cho từng công thức và nguồn nguyên liệu.</div>
""",
"sources": [
    ("Scrivener K. và cộng sự – Limestone Calcined Clay Cements (LC3), EPFL Infoscience", "https://infoscience.epfl.ch/record/286379"),
    ("Limestone calcined clay cement LC3 – Designing Buildings Wiki", "https://www.designingbuildings.co.uk/wiki/Limestone_calcined_clay_cement_LC3"),
    ("Synthesis of LC3 using various clays – SN Applied Sciences (Springer)", "https://link.springer.com/10.1007/s42452-025-07298-2"),
],
},
# ---------------------------------------------------------------- 4
{
"slug": "thuy-tinh-tai-che-trong-terrazzo",
"cat": "nghien-cuu",
"date": "05/11/2026",
"read": 6,
"img": "da-ho-phach.jpg",
"title": "Thủy tinh tái chế trong terrazzo: đẹp, bền và là một câu chuyện kinh tế tuần hoàn",
"excerpt": "Từ chai lọ, kính vụn đến những mặt sàn terrazzo lấp lánh: hạt thủy tinh tái chế đang trở thành cốt liệu được giới thiết kế ưa chuộng. Nhưng muốn dùng tốt, cần hiểu cả ưu điểm lẫn rủi ro kỹ thuật.",
"body": """
<p>Terrazzo – vật liệu ghép từ hạt đá, kính trong nền xi măng hoặc epoxy rồi mài bóng – đang quay trở lại mạnh mẽ trong kiến trúc hiện đại. Một trong những động lực lớn là <b>hạt thủy tinh tái chế</b>: màu sắc rực rỡ, độ trong độc đáo và câu chuyện bền vững hấp dẫn.</p>

<h2>Xu hướng trên thế giới</h2>
<p>Theo Hiệp hội Terrazzo & Mosaic Quốc gia Hoa Kỳ (NTMA), trong các công trình gửi dự giải thưởng của hiệp hội vài năm gần đây, <b>hơn hai phần ba</b> có sử dụng cốt liệu thủy tinh. Các nhà sản xuất cốt liệu có thể cung cấp hàng chục màu, nhiều cỡ hạt, và việc dùng thủy tinh tái chế còn giúp công trình đạt điểm trong các hệ thống chứng nhận công trình xanh.</p>

<h2>Nghiên cứu nói gì?</h2>
<ul>
<li>Các nghiên cứu thực nghiệm thay một phần cốt liệu thô bằng thủy tinh nghiền (10–30% theo khối lượng) cho thấy thủy tinh có thể dùng được cho cả bê tông kết cấu lẫn bê tông trang trí, terrazzo.</li>
<li>Một nghiên cứu sản xuất terrazzo dạng “thạch anh” từ thủy tinh tái chế trên nền xi măng trắng và bột đá cho bề mặt chắc đặc, không nứt, bóng đẹp sau mài – mô phỏng được vẻ ngoài của thạch anh tự nhiên.</li>
</ul>

<h2>Lưu ý kỹ thuật: phản ứng kiềm – silic</h2>
<p>Thủy tinh giàu silic vô định hình. Trong môi trường kiềm của xi măng, thủy tinh có nguy cơ gây <b>phản ứng kiềm – silic (ASR)</b>, tạo gel trương nở dẫn đến nứt về lâu dài. Các cách kiểm soát thường gặp:</p>
<ul>
<li>Dùng nền <b>epoxy</b> thay cho xi măng (terrazzo epoxy).</li>
<li>Bổ sung phụ gia khoáng hoạt tính (xỉ lò cao, puzolan, đất sét nung…) để giảm kiềm tự do.</li>
<li>Kiểm soát cỡ hạt và chọn loại thủy tinh phù hợp, thử nghiệm mẫu trước khi thi công lớn.</li>
</ul>

<h2>Từ phế liệu đến vật liệu cao cấp</h2>
<p>Chuỗi giá trị của hạt thủy tinh trang trí gồm: thu gom phế liệu thủy tinh, gốm, đá → làm sạch → nghiền → sàng phân cỡ → <b>tách màu bằng máy quang học</b> → (tùy chọn) bo tròn cạnh → đóng gói theo màu và cỡ. Khâu tách màu quyết định độ đồng đều giữa các lô – yếu tố mà kiến trúc sư và nhà thầu terrazzo đặc biệt quan tâm.</p>
<div class="note"><b>Góc nhìn Core Material:</b> Core Material cung cấp vật liệu trang trí như hạt đá mài, hạt thủy tinh và bột màu; vật liệu tái chế là một hướng phát triển đang được đánh giá về nguồn, độ ổn định và điều kiện pháp lý.</div>
""",
"sources": [
    ("Trending in Terrazzo – Glass Aggregates, National Terrazzo & Mosaic Association", "https://ntma.com/trending-in-terrazzo/"),
    ("Study on Production of Decorative Concrete with Recycled Crushed Glass – Addis Ababa University (2018)", "https://etd.aau.edu.et/items/12d05934-8796-4e7f-b160-9e8e1e7a530c"),
    ("Implementación de vidrio reciclado en la fabricación de terrazo tipo cuarzo – Editorial INUDI", "https://editorial.inudi.edu.pe/index.php/editorialinudi/catalog/download/185/370/518?inline=1"),
],
},
# ---------------------------------------------------------------- 5
{
"slug": "may-say-cat-long-quay-3-tang",
"cat": "may-moc",
"date": "05/11/2026",
"read": 6,
"img": None,
"title": "Máy sấy cát lồng quay 3 tầng (Triple Pass Rotary Dryer): nguyên lý và những điểm cần biết khi đầu tư",
"excerpt": "Ba ống sấy lồng vào nhau giúp kéo dài đường đi của cát trong một thiết bị gọn, tận dụng nhiệt tốt hơn. Đây là công nghệ phổ biến nhất cho dây chuyền cát khô công suất vừa.",
"body": """
<p>Để sản xuất cát khô cho vữa khô, keo dán gạch, phải đưa độ ẩm cát từ mức vài phần trăm xuống dưới 0,5%. Thiết bị phổ biến nhất cho nhiệm vụ này ở quy mô vài tấn đến vài chục tấn mỗi giờ là <b>máy sấy lồng quay 3 tầng</b>.</p>

<h2>Cấu tạo</h2>
<p>Thay vì một ống sấy dài, máy gồm <b>ba ống đồng tâm lồng vào nhau</b>, cùng quay trên một trục. Bên trong mỗi ống có các cánh nâng (cánh xáo) để hất cát lên, cho cát rơi xuyên qua dòng khí nóng.</p>

<h2>Nguyên lý hoạt động</h2>
<ol>
<li>Cát ướt được cấp vào <b>ống trong cùng</b>, nơi tiếp xúc với dòng khí nóng nhất từ lò đốt.</li>
<li>Cát di chuyển hết chiều dài ống trong, chuyển sang <b>ống giữa</b> và đi ngược chiều lại.</li>
<li>Cuối cùng cát vào <b>ống ngoài</b>, tiếp tục được sấy và đi ra ở cửa xả.</li>
</ol>
<p>Nhờ đi “zigzag” ba lượt, quãng đường của cát dài gấp nhiều lần chiều dài máy. Ống trong nóng nhất được bao bởi hai ống ngoài, nên nhiệt thất thoát ra môi trường ít hơn so với máy sấy một ống. Kết quả là máy <b>gọn hơn</b>, <b>tiết kiệm mặt bằng</b> và <b>hiệu suất nhiệt tốt</b>.</p>

<h2>Các hệ thống đi kèm</h2>
<ul>
<li><b>Lò đốt:</b> dùng củi, than, trấu viên hoặc gas. Nên chọn thiết kế có thể chuyển đổi nhiên liệu để chủ động chi phí.</li>
<li><b>Lọc bụi túi xung (pulse jet):</b> bắt buộc để đạt yêu cầu môi trường và thu hồi hạt mịn có giá trị.</li>
<li><b>Sàng rung:</b> phân loại cát sau sấy theo cỡ hạt.</li>
<li><b>Băng tải, gầu tải, silo và máy đóng bao:</b> quyết định nhịp sản xuất thực tế của cả dây chuyền.</li>
<li><b>Tủ điện, biến tần:</b> điều chỉnh tốc độ quay và lưu lượng cấp liệu theo độ ẩm đầu vào.</li>
</ul>

<h2>Những câu hỏi nên đặt ra khi đầu tư</h2>
<ul>
<li>Công suất thiết kế được tính với <b>độ ẩm đầu vào</b> bao nhiêu? Cát ẩm hơn thì công suất thực giảm.</li>
<li>Tiêu hao nhiên liệu trên mỗi tấn cát khô là bao nhiêu, đo trong điều kiện nào?</li>
<li>Vật liệu chế tạo ống sấy và cánh xáo (thép chịu mài mòn, độ dày) – quyết định tuổi thọ.</li>
<li>Diện tích lọc bụi và hiệu suất lọc có đáp ứng quy chuẩn khí thải của địa phương?</li>
<li>Nhà cung cấp hỗ trợ lắp đặt, chạy thử, đào tạo vận hành và cung ứng phụ tùng ra sao?</li>
</ul>
<div class="note"><b>Góc nhìn Core Material:</b> khi lựa chọn nguồn cát khô, nên yêu cầu nhà cung cấp cung cấp thông tin về công nghệ sấy, kiểm soát bụi và phiếu kiểm tra độ ẩm, cấp phối theo từng lô.</div>
""",
"sources": [],
},
# ---------------------------------------------------------------- 6
{
"slug": "cat-tu-nhien-khan-hiem-vat-lieu-thay-the",
"cat": "khcn",
"date": "05/11/2026",
"read": 5,
"img": None,
"title": "Cát tự nhiên ngày càng khan hiếm: chính sách và vật liệu thay thế tại Việt Nam",
"excerpt": "Áp lực khai thác cát sông, mục tiêu thay thế bằng cát nghiền và cát tái chế, và những nguồn dự trữ mới như cát biển – bức tranh thay đổi nhanh của nguồn cốt liệu tại Việt Nam.",
"body": """
<p>Cát là vật liệu được tiêu thụ nhiều nhất trong xây dựng nhưng lại là tài nguyên đang chịu áp lực lớn. Tại Việt Nam, đặc biệt là khu vực phía Nam và Đồng bằng sông Cửu Long, câu chuyện thiếu cát đã trở thành vấn đề thời sự gắn với các dự án hạ tầng trọng điểm.</p>

<h2>Áp lực lên nguồn cát sông</h2>
<ul>
<li>WWF-Việt Nam năm 2023 đánh giá, nếu tiếp tục khai thác với mức hiện tại, lượng cát tại Đồng bằng sông Cửu Long chỉ còn tồn tại khoảng một thập kỷ.</li>
<li>Việc mở mỏ mới không dễ do quy trình đánh giá tác động môi trường, thăm dò trữ lượng có thể kéo dài nhiều năm.</li>
<li>Khai thác quá mức gắn liền với nguy cơ sạt lở bờ sông – lý do nhiều địa phương siết chặt cấp phép.</li>
</ul>

<h2>Định hướng chính sách: thay thế dần cát tự nhiên</h2>
<p>Định hướng phát triển vật liệu xây dựng đến năm 2030 đặt mục tiêu tăng cường phát triển cát nhân tạo, sử dụng <b>cát nghiền và cát tái chế</b> từ phế thải công nghiệp, xây dựng để thay thế <b>tối thiểu 40%</b> lượng cát thiên nhiên trong xây dựng. Một số địa phương như TP.HCM cũng đã giao khảo sát, quy hoạch vị trí mỏ cát biển làm nguồn dự trữ chiến lược, đồng thời hướng dẫn doanh nghiệp mở rộng mỏ đá để tăng sản lượng cát nghiền.</p>

<h2>Các vật liệu thay thế và thách thức</h2>
<ul>
<li><b>Cát nghiền từ đá:</b> chất lượng ổn định, kiểm soát được cấp phối, nhưng chi phí sản xuất cao hơn và cần kiểm soát hàm lượng bột đá.</li>
<li><b>Cát biển:</b> trữ lượng lớn nhưng phải xử lý muối, cần tiêu chuẩn và quy trình công nghệ phù hợp trước khi dùng rộng rãi cho bê tông.</li>
<li><b>Cát tái chế, tro xỉ:</b> góp phần giải quyết phế thải, đòi hỏi kiểm soát chất lượng đầu vào chặt chẽ.</li>
</ul>

<h2>Ý nghĩa với sản xuất vữa khô</h2>
<p>Khi nguồn cát đầu vào đa dạng hơn, vai trò của khâu <b>chế biến – sấy – sàng – kiểm soát chất lượng</b> càng quan trọng. Đơn vị làm chủ khâu này có thể chuẩn hóa nhiều nguồn cát khác nhau thành sản phẩm đồng nhất, giúp nhà máy vữa khô yên tâm về chất lượng dù thị trường cát biến động.</p>
""",
"sources": [
    ("Thiếu nguồn cung, khó chặn sốt giá cát – Thời báo Kinh tế Sài Gòn", "https://thesaigontimes.vn/thieu-nguon-cung-kho-chan-sot-gia-cat/"),
    ("Mục tiêu dùng cát nghiền, cát tái chế thay thế tối thiểu 40% cát thiên nhiên – Thời báo Kinh tế Sài Gòn", "https://thesaigontimes.vn/?p=1091322"),
    ("TP.HCM khảo sát, quy hoạch vị trí mỏ cát biển làm nguồn dự trữ chiến lược – Bộ Nông nghiệp và Môi trường", "https://mae.gov.vn/tp-hcm-khao-sat-tham-do-quy-hoach-vi-tri-mo-cat-bien-de-lam-nguon-du-tru-chien-luoc-21917.htm"),
    ("Giải bài toán khan hiếm cát sông cho Đồng bằng sông Cửu Long – Nhà Đầu Tư", "https://nhadautu.vn/giai-bai-toan-khan-hiem-cat-song-cho-dong-bang-song-cuu-long-d81887.html"),
],
},
]

# Thư viện vật liệu (thẻ ngắn trên trang chủ)
LIBRARY = [
    ("Xi măng trắng", "Xi măng poóc lăng hàm lượng sắt thấp, cho màu trắng – nền cho vữa trang trí, keo chà ron, terrazzo."),
    ("Cát khô", "Cát đã sấy và sàng phân cỡ, độ ẩm dưới 0,5% – cốt liệu chính của vữa khô, keo dán gạch."),
    ("VAE", "Nhũ tương copolymer vinyl acetate – ethylene, tạo màng dẻo, bám dính cho hệ lỏng và chống thấm."),
    ("RDP", "Bột polymer tái phân tán – “VAE dạng bột” cho sản phẩm trộn khô đóng bao."),
    ("Cellulose ether (HPMC)", "Phụ gia giữ nước, tăng độ dẻo và thời gian thi công cho vữa, keo dán gạch."),
    ("Xỉ lò cao nghiền mịn", "Phụ phẩm luyện thép, phụ gia khoáng hoạt tính giúp giảm clinker và tăng độ bền."),
    ("Hạt thủy tinh tái chế", "Cốt liệu trang trí cho terrazzo, bê tông nghệ thuật; nhiều màu, nhiều cỡ."),
    ("Bột màu oxit", "Pigment vô cơ bền ánh sáng, tạo màu cho vữa, gạch terrazzo, bê tông."),
]
