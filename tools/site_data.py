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
 "id": "cat-kho", "form": "Cát khô", "name": "Cát khô (cát silica phân cỡ)", "short": "Cát khô",
 "img": "img/san-pham/cat-hero.jpg",
 "pledge": [("CLEAN", "Sạch"), ("CONSISTENT", "Đồng đều"), ("RELIABLE", "Đáng tin cậy")],
 "intro": "Cát đã sấy khô và sàng phân cỡ, dùng làm cốt liệu cho vữa khô trộn sẵn, keo dán gạch, vữa tự san phẳng, bê tông trang trí và các ứng dụng công nghiệp khác.",
 "points": [
   "Nhiều cỡ hạt để lựa chọn theo công thức sản phẩm.",
   "Đóng gói theo yêu cầu: bao Jumbo hoặc bao nhỏ.",
   "Thông số kỹ thuật (độ ẩm, cấp phối, tạp chất) cung cấp theo từng lô và từng đơn hàng.",
 ],
 "grades": [
   ("Số 1", "0,0 – 0,3 mm", "img/san-pham/cat-so-1.jpg"),
   ("Số 2", "0,3 – 0,7 mm", "img/san-pham/cat-so-2.jpg"),
   ("Số 3", "0,7 – 1,7 mm", "img/san-pham/cat-so-3.jpg"),
   ("Số 4", "1,7 – 2,4 mm", "img/san-pham/cat-so-4.jpg"),
   ("Số 5", "2,4 – 3,5 mm", "img/san-pham/cat-so-5.jpg"),
   ("Số 6", "3,5 – 5,0 mm", "img/san-pham/cat-so-6.jpg"),
 ],
 "grades_note": "Ảnh mẫu cát phân cỡ. Dải cỡ hạt mang tính tham khảo; thông số chính thức theo phiếu kiểm tra của từng lô.",
 "slots": ["Phiếu kiểm tra chất lượng mẫu (độ ẩm, cấp phối) – chờ tài liệu", "Ảnh đóng gói / giao hàng thực tế"],
},
{
 "id": "xi-mang-trang", "form": "Xi măng trắng", "name": "Xi măng trắng", "short": "Xi măng trắng",
 "img": "img/san-pham/xi-mang-trang-coremat-bao.jpg",
 "img_full": "img/san-pham/xi-mang-trang-coremat.jpg",
 "img_caption": "Hình minh họa bao bì CoreMat dự kiến: bao 40 kg và Jumbo, cấp 42.5 / 52.5",
 "pledge": [("WHITENESS", "Độ trắng"), ("CONSISTENCY", "Tính ổn định"), ("STRENGTH", "Cường độ")],
 "intro": "Cung cấp xi măng trắng cho sản xuất vật liệu (vữa, keo dán gạch, bột trét, gạch terrazzo, sản phẩm trang trí) và cho thi công.",
 "points": [
   "Thông tin thành phần, cấp cường độ, độ trắng và xuất xứ được cung cấp theo từng sản phẩm cụ thể.",
   "Có chứng nhận chất lượng (COA) đi kèm theo lô hàng.",
   "Tư vấn lựa chọn loại xi măng trắng phù hợp với ứng dụng.",
   "Đang phát triển dòng xi măng trắng phối trộn mang thương hiệu CoreMat (dự kiến bao 40 kg và Jumbo, cấp 42.5 / 52.5).",
 ],
 "slots": ["Bảng thông số theo từng mã sản phẩm (cấp cường độ, độ trắng, quy cách bao)"],
},
{
 "id": "hoa-chat", "form": "VAE / RDP", "name": "Phụ gia & hóa chất xây dựng (VAE, RDP…)", "short": "VAE / RDP",
 "img": None,
 "intro": "Nhũ tương VAE và bột polymer tái phân tán RDP cùng các phụ gia cho vữa khô, keo dán gạch, chống thấm và bột trét.",
 "points": [
   "Tư vấn lựa chọn phụ gia theo ứng dụng và yêu cầu kỹ thuật.",
   "Cung cấp tài liệu kỹ thuật (TDS, SDS) theo từng sản phẩm.",
 ],
 "slots": ["Danh mục mã sản phẩm và tài liệu TDS"],
},
{
 "id": "trang-tri", "form": "Đá mài / hạt màu / bột màu", "name": "Đá mài, hạt thủy tinh & bột màu", "short": "Vật liệu trang trí",
 "img": "img/da-ho-phach.jpg",
 "intro": "Vật liệu trang trí cho terrazzo, bê tông nghệ thuật và hoàn thiện kiến trúc: hạt đá mài, hạt thủy tinh màu, cát màu và bột màu.",
 "points": [
   "Nhiều màu sắc và kích cỡ hạt.",
   "Hỗ trợ mẫu để kiến trúc sư và nhà thầu lựa chọn.",
 ],
 "gallery": [
   ("img/hat-xanh-tay.jpg", "Hạt thủy tinh xanh"), ("img/da-ho-phach.jpg", "Hạt hổ phách"),
   ("img/thuy-tinh-luc.jpg", "Thủy tinh xanh lục"), ("img/da-ngoc.jpg", "Hạt ngọc lam"),
   ("img/bot-mau.jpg", "Cát màu & bột màu"), ("img/cat-den.jpg", "Cát đen"),
   ("img/da-xanh-duong.jpg", "Thủy tinh xanh dương"), ("img/hat-luc.jpg", "Hạt xanh lá"),
 ],
},
]

# ---------------- MÁY MÓC & TỰ ĐỘNG HÓA ----------------
TECH_INTRO = "Core Material phát triển mảng thương mại thiết bị và giải pháp công nghệ, kết nối các nhà cung cấp phù hợp với nhu cầu sản xuất và thi công tại Việt Nam."

EQUIPMENT = [
{
 "id": "phun-grc", "form": "Thiết bị phun GRC/GFRC",
 "name": "Thiết bị phun GRC / GFRC", "k": "Sản xuất cấu kiện",
 "img": "img/thiet-bi/may-phun-grc.jpg",
 "short": "Hệ thống phun cho sản xuất cấu kiện bê tông cốt sợi thủy tinh: tấm ốp, phào chỉ, cấu kiện kiến trúc.",
 "intro": [
   "GRC/GFRC (bê tông cốt sợi thủy tinh) được dùng để sản xuất các cấu kiện mỏng, nhẹ nhưng bền: tấm ốp mặt dựng, phào chỉ, lam, chậu, cấu kiện trang trí kiến trúc.",
   "Thiết bị phun GRC cung cấp hỗn hợp vữa và sợi thủy tinh lên khuôn, giúp sản xuất đồng đều và năng suất hơn so với thi công thủ công.",
 ],
 "diff": "Khác với máy phun vữa tô tường (thi công tại công trình), thiết bị phun GRC phục vụ sản xuất cấu kiện tại xưởng, đi kèm khuôn và quy trình bảo dưỡng riêng.",
 "sections": [
   ("Ứng dụng", ["Tấm ốp mặt dựng, phào chỉ, cột, lam trang trí", "Cấu kiện kiến trúc và sản phẩm trang trí từ GFRC", "Xưởng sản xuất cấu kiện đúc sẵn"]),
   ("Cấu hình hệ thống (theo nhà cung cấp)", ["Máy phun và bơm vữa", "Cụm súng phun", "Thiết bị phụ trợ: trộn, cấp liệu, khí nén", "Phụ tùng thay thế đi kèm"]),
 ],
 "spec": [("Model", None), ("Công suất / năng suất", None), ("Nguồn điện", None), ("Khả năng cắt – phun sợi", None), ("Kích thước, trọng lượng", None)],
 "videos": [("media/video-phun-grc.mp4", "media/video-phun-grc-poster.jpg", "Thiết bị phun GRC", "Video từ nhà cung cấp thiết bị"),
            ("media/video-san-xuat-grc.mp4", "media/video-san-xuat-grc-poster.jpg", "Trộn & cấp liệu", "Video từ nhà cung cấp thiết bị")],
 "slots": ["Catalogue và bảng thông số được xác nhận", "Ảnh cụm súng phun và thiết bị phụ trợ"],
},
{
 "id": "phun-vua-to-tuong", "form": "Máy phun vữa tô tường",
 "name": "Máy phun vữa tô tường", "k": "Thi công tại công trình",
 "img": "img/thiet-bi/may-phun-vua-2.jpg",
 "gallery": ["img/thiet-bi/may-phun-vua-1.jpg", "img/thiet-bi/may-phun-vua-4.jpg", "img/thiet-bi/may-phun-vua-5.jpg"],
 "short": "Cơ giới hóa công tác cấp, bơm và phun vữa tô tường, giảm sức lao động và tăng tiến độ thi công.",
 "intro": [
   "Máy phun vữa giúp cơ giới hóa công đoạn cấp vữa, bơm và phun lên tường, thay cho thao tác trát tay. Vữa được phun đều, lớp tô đặc chắc hơn và tiến độ thi công được cải thiện.",
   "Hiệu quả cao nhất khi máy được dùng đồng bộ với vữa trộn sẵn phù hợp, đội ngũ được đào tạo và quy trình vận hành – vệ sinh đúng chuẩn.",
 ],
 "sections": [
   ("Loại vữa phù hợp", ["Vữa tô trộn sẵn gốc xi măng", "Các loại vữa, bột trét khác theo khuyến nghị của nhà sản xuất máy"]),
   ("Cấu hình máy", ["Thân máy, phễu chứa và bơm vữa", "Ống dẫn vữa và súng phun", "Máy nén khí (theo cấu hình)"]),
   ("Yêu cầu điện / nước / khí", ["Nguồn điện theo thông số máy", "Nước sạch để trộn và vệ sinh", "Khí nén cho súng phun"]),
   ("Vận hành & vệ sinh", ["Kiểm tra, bôi trơn trước ca làm việc", "Làm ướt phễu, bơm, ống trước khi cấp vữa", "Vệ sinh bằng nước sạch sau khi kết thúc để tránh tắc ống"]),
 ],
 "package": [
   ("Khảo sát & thử mẫu", "Làm rõ điều kiện công trình, thử phun mẫu (mockup) với vữa sử dụng."),
   ("Đào tạo vận hành", "Đào tạo thao tác, an toàn, vệ sinh và xử lý sự cố cơ bản cho đội thi công."),
   ("Đồng hành thi công", "Hỗ trợ giai đoạn đầu đưa máy vào vận hành thực tế."),
   ("Phụ tùng & hỗ trợ", "Phương án phụ tùng và kênh hỗ trợ kỹ thuật theo thỏa thuận."),
 ],
 "spec": [("Model", None), ("Năng suất phun", None), ("Chiều cao / khoảng cách bơm", None), ("Nguồn điện", None), ("Kích thước, trọng lượng", None)],
 "videos": [("media/video-phun-vua.mp4", "media/video-phun-vua-poster.jpg", "Phun vữa lên tường", "Video từ nhà cung cấp thiết bị")],
 "slots": ["Catalogue và bảng thông số được xác nhận", "Video/ảnh thi công tại công trình ở Việt Nam"],
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
 ("Nguyên liệu & Vật liệu", ["Cát khô", "Xi măng trắng", "VAE / RDP", "Đá mài / hạt màu / bột màu"]),
 ("Máy móc & Tự động hóa", [e["form"] for e in EQUIPMENT]),
 ("Khác", ["Hợp tác đầu tư", "Khác"]),
]
