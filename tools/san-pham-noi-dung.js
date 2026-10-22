// Nội dung 10 trang sản phẩm chủ lực. Giá, quy cách, ảnh lấy tự động từ index.html theo id.
const YEN_GIAY_TO = "Yến sào Việt Cường Nhân sản xuất tại nhà máy đạt ISO 22000, HACCP, GMP; có bản tự công bố sản phẩm và phiếu kiểm nghiệm Eurofins, xem tại mục <a href=\"../../#ho-so\">Hồ sơ pháp lý</a>.";
const CHUNG = "Xem cách làm chi tiết trong bài <a href=\"../../kien-thuc/cach-chung-yen-sao.html\">Cách chưng yến sào đường phèn tại nhà</a>.";

module.exports = [
  {
    id: 113, slug: "yen-rut-long-dap-to-100gr", dm: "yen-tinh-che",
    title: "Yến rút lông đắp tổ 100gr – giá 2.899.000đ | Phát Lộc Natural Food",
    desc: "Yến rút lông đắp tổ Việt Cường Nhân 100gr: nhặt lông bằng tay, giữ sợi dài, định hình lại thành tổ đẹp. Hợp làm quà biếu. Có bản tự công bố, phiếu kiểm nghiệm. Giao toàn quốc.",
    points: ["Nhặt sạch lông bằng tay, giữ nguyên sợi yến dài", "Đắp lại thành tổ tròn đẹp, hợp làm quà biếu", "Sợi chắc, khi chưng không nát, nước yến sánh", "Chỉ cần ngâm 1–2 giờ rồi chưng"],
    body: `<p>Yến rút lông đắp tổ là tổ yến được làm sạch lông bằng tay theo từng sợi, sau đó đắp lại thành tổ. Cách làm này giữ được sợi yến dài, khi chưng sợi không nát, nước yến trong và sánh.</p>
<h2>Cách dùng</h2>
<ol><li>Ngâm 1 tổ trong nước sạch 1–2 giờ cho nở mềm.</li><li>Xé nhẹ theo thớ, để ráo.</li><li>Chưng cách thủy 20–30 phút, cho đường phèn ở 5 phút cuối.</li></ol>
<p>${CHUNG}</p>
<h2>Giấy tờ</h2><p>${YEN_GIAY_TO}</p>`,
    faq: [["100gr yến rút lông đắp tổ có bao nhiêu tổ?", "Tùy kích thước tổ của từng lô; nhắn Zalo 0768 759 419 để được báo số tổ hiện có."], ["Yến rút lông khác yến tinh chế thế nào?", "Yến rút lông nhặt lông bằng tay nên giữ sợi dài; yến tinh chế có thể gãy sợi ngắn hơn và giá mềm hơn. Xem so sánh ở trang <a href=\"../../yen-tinh-che/\">Yến tinh chế</a>."], ["Bảo quản thế nào?", "Để nơi khô ráo, đậy kín hộp; mùa ẩm để ngăn mát tủ lạnh."]]
  },
  {
    id: 111, slug: "yen-tinh-che-1-lop-soi-18-20-tai-100gr", dm: "yen-tinh-che",
    title: "Yến tinh chế 1 lớp sợi 18–20 tai 100gr – 2.390.000đ | Phát Lộc",
    desc: "Yến tinh chế 1 lớp sợi 18–20 tai 100gr Việt Cường Nhân, đã nhặt sạch lông, tai nhỏ dễ chia phần. Có bản tự công bố, phiếu kiểm nghiệm. Giao toàn quốc, kiểm hàng khi nhận.",
    points: ["100gr chia 18–20 tai, mỗi tai khoảng 5gr", "Tai nhỏ vừa một lần chưng cho 1–2 người", "Đã nhặt sạch lông, chỉ cần ngâm rồi chưng", "Có trong nhiều giỏ quà Tết 2027"],
    body: `<p>Yến tinh chế 1 lớp sợi là tổ yến đã làm sạch, ép lại thành tai mỏng một lớp. Loại 18–20 tai mỗi tai khoảng 5gr, tiện chia phần: mỗi lần chưng một tai cho 1–2 người, không phải cân đo.</p>
<h2>Cách dùng</h2>
<ol><li>Ngâm 1 tai trong nước sạch 20–30 phút.</li><li>Xé tơi, để ráo.</li><li>Chưng cách thủy 15–20 phút với đường phèn, táo đỏ hoặc đông trùng.</li></ol>
<p>${CHUNG}</p>
<h2>Giấy tờ</h2><p>${YEN_GIAY_TO}</p>`,
    faq: [["Một tai yến dùng cho mấy người?", "Một tai khoảng 5gr, đủ 1–2 phần chưng."], ["Ngâm bao lâu?", "Khoảng 20–30 phút là sợi nở mềm."], ["Có loại ít tai hơn không?", "Có loại 1 lớp sợi 10 tai (tai to hơn) và 2 lớp sợi, xem trang <a href=\"../../yen-tinh-che/\">Yến tinh chế</a>."]]
  },
  {
    id: 101, slug: "yen-tho-to-ab-it-long-100gr", dm: "yen-tho",
    title: "Yến thô tổ AB ít lông 100gr – 2.150.000đ | Phát Lộc Natural Food",
    desc: "Tổ yến thô AB ít lông 100gr Việt Cường Nhân: tổ nguyên, dáng đẹp, ít lông nên nhặt nhanh, hao ít. Có bản tự công bố, phiếu kiểm nghiệm. Giao toàn quốc, kiểm hàng khi nhận.",
    points: ["Tổ nguyên, dáng đẹp, chưa qua xử lý", "Ít lông, nhặt nhanh, hao ít khi làm sạch", "Giá thấp hơn yến tinh chế cùng trọng lượng", "Hợp người muốn tự làm sạch, biết rõ tổ yến"],
    body: `<p>Tổ AB là tổ yến thô có dáng đẹp, ít lông, được chọn từ tổ khai thác trong nhà yến. Vì chưa qua làm sạch nên giữ nguyên hình dạng tự nhiên, phù hợp người muốn tự tay xử lý hoặc kiểm tra tổ yến nguyên bản.</p>
<h2>Làm sạch tại nhà</h2>
<ol><li>Ngâm tổ 1–2 giờ cho nở mềm.</li><li>Xé theo thớ, dùng nhíp nhặt lông trên đĩa nền trắng, thay nước vài lần.</li><li>Để ráo rồi chưng cách thủy.</li></ol>
<p>Không có thời gian nhặt lông thì chọn <a href="../yen-rut-long-dap-to-100gr/">yến rút lông đắp tổ</a>.</p>
<h2>Giấy tờ</h2><p>${YEN_GIAY_TO}</p>`,
    faq: [["Yến thô hao bao nhiêu khi làm sạch?", "Thường khoảng 10–20% khối lượng, tổ AB ít lông hao ít hơn."], ["Nhặt lông mất bao lâu?", "Khoảng 15–30 phút mỗi tổ tùy độ quen tay."], ["Có kiểm hàng được không?", "Có, khách được kiểm hàng khi nhận."]]
  },
  {
    id: 129, slug: "loc-6-hu-yen-vcn-nest-0-8gr", dm: "nuoc-yen",
    title: "Lốc 6 hũ nước yến VCN Nest 0.8gr – 300.000đ | Phát Lộc Natural Food",
    desc: "Lốc 6 hũ nước yến chưng sẵn VCN Nest, mỗi hũ 0.8gr tổ yến thô. Uống ngay, tiện mang theo, làm quà. Giá 300.000đ. Giao toàn quốc.",
    points: ["6 hũ, mỗi hũ dùng 0.8gr tổ yến thô", "Mở nắp là uống, ngon hơn khi để lạnh", "Tiện mang đi làm, đi học, làm quà", "Có loại kèm hộp quà"],
    body: `<p>Nước yến VCN Nest là yến chưng sẵn đóng hũ của Việt Cường Nhân. Loại 0.8gr dùng nhiều yến hơn loại 0.3gr, sợi yến nhiều hơn trong mỗi hũ, phù hợp bồi bổ hằng ngày.</p>
<h2>Bảo quản</h2><p>Để nơi khô mát, tránh nắng. Đã mở nắp dùng hết trong ngày.</p>
<h2>Lựa chọn khác</h2><p>Lốc 10 hũ tiết kiệm hơn, hoặc lốc có hộp để biếu; xem trang <a href="../../nuoc-yen/">Nước yến chưng sẵn</a>.</p>`,
    faq: [["0.8gr nghĩa là gì?", "Là lượng tổ yến thô dùng để chưng cho mỗi hũ."], ["Uống lúc nào tốt?", "Có thể uống buổi sáng hoặc trước khi ngủ; để lạnh uống ngon hơn."], ["Trẻ em uống được không?", "Trẻ từ 1 tuổi có thể dùng lượng nhỏ; nên hỏi bác sĩ nếu trẻ có tiền sử dị ứng."]]
  },
  {
    id: 136, slug: "nam-dong-trung-ha-thao-loai-cay-100gr", dm: "dong-trung-ha-thao",
    title: "Nấm đông trùng hạ thảo sấy khô loại cây 100gr – 599.000đ | Phát Lộc",
    desc: "Nấm đông trùng hạ thảo sấy khô loại cây 100gr, sợi nguyên, đều màu. Pha trà, chưng yến, nấu canh. Có bản tự công bố, phiếu kiểm nghiệm. Giao toàn quốc.",
    points: ["Sợi nấm nguyên cây, đều màu cam vàng", "Pha trà, chưng yến, nấu canh, hầm gà", "100gr dùng được lâu cho cả gia đình", "Có loại 50gr và loại gãy giá mềm"],
    body: `<p>Nấm đông trùng hạ thảo loại cây giữ sợi nấm nguyên, đẹp, hợp vừa dùng vừa làm quà. Sấy khô nên bảo quản được lâu, dùng linh hoạt trong nhiều món.</p>
<h2>Cách dùng</h2>
<ul><li><b>Pha trà:</b> 5–10 sợi với nước nóng khoảng 90°C, hãm 5 phút, châm 2–3 lần, ăn luôn sợi nấm.</li><li><b>Chưng yến:</b> thêm vài sợi khi chưng yến với đường phèn.</li><li><b>Nấu món:</b> cho vào canh, cháo, gà hầm ở 10 phút cuối.</li></ul>
<p>Chi tiết trong bài <a href="../../kien-thuc/cach-dung-dong-trung-ha-thao.html">Cách dùng đông trùng hạ thảo sấy khô</a>.</p>`,
    faq: [["Bảo quản thế nào?", "Đậy kín, nơi khô ráo hoặc ngăn mát tủ lạnh, tránh ẩm."], ["Loại cây khác loại gãy gì?", "Cùng nguồn nấm; loại cây sợi nguyên đẹp hơn, loại gãy giá mềm hơn."], ["Mua kèm quà tặng không?", "Một số sản phẩm đông trùng có tặng táo đỏ như ghi trên ảnh; nhân viên xác nhận khi gọi lại."]]
  },
  {
    id: 306, slug: "gio-qua-phu-quy-dai-cat-qtg06", dm: "qua-tet",
    title: "Giỏ quà Tết Phú Quý Đại Cát QTG06 – 3.813.000đ | Phát Lộc",
    desc: "Giỏ quà Tết 2027 Phú Quý Đại Cát QTG06: yến rút lông đắp tổ 100gr, đông trùng hạ thảo 20gr, táo đỏ hộp tròn, 4 hũ yến chưng. Quà biếu sếp, đối tác, cha mẹ.",
    points: ["Yến rút lông đắp tổ 100gr Việt Cường Nhân", "Nấm đông trùng hạ thảo 20gr", "Táo đỏ hộp tròn", "4 hũ yến chưng sẵn"],
    body: `<p>Phú Quý Đại Cát là giỏ quà Tết cao cấp với thành phần chính là 100gr yến rút lông đắp tổ, kèm đông trùng hạ thảo, táo đỏ và yến chưng sẵn. Phù hợp biếu sếp, đối tác quan trọng hoặc cha mẹ, ông bà dịp Tết Đinh Mùi 2027.</p>
<h2>Đặt số lượng cho doanh nghiệp</h2><p>Từ 20 giỏ có chiết khấu, xuất hóa đơn điện tử, giao theo danh sách. Gửi yêu cầu tại <a href="../../#doanh-nghiep">mục Quà Tết doanh nghiệp</a>.</p>
<h2>Giấy tờ</h2><p>${YEN_GIAY_TO}</p>`,
    faq: [["Đặt trước bao lâu?", "Đơn lẻ trước 3–5 ngày; đơn doanh nghiệp nhận đặt từ 22/10/2026, nên đặt sớm để chủ động lịch giao."], ["Có thiệp và in logo công ty không?", "Nhắn Zalo 0768 759 419 để được tư vấn theo số lượng."], ["Giao tận nơi người nhận được không?", "Có, giao toàn quốc, người nhận được kiểm hàng."]]
  },
  {
    id: 313, slug: "gio-qua-hoang-gia-qtg13", dm: "qua-tet",
    title: "Giỏ quà Tết Hoàng Gia QTG13 – 5.202.000đ | Phát Lộc Natural Food",
    desc: "Giỏ quà Tết 2027 Hoàng Gia QTG13: yến rút lông đắp tổ 100gr, yến tinh chế 50gr 18–20 tai, đông trùng hạ thảo 50gr, táo đỏ, 3 hũ yến chưng. Mẫu quà Tết cao cấp nhất.",
    points: ["Yến rút lông đắp tổ 100gr", "Yến tinh chế 50gr 18–20 tai", "Nấm đông trùng hạ thảo 50gr", "Táo đỏ hộp tròn và 3 hũ yến chưng"],
    body: `<p>Hoàng Gia là mẫu quà Tết cao cấp nhất của Phát Lộc, gồm 150gr yến sào (100gr rút lông đắp tổ và 50gr tinh chế) cùng 50gr đông trùng hạ thảo. Dành cho đối tác chiến lược, lãnh đạo hoặc người thân đặc biệt.</p>
<h2>Đặt số lượng cho doanh nghiệp</h2><p>Chiết khấu từ 20 giỏ, xuất hóa đơn điện tử. Gửi yêu cầu tại <a href="../../#doanh-nghiep">mục Quà Tết doanh nghiệp</a>.</p>
<h2>Giấy tờ</h2><p>${YEN_GIAY_TO}</p>`,
    faq: [["Tổng lượng yến trong giỏ là bao nhiêu?", "150gr yến khô (100gr rút lông đắp tổ, 50gr tinh chế) và 3 hũ yến chưng."], ["Đặt trước bao lâu?", "Nên đặt trước 3–5 ngày; đơn số lượng nhận đặt từ 22/10/2026, đặt sớm để giữ hàng."], ["Có xuất hóa đơn không?", "Có, xuất hóa đơn điện tử theo thông tin công ty."]]
  },
  {
    id: 338, slug: "hop-qua-yen-sao-cao-cap-qth24", dm: "qua-tet",
    title: "Hộp quà yến sào cao cấp QTH24 – yến tinh chế 100gr – 2.798.000đ | Phát Lộc",
    desc: "Hộp quà Tết yến sào cao cấp QTH24: yến tinh chế 100gr hộp bát giác, đường phèn, táo đỏ, hộp quà đỏ khay vàng kèm túi. Quà biếu Tết 2027 sang trọng.",
    points: ["Yến tinh chế 100gr trong hộp bát giác", "Kèm đường phèn và táo đỏ hộp nhỏ", "Hộp quà đỏ, khay vàng, túi xách", "Gọn, sang, dễ mang đi biếu"],
    body: `<p>QTH24 là hộp quà tập trung vào 100gr yến tinh chế, đóng hộp bát giác đặt trên khay vàng trong hộp đỏ. Mẫu quà gọn, sang, hợp biếu sếp, khách hàng lớn hoặc người lớn tuổi.</p>
<h2>Đặt số lượng</h2><p>Chiết khấu từ 20 hộp, xuất hóa đơn điện tử. Gửi yêu cầu tại <a href="../../#doanh-nghiep">mục Quà Tết doanh nghiệp</a>.</p>
<h2>Giấy tờ</h2><p>${YEN_GIAY_TO}</p>`,
    faq: [["Yến trong hộp là loại nào?", "Yến tinh chế Việt Cường Nhân 100gr."], ["Có túi xách kèm không?", "Có, hộp quà kèm túi."], ["Giao tỉnh được không?", "Có, giao toàn quốc, kiểm hàng khi nhận."]]
  },
  {
    id: 323, slug: "hop-qua-an-lac-qth06", dm: "qua-tet",
    title: "Hộp quà An Lạc QTH06 – 10 hũ yến chưng 5 vị – 524.000đ | Phát Lộc",
    desc: "Hộp quà Tết An Lạc QTH06: 10 hũ yến chưng sẵn 5 vị, muỗng vàng nhỏ, hộp giấy cứng, túi giấy. Giá 524.000đ, hợp quà cho khách hàng, nhân viên.",
    points: ["10 hũ yến chưng sẵn, 5 vị", "Kèm muỗng vàng nhỏ", "Hộp giấy cứng, túi giấy", "Hợp quà khách hàng, nhân viên"],
    body: `<p>An Lạc là hộp quà Tết dưới 600.000đ với 10 hũ yến chưng sẵn 5 vị, người nhận dùng ngay không cần chế biến. Hợp tặng khách hàng và nhân viên số lượng lớn.</p>
<h2>Đặt số lượng</h2><p>Chiết khấu từ 20 hộp, xuất hóa đơn điện tử, giao theo danh sách. Gửi yêu cầu tại <a href="../../#doanh-nghiep">mục Quà Tết doanh nghiệp</a>, hoặc xem bài <a href="../../kien-thuc/qua-tet-doanh-nghiep-theo-ngan-sach.html">Chọn quà Tết doanh nghiệp theo ngân sách</a>.</p>`,
    faq: [["5 vị gồm những vị nào?", "Nhắn Zalo 0768 759 419 để được báo các vị đang có tại thời điểm đặt."], ["Đặt 100 hộp mất bao lâu?", "Thường 3–7 ngày tùy thời điểm; nhận đặt từ 22/10/2026, nên đặt sớm trước cao điểm Tết."], ["Bảo quản thế nào?", "Để nơi khô mát, tránh nắng; ngon hơn khi để lạnh."]]
  },
  {
    id: 347, slug: "tui-qua-xuan-sac-qtt05", dm: "qua-tet",
    title: "Túi quà Tết Xuân Sắc QTT05 – mỹ phẩm T'Beauty – 608.000đ | Phát Lộc",
    desc: "Túi quà Tết cho phái đẹp Xuân Sắc QTT05: 1 hộp mặt nạ yến T'Beauty 10 miếng, sữa rửa mặt, nước tẩy trang. Có phiếu công bố mỹ phẩm. Giá 608.000đ.",
    points: ["1 hộp mặt nạ yến T'Beauty (10 miếng)", "Sữa rửa mặt T'Beauty", "Nước tẩy trang T'Beauty", "Có phiếu công bố của Cục Quản lý Dược"],
    body: `<p>Xuân Sắc là túi quà Tết dành cho mẹ, vợ, chị em hoặc nhân viên nữ: bộ làm sạch da (tẩy trang, sữa rửa mặt) và một hộp mặt nạ yến T'Beauty dùng 2–3 lần mỗi tuần.</p>
<h2>Giấy tờ</h2><p>Mỹ phẩm T'Beauty có phiếu công bố mỹ phẩm của Cục Quản lý Dược, xem tại mục <a href="../../#ho-so">Hồ sơ pháp lý</a>. Xem thêm sản phẩm lẻ ở trang <a href="../../my-pham/">Mỹ phẩm</a>.</p>`,
    faq: [["Da nhạy cảm dùng được không?", "Nên thử một lượng nhỏ trước 24 giờ; ngưng nếu đỏ, ngứa."], ["Đặt số lượng tặng nhân viên nữ được không?", "Được, chiết khấu từ 20 túi, xuất hóa đơn điện tử."], ["Có túi quà mỹ phẩm khác không?", "Có QTT09, QTT15–QTT17, xem trang <a href=\"../../qua-tet/\">Quà Tết 2027</a>."]]
  }
];
