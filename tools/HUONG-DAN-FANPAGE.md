# Hướng dẫn đăng bài Fanpage tự động – Phát Lộc Natural Food

Mỗi ngày lên lịch **2 bài** trên Page "Phát Lộc Natural Food - Yến Sào & Đông Trùng Hạ Thảo"
(asset_id 1415830271609330, business_id 1837579484336824) lúc **11:00** và **18:00** cùng ngày.
Từ 23/10 đến 29/10/2026 buổi tối đã có bài 19:30 lên lịch sẵn: những ngày này chỉ lên lịch bài 11:00.

## Làm bù khi lỡ lịch (yêu cầu của anh Việt)

Việc này chạy mỗi giờ từ 8:40 đến 20:40. Mỗi lần chạy:
1. Xem `tools/fanpage-da-dang.json`: hôm nay đã có đủ bài 11:00 và 18:00 chưa (23–29/10/2026 chỉ cần bài 11:00),
   và các ngày trước kể từ 23/10/2026 có ngày nào thiếu không.
2. Nếu đủ hết: dừng ngay, **không** mở Chrome, **không** gửi thông báo, không commit gì.
3. Nếu thiếu: lên lịch bù ngay khi kết nối được.
   - Bài hôm nay mà giờ đã qua (vd 11:00 đã qua): lên lịch sớm nhất có thể (hiện tại + 20 phút).
   - Bài các ngày trước bị lỡ: lên lịch trong hôm nay, cách nhau ít nhất 90 phút, trước 21:30; tổng cả ngày
     tối đa 4 bài, còn dư thì dời sang các khung trống ngày mai (8:00, 13:00, 15:00) và ghi rõ.
   - Thông báo ghi rõ "Lên lịch bù" và giờ đăng mới.
4. Không kết nối được Chrome / Facebook: gửi thông báo lỗi **một lần mỗi buổi** (sáng, chiều), không gửi mỗi giờ;
   lần chạy sau tự thử lại.

## Chọn nội dung

- **11:00 – chia sẻ bài web mới:** bài kiến thức đăng sáng cùng ngày trên phatlocnaturalfood.com
  (bài có `ngay_dang` hôm nay trong `tools/lich-bai.json`). Chưa có thì lấy bài web gần nhất chưa chia sẻ.
- **18:00 – theo tuần mẫu:** T2 kiến thức yến · T3 mẫu quà Tết · T4 uy tín, giấy tờ · T5 công thức ·
  T6 quà Tết doanh nghiệp · T7 sản phẩm lẻ (yến, đông trùng, táo đỏ, nha đam, mỹ phẩm) · CN hỏi đáp.
  Từ 01/12/2026 đến Tết: T3 và T6 đều là quà Tết.
- Không lặp chủ đề/mẫu đã đăng trong 14 ngày gần nhất (xem `tools/fanpage-da-dang.json`).
- Giá, tên, thành phần chỉ lấy từ bảng giá web (`tools/bai_chung.py`: `BY[id]`). Ảnh lấy từ
  `images/san-pham/` (bản .jpg 900–1000px) của đúng sản phẩm, hoặc `images/mxh/`, `ho-so/` cho bài uy tín.

## Chuẩn bài (SEO Facebook)

1. Dòng đầu: biểu tượng + từ khóa chính + lợi ích, dưới 80 ký tự.
2. 1 câu hỏi gợi nhu cầu.
3. 3–5 dòng ✅ nội dung chính.
4. Link web có mã theo dõi: `https://phatlocnaturalfood.com/<đường dẫn>?utm_source=facebook&utm_medium=bai_viet&utm_campaign=tet2027` (anchor `#...` đặt sau tham số).
5. `📞 Zalo/Hotline: 0768 759 419`
6. 1 câu hỏi mời bình luận.
7. Dòng trống rồi 5 hashtag theo nhóm, kết thúc bằng 1 dấu cách:
   - Quà Tết: #QuaTet2027 #GioQuaTet #QuaBieuTet #YenSao #PhatLocNaturalFood
   - Quà Tết doanh nghiệp: #QuaTetDoanhNghiep #QuaTangDoanhNghiep #QuaTet2027 #YenSao #PhatLocNaturalFood
   - Kiến thức yến: #YenSao #YenSaoChinhHang #ChungYenSao #VietCuongNhan #PhatLocNaturalFood
   - Đông trùng: #DongTrungHaThao #TraDongTrung #QuaSucKhoe #YenSao #PhatLocNaturalFood
   - Táo đỏ, nha đam: #TaoDoTanCuong #NhaDam #MonNgonMoiNgay #ThucPhamThienNhien #PhatLocNaturalFood
   - Mỹ phẩm: #MyPhamYenSao #TBeauty #ChamSocDa #QuaTetChoMe #PhatLocNaturalFood

Không được: ghi mức chiết khấu sỉ/cộng tác viên (chỉ mời nhắn Zalo); viết công dụng chữa bệnh; bịa nhận xét
khách, số đã bán, "bán chạy nhất"; hứa khuyến mãi chưa có; đăng lên Page khác (đặc biệt "Yến Sào Đỗ Thị Toán",
"YẾN & SỨC KHỎE").

## Thao tác Business Suite (Claude in Chrome)

0. **Quan trọng (từ 22/10/2026 Page đã nối Instagram):** ô "Đăng lên" mặc định chọn cả Facebook và Instagram.
   Bài Fanpage: mở ô "Đăng lên", **bỏ tick phatlocnaturalfood (Instagram)**, chỉ giữ Page. Bài Instagram làm ngược lại.
1. Chọn trình duyệt có Business Suite đã đăng nhập phatlocnaturalfood@gmail.com (hồ sơ "PHÁT LỘC NATURAL FOODS"),
   gọi tabs_context_mcp, mở tab mới:
   `https://business.facebook.com/latest/composer?asset_id=1415830271609330&business_id=1837579484336824`
2. Chép ảnh vào `/mnt/user-data/uploads/fb/` (chỉ thư mục uploads được phép tải lên).
3. Ô chọn file của Facebook tạo động: trước khi bấm "Thêm ảnh/video", chạy JS
   `const o=HTMLInputElement.prototype.click;HTMLInputElement.prototype.click=function(){if(this.type==='file'){this.setAttribute('aria-label','claude-upload');this.style.display='block';if(!this.isConnected)document.body.appendChild(this);return;}return o.call(this)};`
   rồi bấm "Thêm ảnh/video", `find` "file input labeled claude-upload", `file_upload` đường dẫn ảnh.
4. Bấm ô Văn bản, gõ nội dung, nhấn Escape. Kiểm tra bằng JS `innerText` của ô contenteditable rằng hashtag cuối còn đủ.
5. Bật "Đặt ngày và giờ", bấm ô ngày chọn đúng ngày trong lịch; ô giờ: bấm phần giờ gõ 2 chữ số, bấm phần phút gõ 2 chữ số;
   bấm ra ngoài, phóng to xác nhận đúng ngày giờ rồi bấm "Lên lịch". Hộp gợi ý quảng cáo hiện ra thì bấm "Để sau".
6. Mở `https://business.facebook.com/latest/posts/scheduled_posts?asset_id=1415830271609330&business_id=1837579484336824`
   xác nhận 2 bài mới đúng giờ, không trùng. Đóng tab đã mở.
7. Ghi 2 bài vào `tools/fanpage-da-dang.json`, commit + PR + merge như quy định repo.

---

# Instagram @phatlocnaturalfood (anh Việt yêu cầu 22/10/2026: tự lên lịch mỗi ngày cùng Fanpage)

Mỗi ngày **1 bài feed lúc 19:30** trên Instagram @phatlocnaturalfood, lên lịch qua Business Suite cùng lượt chạy Fanpage.
23–25/10/2026 đã lên lịch 9 bài ra mắt (xem `tools/instagram-da-dang.json`); việc tự động bắt đầu từ **26/10/2026**.
Lịch chi tiết và tuần mẫu: tab "Lịch Instagram hằng ngày" trong tài liệu kế hoạch SEO (claude.ai/artifact/EQrUZDTHHn7ZLVqoiZgFaK).

## Làm bù
Giống Fanpage: xem `tools/instagram-da-dang.json`; ngày nào từ 26/10/2026 thiếu bài 19:30 thì lên lịch bù
(giờ đã qua → hiện tại + 20 phút; bài ngày cũ cách nhau ≥ 90 phút, trước 21:30, tối đa 2 bài Instagram/ngày).

## Chọn nội dung (tuần mẫu)
T2 carousel kiến thức (tóm bài web sáng cùng ngày, 3–5 ảnh) · T3 mẫu quà Tết · T4 Reels hoặc carousel nhiều mẫu quà theo ngân sách ·
T5 carousel công thức · T6 quà Tết doanh nghiệp · T7 Reels video anh quay (chưa có video thì carousel ảnh cửa hàng/sản phẩm) · CN hỏi đáp.
Từ 01/12/2026 đến Tết: T3 và T6 đều là quà Tết. Không lặp mẫu đã đăng Instagram trong 14 ngày.
Không dùng ảnh có chữ "5 vị" (ảnh ghép `images/mxh/qua-tet-theo-ngan-sach.jpg`, ảnh QTH06 cũ).

## Chuẩn bài (SEO Instagram)
1. Dòng đầu: biểu tượng + từ khóa chính + lợi ích, dưới 125 ký tự.
2. 1 câu hỏi gợi nhu cầu, 3–5 dòng ✅, giá đúng theo web (`BY[id]`).
3. `👉 Xem mẫu và đặt hàng: link ở bio` (link trong bài Instagram không bấm được – không dán URL).
4. `📞 Zalo 0768 759 419`, 1 câu mời bình luận/lưu bài/tag bạn.
5. Dòng trống + 5 hashtag (bộ hashtag như Fanpage), kết thúc bằng 1 dấu cách.
Cùng các điều cấm như Fanpage (không chiết khấu sỉ/CTV, không công dụng chữa bệnh, không bịa nhận xét).

## Thao tác
Composer như Fanpage, nhưng ở "Đăng lên" chỉ giữ **phatlocnaturalfood** (bỏ tick Page). Hộp văn bản Instagram ở y≈590;
"Đặt ngày và giờ" → chọn ngày, giờ 19:30 → "Lên lịch" → "Để sau". Kiểm tra trang "Đã lên lịch": dòng có tên phatlocnaturalfood.
Ghi bài vào `tools/instagram-da-dang.json` (cùng commit với Fanpage). Thông báo gộp: "Fanpage: … | IG 19:30: …".
Story và link bio: anh Việt tự làm trên điện thoại (Business Suite web không gắn được sticker link).
