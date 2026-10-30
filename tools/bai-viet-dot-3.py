# Sinh 4 bài kiến thức đợt 3 (lịch tuần 9/11 và 16/11) và trang Hỏi đáp mua hàng.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bai_chung import *

L = lambda slug, t: f'<a href="{slug}.html">{t}</a>'
NOTE = '  <p class="note">Thông tin mang tính tham khảo. Thực phẩm này không phải là thuốc và không có tác dụng thay thế thuốc chữa bệnh. Người có bệnh lý, phụ nữ mang thai, trẻ nhỏ nên hỏi ý kiến bác sĩ trước khi dùng.</p>'

# 1. Quà Tết cho nhân viên dưới 500.000đ
b1 = f'''  <p class="lede">Với ngân sách dưới 500.000đ mỗi phần, quà Tết yến sào cho nhân viên nên ưu tiên loại dùng ngay, đóng hộp đẹp và giá ổn định khi đặt số lượng. Phát Lộc có hơn 10 mẫu trong khoảng 230.000đ – 481.000đ.</p>

  <h2>Dưới 300.000đ</h2>
  <ul>
{li(132, "Lốc 6 hũ có hộp, gọn, dễ phát.")}
{li(335, "Hộp có tay xách, cầm về tiện.")}
{li(350, "Thêm nước hồng sâm và kẹo sâm.")}
  </ul>

  <h2>Từ 300.000đ đến 400.000đ</h2>
  <ul>
{li(334)}
{li(354)}
{li(353)}
{li(345)}
  </ul>

  <h2>Từ 400.000đ đến 500.000đ</h2>
  <ul>
{li(346)}
{li(343)}
{li(344)}
{li(312)}
  </ul>

  <h2>Kinh nghiệm đặt quà cho cả công ty</h2>
  <ul>
    <li><b>Chốt danh sách sớm:</b> gửi số lượng, ngân sách, ngày cần hàng trước 3–4 tuần để có giá tốt và kịp đóng gói.</li>
    <li><b>Một mẫu cho đa số:</b> chọn 1–2 mẫu chung giúp giao nhanh, đồng đều; quản lý có thể nhận mẫu cao hơn.</li>
    <li><b>Hóa đơn:</b> Phát Lộc xuất hóa đơn điện tử, chiết khấu từ 20 phần.</li>
    <li><b>Giao hàng:</b> giao một lần tại công ty hoặc theo danh sách địa chỉ.</li>
  </ul>
  <p>Gửi yêu cầu báo giá tại <a href="../doanh-nghiep/">mục Quà Tết doanh nghiệp</a>. Xem thêm {L("qua-tet-doanh-nghiep-theo-ngan-sach", "Chọn quà Tết doanh nghiệp 2027 theo ngân sách")}.</p>'''
page('qua-tet-cho-nhan-vien-duoi-500k',
     'Gợi ý quà Tết 2027 cho nhân viên dưới 500.000đ: yến chưng sẵn, hộp quà, túi quà yến sào từ 230.000đ, kèm kinh nghiệm đặt số lượng, hóa đơn, giao hàng.',
     'Quà Tết cho nhân viên dưới 500.000đ – 11 gợi ý yến sào', 'Quà Tết', 'Quà Tết cho nhân viên dưới 500.000đ', b1,
     '    <a class="btn btn-gold" href="../doanh-nghiep/">Nhận báo giá số lượng</a>',
     faq=[("Đặt quà Tết cho nhân viên trước bao lâu?", "Nên đặt trước 3–4 tuần với đơn từ 50 phần để kịp đóng gói và giao trước kỳ nghỉ Tết."),
          ("Có xuất hóa đơn điện tử không?", "Có, Phát Lộc xuất hóa đơn điện tử theo thông tin công ty."),
          ("Đặt bao nhiêu phần thì có chiết khấu?", "Từ 20 phần, mức chiết khấu tăng theo số lượng; gửi yêu cầu để nhận báo giá trong ngày.")])

# 2. Quà Tết cho đối tác
b2 = f'''  <p class="lede">Quà Tết cho đối tác thể hiện sự trân trọng và hình ảnh doanh nghiệp. Mẫu quà nên trang trọng, có nguồn gốc rõ ràng và được trao đúng thời điểm. Dưới đây là cách chọn và một số lưu ý khi biếu.</p>

  <h2>Chọn quà theo mức độ quan hệ</h2>
  <ul>
    <li><b>Đối tác thường xuyên (khoảng 1 triệu):</b> {BY[337][2]} – {vnd(BY[337][4])}; {BY[340][2]} – {vnd(BY[340][4])}.</li>
    <li><b>Đối tác quan trọng (1,5 – 3 triệu):</b> <a href="{link(324)}">{BY[324][2]}</a> – {vnd(BY[324][4])}; <a href="{link(336)}">{BY[336][2]}</a> (hộp gỗ) – {vnd(BY[336][4])}; <a href="{link(338)}">{BY[338][2]}</a> – {vnd(BY[338][4])}.</li>
    <li><b>Đối tác chiến lược (trên 3 triệu):</b> <a href="{link(306)}">{BY[306][2]}</a> – {vnd(BY[306][4])}; <a href="{link(313)}">{BY[313][2]}</a> – {vnd(BY[313][4])}.</li>
  </ul>

  <h2>Lưu ý khi biếu quà đối tác</h2>
  <ul>
    <li><b>Tìm hiểu quy định nhận quà:</b> một số doanh nghiệp, cơ quan có giới hạn giá trị quà; nên chọn mức phù hợp.</li>
    <li><b>Thời điểm:</b> thường từ giữa tháng Chạp; tránh những ngày cuối năm đối tác bận quyết toán.</li>
    <li><b>Người trao:</b> lãnh đạo hoặc người phụ trách trực tiếp mối quan hệ trao tận tay, kèm lời chúc ngắn.</li>
    <li><b>Thiệp và thương hiệu:</b> thiệp ghi tên công ty, lời cảm ơn cụ thể về năm hợp tác.</li>
    <li><b>Giao tận nơi:</b> với đối tác ở xa, giao thẳng đến văn phòng hoặc nhà riêng theo danh sách.</li>
  </ul>
  <p>Xem đủ mẫu tại <a href="../qua-tet/">Quà Tết yến sào 2027</a> hoặc gửi danh sách để nhận báo giá tại <a href="../doanh-nghiep/">Quà Tết doanh nghiệp</a>.</p>'''
page('qua-tet-cho-doi-tac',
     'Cách chọn quà Tết cho đối tác theo mức độ quan hệ, gợi ý giỏ quà, hộp quà yến sào từ 1 đến 5 triệu và lưu ý khi biếu: thời điểm, người trao, thiệp, quy định nhận quà.',
     'Quà Tết cho đối tác: cách chọn và lưu ý khi biếu', 'Quà Tết', 'Quà Tết cho đối tác: cách chọn và lưu ý khi biếu', b2,
     '    <a class="btn btn-gold" href="../qua-tet/">Xem quà Tết 2027</a>',
     faq=[("Quà Tết cho đối tác nên bao nhiêu tiền?", "Tùy mức độ quan hệ và quy định nhận quà của đối tác; phổ biến từ 1 đến 3 triệu, đối tác chiến lược có thể cao hơn."),
          ("Có giao quà đến từng đối tác không?", "Có, Phát Lộc giao theo danh sách địa chỉ trên toàn quốc."),
          ("Có in thiệp tên công ty không?", "Nhắn Zalo 0768 759 419 để được tư vấn thiệp và cách trình bày theo số lượng.")])

# 3. Mỗi ngày ăn bao nhiêu yến
b3 = f'''  <p class="lede">Không có liều lượng chuẩn bắt buộc cho yến sào vì đây là thực phẩm, không phải thuốc. Mức dùng phổ biến được nhiều người tham khảo với người lớn khỏe mạnh là khoảng 3–5gr yến khô mỗi lần, 2–3 lần mỗi tuần. Ăn đều đặn quan trọng hơn ăn nhiều một lúc.</p>

  <h2>Mức dùng tham khảo</h2>
  <table class="cmp">
    <thead><tr><th>Đối tượng</th><th>Mỗi lần (yến khô)</th><th>Số lần</th></tr></thead>
    <tbody>
      <tr><td>Người lớn khỏe mạnh</td><td>3–5gr</td><td>2–3 lần/tuần</td></tr>
      <tr><td>Người lớn tuổi</td><td>2–3gr</td><td>2–3 lần/tuần</td></tr>
      <tr><td>Trẻ từ 1 tuổi</td><td>1–2gr</td><td>1–2 lần/tuần, hỏi bác sĩ trước</td></tr>
    </tbody>
  </table>
  <p>Đổi ra sản phẩm: 1 tai <a href="{link(111)}">yến tinh chế 18–20 tai</a> khoảng 5gr, đủ 1–2 phần chưng; 100gr dùng được khoảng 1–2 tháng cho một người.</p>

  <h2>Khi nào ăn</h2>
  <ul>
    <li>Buổi sáng lúc bụng đói nhẹ hoặc buổi tối trước khi ngủ khoảng 1 giờ là thời điểm nhiều người chọn.</li>
    <li>Không cần ăn mỗi ngày; duy trì đều theo tuần.</li>
  </ul>

  <h2>Những điều nên tránh</h2>
  <ul>
    <li>Ăn quá nhiều một lần không giúp hấp thu nhiều hơn mà gây lãng phí.</li>
    <li>Chưng quá lâu hoặc đun sôi trực tiếp làm yến tan, mất kết cấu; xem {L("cach-chung-yen-sao", "cách chưng yến đường phèn")}.</li>
    <li>Người đang dị ứng, sốt, có bệnh lý đặc biệt nên hỏi bác sĩ.</li>
  </ul>
{NOTE}'''
page('moi-ngay-an-bao-nhieu-yen',
     'Mỗi ngày ăn bao nhiêu yến sào là đủ? Mức dùng tham khảo cho người lớn, người lớn tuổi, trẻ nhỏ, thời điểm ăn và những điều nên tránh khi dùng yến.',
     'Mỗi ngày ăn bao nhiêu yến là đủ?', 'Yến sào', 'Mỗi ngày ăn bao nhiêu yến là đủ?', b3,
     '    <a class="btn btn-gold" href="../yen-tinh-che/">Xem yến tinh chế</a>\n    <a class="btn btn-line" href="../nuoc-yen/">Xem nước yến chưng sẵn</a>',
     faq=[("Ăn yến mỗi ngày có được không?", "Được, nhưng nên dùng lượng nhỏ; phổ biến là 2–3 lần mỗi tuần với người lớn."),
          ("100gr yến dùng được bao lâu?", "Khoảng 1–2 tháng cho một người nếu dùng 3–5gr mỗi lần, 2–3 lần mỗi tuần."),
          ("Nước yến chưng sẵn có thay được yến khô không?", "Nước yến tiện dùng nhưng lượng yến mỗi hũ ít hơn một phần yến tự chưng; có thể dùng xen kẽ.")])

# 4. Trẻ em, bà bầu, người già ăn yến
b4 = f'''  <p class="lede">Yến sào là thực phẩm dễ ăn, nhiều gia đình dùng cho trẻ nhỏ, phụ nữ mang thai và người lớn tuổi. Mỗi nhóm cần lưu ý riêng về lượng dùng, thời điểm bắt đầu và cách chế biến. Thông tin dưới đây mang tính tham khảo; hãy hỏi bác sĩ với trường hợp cụ thể.</p>

  <h2>Trẻ em</h2>
  <ul>
    <li><b>Thời điểm:</b> nhiều gia đình cho trẻ dùng từ khoảng 1 tuổi, khi đã ăn dặm quen; trẻ dưới 1 tuổi nên hỏi bác sĩ.</li>
    <li><b>Lượng:</b> bắt đầu rất ít, khoảng 1gr yến khô mỗi lần, quan sát dấu hiệu dị ứng trong 1–2 ngày.</li>
    <li><b>Cách nấu:</b> chưng ít đường hoặc nấu cùng cháo, súp; chọn <a href="../yen-tinh-che/">yến vụn, yến tinh chế</a> cho dễ ăn.</li>
  </ul>

  <h2>Phụ nữ mang thai</h2>
  <ul>
    <li><b>Thời điểm:</b> nhiều người chờ qua 3 tháng đầu; tốt nhất hỏi bác sĩ sản khoa trước khi dùng.</li>
    <li><b>Lượng:</b> khoảng 3gr mỗi lần, 2–3 lần mỗi tuần (tham khảo).</li>
    <li><b>Lưu ý:</b> người có tiểu đường thai kỳ nên hạn chế đường phèn; chọn yến có nguồn gốc rõ, đủ giấy tờ.</li>
  </ul>

  <h2>Người lớn tuổi</h2>
  <ul>
    <li><b>Lượng:</b> 2–3gr mỗi lần, 2–3 lần mỗi tuần.</li>
    <li><b>Cách nấu:</b> chưng mềm, có thể thêm táo đỏ, hạt sen; người tiểu đường dùng ít hoặc không đường.</li>
    <li><b>Tiện nhất:</b> <a href="../nuoc-yen/">nước yến chưng sẵn</a> hoặc tai yến nhỏ chia sẵn phần.</li>
  </ul>

  <h2>Chọn yến an toàn cho gia đình</h2>
  <p>Ưu tiên yến có bản tự công bố, phiếu kiểm nghiệm và chứng nhận nhà máy. Xem {L("phan-biet-yen-sao-that-gia", "Cách phân biệt yến sào thật – giả")} và hồ sơ yến Việt Cường Nhân tại <a href="../chung-nhan/#ho-so">Hồ sơ pháp lý</a>.</p>
{NOTE}'''
page('tre-em-ba-bau-nguoi-gia-an-yen',
     'Trẻ em, bà bầu, người lớn tuổi ăn yến sào thế nào: thời điểm bắt đầu, lượng dùng tham khảo, cách chế biến và lưu ý an toàn. Nên hỏi bác sĩ với trường hợp cụ thể.',
     'Trẻ em, bà bầu, người già ăn yến sào thế nào?', 'Yến sào', 'Trẻ em, bà bầu, người già ăn yến sào thế nào?', b4,
     '    <a class="btn btn-gold" href="../yen-tinh-che/">Xem yến tinh chế</a>',
     faq=[("Trẻ mấy tuổi ăn được yến?", "Nhiều gia đình cho trẻ dùng từ khoảng 1 tuổi với lượng rất nhỏ; trẻ dưới 1 tuổi nên hỏi bác sĩ."),
          ("Bà bầu ăn yến từ tháng thứ mấy?", "Nhiều người bắt đầu sau 3 tháng đầu thai kỳ; nên hỏi bác sĩ sản khoa trước."),
          ("Người tiểu đường ăn yến được không?", "Có thể dùng yến chưng không đường hoặc ít đường; nên hỏi bác sĩ điều trị.")])

# 5. Hỏi đáp mua hàng
QA = [
  ("Đặt hàng", [
    ("Đặt hàng bằng cách nào?", 'Điền form <a href="../#dat-hang">Đặt hàng</a> trên website, nhắn Zalo hoặc gọi 0768 759 419, hoặc nhắn Fanpage Phát Lộc Natural Food. Nhân viên gọi xác nhận đơn trước khi giao.'),
    ("Có mua tại cửa hàng được không?", "Có, tại 511/9 Bùi Thị Xuân, Phường Tân Đông Hiệp, TP. Hồ Chí Minh, mở cửa 7:30–21:00 mỗi ngày."),
    ("Đặt quà Tết số lượng cho công ty thế nào?", 'Gửi số lượng, ngân sách, ngày cần hàng tại <a href="../doanh-nghiep/">mục Quà Tết doanh nghiệp</a>; Phát Lộc báo giá trong ngày, chiết khấu từ 20 phần.')]),
  ("Giao hàng", [
    ("Giao hàng mất bao lâu?", "TP. Hồ Chí Minh và lân cận 1–2 ngày làm việc; tỉnh, thành khác 2–5 ngày làm việc. Dịp lễ, Tết có thể lâu hơn."),
    ("Phí giao hàng bao nhiêu?", "Tính theo khu vực và khối lượng đơn, nhân viên báo khi gọi xác nhận, trước khi giao."),
    ("Có được kiểm hàng khi nhận không?", "Có. Khách kiểm tra kiện hàng, số lượng, loại sản phẩm, niêm phong trước khi thanh toán; hàng sai hoặc hư hỏng có quyền từ chối nhận.")]),
  ("Thanh toán và hóa đơn", [
    ("Thanh toán bằng cách nào?", "Thanh toán khi nhận hàng (COD) hoặc chuyển khoản vào tài khoản đứng tên CÔNG TY TNHH SẢN XUẤT PHÁT LỘC NATURAL FOOD, số tài khoản do nhân viên gửi khi xác nhận đơn."),
    ("Có xuất hóa đơn điện tử không?", "Có, khách báo thông tin xuất hóa đơn khi xác nhận đơn.")]),
  ("Đổi trả", [
    ("Trường hợp nào được đổi trả?", 'Giao sai sản phẩm, thiếu hàng, hư hỏng do vận chuyển hoặc lỗi nhà sản xuất, hết hạn sử dụng. Báo trong 03 ngày kể từ khi nhận, kèm hình ảnh hoặc video mở hàng. Xem <a href="../chinh-sach/doi-tra.html">Chính sách đổi trả</a>.'),
    ("Hoàn tiền mất bao lâu?", "Trong 07 ngày làm việc kể từ khi Phát Lộc nhận lại hàng, chuyển khoản vào tài khoản khách cung cấp.")]),
  ("Sản phẩm và giấy tờ", [
    ("Yến sào của Phát Lộc có nguồn gốc từ đâu?", 'Yến sào Việt Cường Nhân, Phát Lộc phân phối theo giấy ủy quyền. Nhà máy đạt ISO 22000, HACCP, GMP; xem <a href="../chung-nhan/#ho-so">Hồ sơ pháp lý</a>.'),
    ("Sản phẩm có bản tự công bố và kiểm nghiệm không?", "Có. Bản tự công bố, phiếu kiểm nghiệm Eurofins và phiếu công bố mỹ phẩm được đăng công khai trên website."),
    ("Bảo quản yến sào thế nào?", "Yến khô để nơi khô ráo, đậy kín, mùa ẩm để ngăn mát tủ lạnh. Yến đã ngâm nở nên chưng ngay; nước yến chưng sẵn đã mở nắp dùng hết trong ngày.")])
]
faq_all = [qa for _, g in QA for qa in g]
b5 = '  <p class="lede">Giải đáp nhanh về đặt hàng, giao hàng, thanh toán, đổi trả và giấy tờ sản phẩm tại Phát Lộc Natural Food. Chưa thấy câu trả lời, anh chị nhắn Zalo 0768 759 419.</p>\n' + '\n'.join(
    f'\n  <h2>{g}</h2>\n' + '\n'.join(f'  <details><summary>{q}</summary><p>{a}</p></details>' for q, a in items) for g, items in QA)
import re as _re
ld_faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": _re.sub(r'<[^>]+>', '', a)}} for q, a in faq_all]}
page('hoi-dap-mua-hang', 'Hỏi đáp mua hàng tại Phát Lộc Natural Food: cách đặt hàng, thời gian và phí giao hàng, kiểm hàng, thanh toán COD, chuyển khoản, hóa đơn điện tử, đổi trả, giấy tờ yến sào.',
     'Hỏi đáp mua hàng', 'Hỏi đáp', 'Hỏi đáp mua hàng', b5,
     '    <a class="btn btn-gold" href="https://zalo.me/0768759419">Nhắn Zalo 0768 759 419</a>')
# Bài hỏi đáp: thay schema Article bằng FAQPage
p = R + 'kien-thuc/hoi-dap-mua-hang.html'
h = open(p, encoding='utf-8').read()
h = _re.sub(r'<script type="application/ld\+json">.*?</script>\n', '<script type="application/ld+json">' + json.dumps(ld_faq, ensure_ascii=False) + '</script>\n', h, count=1, flags=_re.S)
h = h.replace('</head>', '<style>.article details{background:var(--paper);border:1px solid var(--line);border-radius:10px;padding:12px 16px;margin-bottom:10px}.article summary{cursor:pointer;font-weight:600}.article details p{margin:10px 0 0;color:var(--muted)}</style>\n</head>', 1)
open(p, 'w', encoding='utf-8').write(h)

# Danh sách bài + sitemap
ix = open(R + 'kien-thuc/index.html', encoding='utf-8').read()
cards = [
  ('qua-tet-cho-nhan-vien-duoi-500k', 'qua-tet', 'Quà Tết', 'Quà Tết cho nhân viên dưới 500.000đ', '11 gợi ý yến sào từ 230.000đ và kinh nghiệm đặt số lượng cho công ty.'),
  ('qua-tet-cho-doi-tac', 'qua-tet', 'Quà Tết', 'Quà Tết cho đối tác: cách chọn và lưu ý khi biếu', 'Chọn mẫu theo mức độ quan hệ, thời điểm, người trao, thiệp.'),
  ('moi-ngay-an-bao-nhieu-yen', 'yen-sao', 'Yến sào', 'Mỗi ngày ăn bao nhiêu yến là đủ?', 'Mức dùng tham khảo theo đối tượng, thời điểm ăn và điều nên tránh.'),
  ('tre-em-ba-bau-nguoi-gia-an-yen', 'yen-sao', 'Yến sào', 'Trẻ em, bà bầu, người già ăn yến sào thế nào?', 'Thời điểm bắt đầu, lượng dùng, cách nấu và lưu ý an toàn.'),
  ('hoi-dap-mua-hang', 'yen-sao', 'Hỏi đáp', 'Hỏi đáp mua hàng', 'Đặt hàng, giao hàng, thanh toán, hóa đơn, đổi trả, giấy tờ sản phẩm.'),
]
add = ''.join(f'''    <a class="post" href="{s}.html" data-cat="{c}">
      <span class="eyebrow">{e}</span>
      <h2>{t}</h2>
      <p>{d}</p>
      <span class="more">Đọc bài</span>
    </a>
''' for s, c, e, t, d in cards if f'href="{s}.html"' not in ix)
ix = ix.replace('  <div class="posts" id="posts">\n', '  <div class="posts" id="posts">\n' + add, 1)
open(R + 'kien-thuc/index.html', 'w', encoding='utf-8').write(ix)
sm = open(R + 'sitemap.xml', encoding='utf-8').read()
add = ''.join(f'  <url><loc>https://phatlocnaturalfood.com/kien-thuc/{c[0]}.html</loc><lastmod>2026-10-22</lastmod></url>\n' for c in cards if f'kien-thuc/{c[0]}.html' not in sm)
open(R + 'sitemap.xml', 'w', encoding='utf-8').write(sm.replace('</urlset>', add + '</urlset>'))
print('ok')
