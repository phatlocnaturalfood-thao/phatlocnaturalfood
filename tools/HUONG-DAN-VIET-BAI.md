# Hướng dẫn viết bài SEO tự động – Phát Lộc Natural Food

Mỗi lần chạy viết **đúng 1 bài**, lấy bài đầu tiên có `"trang_thai": "chua_viet"` trong `tools/lich-bai.json`
(bỏ qua `cho_anh_xac_nhan`). Hết bài trong lịch thì tự chọn chủ đề mới cùng các nhóm (quà Tết, yến sào,
đông trùng, táo đỏ, nha đam, mỹ phẩm), không trùng bài đã có trong `kien-thuc/`.

## Các bước

1. Đọc bài cần viết trong `tools/lich-bai.json`: `tieu_de`, `tu_khoa`, `link_ve`.
2. Đọc giá, tên sản phẩm thật từ bảng giá: trong Python `from bai_chung import BY, li, link, vnd`
   (`BY[id]` = [id, nhóm, tên, quy cách, giá]; `li(id, "ghi chú")` tạo dòng `<li>` có link và giá;
   `link(id)` trả link trang sản phẩm hoặc form đặt hàng). Không tự bịa giá, mã, thành phần.
3. Viết file JSON tạm (ngoài repo) theo khuôn trong `tools/dang-bai.py`, rồi chạy
   `python3 tools/dang-bai.py <file.json>`.
4. Kiểm tra: mở file HTML vừa tạo, mọi link nội bộ tồn tại, `xmllint --noout sitemap.xml`.
5. Tạo nhánh `bai-<slug>`, commit (kèm dòng Co-Authored-By / Claude-Session theo quy định repo),
   push, tạo PR và merge squash bằng `gh api` (như các PR trước).

## Quy cách bài

- 800–1.200 chữ tiếng Việt có dấu, câu ngắn, giọng tư vấn thân thiện, gọi người đọc là "bạn".
- `title` ≤ 65 ký tự, có từ khóa chính ở đầu; `desc` 140–160 ký tự, có từ khóa.
- `slug`: không dấu, gạch nối, ≤ 60 ký tự, có từ khóa (vd `cach-ngam-yen-dung`).
- `crumb`: "Quà Tết" hoặc "Yến sào" (hoặc "Đông trùng hạ thảo", "Táo đỏ", "Nha đam", "Mỹ phẩm");
  `the_loai`: `qua-tet` cho bài quà Tết, còn lại `yen-sao`.
- `body` là HTML: mở đầu `<p class="lede">` trả lời ngay câu hỏi của tiêu đề; 3–5 mục `<h2>`;
  danh sách `<ul>/<ol>`; bảng so sánh dùng `<table class="cmp">`.
- Link: ít nhất 1 link tới trang trong cột `link_ve` (đường dẫn tương đối từ `kien-thuc/`,
  vd `../qua-tet/`, `../san-pham/<slug>/`, `../#ho-so`, `../#doanh-nghiep`) và 1–2 bài kiến thức cũ.
- `faq`: 3 câu hỏi – đáp ngắn đúng ý tìm kiếm của người dùng.
- `cta`: 1–2 nút, dạng `    <a class="btn btn-gold" href="../qua-tet/">Xem quà Tết 2027</a>`.

## Không được

- Không viết công dụng chữa bệnh, phòng bệnh, "tăng miễn dịch", "chống ung thư"… Bài có nói về sức khỏe,
  bà bầu, trẻ em, người bệnh phải có câu: "Thông tin mang tính tham khảo. Thực phẩm này không phải là thuốc
  và không có tác dụng thay thế thuốc chữa bệnh." và khuyên hỏi bác sĩ.
- Không bịa số liệu, chứng nhận, giải thưởng, nhận xét khách hàng, "bán chạy nhất", số lượng đã bán.
- Không hứa chính sách chưa có trên web (giá sỉ, cộng tác viên, miễn phí giao hàng, quà tặng…).
  Chính sách có sẵn: giao toàn quốc (TP.HCM 1–2 ngày, tỉnh 2–5 ngày), kiểm hàng khi nhận, COD/chuyển khoản,
  hóa đơn điện tử, chiết khấu quà Tết doanh nghiệp từ 20 hộp, đổi trả trong 03 ngày theo chính sách.
  Có chính sách **giá sỉ cho đại lý** và **cộng tác viên** (anh Việt xác nhận 22/10/2026), nhưng chưa có mức
  chiết khấu, điều kiện cụ thể: chỉ viết là có chính sách và mời liên hệ Zalo 0768 759 419 để nhận bảng giá sỉ /
  điều kiện cộng tác viên; không tự đặt con số, phần trăm hay quyền lợi.
- Không sửa trang chủ, giá, trang danh mục, trang sản phẩm trong lần chạy viết bài.
- Không đăng lên Facebook, Zalo hay kênh khác.

## Thông tin cửa hàng

Phát Lộc Natural Food – 511/9 Bùi Thị Xuân, Phường Tân Đông Hiệp, TP. Hồ Chí Minh – 0768 759 419 (Zalo) –
mở cửa 7:30–21:00 hằng ngày. Phân phối yến sào Việt Cường Nhân theo giấy ủy quyền; nhà máy đạt
ISO 22000, HACCP, GMP; có bản tự công bố, phiếu kiểm nghiệm Eurofins (mục Hồ sơ pháp lý trên trang chủ).
