# -*- coding: utf-8 -*-
"""DỮ LIỆU WEBSITE www.corematerial.vn
Sửa nội dung tại đây rồi chạy:  python3 tools/build_site.py        (bản công khai)
                                PREVIEW=1 python3 tools/build_site.py (bản xem trước, hiện ô chờ ảnh/thông số)
Quy ước:
  - spec: danh sách (tên thông số, giá trị). Giá trị None = "đang cập nhật" (bản công khai ẩn dòng đó).
  - media: ảnh trong public/img/... ; video trong public/media/...
  - slots: các vị trí chờ bổ sung (chỉ hiện ở bản xem trước).
"""

COMPANY = {
    "legal": "CÔNG TY CỔ PHẦN KHOA HỌC CÔNG NGHỆ CORE MATERIAL",
    "brand": "Core Material JSC",
    "slogan": "Building Values, Enriching Life",
    "tax": "0319732343",
    "hotline": "0938.903.557",
    "email": "info@corematerial.vn",
    "address": "114bis Trần Quốc Toản, P. Xuân Hòa, TP. Hồ Chí Minh",
    "site": "https://www.corematerial.vn",
}

VALUES = [
    ("INTEGRITY", "Chính trực", "Minh bạch về nguồn gốc, chất lượng và phạm vi cung cấp. Chỉ cam kết những gì có tài liệu và thỏa thuận rõ ràng."),
    ("INNOVATION", "Đổi mới", "Chủ động tìm kiếm vật liệu, thiết bị và giải pháp công nghệ phù hợp hơn cho sản xuất và thi công tại Việt Nam."),
    ("PARTNERSHIP", "Đồng hành", "Làm việc lâu dài cùng khách hàng và nhà cung cấp: từ chọn giải pháp, thử nghiệm đến hỗ trợ sau bán hàng."),
]

# ---------------- NGUYÊN LIỆU & VẬT LIỆU ----------------
MATERIALS = [
{
 "id": "cat-kho", "form": "Cát khô", "name": "Cát khô (cát silica sấy & phân cỡ)", "short": "Cát khô",
 "img": "img/san-pham/cat-hero.jpg",
 "pledge": [("CLEAN", "Sạch"), ("CONSISTENT", "Đồng đều"), ("RELIABLE", "Đáng tin cậy")],
 "intro": "Cát đã sấy khô và sàng phân cỡ, dùng làm cốt liệu cho vữa khô trộn sẵn, keo dán gạch, vữa tự san phẳng, GRC, bê tông trang trí và các ứng dụng công nghiệp khác. Core Material cung cấp từ hai nguồn: cát sông Mekong sấy – sàng tại xưởng và cát trắng mỏ Bảo Lộc cho các dòng sản phẩm cần màu sáng.",
 "points": [
   "Nhiều cỡ hạt để lựa chọn theo công thức sản phẩm.",
   "Đóng gói theo yêu cầu: bao Jumbo hoặc bao nhỏ.",
   "Thông số kỹ thuật (độ ẩm, cấp phối, tạp chất) cung cấp theo từng lô và từng đơn hàng.",
 ],
 "sources": [
   ("Cát sông Mekong – sấy & sàng tại xưởng", "Cát sông được sấy bằng lò sấy thùng quay, sàng phân cỡ và đóng bao Jumbo ngay tại xưởng.", ["Số 1: 0 – 0,3 mm", "Số 2: 0,3 – 0,7 mm", "Số 3: 0,7 – 1,2 mm", "Số 4: 1,2 – 2,4 mm"]),
   ("Cát trắng Bảo Lộc (cát mỏ)", "Cát mỏ màu sáng cho sản phẩm cần màu trắng: keo dán gạch trắng, vữa và bột trét trang trí, terrazzo.", []),
 ],
 "grades_title": "Cát trắng Bảo Lộc – mẫu phân cỡ",
 "grades": [
   ("Số 1", "0,0 – 0,3 mm", "img/san-pham/cat-so-1.jpg"),
   ("Số 2", "0,3 – 0,7 mm", "img/san-pham/cat-so-2.jpg"),
   ("Số 3", "0,7 – 1,7 mm", "img/san-pham/cat-so-3.jpg"),
   ("Số 4", "1,7 – 2,4 mm", "img/san-pham/cat-so-4.jpg"),
   ("Số 5", "2,4 – 3,5 mm", "img/san-pham/cat-so-5.jpg"),
   ("Số 6", "3,5 – 5,0 mm", "img/san-pham/cat-so-6.jpg"),
 ],
 "grades_note": "Ảnh mẫu cát phân cỡ. Dải cỡ hạt mang tính tham khảo; thông số chính thức theo phiếu kiểm tra của từng lô.",
 "gallery_title": "Xưởng sấy – sàng cát sông Mekong",
 "gallery": [
   ("img/san-pham/cat-mekong-xuong-say.jpg", "Lò sấy thùng quay & trạm điều khiển"), 
   ("img/san-pham/cat-mekong-mau-so-2.jpg", "Mẫu cát số 2"), 
   ("img/san-pham/cat-kho-bao-jumbo-minh-hoa.jpg", "Kho thành phẩm – bao Jumbo 1 tấn (hình minh họa)"), ("img/san-pham/cat-bao-jumbo-minh-hoa.jpg", "Minh họa bao Jumbo Core Material (dự kiến)"),
 ],
 "videos": [("media/video-cat-mekong-xuong.mp4", "media/video-cat-mekong-xuong-poster.jpg", "Xưởng sấy – sàng cát", "Cát sông Mekong"),
            ("media/video-cat-mekong-mau.mp4", "media/video-cat-mekong-mau-poster.jpg", "Kiểm tra mẫu cát thành phẩm", "Cát sông Mekong")],
 "slots": ["Phiếu kiểm tra chất lượng mẫu (độ ẩm, cấp phối) – chờ tài liệu"],
},
{
 "id": "xi-mang-trang", "form": "Xi măng trắng", "name": "Xi măng trắng", "short": "Xi măng trắng",
 "img": "img/san-pham/xi-mang-trang-coremat-bao.jpg",
 "img_full": "img/san-pham/xi-mang-trang-coremat.jpg",
 "img_caption": "Hình minh họa bao bì CoreMat dự kiến: bao 40 kg và Jumbo",
 "pledge": [("WHITENESS", "Độ trắng"), ("CONSISTENCY", "Tính ổn định"), ("STRENGTH", "Cường độ")],
 "intro": "Cung cấp xi măng trắng cho sản xuất vật liệu (vữa, keo dán gạch, bột trét, gạch terrazzo, đá mài, sản phẩm trang trí) và cho thi công.",
 "points": [
   "Dòng xi măng trắng phối trộn thương hiệu CoreMat (đang phát triển), quy cách bao 40 kg và Jumbo: PCW 32.5 – cho đá mài; PCW 42.5 – cho terrazzo và bột trét; PCW 52.5 – cho bột trét cao cấp.",
   "Thông tin thành phần, cấp cường độ, độ trắng và xuất xứ được cung cấp theo từng sản phẩm cụ thể; có chứng nhận chất lượng (COA) theo lô hàng.",
   "Tư vấn lựa chọn loại xi măng trắng phù hợp với ứng dụng.",
   "Định hướng nghiên cứu các dòng xi măng trắng đặc chủng: UHPC, micro-cement, vữa tự san phẳng, xi măng chuyên dụng cho terrazzo.",
 ],
 "slots": ["Bảng thông số theo từng mã sản phẩm (cấp cường độ, độ trắng, quy cách bao)"],
},
{
 "id": "hoa-chat", "form": "VAE / RDP", "name": "Phụ gia, khoáng chất & hóa chất xây dựng", "short": "Phụ gia & khoáng chất",
 "img": None,
 "intro": "Nhũ tương VAE, bột polymer tái phân tán RDP, khoáng chất và các phụ gia cho vữa khô, keo dán gạch, chống thấm, bột trét và sơn.",
 "points": [
   "Phụ gia polymer: VAE, RDP – tăng bám dính, chống chảy xệ cho keo dán gạch và vữa.",
   "Khoáng chất: bột CaCO₃ siêu trắng, talc, BaSO₄, thạch cao, titan dioxide (TiO₂).",
   "Định hướng mở rộng: phụ gia chống thấm, chất tăng cứng bề mặt (hardener), keo dán chuyên dụng.",
   "Tư vấn lựa chọn theo ứng dụng; cung cấp tài liệu kỹ thuật (TDS, SDS) theo từng sản phẩm.",
 ],
 "slots": ["Danh mục mã sản phẩm và tài liệu TDS"],
},
{
 "id": "soi-be-tong", "form": "Sợi gia cường bê tông", "name": "Sợi gia cường bê tông (sợi thép, sợi PP)", "short": "Sợi bê tông",
 "img": None,
 "intro": "Sợi phân tán trong bê tông và vữa giúp hạn chế nứt co ngót, tăng độ dai và khả năng chịu va đập – dùng cho sàn công nghiệp, bê tông phun, cấu kiện đúc sẵn và vữa.",
 "points": [
   "Sợi thép neo đầu 3D / 4D: sàn công nghiệp, bê tông phun hầm – mái dốc, cấu kiện đúc sẵn.",
   "Sợi polypropylene (PP): chống nứt co ngót cho vữa, bê tông, sàn và lớp láng.",
   "Tư vấn liều lượng theo ứng dụng; tài liệu kỹ thuật (TDS) theo từng mã sản phẩm.",
 ],
 "slots": ["Ảnh sản phẩm sợi thép / sợi PP và bảng thông số"],
},
{
 "id": "trang-tri", "form": "Đá mài / hạt màu / bột màu", "name": "Đá mài, cát màu, hạt thủy tinh & bột màu", "short": "Vật liệu trang trí",
 "img": "img/da-ho-phach.jpg",
 "intro": "Vật liệu trang trí cho terrazzo, sàn và tường trang trí, bê tông nghệ thuật và hoàn thiện kiến trúc: hạt đá mài, cát màu, hạt thủy tinh màu và bột màu.",
 "points": [
   "Nhiều màu sắc và kích cỡ hạt.",
   "Cát màu tự nhiên, cát màu phủ epoxy và vảy màu (flake) cho sàn, tường trang trí.",
   "Gia công nghiền đá màu / cát màu siêu mịn cho sơn và vữa màu theo đơn hàng.",
   "Hỗ trợ mẫu để kiến trúc sư và nhà thầu lựa chọn.",
 ],
 "gallery": [
   ("img/hat-xanh-tay.jpg", "Hạt thủy tinh xanh"), ("img/da-ho-phach.jpg", "Hạt hổ phách"),
   ("img/thuy-tinh-luc.jpg", "Thủy tinh xanh lục"), ("img/da-ngoc.jpg", "Hạt ngọc lam"),
   ("img/bot-mau.jpg", "Cát màu & bột màu"), ("img/cat-den.jpg", "Cát đen"),
   ("img/da-xanh-duong.jpg", "Thủy tinh xanh dương"), ("img/hat-luc.jpg", "Hạt xanh lá"),
 ],
},
{
 "id": "hat-mai-sic", "form": "Hạt mài Silicon Carbide (SiC)", "name": "Hạt mài siêu cứng Silicon Carbide (SiC đen & SiC xanh)", "short": "Hạt mài SiC",
 "img": "img/san-pham/sic-minh-hoa.jpg",
 "img_caption": "Hình minh họa cấu trúc tinh thể SiC – ảnh mẫu hạt thật sẽ cập nhật",
 "pledge": [("HARDNESS", "Độ cứng"), ("PURITY", "Độ tinh khiết"), ("CONSISTENCY", "Đồng đều cỡ hạt")],
 "intro": "Silicon carbide (SiC) là hạt mài nhân tạo được nấu từ cát thạch anh và cốc dầu mỏ trong lò điện trở ở nhiệt độ trên 2.000 °C. Hạt có độ cứng Mohs 9,2–9,4 – chỉ đứng sau kim cương và boron carbide trong nhóm vật liệu mài thông dụng – sắc cạnh, tự tạo cạnh mới khi mài, dẫn nhiệt tốt, giãn nở nhiệt thấp và bền hóa học. Core Material cung cấp hai dòng SiC đen và SiC xanh, từ cát phân đoạn đến bột siêu mịn.",
 "points": [
   "Đá mài, đĩa mài sàn terrazzo, đá granite, bê tông mài; giấy nhám và dụng cụ mài liên kết.",
   "Hạt chống trơn trượt cho sàn epoxy, cầu thang, sàn công nghiệp; hạt tăng cứng bề mặt sàn bê tông.",
   "Phun cát làm sạch – tẩy gỉ kim loại, khắc mờ kính và đá; mài nghiền, đánh bóng, cắt dây.",
   "Vật liệu chịu lửa, lót lò cho nhà máy gốm sứ, gạch, thép; phụ gia khử oxy trong luyện kim.",
   "Hạt thô theo chuẩn FEPA (F) và giấy nhám (P), bột mịn F/JIS; đóng gói bao giấy 25 kg hoặc bao Jumbo 1 tấn; COA theo từng lô.",
   "Cung cấp theo yêu cầu các hạt mài siêu cứng khác (Mohs ≥ 9): nhôm oxit nung chảy trắng & nâu, boron carbide.",
 ],
 "sources": [
   ("SiC đen (Black SiC)", "Dai, giá kinh tế. Phù hợp mài gang, kim loại màu, đá tự nhiên, bê tông, cao su; phun cát; vật liệu chịu lửa và phụ gia luyện kim.", ["Cát phân đoạn 0–1 / 1–3 / 3–5 mm", "Hạt thô F12 – F220", "P12 – P220", "Bột mịn F230 – F1200", "P240 – P1200"]),
   ("SiC xanh (Green SiC)", "Tinh khiết hơn (SiC ≥ 99%), cứng và sắc hơn. Phù hợp mài – đánh bóng chính xác hợp kim cứng, gốm kỹ thuật, kính, thạch anh, đá quý; bước đánh bóng hoàn thiện.", ["Hạt thô F12 – F220", "P24 – P240", "Bột mịn F230 – F1200", "JIS #240 – #3000"]),
 ],
 "tables": [
   ("Tính chất tiêu biểu", ["Chỉ tiêu", "SiC đen", "SiC xanh"], [
     ["SiC (%)", "90 – 99 (tùy mác)", "97,5 – 99,5"],
     ["Fe₂O₃ (%)", "0,10 – 0,35", "0,05 – 0,25"],
     ["Cacbon tự do – F.C (%)", "0,10 – 0,35", "0,05 – 0,25"],
     ["Độ cứng Mohs", "9,2", "9,4"],
     ["Tỷ trọng thực (g/cm³)", "3,20 – 3,25", "3,20 – 3,25"],
     ["Nhiệt độ sử dụng tối đa", "~1.900 °C", "~1.900 °C"],
   ], ""),
   ("Phân loại theo mục đích sử dụng", ["Nhóm", "SiC tối thiểu", "Cỡ hạt", "Ứng dụng"], [
     ["Hạt mài (Abrasives)", "98,5%", "Chuẩn FEPA & JIS", "Mài, đánh bóng, cắt dây, phun cát"],
     ["Bột gốm (Ceramic powder)", "99%", "Theo yêu cầu", "Gốm kỹ thuật, đánh bóng"],
     ["Chịu lửa (Refractory)", "90%", "0–1, 1–3, 3–5 mm", "Vật liệu chịu lửa, phụ gia luyện kim"],
   ], ""),
   ("Hạt thô chuẩn F – thành phần hóa", ["Cỡ hạt", "Loại", "SiC ≥ (%)", "Fe₂O₃ ≤ (%)", "F.C ≤ (%)", "Tỷ trọng đổ đống (g/cm³)"], [
     ["F24 – F120", "SiC đen", "98,5", "0,20", "0,20", "1,41 – 1,59"],
     ["F150 – F220", "SiC đen", "98,0", "0,25", "0,25", "1,29 – 1,47"],
     ["F24 – F120", "SiC xanh", "99,0", "0,15", "0,15", "1,38 – 1,60"],
     ["F150 – F220", "SiC xanh", "98,5", "0,20", "0,20", "1,30 – 1,48"],
   ], ""),
   ("Bột mịn chuẩn F – cỡ hạt trung bình D50 & hàm lượng SiC", ["Cỡ", "D50 (µm)", "SiC đen ≥ (%)", "SiC xanh ≥ (%)"], [
     ["F240", "44,5 ± 2,0", "99", "99"], ["F280", "36,5 ± 1,5", "99", "99"], ["F320", "29,2 ± 1,5", "99", "99"],
     ["F360", "22,8 ± 1,5", "99", "99"], ["F400", "17,3 ± 1,0", "99", "99"], ["F500", "12,8 ± 1,0", "98,5", "99"],
     ["F600", "9,3 ± 1,0", "98,5", "99"], ["F800", "6,5 ± 1,0", "98,5", "98,5"], ["F1000", "4,5 ± 0,8", "98", "97"],
     ["F1200", "3,0 ± 0,5", "97,5", "96,5"],
   ], "Thông số tham khảo. Thông số chính thức theo phiếu kiểm tra (COA) của từng lô hàng; bảng chi tiết từng cỡ hạt gửi kèm báo giá."),
 ],
 "slots": ["Ảnh mẫu hạt SiC đen / SiC xanh thật (chụp mẫu Core)", "TDS / COA bản chính thức"],
},
]

# ---------------- MÁY MÓC & TỰ ĐỘNG HÓA ----------------
TECH_INTRO = "Core Material phát triển mảng thương mại thiết bị và giải pháp công nghệ, kết nối các nhà cung cấp phù hợp với nhu cầu sản xuất và thi công tại Việt Nam."

EQUIPMENT = [
{
 "id": "phun-grc", "form": "Thiết bị phun GRC/GFRC",
 "name": "Thiết bị phun GRC / GFRC", "k": "Sản xuất cấu kiện",
 "img": "img/thiet-bi/may-phun-grc.jpg",
 "gallery": ["img/thiet-bi/may-phun-grc-2.jpg", "img/thiet-bi/may-phun-grc-3.jpg"],
 "short": "Hệ thống phun cho sản xuất cấu kiện bê tông cốt sợi thủy tinh: tấm ốp, phào chỉ, cấu kiện kiến trúc.",
 "intro": [
   "GRC/GFRC (bê tông cốt sợi thủy tinh) được dùng để sản xuất các cấu kiện mỏng, nhẹ nhưng bền: tấm ốp mặt dựng, phào chỉ, lam, chậu, cấu kiện trang trí kiến trúc.",
   "Thiết bị phun GRC cung cấp hỗn hợp vữa và sợi thủy tinh lên khuôn, giúp sản xuất đồng đều và năng suất hơn so với thi công thủ công.",
 ],
 "diff": "Khác với máy phun vữa tô tường (thi công tại công trình), thiết bị phun GRC phục vụ sản xuất cấu kiện tại xưởng, đi kèm khuôn và quy trình bảo dưỡng riêng.",
 "sections": [
   ("Ứng dụng", ["Tấm ốp mặt dựng, phào chỉ, cột, lam trang trí", "Cấu kiện kiến trúc và sản phẩm trang trí từ GFRC", "Xưởng sản xuất cấu kiện đúc sẵn"]),
   ("Bộ máy tiêu chuẩn", ["Máy phun GRC trục vít kèm tay cần ngang và tủ điện", "Máy trộn tốc độ cao 200 L (motor 2,2 kW, 960 vòng/phút) – đồng bộ trong bộ máy", "Stator / rotor bơm vữa", "Súng phun tích hợp bộ cắt sợi, đầu phun và lõi súng dự phòng", "Ống khí 16 m, ống vữa 10 m", "Lưỡi cắt sợi, con lăn GRC và phụ kiện đi kèm"]),
   ("Cắt sợi & tỷ lệ phối trộn", ["Dùng sợi roving kháng kiềm 2.400 tex hoặc 4.800 tex", "Tỷ lệ sợi / vữa điều chỉnh trong khoảng 3 – 5%", "Chiều dài sợi cắt điều chỉnh theo số lượng và khoảng cách lưỡi dao trên con lăn; có thể cắt ngắn đến 6 – 8 mm"]),
   ("Thiết bị & vật tư tùy chọn", ["Sợi thủy tinh kháng kiềm AR: cuộn 19 kg, 2.400 tex, hàm lượng ZrO₂ 16,75% – có phiếu thử nghiệm độc lập theo EN 15422", "Máy nén khí (không kèm bộ máy): khuyến nghị máy trục vít 15 kW, lưu lượng 1,1 m³/phút, áp suất tối đa 1,58 MPa", "Bộ phụ tùng dự phòng: stator/rotor, súng phun lớp phủ, súng phun đồng trục"]),
   ("Vật tư hao mòn (theo nhà sản xuất)", ["Stator / rotor bơm: tuổi thọ khoảng 5.000 m² phun, sau đó cần thay mới", "Motor súng phun: khuyến nghị thay khoảng 6 tháng/lần khi vận hành liên tục hằng ngày"]),
   ("Bảo hành & hỗ trợ", ["Bảo hành 12 tháng theo chính sách nhà sản xuất đối với lỗi không do người sử dụng", "Kèm hướng dẫn vận hành (tiếng Anh), sơ đồ điện và video hướng dẫn", "Hỗ trợ đào tạo vận hành và chạy thử lần đầu qua video từ xa", "Phạm vi lắp đặt, đào tạo và hỗ trợ của Core Material theo thỏa thuận cụ thể"]),
 ],
 "spec": [
   ("Model", "Máy phun GRC trục vít loại 80"),
   ("Công suất motor phun / motor trộn", "4,0 kW / 2,2 kW"),
   ("Tốc độ trục vít", "20 – 200 vòng/phút"),
   ("Lưu lượng cấp vữa", "1.600 kg/giờ"),
   ("Dung tích phễu", "80 L"),
   ("Áp suất khí nén làm việc", "0,6 – 0,8 MPa"),
   ("Bán kính tay cần ngang", "4,5 m"),
   ("Năng suất phun (theo nhà sản xuất)", "đến 500 m²/giờ – tính theo thời gian phun thuần, thợ có kinh nghiệm; chưa gồm thời gian cấp vữa, vệ sinh và dừng máy"),
   ("Nguồn điện", "3 pha 380 V / 50 Hz (máy phun và máy trộn)"),
   ("Khí nén yêu cầu", "khuyến nghị 1,1 m³/phút (máy nén trục vít 15 kW)"),
   ("Kích thước (D × R × C)", "1.400 × 1.000 × 2.200 mm"),
   ("Trọng lượng", "700 kg (máy phun + máy trộn)"),
   ("Đóng gói", "Thùng gỗ, 2 kiện"),
 ],
 "videos": [("media/video-phun-grc.mp4", "media/video-phun-grc-poster.jpg", "Thiết bị phun GRC", "Video từ nhà cung cấp thiết bị"),
            ("media/video-san-xuat-grc.mp4", "media/video-san-xuat-grc-poster.jpg", "Trộn & cấp liệu", "Video từ nhà cung cấp thiết bị")],
 "slots": ["Ảnh máy thực tế khi hàng về Việt Nam"],
},
{
 "id": "phun-vua-to-tuong", "form": "Máy phun vữa tô tường",
 "name": "Máy phun vữa tô tường", "k": "Thi công tại công trình",
 "img": "img/thiet-bi/may-bom-phun-vua-tw20f.jpg",
 "gallery": ["img/thiet-bi/ung-dung-phun-vua-to.jpg", "img/thiet-bi/ung-dung-phun-vua-tran-tuong.jpg", "img/thiet-bi/ung-dung-gia-co-mai-doc.jpg"],
 "short": "Hai dòng máy phun vữa cho thi công tại công trình: máy bơm phun vữa bóp ống (3 model, bơm xa – bơm cao) và máy phun vữa trục vít cơ động cho tô trát tường.",
 "intro": [
   "Thiếu thợ lành nghề, chi phí nhân công tăng và chất lượng trát tay không đồng đều (bộp, nứt, lớp tô dày mỏng khác nhau) là những điểm nghẽn của công tác tô trát truyền thống. Máy bơm phun vữa cơ giới hóa cả chuỗi: trộn vữa – bơm qua đường ống – phun trực tiếp lên bề mặt.",
   "Dòng máy Core Material giới thiệu dùng nguyên lý bơm bóp ống (squeeze pump): con lăn ép ống bóp để đẩy vữa, vữa chỉ đi trong ống bóp nên ít chi tiết mài mòn tiếp xúc với vữa và việc vệ sinh nhanh gọn.",
   "Hiệu quả cao nhất khi máy được dùng đồng bộ với vữa trộn sẵn phù hợp, đội ngũ được đào tạo và quy trình vận hành – vệ sinh đúng chuẩn.",
 ],
 "sections": [
   ("Ứng dụng", ["Phun vữa tô tường, trần – trong nhà và mặt ngoài", "Bơm vữa lấp lòng vách ngăn nhẹ", "Phun vữa cho hệ coffa để lại (lưới thép định hình)", "Phun vữa gia cố mái dốc, bờ sông, taluy"]),
   ("Bộ máy tiêu chuẩn (theo báo giá nhà sản xuất)", ["Máy bơm vữa bóp ống kèm 02 ống bóp", "Máy trộn vữa và bộ khuấy phễu chống lắng", "Ống thép dẫn vữa khoảng 60 m (TW-60: khoảng 30 m), kèm co 45°/90° và khớp nối inox", "02 ống mềm 10 m đầu nối nhanh camlock", "Súng phun vữa", "Danh mục và số lượng cụ thể được xác nhận theo từng đơn hàng"]),
   ("Quy trình thi công 4 bước", ["Chuẩn bị: bố trí máy hợp lý, tập trung điện – nước – vật liệu tại một điểm", "Cấp liệu định lượng: trộn vữa và nước theo tỷ lệ, bảo đảm hỗn hợp đồng đều", "Bơm & phun: vữa đi qua ống thép, ống mềm và được phun trực tiếp bằng súng chuyên dụng", "Vệ sinh nhanh: cho bóng xốp chuyên dụng chạy qua đường ống – vệ sinh định kỳ khoảng 10 phút (theo nhà sản xuất)"]),
   ("Năng suất tham khảo (theo nhà sản xuất)", ["Trát tay truyền thống: khoảng 20 m²/công", "Máy trộn + trát tay: khoảng 90 m²/công", "Bơm phun vữa bóp ống: khoảng 200 m²/công", "Năng suất thực tế phụ thuộc cấp phối, cốt liệu, phụ gia, chiều dày lớp tô và bố trí đường ống"]),
   ("Yêu cầu điện / nước", ["Máy bơm và bộ khuấy phễu: 3 pha 220 V / 50 Hz (cấu hình tiêu chuẩn); máy trộn: 1 pha 220 V / 50 Hz", "Công trình dùng lưới 3 pha 380 V: phương án nguồn điện được xác nhận khi đặt hàng", "Nước sạch để trộn vữa và vệ sinh máy"]),
   ("Vận hành & vệ sinh", ["Kiểm tra máy và ống bóp trước ca làm việc", "Làm ướt phễu, ống bóp, đường ống trước khi cấp vữa", "Vệ sinh đường ống ngay sau khi kết thúc để tránh tắc ống"]),
 ],
 "models_title": "Dòng máy & thông số",
 "models_lead": "Ba dòng máy bơm phun vữa bóp ống, chọn theo quy mô công trình và chiều cao/khoảng cách cần bơm.",
 "model_cols": ["Lưu lượng", "Bơm đứng / ngang tối đa", "Ống bóp (đường kính trong)", "Ống dẫn vữa"],
 "models": [
   ("TW-60", "img/thiet-bi/may-bom-phun-vua-tw60.jpg", "Nhà riêng, công trình nhỏ, trình diễn – thử nghiệm", ["0,7 – 2 m³/giờ", "12 m / 40 m", "33 mm", "D38"]),
   ("TW-20F", "img/thiet-bi/may-bom-phun-vua-tw20f.jpg", "Công trình diện tích lớn, nhà xưởng", ["1,4 – 2,5 m³/giờ", "60 m / 200 m", "38 mm", "D38"]),
   ("TW-75 / TW-105", "img/thiet-bi/may-bom-phun-vua-tw75.jpg", "Khối lượng bơm lớn – lưu lượng cao nhất dòng máy", ["2 – 6 m³/giờ", "45 m / 160 m", "43 / 50 mm", "D43"]),
 ],
 "models_note": "Lưu lượng và khoảng cách là thông số nhà sản xuất công bố; khoảng cách bơm đứng và ngang tối đa không đạt đồng thời. Kết quả thực tế phụ thuộc cấp phối vữa, đặc tính cốt liệu, tỷ lệ phụ gia và bố trí đường ống – cần xác nhận với loại vữa và điều kiện công trường trước khi chọn máy.",
 "apps_title": "Ứng dụng thi công",
 "apps": [
   ("img/thiet-bi/ung-dung-phun-vua-tran-tuong.jpg", "Phun vữa tô tường"),
   ("img/thiet-bi/ung-dung-bom-vua-vach-nhe.jpg", "Bơm vữa vách ngăn nhẹ"),
   ("img/thiet-bi/ung-dung-coffa-de-lai.jpg", "Phun vữa coffa để lại"),
   ("img/thiet-bi/ung-dung-gia-co-mai-doc.jpg", "Gia cố mái dốc, bờ sông"),
 ],
 "package": [
   ("Khảo sát & thử mẫu", "Làm rõ điều kiện công trình, thử phun mẫu (mockup) với vữa sử dụng."),
   ("Đào tạo vận hành", "Đào tạo thao tác, an toàn, vệ sinh và xử lý sự cố cơ bản cho đội thi công."),
   ("Đồng hành thi công", "Hỗ trợ giai đoạn đầu đưa máy vào vận hành thực tế."),
   ("Phụ tùng & hỗ trợ", "Phương án phụ tùng (ống bóp, súng phun…) và kênh hỗ trợ kỹ thuật theo thỏa thuận."),
 ],
 "spec": [
   ("Nguyên lý", "Bơm bóp ống (squeeze pump) hoặc bơm trục vít (rotor / stator)"),
   ("Dòng máy", "Bơm bóp ống: TW-60 · TW-20F · TW-75 / TW-105; máy phun vữa trục vít cơ động"),
   ("Lưu lượng", "0,7 – 6 m³/giờ tùy model"),
   ("Khoảng cách bơm tối đa", "đứng đến 60 m, ngang đến 200 m tùy model"),
   ("Nguồn điện", "3 pha 220 V / 50 Hz (tiêu chuẩn); phương án lưới 380 V xác nhận khi đặt hàng"),
   ("Xuất xứ", "Đài Loan"),
 ],
 "line2": {
   "title": "Dòng máy phun vữa trục vít",
   "lead": "Dòng máy thứ hai, từ một nhà sản xuất khác: máy phun vữa trục vít cơ động, gọn nhẹ, phù hợp tô trát tường cho công trình vừa và nhỏ.",
   "gallery": [("img/thiet-bi/may-phun-vua-5.jpg", "Toàn cảnh máy"), ("img/thiet-bi/may-phun-vua-4.jpg", "Phễu chứa có lưới lọc"), ("img/thiet-bi/may-phun-vua-2.jpg", "Mặt sau máy"), ("img/thiet-bi/may-phun-vua-1.jpg", "Tủ điện điều khiển")],
   "points": ["Bơm trục vít (rotor / stator) đẩy vữa liên tục, lưu lượng ổn định", "Phễu chứa có lưới lọc và mô-tơ rung chống vón cục", "Tủ điện điều khiển, máy nén khí lắp trên máy (theo cấu hình)", "Khung có bánh xe, dễ di chuyển trong công trình", "Thông số kỹ thuật và cấu hình cung cấp theo catalogue – vui lòng liên hệ"],
 },
 "videos": [("media/video-phun-vua.mp4", "media/video-phun-vua-poster.jpg", "Máy phun vữa trục vít", "Video từ nhà cung cấp thiết bị")],
 "slots": ["Video/ảnh thi công tại công trình ở Việt Nam", "Kích thước, trọng lượng từng model (chờ catalogue chi tiết)"],
},
{
 "id": "robot-xep-pallet", "form": "Robot bốc xếp & xếp pallet",
 "name": "Robot bốc xếp & xếp pallet", "k": "Tự động hóa nhà máy",
 "img": None,
 "short": "Tự động hóa bốc xếp bao vật liệu và xếp pallet tại nhà máy: giảm phụ thuộc lao động thủ công, ổn định nhịp sản xuất.",
 "intro": [
   "Tại các nhà máy vữa khô, xi măng, bột đá…, khâu bốc xếp bao và xếp pallet đòi hỏi nhiều lao động nặng. Robot xếp pallet và hệ thống nạp liệu tự động giúp giảm sức lao động và ổn định năng suất.",
   "Mỗi dự án cần khảo sát mặt bằng, loại bao và nhịp sản xuất để chọn cấu hình phù hợp.",
 ],
 "sections": [
   ("Thông tin cần khảo sát", ["Sản phẩm xử lý: loại bao, khối lượng bao, chất liệu bao", "Tải trọng và năng suất mong muốn (bao/giờ)", "Kiểu tay gắp phù hợp", "Băng tải, vị trí đặt pallet", "Mặt bằng bố trí và an toàn khu vực"]),
 ],
 "spec": [("Sản phẩm xử lý", None), ("Tải trọng", None), ("Năng suất", None), ("Tay gắp", None), ("Băng tải & mặt bằng", None)],
 "videos": [],
 "slots": ["Ảnh / video robot thật có quyền sử dụng", "Thông số và phạm vi cung cấp"],
},
]

PROCESS = [
 ("Tiếp nhận nhu cầu", "Tiếp nhận nhu cầu và điều kiện sử dụng: sản phẩm, công trình, mặt bằng, năng suất."),
 ("Lựa chọn cấu hình", "Phối hợp nhà cung cấp lựa chọn cấu hình thiết bị phù hợp."),
 ("Phương án triển khai", "Làm rõ phương án cung cấp, lắp đặt và chạy thử."),
 ("Đào tạo & hậu mãi", "Thống nhất đào tạo, phụ tùng và hỗ trợ sau bán hàng."),
]
SCOPE_NOTE = "Phạm vi cung cấp và hỗ trợ được xác định theo từng thiết bị và thỏa thuận cụ thể."

# Nhóm cho form liên hệ
FORM_GROUPS = [
 ("Nguyên liệu & Vật liệu", ["Cát khô", "Xi măng trắng", "VAE / RDP", "Sợi gia cường bê tông", "Đá mài / hạt màu / bột màu", "Hạt mài Silicon Carbide (SiC)"]),
 ("Máy móc & Tự động hóa", [e["form"] for e in EQUIPMENT]),
 ("Khác", ["Hợp tác đầu tư", "Khác"]),
]
