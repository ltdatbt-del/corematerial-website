# -*- coding: utf-8 -*-
"""Nội dung bài viết cho corematerial.info.
Thêm bài mới: thêm một dict vào ARTICLES rồi chạy  python3 tools/build_info.py
"""

CATEGORIES = {
    "grc":        ("GRC / GFRC",           "Vật liệu, cấp phối, thiết bị phun và kỹ thuật sản xuất cấu kiện bê tông cốt sợi thủy tinh."),
    "vat-lieu":   ("Vật liệu",             "Đặc tính, tiêu chuẩn và cách chọn vật liệu nền cho vữa khô, keo dán gạch, terrazzo."),
    "nghien-cuu": ("Nghiên cứu & Xu hướng", "Những hướng nghiên cứu mới về vật liệu xây dựng carbon thấp và kinh tế tuần hoàn."),
    "may-moc":    ("Máy móc & Công nghệ",  "Nguyên lý, vận hành và lựa chọn thiết bị sản xuất vật liệu."),
    "khcn":       ("KHCN & Chính sách",    "Khoa học công nghệ, chính sách và thị trường vật liệu tại Việt Nam."),
}

ARTICLES = [
# ---------------------------------------------------------------- GRC-1
{
"slug": "san-xuat-grc-bang-may-phun-quy-trinh-7-buoc",
"cat": "grc",
"date": "06/11/2026",
"read": 9,
"img": "grc-may-phun.jpg",
"title": "Sản xuất GRC bằng máy phun: quy trình 7 bước từ cấp phối đến tháo khuôn",
"excerpt": "Phun máy cho tấm GRC mỏng, nhẹ mà vẫn đạt cường độ uốn cao – nhưng chỉ khi từng bước được làm đúng: cấp phối, hiệu chỉnh tỷ lệ sợi, độ dày từng lớp phun, lèn và bảo dưỡng. Đây là quy trình chuẩn kèm các con số cần nhớ.",
"body": """
<p>GRC (Glass-fibre Reinforced Concrete), còn gọi là GFRC, là vữa xi măng – cát mịn được gia cường bằng <b>sợi thủy tinh kháng kiềm (AR)</b>. Nhờ sợi, một tấm GRC dày chỉ khoảng 10–15 mm vẫn chịu uốn tốt, nên được dùng nhiều cho tấm ốp mặt dựng, phào chỉ, cột, lam, chậu cây và các cấu kiện kiến trúc có hình dáng phức tạp.</p>
<p>Có hai cách sản xuất chính: <b>đổ khuôn hỗn hợp trộn sẵn sợi (premix)</b> và <b>phun máy (spray-up)</b>. Phương pháp phun đưa vữa và sợi cắt ngắn lên khuôn cùng lúc, cho hàm lượng sợi cao hơn và sợi phân bố theo mặt phẳng tấm – vì vậy cường độ uốn thường cao hơn rõ rệt. Bài này đi qua quy trình phun máy theo đúng thứ tự một xưởng cần làm.</p>

<h2>Thiết bị và dụng cụ cần chuẩn bị</h2>
<ul>
<li><b>Máy phun GRC:</b> gồm phễu chứa vữa, bơm trục vít, tủ điện, tay cần và súng phun có bộ cắt sợi. Súng phun quyết định phần lớn chất lượng sản phẩm.</li>
<li><b>Máy trộn tốc độ cao:</b> vữa GRC thường dùng xi măng đông kết nhanh, cần trộn đồng nhất trong khoảng 30–60 giây.</li>
<li><b>Máy nén khí:</b> cấp khí cho súng phun, mô-tơ cắt sợi và bộ rung phễu – lưu lượng phải đủ theo khuyến cáo của nhà sản xuất máy.</li>
<li><b>Hai cân:</b> loại 50 kg (sai số khoảng ±50 g) để cân vữa, loại 500 g (sai số ±1 g) để thử tỷ lệ sợi.</li>
<li><b>Con lăn lò xo các cỡ và bay:</b> GRC không đầm rung được, việc lèn chặt hoàn toàn bằng con lăn.</li>
</ul>

<h2>Bước 1 – Thiết kế cấp phối</h2>
<p>Cấp phối được chọn theo cường độ uốn yêu cầu của sản phẩm. Bảng dưới là một cấp phối tham chiếu phổ biến (tính theo khối lượng, xi măng = 100 phần):</p>
<table>
<tr><th>Thành phần</th><th>Tỷ lệ (phần khối lượng)</th></tr>
<tr><td>Xi măng</td><td>100</td></tr>
<tr><td>Cát thạch anh (cát mịn, sạch, khô)</td><td>100 – 120</td></tr>
<tr><td>Nhũ tương acrylic (dạng lỏng đậm đặc)</td><td>8 – 12</td></tr>
<tr><td>Phụ gia giảm nước gốc polycarboxylate</td><td>0,6 – 1,2</td></tr>
<tr><td>Nước trộn</td><td>18 – 24</td></tr>
<tr><td>Sợi thủy tinh kháng kiềm (ZrO₂ &gt; 16%, dài 12 – 18 mm)</td><td>4 – 5% khối lượng sản phẩm</td></tr>
</table>
<div class="note"><b>Lưu ý:</b> đây là cấp phối khởi điểm để thử. Mỗi loại xi măng, cát và phụ gia cho kết quả khác nhau – cần đúc mẫu và thử uốn trước khi sản xuất hàng loạt.</div>

<h2>Bước 2 – Chuẩn bị khuôn</h2>
<p>Khuôn có thể làm bằng gỗ, thép, GRC, composite FRP hoặc silicone. Yêu cầu chung: kích thước chính xác, đủ cứng để không biến dạng khi lăn lèn. Bề mặt khuôn phải sạch, phủ chất chống dính đều tay; kiểm tra lại vị trí các chi tiết chôn sẵn (bản mã, neo liên kết) trước khi phun.</p>

<h2>Bước 3 – Kiểm tra thiết bị trước ca</h2>
<ul>
<li>Kiểm tra lưỡi cắt sợi trong súng: khe hở giữa lưỡi và vành cắt khoảng <b>1,0 – 1,1 mm</b>. Lắp sai gây gãy lưỡi và phải dừng sản xuất.</li>
<li>Kiểm tra áp suất máy nén khí theo khuyến cáo của nhà sản xuất máy phun.</li>
<li>Chuẩn bị sẵn phụ tùng hao mòn (lưỡi cắt, con lăn cao su, đầu phun) và dụng cụ thử nghiệm tại chỗ.</li>
<li><b>Không chạy bơm trục vít khô:</b> trước khi khởi động, đổ một ít nước hoặc chất lỏng loãng vào phễu để bôi trơn stator cao su. Chạy khô vài giây cũng có thể làm cháy stator.</li>
</ul>

<h2>Bước 4 – Cân và trộn vữa</h2>
<p>Cát hiếm khi khô tuyệt đối. Nếu không trừ lượng nước có sẵn trong cát, tỷ lệ nước/xi măng thực tế sẽ cao hơn thiết kế – vữa loãng hơn, cường độ thấp hơn và dễ co ngót, nứt. Hãy đo độ ẩm cát trước mỗi mẻ rồi hiệu chỉnh:</p>
<ul>
<li>Khối lượng cát ẩm cần cân: <b>X = Xs ÷ (1 − A%)</b></li>
<li>Lượng nước thực tế cần thêm: <b>W = Ws − X × A%</b></li>
</ul>
<p>Trong đó Xs là khối lượng cát khô theo cấp phối, A% là độ ẩm cát, Ws là lượng nước theo cấp phối. Ví dụ: cấp phối cần 100 kg cát khô và 22 kg nước, cát đang ẩm 2% → cân X ≈ 102,0 kg cát ẩm và chỉ thêm W ≈ 22 − 2,04 ≈ 20,0 kg nước.</p>
<p>Dùng <b>cát khô công nghiệp</b> (độ ẩm dưới 0,5%) giúp bước này đơn giản và ổn định hơn rất nhiều. Trộn đúng thứ tự cho vật liệu vào để vữa đồng nhất, không vón cục; sàng vữa trước khi đổ vào phễu máy.</p>

<h2>Bước 5 – Hiệu chỉnh máy: thử túi và thử xô</h2>
<p>Đây là bước quyết định hàm lượng sợi – yếu tố số một của cường độ GRC phun. Mục tiêu thường là <b>4 – 5% sợi theo khối lượng</b> sản phẩm.</p>
<p><b>Thử túi (lưu lượng sợi):</b></p>
<ol>
<li>Cân túi rỗng (W, gam).</li>
<li>Phun sợi đã cắt vào túi trong đúng 15 giây.</li>
<li>Cân túi có sợi (G, gam).</li>
<li>Lưu lượng sợi = (G − W) × 4, đơn vị gam/phút. Điều chỉnh áp suất khí của mô-tơ cắt sợi cho đến khi đạt giá trị mục tiêu.</li>
</ol>
<p><b>Thử xô (lưu lượng vữa):</b></p>
<ol>
<li>Cân xô rỗng (W, kg).</li>
<li>Phun vữa vào xô trong đúng 30 giây.</li>
<li>Cân xô có vữa (S, kg).</li>
<li>Lưu lượng vữa = (S − W) × 2, đơn vị kg/phút. Điều chỉnh tốc độ bơm cho đến khi đạt mục tiêu.</li>
</ol>
<p>Quan hệ giữa hai lưu lượng: <b>vữa = sợi × (1 − a) ÷ a</b>, với a là tỷ lệ sợi mục tiêu. Ví dụ: muốn a = 5% và máy đang cắt 300 g sợi/phút → lưu lượng vữa cần là 300 × 0,95 ÷ 0,05 = 5.700 g, tức khoảng <b>5,7 kg vữa/phút</b>.</p>
<div class="note"><b>Thực hành tốt:</b> thử túi và thử xô ở đầu mỗi ca, sau mỗi lần thay lưỡi cắt hoặc con lăn, và ghi vào sổ sản xuất. Đây cũng là bằng chứng chất lượng khi khách hàng hoặc tư vấn giám sát yêu cầu.</div>

<h2>Bước 6 – Phun và lèn</h2>
<ol>
<li><b>Lớp mặt (không sợi):</b> phun một lớp vữa mỏng không có sợi để sợi không lộ ra bề mặt – khoảng <b>1 mm</b> với vữa thường, <b>2 mm</b> với vữa màu. Lớp này dày hơn mức đó rất dễ nứt chân chim.</li>
<li><b>Các lớp có sợi:</b> mỗi lớp dày <b>3 – 4 mm</b>, lăn lèn ngay sau khi phun để đuổi bọt khí và ép sợi vào vữa.</li>
<li><b>Đường phun:</b> phun theo hình chữ S so le, hai dải phun liền kề chồng lên nhau 50% bề rộng dải.</li>
<li><b>Tư thế súng:</b> đầu súng vuông góc với mặt khuôn, cách khoảng <b>300 – 400 mm</b>. Phun góc và cạnh trước, mặt phẳng lớn sau; phun phần thấp trước, phần cao sau.</li>
<li><b>Góc cạnh:</b> góc trong không dùng con lăn mà dùng thép góc hoặc cọ để ép; góc ngoài không có thành khuôn thì giữ vữa bằng bay rồi mới lăn. Khi lăn sát thành khuôn, chừa khe nhỏ để không kéo xô lớp vữa đã phun.</li>
</ol>

<h2>Bước 7 – Tháo khuôn và bảo dưỡng</h2>
<ul>
<li>Phủ ngay màng nilon lên cấu kiện vừa phun để nước không bốc hơi nhanh – đây là lúc GRC dễ nứt nhất.</li>
<li>Chỉ tháo khuôn khi cường độ uốn đạt khoảng <b>2 MPa</b> trở lên (đúc mẫu đi kèm để kiểm tra).</li>
<li>Sau tháo khuôn, tiếp tục bảo dưỡng ẩm liên tục khoảng <b>7 ngày</b> trong môi trường độ ẩm tương đối từ 95% trở lên.</li>
</ul>

<h2>Sau ca làm việc: vệ sinh máy</h2>
<p>Ngừng cấp vữa, phun hết vữa còn trong ống, sau đó cấp nước sạch và tiếp tục phun để súc rửa bơm và ống dẫn. Vệ sinh kỹ súng phun, đáy phễu và các khớp nối nhanh. Vữa đông kết nhanh bám lại trong bơm là nguyên nhân hàng đầu làm giảm tuổi thọ stator/rotor và gây tắc ống ở ca sau.</p>

<h2>Tóm tắt các con số cần nhớ</h2>
<table>
<tr><th>Hạng mục</th><th>Giá trị tham chiếu</th></tr>
<tr><td>Hàm lượng sợi AR</td><td>4 – 5% khối lượng</td></tr>
<tr><td>Chiều dài sợi cắt</td><td>12 – 18 mm (thường dùng)</td></tr>
<tr><td>Lớp mặt không sợi</td><td>1 mm (vữa thường) / 2 mm (vữa màu)</td></tr>
<tr><td>Mỗi lớp phun có sợi</td><td>3 – 4 mm, lăn lèn ngay</td></tr>
<tr><td>Khoảng cách súng – khuôn</td><td>300 – 400 mm, vuông góc</td></tr>
<tr><td>Chồng dải phun</td><td>50%</td></tr>
<tr><td>Tháo khuôn</td><td>khi cường độ uốn ≥ 2 MPa</td></tr>
<tr><td>Bảo dưỡng ẩm</td><td>7 ngày, độ ẩm ≥ 95%</td></tr>
</table>

<div class="note"><b>Góc nhìn Core Material:</b> Core Material cung cấp thiết bị phun GRC/GFRC trọn bộ (máy phun trục vít, máy trộn tốc độ cao 200 L, súng phun có bộ cắt sợi) cùng cát khô và sợi thủy tinh kháng kiềm. Xem thông số máy tại <a href="https://www.corematerial.vn/may-moc/phun-grc/">trang thiết bị phun GRC</a> hoặc <a href="https://www.corematerial.vn/lien-he/">liên hệ</a> để được tư vấn cấu hình cho xưởng của bạn.</div>
""",
"sources": [
    ("Tài liệu hướng dẫn vận hành máy phun GRC trục vít và quy trình sản xuất GRC của nhà sản xuất thiết bị (2026)", None),
    ("PCI MNL-130 – Manual for Quality Control for Plants and Production of Glass Fiber Reinforced Concrete Products", None),
    ("EN 1169 – Precast concrete products: General rules for factory production control of glass-fibre reinforced cement", None),
    ("JC/T 940 – Sản phẩm trang trí GRC (tiêu chuẩn ngành vật liệu xây dựng Trung Quốc)", None),
],
},
# ---------------------------------------------------------------- GRC-4
{
"slug": "truoc-khi-mua-may-phun-grc-10-cau-can-hoi",
"cat": "grc",
"date": "06/11/2026",
"read": 8,
"img": "grc-may-phun-2.jpg",
"title": "Trước khi mua máy phun GRC: 10 câu cần hỏi nhà cung cấp",
"excerpt": "Báo giá máy phun GRC thường chỉ có vài dòng thông số và một con số năng suất rất đẹp. Mười câu hỏi dưới đây giúp tránh những bất ngờ khi máy về: sai điện áp, thiếu máy nén khí, năng suất không như kỳ vọng, phụ tùng hao mòn nhanh.",
"body": """
<p>Một bộ máy phun GRC không đắt so với giá trị nó tạo ra, nhưng mua sai thì rất tốn: máy về không chạy được với điện xưởng, phải mua thêm thiết bị ngoài dự kiến, hay năng suất thực chỉ bằng một phần nhỏ con số trong báo giá. Dưới đây là 10 câu nên hỏi bằng văn bản trước khi đặt cọc – và cách đọc câu trả lời.</p>

<h2>1. Máy được chế tạo cho điện áp và tần số nào?</h2>
<p>Lưới điện công nghiệp tại Việt Nam là <b>3 pha 380 V / 50 Hz</b>. Báo giá từ nước ngoài đôi khi ghi điện áp khác (ví dụ 480 V / 60 Hz cho thị trường khác). Yêu cầu nhà cung cấp xác nhận điện áp cho <b>cả máy phun và máy trộn</b>, ghi rõ trong hóa đơn chiếu lệ (PI) và gửi ảnh nhãn động cơ.</p>

<h2>2. Con số năng suất được tính trong điều kiện nào?</h2>
<p>Báo giá thường ghi năng suất tính bằng m²/giờ. Hãy hỏi rõ con số đó là <b>thời gian phun thuần</b> (chưa tính cấp vữa, vệ sinh, dừng máy), ứng với <b>độ dày bao nhiêu</b> và tay nghề thợ ra sao. Cách tự kiểm tra nhanh là quy về lưu lượng vữa:</p>
<div class="note"><b>Ví dụ tự kiểm tra:</b> máy bơm tối đa khoảng 1.600 kg vữa/giờ. Tấm GRC dày 12 mm, khối lượng thể tích khoảng 2,0 tấn/m³ → mỗi m² tấm hoàn chỉnh cần khoảng 24 kg vữa → năng suất tối đa theo lưu lượng bơm vào khoảng <b>65 m² tấm hoàn chỉnh/giờ phun thuần</b>. Con số hàng trăm m²/giờ thường là diện tích quét của một lượt phun mỏng. Năng suất thực trong ca còn thấp hơn do thời gian trộn, cấp vữa, đổi khuôn và vệ sinh.</div>

<h2>3. Bộ máy gồm những gì – máy trộn có nằm trong giá không?</h2>
<p>Hỏi danh sách đóng gói chi tiết: máy phun, tay cần, súng phun, ống khí, ống vữa (dài bao nhiêu mét), lưỡi cắt và con lăn dự phòng… Đặc biệt hỏi rõ <b>máy trộn tốc độ cao</b> có trong giá hay tính riêng – đây là thiết bị bắt buộc vì vữa GRC cần trộn đồng nhất trong 30 – 60 giây.</p>

<h2>4. Súng phun có bộ cắt sợi không, dùng sợi loại nào?</h2>
<ul>
<li>Súng phun có tích hợp bộ cắt sợi hay phải mua riêng?</li>
<li>Dùng sợi roving bao nhiêu tex (ví dụ 2.400 tex, 4.800 tex)?</li>
<li>Tỷ lệ sợi / vữa điều chỉnh được trong khoảng nào (GRC phun thường cần 3 – 5%)?</li>
<li>Chiều dài sợi cắt điều chỉnh thế nào (thường bằng số lượng và khoảng cách lưỡi dao trên con lăn)?</li>
</ul>

<h2>5. Cần máy nén khí công suất bao nhiêu – có kèm theo không?</h2>
<p>Máy nén khí thường <b>không nằm trong bộ máy</b> nhưng lại bắt buộc để chạy súng phun, mô-tơ cắt sợi và bộ rung phễu. Hỏi lưu lượng (m³/phút) và áp suất yêu cầu, model khuyến nghị. Thiếu khí là nguyên nhân phổ biến khiến sợi cắt không đều và năng suất giảm. Đây là khoản đầu tư thêm cần đưa vào ngân sách ngay từ đầu.</p>

<h2>6. Sợi thủy tinh kháng kiềm đi kèm có chứng nhận gì?</h2>
<p>Nếu mua kèm sợi, hỏi trọng lượng cuộn, độ mảnh (tex), <b>hàm lượng ZrO₂</b> (nên từ khoảng 16% trở lên) và <b>phiếu thử nghiệm của phòng thí nghiệm độc lập</b> theo EN 15422. Sợi không kháng kiềm làm GRC giòn dần theo thời gian – lỗi chỉ lộ ra sau khi công trình đã bàn giao.</p>

<h2>7. Bảo hành tính từ ngày nào, bao lâu, gồm những gì?</h2>
<p>"Bảo hành 12 tháng" có thể tính từ ngày giao hàng, ngày nghiệm thu, hoặc – phổ biến với hàng nhập khẩu – từ <b>ngày xếp hàng lên tàu ghi trên vận đơn (B/L)</b>. Với thời gian vận chuyển, thông quan và lắp đặt, thời gian bảo hành thực tế tại xưởng có thể ngắn hơn đáng kể. Hỏi rõ mốc tính, thời hạn tối đa, và bảo hành áp dụng cho bộ phận nào (động cơ, bơm, tủ điện).</p>

<h2>8. Phụ tùng hao mòn bền bao lâu và mua ở đâu?</h2>
<p>Bơm trục vít có <b>stator và rotor</b> là vật tư hao mòn, tuổi thọ thường tính theo diện tích phun (vài nghìn m²). Mô-tơ súng phun, lưỡi cắt, con lăn cao su, đầu phun cũng cần thay định kỳ. Hỏi tuổi thọ dự kiến, thời gian giao phụ tùng và nên mua sẵn bộ dự phòng nào kèm máy – để máy không phải nằm chờ hàng vài tuần giữa mùa cao điểm.</p>

<h2>9. Có những tài liệu và chứng từ gì?</h2>
<ul>
<li>Hướng dẫn vận hành bằng tiếng Anh (hoặc tiếng Việt), sơ đồ điện, video vận hành.</li>
<li>Danh sách đóng gói (packing list) – đối chiếu trọng lượng, số kiện, thể tích với báo giá và PI.</li>
<li><b>Giấy chứng nhận xuất xứ (C/O)</b>: với hàng từ Trung Quốc, C/O mẫu E giúp hưởng thuế suất ưu đãi theo Hiệp định thương mại tự do ASEAN – Trung Quốc. Hỏi rõ nhà cung cấp cấp được mẫu E hay chỉ C/O thông thường.</li>
<li>Chứng nhận CE của thiết bị (nếu có) – lưu ý dấu CE trên động cơ chưa phải chứng nhận cho cả máy.</li>
</ul>

<h2>10. Đóng gói, thời gian giao và hỗ trợ chạy thử ra sao?</h2>
<ul>
<li>Quy cách đóng gói (thùng gỗ?), số kiện, trọng lượng, kích thước – để tính chi phí vận chuyển và bốc dỡ.</li>
<li>Thời gian sản xuất và giao đến cảng.</li>
<li>Có hỗ trợ <b>đào tạo vận hành, chạy thử lần đầu</b> không – tại chỗ hay từ xa qua video? Ai hỗ trợ khi máy gặp sự cố?</li>
</ul>

<h2>Và 3 câu cần tự hỏi mình</h2>
<ul>
<li><b>Điện và khí:</b> xưởng đã có nguồn 3 pha đủ công suất cho máy phun, máy trộn và máy nén khí chưa?</li>
<li><b>Vật tư:</b> đã có nguồn cát khô đúng cỡ, sợi AR và xi măng ổn định chưa? Máy tốt đến đâu cũng không bù được vật liệu đầu vào biến động.</li>
<li><b>Con người:</b> ai sẽ là thợ phun chính, ai phụ trách hiệu chỉnh máy và ghi sổ chất lượng mỗi ca?</li>
</ul>

<div class="note"><b>Góc nhìn Core Material:</b> Core Material đã làm rõ toàn bộ các câu hỏi trên với nhà sản xuất trước khi đưa <a href="https://www.corematerial.vn/may-moc/phun-grc/">thiết bị phun GRC/GFRC</a> về Việt Nam: máy chạy điện 3 pha 380 V / 50 Hz, máy trộn 200 L nằm trong bộ máy, súng phun có bộ cắt sợi, kèm sợi AR có phiếu thử nghiệm độc lập. Xem thêm quy trình vận hành trong bài <a href="san-xuat-grc-bang-may-phun-quy-trinh-7-buoc.html">Sản xuất GRC bằng máy phun: quy trình 7 bước</a>, hoặc <a href="https://www.corematerial.vn/lien-he/">liên hệ</a> để được tư vấn cấu hình.</div>
""",
"sources": [
    ("Hiệp định Thương mại Hàng hóa ASEAN – Trung Quốc (ACFTA) – quy tắc xuất xứ, C/O mẫu E", None),
    ("EN 15422 – Precast concrete products: Specification of glassfibres for reinforcement of mortars and concretes", None),
    ("PCI MNL-130 – Manual for Quality Control for Plants and Production of Glass Fiber Reinforced Concrete Products", None),
],
},
# ---------------------------------------------------------------- GRC-3
{
"slug": "cat-cho-grc-va-vua-kho-cach-chon-va-tru-nuoc",
"cat": "vat-lieu",
"date": "06/11/2026",
"read": 7,
"img": "cat-xam.jpg",
"title": "Cát cho GRC và vữa khô: chọn cát thế nào, cỡ hạt bao nhiêu và cách trừ nước theo độ ẩm",
"excerpt": "Trong GRC, cát chiếm gần một nửa khối lượng vữa nhưng thường được mua theo cảm tính. Cát quá cỡ làm tắc súng phun, cát bẩn làm tăng nước, cát ẩm làm lệch cấp phối. Đây là những gì cần kiểm soát và bảng trừ nước dùng ngay được.",
"body": """
<p>Trong cấp phối GRC phổ biến, cứ 100 phần xi măng thì có khoảng <b>100 – 120 phần cát</b>. Nói cách khác, cát chiếm gần một nửa khối lượng vữa. Vậy mà ở nhiều xưởng, cát vẫn được mua theo kiểu "cát mịn, sạch là được". Bài này tóm tắt những gì cần kiểm soát ở cát cho GRC phun và vữa khô đóng bao – hai ứng dụng khắt khe nhất về cát.</p>

<h2>1. Loại cát: vì sao thường dùng cát thạch anh (silica)</h2>
<ul>
<li><b>Bền và trơ:</b> cát thạch anh có hàm lượng SiO₂ cao, hạt cứng, ít tạp chất phản ứng – phù hợp với cấu kiện mỏng cần cường độ và độ bền lâu dài.</li>
<li><b>Màu sạch:</b> với GRC trắng hoặc GRC màu dùng xi măng trắng, cát sáng màu giúp màu sắc ổn định giữa các lô. Cát lẫn sét, hữu cơ làm bề mặt ngả xám, loang màu.</li>
<li><b>Hạt tròn cạnh, cấp phối liên tục:</b> giúp vữa dễ bơm qua bơm trục vít và ống dẫn, giảm mài mòn stator.</li>
</ul>

<h2>2. Cỡ hạt: nhỏ nhưng không được quá mịn</h2>
<p>Với GRC phun, cát cần đủ nhỏ để đi qua bơm, ống và đầu phun mà không gây tắc – thực tế thường dùng cát có cỡ hạt lớn nhất khoảng <b>1,2 mm</b>, đã sàng loại hạt quá cỡ. Tài liệu vận hành máy phun đều ghi rõ: <b>hạt quá cỡ trong vữa là nguyên nhân hàng đầu gây tắc ống và đầu phun</b>, cách khắc phục là sàng vữa trước khi đổ vào phễu.</p>
<p>Ngược lại, cát quá mịn (nhiều hạt bụi dưới 0,075 mm) làm tăng diện tích bề mặt phải bao bọc bởi hồ xi măng – vữa "khát nước" hơn, phải thêm nước hoặc phụ gia, dẫn đến co ngót và nứt. Cát tốt cho GRC là cát <b>có cấp phối ổn định giữa các lô</b>: cùng lượng nước, vữa cho cùng độ dẻo.</p>
<table>
<tr><th>Ứng dụng</th><th>Yêu cầu cỡ hạt thường gặp</th><th>Lý do</th></tr>
<tr><td>GRC phun</td><td>Cát mịn, hạt lớn nhất khoảng 1,2 mm, đã sàng loại hạt quá cỡ</td><td>Không tắc bơm, ống, đầu phun; bề mặt mịn</td></tr>
<tr><td>GRC đổ khuôn (premix)</td><td>Tương tự, có thể nới nhẹ tùy chiều dày cấu kiện</td><td>Dễ chảy vào khuôn, bề mặt đẹp</td></tr>
<tr><td>Vữa tô hoàn thiện, keo dán gạch</td><td>Cát mịn, FM khoảng 1,5</td><td>Bề mặt mịn, dễ cán</td></tr>
<tr><td>Vữa xây, vữa tô lót</td><td>Cát trung, FM khoảng 2,0 – 2,5</td><td>Khung hạt chắc, ít co ngót</td></tr>
</table>
<p>Xem thêm về mô đun độ lớn (FM) trong bài <a href="cat-kho-cong-nghiep-do-am-mo-dun-do-lon.html">Cát khô công nghiệp cho vữa khô: độ ẩm và mô đun độ lớn</a>.</p>

<h2>3. Tạp chất: bùn, sét và muối</h2>
<p>Bùn, sét bám trên hạt cát làm giảm liên kết giữa hồ xi măng và cát, đồng thời hút nước – vữa cần nhiều nước hơn và dễ nứt. Với cấu kiện chỉ dày 10 – 15 mm như GRC, ảnh hưởng này lớn hơn nhiều so với bê tông thông thường. Cát nhiễm muối có thể gây loang trắng (muối nở hoa) trên bề mặt. Các chỉ tiêu và phương pháp thử cốt liệu được quy định trong <b>TCVN 7570</b> và bộ <b>TCVN 7572</b>; nhà sản xuất GRC nên đặt ngưỡng nội bộ chặt hơn.</p>

<h2>4. Độ ẩm: biến số "vô hình" làm lệch cấp phối</h2>
<p>Với <b>vữa khô đóng bao</b>, cát gần như bắt buộc phải khô dưới khoảng 0,5% – nếu không, nước trong cát phản ứng với xi măng ngay trong bao, gây vón cục và giảm hạn dùng.</p>
<p>Với <b>GRC trộn tại xưởng</b>, cát ẩm vẫn dùng được nhưng phải trừ lượng nước cát mang theo. Nếu không, tỷ lệ nước/xi măng thực tế cao hơn thiết kế, cường độ giảm và nguy cơ nứt tăng. Công thức hiệu chỉnh:</p>
<ul>
<li>Khối lượng cát ẩm cần cân: <b>X = Xs ÷ (1 − A%)</b></li>
<li>Lượng nước cần thêm: <b>W = Ws − X × A%</b></li>
</ul>
<p>Trong đó Xs là khối lượng cát khô theo cấp phối, Ws là lượng nước theo cấp phối, A% là độ ẩm cát. Bảng dưới tính sẵn cho mẻ có <b>100 kg cát khô và 22 kg nước</b> theo cấp phối:</p>
<table>
<tr><th>Độ ẩm cát (A%)</th><th>Cát ẩm cần cân (X)</th><th>Nước cần thêm (W)</th><th>Nước cát mang theo</th></tr>
<tr><td>0,5%</td><td>100,5 kg</td><td>21,5 kg</td><td>0,5 kg</td></tr>
<tr><td>1%</td><td>101,0 kg</td><td>21,0 kg</td><td>1,0 kg</td></tr>
<tr><td>2%</td><td>102,0 kg</td><td>20,0 kg</td><td>2,0 kg</td></tr>
<tr><td>3%</td><td>103,1 kg</td><td>18,9 kg</td><td>3,1 kg</td></tr>
<tr><td>5%</td><td>105,3 kg</td><td>16,7 kg</td><td>5,3 kg</td></tr>
</table>
<p>Ở độ ẩm 5%, nếu không hiệu chỉnh, mẻ vữa thừa khoảng <b>5 kg nước – gần 25% lượng nước thiết kế</b>. Đó là chênh lệch đủ để biến một mẻ đạt chuẩn thành một mẻ nứt.</p>
<div class="note"><b>Đo độ ẩm nhanh tại xưởng:</b> cân khoảng 500 g cát, sấy (tủ sấy 105 – 110 °C, hoặc chảo trên bếp nếu không có tủ) đến khi khối lượng không đổi, cân lại. Độ ẩm = (khối lượng trước − sau) ÷ khối lượng sau × 100%. Cát để ngoài trời có thể thay đổi độ ẩm trong ngày, nên đo lại khi thời tiết thay đổi.</div>

<h2>5. Checklist nhận một lô cát</h2>
<ul>
<li>☐ Phiếu kiểm tra của nhà cung cấp: độ ẩm, thành phần hạt (hoặc FM), hàm lượng bùn sét, số lô.</li>
<li>☐ Tự kiểm tra độ ẩm mẫu đại diện của lô.</li>
<li>☐ Sàng thử: không có hạt quá cỡ so với yêu cầu (với GRC phun: khoảng 1,2 mm).</li>
<li>☐ Quan sát màu so với mẫu lưu – đặc biệt với GRC trắng, GRC màu.</li>
<li>☐ Đúc mẫu thử với cấp phối chuẩn khi đổi nguồn cát hoặc thấy lô bất thường.</li>
<li>☐ Lưu kho có mái che, kê cao, dùng theo thứ tự nhập trước – xuất trước.</li>
</ul>

<h2>Kết luận</h2>
<p>Cát rẻ nhất trên đơn giá chưa chắc rẻ nhất trên một mét vuông GRC đạt chuẩn. Một nguồn cát <b>khô, sạch, đúng cỡ và ổn định giữa các lô</b> giúp loại bỏ một biến số lớn trong sản xuất – để thợ phun và đội QC tập trung vào những việc khác.</p>
<div class="note"><b>Góc nhìn Core Material:</b> Core Material cung cấp <a href="https://www.corematerial.vn/vat-lieu/#cat-kho">cát khô silica phân cỡ</a> cho vữa khô, keo dán gạch và GRC, kiểm soát độ ẩm và cấp phối theo từng lô. <a href="https://www.corematerial.vn/lien-he/">Liên hệ</a> để nhận mẫu thử cho xưởng của bạn.</div>
""",
"sources": [
    ("TCVN 7570:2006 – Cốt liệu cho bê tông và vữa – Yêu cầu kỹ thuật", None),
    ("TCVN 7572 – Cốt liệu cho bê tông và vữa – Phương pháp thử", None),
    ("Tài liệu hướng dẫn vận hành máy phun GRC và quy trình sản xuất GRC của nhà sản xuất thiết bị (2026)", None),
    ("PCI MNL-130 – Manual for Quality Control for Plants and Production of Glass Fiber Reinforced Concrete Products", None),
],
},
# ---------------------------------------------------------------- GRC-2
{
"slug": "vi-sao-tam-grc-bi-nut-va-cach-phong-tranh",
"cat": "grc",
"date": "06/11/2026",
"read": 8,
"img": None,
"title": "Vì sao tấm GRC bị nứt? 8 nguyên nhân thường gặp và cách phòng tránh",
"excerpt": "Nứt là lỗi gây thiệt hại lớn nhất trong sản xuất GRC: hàng phải hủy, giao trễ, mất uy tín với chủ đầu tư. Phần lớn vết nứt có thể truy ra từ một vài khâu cụ thể – và đều phòng được.",
"body": """
<p>Với xưởng GRC, một tấm bị nứt không chỉ mất tiền vật liệu: còn là công khuôn, công phun, tiến độ giao hàng và uy tín với nhà thầu. Tin tốt là phần lớn vết nứt không đến từ "xui", mà có thể truy ra từ một vài khâu cụ thể trong quy trình. Dưới đây là 8 nguyên nhân thường gặp nhất và cách phòng tránh từng nguyên nhân.</p>

<h2>Đọc vết nứt trước khi tìm nguyên nhân</h2>
<p>Hình dạng và thời điểm xuất hiện vết nứt cho biết nên kiểm tra khâu nào trước:</p>
<table>
<tr><th>Dạng nứt</th><th>Thời điểm thường gặp</th><th>Nghi ngờ trước tiên</th></tr>
<tr><td>Nứt chân chim, mạng nhện trên bề mặt</td><td>Vài giờ đến vài ngày sau phun</td><td>Lớp mặt quá dày, mất nước sớm, thừa nước trộn</td></tr>
<tr><td>Nứt ở góc, cạnh, chỗ thay đổi tiết diện</td><td>Khi tháo khuôn hoặc vận chuyển</td><td>Tháo khuôn sớm, lèn góc không kỹ, thiếu sợi ở góc</td></tr>
<tr><td>Nứt dài, xuyên chiều dày</td><td>Sau lắp đặt, theo mùa nắng – mưa</td><td>Liên kết quá cứng, không cho tấm co giãn</td></tr>
<tr><td>Tấm giòn dần, nứt khi chịu tải sau vài năm</td><td>Nhiều năm sau</td><td>Sợi không kháng kiềm, hàm lượng sợi thấp</td></tr>
</table>

<h2>1. Lớp mặt quá dày</h2>
<p>Lớp vữa mặt không có sợi chỉ để che sợi và tạo bề mặt đẹp – nên giữ khoảng <b>1 mm</b> với vữa thường và <b>2 mm</b> với vữa màu. Lớp này dày hơn thì không có sợi đỡ, co ngót tự do và nứt chân chim. Đây là nguyên nhân rất phổ biến ở các xưởng mới chuyển từ trát tay sang phun.</p>

<h2>2. Mất nước quá sớm, bảo dưỡng không đủ</h2>
<p>GRC mỏng, giàu xi măng (tỷ lệ xi măng : cát gần 1 : 1) nên co ngót khô lớn hơn bê tông thông thường. Nếu bề mặt bị gió, nắng hút nước trong vài giờ đầu, vết nứt xuất hiện gần như chắc chắn.</p>
<ul>
<li>Phủ nilon ngay sau khi phun xong, không để cấu kiện trần trong xưởng thông gió mạnh.</li>
<li>Bảo dưỡng ẩm liên tục khoảng <b>7 ngày</b> ở độ ẩm tương đối từ 95% trở lên sau tháo khuôn.</li>
<li>Polymer acrylic trong cấp phối giúp giữ nước và giảm nứt, nhưng không thay thế hoàn toàn việc bảo dưỡng nếu chưa có thí nghiệm chứng minh.</li>
</ul>

<h2>3. Thừa nước trộn – thường do không trừ nước trong cát</h2>
<p>Thêm nước cho dễ phun là thói quen nguy hiểm: tỷ lệ nước/xi măng tăng làm cường độ giảm và co ngót tăng. Một nguyên nhân "vô hình" là <b>cát ẩm</b>: cát ẩm 3% nghĩa là cứ 100 kg cát đã mang theo khoảng 3 kg nước chưa được tính. Hãy đo độ ẩm cát và trừ nước tương ứng mỗi mẻ, hoặc dùng cát khô công nghiệp có độ ẩm dưới 0,5% để loại bỏ biến số này. Phụ gia giảm nước giúp vữa đủ dẻo để phun mà không cần thêm nước.</p>

<h2>4. Hàm lượng sợi thấp hoặc không đều</h2>
<p>Sợi là "cơ bắp" của GRC. Với GRC phun, hàm lượng mục tiêu thường là <b>4 – 5% khối lượng</b>. Lưỡi cắt mòn, con lăn cao su mòn hoặc áp suất khí thay đổi đều làm lượng sợi giảm mà mắt thường khó thấy.</p>
<ul>
<li>Thử túi (lưu lượng sợi) và thử xô (lưu lượng vữa) đầu mỗi ca và sau mỗi lần thay phụ tùng.</li>
<li>Sợi ra dài bất thường, cắt không đứt hoặc rơi rụng: kiểm tra lưỡi cắt và khe hở con lăn.</li>
<li>Phun góc, cạnh trước và đủ dày – đây là nơi thường thiếu sợi nhất.</li>
</ul>

<h2>5. Lèn không kỹ</h2>
<p>GRC không đầm rung được, chỉ lèn bằng con lăn. Mỗi lớp phun có sợi nên dày <b>3 – 4 mm</b> và lăn ngay. Phun một lớp quá dày rồi mới lăn sẽ để lại bọt khí và vùng sợi không thấm vữa – điểm yếu khởi phát nứt và tách lớp. Góc trong nên ép bằng thép góc hoặc cọ thay vì con lăn.</p>

<h2>6. Tháo khuôn quá sớm hoặc thao tác mạnh tay</h2>
<p>Áp lực tiến độ khiến nhiều xưởng tháo khuôn khi tấm "trông đã cứng". Nên chờ cường độ uốn đạt khoảng <b>2 MPa</b> trở lên, kiểm tra bằng mẫu đúc kèm. Khi nâng, lật tấm lớn, dùng điểm nâng và giá đỡ phù hợp để tránh uốn cục bộ ở tuổi sớm.</p>

<h2>7. Dùng sợi không kháng kiềm</h2>
<p>Môi trường xi măng có tính kiềm cao. Sợi thủy tinh thông thường (E-glass) bị kiềm ăn mòn dần, tấm mất độ dẻo dai và nứt sau một thời gian sử dụng – lỗi xuất hiện khi công trình đã bàn giao, rất khó xử lý. Chỉ dùng <b>sợi thủy tinh kháng kiềm (AR)</b> có hàm lượng ZrO₂ từ khoảng 16% trở lên, và yêu cầu nhà cung cấp phiếu thử nghiệm theo EN 15422 cho từng lô.</p>

<h2>8. Liên kết quá cứng – nứt sau khi lắp đặt</h2>
<p>Tấm GRC co giãn theo nhiệt độ và độ ẩm. Nếu tấm bị ngàm cứng ở tất cả các điểm, ứng suất tích tụ qua các chu kỳ nắng – mưa sẽ gây nứt dài, thường xuất phát từ vị trí bản mã. Hệ liên kết cần có điểm chịu tải cố định và các điểm neo cho phép chuyển vị; thiết kế liên kết nên do kỹ sư kết cấu thực hiện, phối hợp với xưởng sản xuất.</p>

<h2>Một lưu ý về vật liệu đầu vào</h2>
<p>Xi măng hút ẩm khi lưu kho lâu, nhất là kho hở hoặc để ngoài trời; phụ gia polymer cũng có hạn dùng. Sau các đợt nghỉ dài ngày như Tết, khi vật liệu tồn kho lâu hơn bình thường, nên kiểm tra lại xi măng (vón cục, thời gian đông kết) và đúc mẫu thử trước khi chạy lại sản xuất hàng loạt.</p>

<h2>Checklist chống nứt cho mỗi ca</h2>
<ul>
<li>☐ Đo độ ẩm cát, trừ nước theo cấp phối (hoặc dùng cát khô &lt; 0,5%).</li>
<li>☐ Thử túi và thử xô, ghi tỷ lệ sợi vào sổ (mục tiêu 4 – 5%).</li>
<li>☐ Lớp mặt 1 – 2 mm, không dày hơn.</li>
<li>☐ Mỗi lớp có sợi 3 – 4 mm, lăn ngay; góc cạnh phun trước, đủ dày.</li>
<li>☐ Phủ nilon ngay sau khi phun.</li>
<li>☐ Tháo khuôn khi mẫu đạt ≥ 2 MPa; bảo dưỡng ẩm 7 ngày.</li>
<li>☐ Kiểm tra phiếu thử nghiệm sợi AR và tình trạng xi măng khi nhập lô mới.</li>
</ul>

<div class="note"><b>Góc nhìn Core Material:</b> phần lớn nguyên nhân nứt nằm ở sự ổn định của vật liệu đầu vào và hiệu chỉnh máy. Core Material cung cấp cát khô kiểm soát độ ẩm và cấp phối, sợi thủy tinh kháng kiềm có phiếu thử nghiệm, cùng <a href="https://www.corematerial.vn/may-moc/phun-grc/">thiết bị phun GRC trọn bộ</a>. <a href="https://www.corematerial.vn/lien-he/">Liên hệ</a> để được tư vấn cho xưởng của bạn.</div>
""",
"sources": [
    ("Tài liệu hướng dẫn quy trình sản xuất GRC phun của nhà sản xuất thiết bị (2026)", None),
    ("PCI MNL-128 – Recommended Practice for Glass Fiber Reinforced Concrete Panels", None),
    ("PCI MNL-130 – Manual for Quality Control for Plants and Production of Glass Fiber Reinforced Concrete Products", None),
    ("EN 15422 – Precast concrete products: Specification of glassfibres for reinforcement of mortars and concretes", None),
],
},
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
