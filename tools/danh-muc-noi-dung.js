// Nội dung chữ cho từng trang danh mục. Sản phẩm và giá lấy tự động từ index.html.
const B = (lo, hi) => p => p[4] >= lo && p[4] < hi;
const L = (slug, text) => `<a href="../kien-thuc/${slug}.html">${text}</a>`;

module.exports = [
  {
    slug: "qua-tet",
    menu: "Quà Tết 2027",
    crumb: "Quà Tết 2027",
    eyebrow: "Tết Đinh Mùi 2027",
    cats: ["Quà Tết"],
    sort: true,
    title: "Quà Tết yến sào 2027 – 59 mẫu giỏ, hộp quà theo ngân sách | Phát Lộc",
    h1: "Quà Tết yến sào 2027",
    desc: "59 mẫu giỏ quà, hộp quà, túi quà Tết yến sào 2027 từ 260.000đ đến 5.202.000đ. Yến sào Việt Cường Nhân, đông trùng hạ thảo, táo đỏ. Nhận đặt số lượng cho doanh nghiệp, xuất hóa đơn điện tử.",
    groups: [
      ["Dưới 500.000đ", B(0, 500000)],
      ["Từ 500.000đ đến 1 triệu", B(500000, 1000000)],
      ["Từ 1 đến 2 triệu", B(1000000, 2000000)],
      ["Trên 2 triệu", B(2000000, Infinity)]
    ],
    lede: `<p>Phát Lộc có 59 mẫu quà Tết 2027 chia theo 4 mức ngân sách, từ hộp xách 6 hũ yến chưng 260.000đ đến giỏ quà Hoàng Gia 5.202.000đ. Thành phần chính là yến sào Việt Cường Nhân (nhà máy đạt ISO 22000, HACCP, GMP), kèm đông trùng hạ thảo, táo đỏ Tân Cương, kỷ tử, đường phèn hoặc nước hồng sâm.</p>
<p>Mỗi mẫu có mã riêng (QTG giỏ quà, QTH hộp quà, QTK khay quà, QTT túi quà). Bấm <b>Liên hệ</b> ở mẫu anh/chị thích để nhắn Zalo 0768 759 419, Phát Lộc tư vấn theo người nhận.</p>`,
    guide: `      <h2>Chọn quà Tết yến sào theo người nhận</h2>
      <ul>
        <li><b>Nhân viên, phát đồng loạt:</b> hộp xách hoặc túi quà dưới 500.000đ, có yến chưng sẵn dùng ngay.</li>
        <li><b>Khách hàng thân thiết:</b> hộp quà 500.000đ – 1 triệu có yến vụn sạch, đông trùng, táo đỏ để tự chưng.</li>
        <li><b>Cha mẹ, người lớn tuổi:</b> giỏ quà 1 – 2 triệu với yến tinh chế 25–50gr và đông trùng hạ thảo.</li>
        <li><b>Sếp, đối tác quan trọng:</b> giỏ hoặc khay trên 2 triệu có yến rút lông đắp tổ 100gr.</li>
        <li><b>Phái đẹp:</b> túi quà mỹ phẩm yến T'Beauty (QTT05, QTT09, QTT15–QTT17).</li>
      </ul>
      <h2>Đặt quà Tết số lượng cho doanh nghiệp</h2>
      <p><b>Nhận đặt quà Tết doanh nghiệp từ 22/10/2026.</b> Từ 20 hộp có chiết khấu theo số lượng, xuất hóa đơn điện tử và giao tận nơi theo danh sách. Gửi yêu cầu tại <a href="../#doanh-nghiep">mục Quà Tết doanh nghiệp</a>, Phát Lộc báo giá trong ngày. Xem thêm bài ${L("qua-tet-doanh-nghiep-theo-ngan-sach", "Chọn quà Tết doanh nghiệp 2027 theo ngân sách")}.</p>`,
    faq: [
      ["Đặt quà Tết 2027 trước bao lâu?", "Đơn lẻ nên đặt trước 3–5 ngày. Phát Lộc nhận đặt quà Tết doanh nghiệp từ 22/10/2026; đơn số lượng nên đặt càng sớm càng chủ động mẫu và lịch giao trước Tết."],
      ["Có xuất hóa đơn điện tử không?", "Có. Phát Lộc xuất hóa đơn điện tử cho đơn quà Tết doanh nghiệp theo thông tin công ty cung cấp."],
      ["Đặt nhiều hộp có được giảm giá không?", "Có chiết khấu từ 20 hộp, tăng theo mốc 50 và 100 hộp. Gửi số lượng và ngân sách để nhận báo giá trong ngày."],
      ["Có giao quà tận nơi cho từng người nhận không?", "Có. Giao toàn quốc; với đơn doanh nghiệp có thể giao theo danh sách địa chỉ người nhận. Khách được kiểm hàng khi nhận."],
      ["Yến sào trong giỏ quà có giấy tờ không?", "Có. Yến sào Việt Cường Nhân có bản tự công bố, phiếu kiểm nghiệm Eurofins và chứng nhận ISO 22000, HACCP, GMP, đăng công khai ở mục <a href=\"../#ho-so\">Hồ sơ pháp lý</a>."]
    ]
  },
  {
    slug: "yen-tinh-che",
    menu: "Yến tinh chế",
    crumb: "Yến tinh chế",
    eyebrow: "Tổ yến đã nhặt sạch lông",
    cats: ["Tổ Yến Đã Nhặt Sạch Lông"],
    title: "Yến tinh chế, yến rút lông 100gr – giá mới nhất | Phát Lộc Natural Food",
    h1: "Yến tinh chế và yến rút lông",
    desc: "Yến tinh chế, yến rút lông đắp tổ, định hình, chân tua sạch 100gr Việt Cường Nhân. Đã nhặt sạch lông, chỉ cần ngâm và chưng. Có bản tự công bố, phiếu kiểm nghiệm. Giao toàn quốc.",
    groups: [
      ["Yến rút lông", p => /Rút Lông|Đắp Miếng|Vuông Miếng/.test(p[2])],
      ["Yến tinh chế", p => /Tinh Chế/.test(p[2])],
      ["Chân tua và viên baby", p => /Chân Tua|Viên Baby/.test(p[2])]
    ],
    lede: `<p>Yến tinh chế là tổ yến đã được làm sạch lông và tạp chất, về nhà chỉ cần ngâm rồi chưng. Phát Lộc phân phối yến sào Việt Cường Nhân từ 1.680.000đ đến 4.169.000đ cho 100gr, chia theo độ nguyên sợi: vụn, sợi ngắn, 1 lớp, 2 lớp, rút lông đắp tổ và rút lông khô.</p>
<p>Sợi càng dài, càng nguyên tổ thì giá càng cao và khi chưng giữ sợi đẹp hơn. Yến vụn và chân tua có dinh dưỡng tương tự, hợp để dùng hằng ngày hoặc nấu cho trẻ nhỏ.</p>`,
    guide: `      <h2>Yến tinh chế khác yến rút lông thế nào</h2>
      <ul>
        <li><b>Yến tinh chế:</b> làm sạch bằng nước, sợi có thể gãy ngắn; giá mềm hơn, hợp dùng thường xuyên.</li>
        <li><b>Yến rút lông:</b> nhặt lông bằng tay giữ nguyên sợi, định hình lại thành tổ; sợi dài, đẹp, hợp làm quà biếu.</li>
        <li><b>Chân tua:</b> phần chân tổ bám vào vách, sợi dày và dai, nở nhiều khi ngâm.</li>
      </ul>
      <h2>100gr yến dùng được bao lâu</h2>
      <p>Mỗi tai yến tinh chế khoảng 5–10gr tùy loại. Người lớn thường dùng khoảng 3–5gr yến khô mỗi lần, 2–3 lần mỗi tuần, nên 100gr dùng được khoảng 1–2 tháng cho một người. Xem cách làm trong bài ${L("cach-chung-yen-sao", "Cách chưng yến sào đường phèn tại nhà")} và ${L("phan-biet-yen-sao-that-gia", "Cách phân biệt yến sào thật – giả")}.</p>`,
    faq: [
      ["Yến tinh chế có cần nhặt lông nữa không?", "Không. Yến đã được làm sạch lông và tạp chất, chỉ cần ngâm nước sạch cho nở mềm rồi chưng cách thủy."],
      ["Ngâm yến tinh chế bao lâu?", "Khoảng 20–40 phút với yến vụn, sợi ngắn; 1–2 giờ với yến rút lông nguyên tổ và chân tua. Sợi nở mềm, tơi ra là được."],
      ["Bảo quản yến tinh chế thế nào?", "Để nơi khô ráo, thoáng mát, đậy kín hộp; mùa ẩm nên để ngăn mát tủ lạnh. Yến đã ngâm nở nên chưng ngay, không để lâu."],
      ["Có làm hộp quà yến tinh chế không?", "Có. Yến tinh chế 25gr, 50gr, 100gr có sẵn trong các mẫu <a href=\"../qua-tet/\">quà Tết 2027</a>, hoặc nhắn Zalo để đóng hộp theo yêu cầu."]
    ]
  },
  {
    slug: "yen-tho",
    menu: "Yến thô",
    crumb: "Yến thô",
    eyebrow: "Tổ yến thô nguyên tổ",
    cats: ["Tổ Yến Thô"],
    title: "Yến thô nguyên tổ 100gr – tổ AB ít lông, giá mềm | Phát Lộc Natural Food",
    h1: "Tổ yến thô nguyên tổ",
    desc: "Tổ yến thô Việt Cường Nhân 100gr: tổ AB ít lông, nguyên tổ giá mềm, bể nứt nhẹ, chân rìa. Giá từ 1.590.000đ. Có bản tự công bố, phiếu kiểm nghiệm. Giao toàn quốc, kiểm hàng khi nhận.",
    lede: `<p>Tổ yến thô là tổ yến còn nguyên như khi khai thác, chưa nhặt lông. Giá tốt hơn yến tinh chế cùng trọng lượng, phù hợp người có thời gian tự làm sạch hoặc muốn biết rõ tổ yến nguyên bản. Phát Lộc có 5 loại yến thô Việt Cường Nhân 100gr, từ 1.590.000đ đến 2.150.000đ.</p>
<p>Tổ AB ít lông giữ dáng đẹp, ít lông nên nhặt nhanh. Loại bể nứt nhẹ và chân rìa giá mềm hơn, dinh dưỡng tương tự.</p>`,
    guide: `      <h2>Làm sạch yến thô tại nhà</h2>
      <ol>
        <li>Ngâm tổ yến trong nước sạch 1–2 giờ cho nở mềm.</li>
        <li>Xé nhỏ theo thớ, dùng nhíp nhặt lông trên đĩa nền trắng, thay nước vài lần.</li>
        <li>Để ráo rồi chưng cách thủy, xem chi tiết trong bài ${L("cach-chung-yen-sao", "Cách chưng yến sào đường phèn tại nhà")}.</li>
      </ol>
      <p>Không có thời gian nhặt lông thì chọn <a href="../yen-tinh-che/">yến tinh chế</a> đã làm sạch sẵn.</p>`,
    faq: [
      ["Yến thô và yến tinh chế loại nào lợi hơn?", "Yến thô giá thấp hơn nhưng hao khoảng 10–20% khối lượng khi làm sạch và mất thời gian nhặt lông. Yến tinh chế đắt hơn nhưng dùng ngay."],
      ["Tổ AB ít lông là gì?", "Là tổ yến nguyên, dáng đẹp, lượng lông ít, nên nhặt nhanh và hao ít hơn so với tổ nhiều lông."],
      ["Mua yến thô có kiểm hàng được không?", "Có. Khách được kiểm hàng khi nhận; nên quay video lúc mở hàng để làm căn cứ đổi trả."]
    ]
  },
  {
    slug: "nuoc-yen",
    menu: "Nước yến",
    crumb: "Nước yến chưng sẵn",
    eyebrow: "Yến hũ chưng tiệt trùng",
    cats: ["Yến Hũ Chưng Tiệt Trùng"],
    title: "Nước yến chưng sẵn – hũ lẻ, lốc 6, lốc 10 hũ VCN Nest | Phát Lộc",
    h1: "Nước yến chưng sẵn",
    desc: "Nước yến chưng sẵn VCN Nest và yến chưng thủ công yến tươi: hũ lẻ từ 35.000đ, lốc 6 hũ, lốc 10 hũ có hộp. Uống ngay, tiện làm quà. Giao toàn quốc.",
    lede: `<p>Nước yến chưng sẵn là cách dùng yến tiện nhất: mở nắp là uống, không phải ngâm hay chưng. Phát Lộc có nước yến VCN Nest (0.3gr và 0.8gr tổ yến thô mỗi hũ) và yến chưng thủ công từ yến tươi (12gr và 36gr), giá từ 35.000đ một hũ.</p>
<p>Lốc 6 hũ và lốc 10 hũ có loại kèm hộp quà, hợp để biếu hoặc phát cho nhân viên dịp Tết.</p>`,
    guide: `      <h2>Chọn nước yến theo nhu cầu</h2>
      <ul>
        <li><b>Uống hằng ngày:</b> hũ 0.3gr giá mềm, mua lốc 10 hũ tiết kiệm hơn.</li>
        <li><b>Bồi bổ, người lớn tuổi:</b> hũ 0.8gr hoặc yến chưng thủ công 36gr yến tươi.</li>
        <li><b>Làm quà:</b> lốc 6 hoặc 10 hũ có hộp, hoặc các mẫu <a href="../qua-tet/">quà Tết</a> kèm yến chưng.</li>
      </ul>
      <p>Hàm lượng yến ghi trên nhãn là lượng tổ yến dùng cho mỗi hũ. Muốn tự chưng đậm hơn, xem <a href="../yen-tinh-che/">yến tinh chế</a> và bài ${L("cach-chung-yen-sao", "Cách chưng yến sào đường phèn tại nhà")}.</p>`,
    faq: [
      ["Nước yến chưng sẵn bảo quản thế nào?", "Để nơi khô mát, tránh nắng; ngon hơn khi uống lạnh. Đã mở nắp thì dùng hết trong ngày."],
      ["Trẻ em uống nước yến được không?", "Trẻ từ 1 tuổi có thể dùng lượng nhỏ, nên hỏi ý kiến bác sĩ nếu trẻ có tiền sử dị ứng. Thực phẩm này không phải là thuốc."],
      ["Lốc có hộp khác lốc thường thế nào?", "Cùng hũ yến bên trong, lốc có hộp có thêm hộp giấy in đẹp để làm quà biếu."]
    ]
  },
  {
    slug: "dong-trung-ha-thao",
    menu: "Đông trùng hạ thảo",
    crumb: "Đông trùng hạ thảo",
    eyebrow: "Nấm đông trùng hạ thảo",
    cats: ["Nấm Đông Trùng Hạ Thảo"],
    title: "Nấm đông trùng hạ thảo sấy khô – loại cây, loại gãy | Phát Lộc Natural Food",
    h1: "Nấm đông trùng hạ thảo",
    desc: "Nấm đông trùng hạ thảo sấy khô loại cây, loại gãy 50gr, 100gr và đông trùng tươi hũ. Giá từ 99.000đ. Có bản tự công bố, phiếu kiểm nghiệm. Giao toàn quốc.",
    lede: `<p>Phát Lộc có nấm đông trùng hạ thảo sấy khô loại cây (50gr, 100gr), loại gãy 100gr, hũ 10gr, 20gr và đông trùng tươi, giá từ 99.000đ. Loại cây sợi nguyên, đẹp, hợp làm quà; loại gãy cùng chất lượng nhưng giá mềm hơn, hợp dùng hằng ngày.</p>
<p>Đông trùng thường được pha trà, ngâm mật ong, nấu canh, hầm gà hoặc chưng cùng yến sào.</p>`,
    guide: `      <h2>Cách dùng đông trùng hạ thảo sấy khô</h2>
      <ul>
        <li><b>Pha trà:</b> 5–10 sợi với nước nóng 90°C, hãm 5 phút, châm được 2–3 lần, ăn luôn sợi nấm.</li>
        <li><b>Chưng với yến:</b> cho vài sợi vào chưng cùng yến và đường phèn.</li>
        <li><b>Nấu món:</b> cho vào canh, cháo, gà hầm ở 10 phút cuối.</li>
      </ul>
      <p>Chi tiết trong bài ${L("cach-dung-dong-trung-ha-thao", "Cách dùng đông trùng hạ thảo sấy khô")}.</p>`,
    faq: [
      ["Đông trùng loại cây và loại gãy khác gì?", "Cùng nguồn nấm, loại cây giữ sợi nguyên dài, đẹp; loại gãy sợi ngắn hơn nên giá mềm, phù hợp pha trà, nấu món hằng ngày."],
      ["Bảo quản đông trùng sấy khô thế nào?", "Đậy kín, để nơi khô ráo hoặc ngăn mát tủ lạnh, tránh ẩm để nấm không mềm và mất màu."],
      ["Có làm quà biếu đông trùng không?", "Có. Đông trùng 10gr–50gr có trong nhiều mẫu <a href=\"../qua-tet/\">quà Tết 2027</a> kèm yến sào và táo đỏ."]
    ]
  },
  {
    slug: "tao-do",
    menu: "Táo đỏ",
    crumb: "Táo đỏ Tân Cương",
    eyebrow: "Táo đỏ sấy khô",
    cats: ["Táo Đỏ Tân Cương"],
    title: "Táo đỏ Tân Cương sấy khô – size trung, đại, thượng hạng | Phát Lộc",
    h1: "Táo đỏ Tân Cương sấy khô",
    desc: "Táo đỏ Tân Cương sấy khô size trung, đại, thượng hạng túi 1kg và hộp 350gr, táo đỏ Nhược Khương. Giá từ 45.000đ. Dùng chưng yến, nấu chè, pha trà. Giao toàn quốc.",
    lede: `<p>Táo đỏ Tân Cương quả to, thịt dày, ngọt tự nhiên, là nguyên liệu quen thuộc khi chưng yến, nấu chè, hầm gà hay pha trà. Phát Lộc có 3 size theo số quả mỗi kg (trung 100–120 quả, đại 80–100 quả, thượng hạng 70–80 quả), đóng túi 1kg hoặc hộp 350gr, giá từ 45.000đ.</p>
<p>Táo Nhược Khương quả nhỏ hơn, vị ngọt đậm, giá mềm, hợp dùng hằng ngày.</p>`,
    guide: `      <h2>Chọn size táo đỏ</h2>
      <ul>
        <li><b>Thượng hạng (70–80 quả/kg):</b> quả to đều, đẹp, hợp làm quà và ăn trực tiếp.</li>
        <li><b>Size đại (80–100 quả/kg):</b> cân bằng giữa giá và độ to, dùng nấu chè, hầm.</li>
        <li><b>Size trung (100–120 quả/kg):</b> giá tốt, hợp chưng yến, pha trà hằng ngày.</li>
      </ul>
      <p>Chưng yến với 2–3 quả táo đỏ bổ đôi, bỏ hạt cho vị ngọt thanh; xem bài ${L("cach-chung-yen-sao", "Cách chưng yến sào đường phèn tại nhà")}.</p>`,
    faq: [
      ["Bảo quản táo đỏ sấy khô thế nào?", "Đậy kín, để nơi khô thoáng; mùa nồm nên để ngăn mát tủ lạnh để táo không bị ẩm, mốc."],
      ["Táo đỏ hộp 350gr và túi 1kg khác gì?", "Cùng loại táo; hộp 350gr tiện dùng thử hoặc làm quà, túi 1kg tiết kiệm hơn cho gia đình dùng thường xuyên."],
      ["Mua táo đỏ kèm yến có quà tặng không?", "Một số sản phẩm yến sào có tặng kèm táo đỏ như ghi trên ảnh sản phẩm; nhân viên xác nhận quà tặng khi gọi xác nhận đơn."]
    ]
  },
  {
    slug: "nha-dam",
    menu: "Nha đam",
    crumb: "Thạch nha đam",
    eyebrow: "Nha đam Tây Nguyên",
    cats: ["Thạch Nha Đam"],
    title: "Thạch nha đam Tây Nguyên có đường, không đường – túi, hũ 1kg | Phát Lộc",
    h1: "Thạch nha đam Tây Nguyên",
    desc: "Thạch nha đam Tây Nguyên đã sơ chế, có đường và không đường, túi 1kg 59.000đ, hũ 1kg 69.000đ. Giòn, không đắng, dùng làm chè, sữa chua, nước giải khát.",
    lede: `<p>Thạch nha đam Tây Nguyên đã gọt vỏ, cắt hạt lựu và xử lý hết nhớt đắng, mở ra là dùng. Có loại có đường và không đường, đóng túi 1kg (59.000đ) hoặc hũ 1kg (69.000đ).</p>
<p>Loại không đường hợp người hạn chế đường hoặc muốn tự nêm; loại có đường dùng ngay cho chè, sữa chua, trà trái cây.</p>`,
    guide: `      <h2>Gợi ý dùng thạch nha đam</h2>
      <ul>
        <li><b>Sữa chua nha đam:</b> trộn 2–3 muỗng thạch với một hũ sữa chua, để lạnh.</li>
        <li><b>Chè, trà trái cây:</b> thêm thạch nha đam vào cuối để giữ độ giòn.</li>
        <li><b>Nước nha đam hạt chia:</b> thạch nha đam, hạt chia, đường phèn, đá.</li>
      </ul>
      <p>Muốn tự sơ chế lá nha đam tươi, xem bài ${L("so-che-nha-dam", "Sơ chế nha đam không đắng, không nhớt")}.</p>`,
    faq: [
      ["Thạch nha đam để được bao lâu?", "Chưa mở để ngăn mát tủ lạnh theo hạn ghi trên bao bì; đã mở nên đậy kín, dùng trong vài ngày."],
      ["Nên chọn túi hay hũ?", "Cùng thạch bên trong; hũ tiện đậy lại sau khi mở, túi giá tốt hơn cho quán hoặc gia đình dùng nhiều."],
      ["Có giao nha đam đi tỉnh không?", "Có, giao toàn quốc; khách được kiểm hàng khi nhận."]
    ]
  },
  {
    slug: "my-pham",
    menu: "Mỹ phẩm",
    crumb: "Mỹ phẩm",
    eyebrow: "Chăm sóc da và tóc",
    cats: ["Mỹ Phẩm"],
    title: "Mỹ phẩm T'Beauty, mặt nạ yến, dầu gội nhân sâm Hàn Quốc | Phát Lộc",
    h1: "Mỹ phẩm chăm sóc da và tóc",
    desc: "Nước tẩy trang, sữa rửa mặt, toner, serum, kem dưỡng, kem chống nắng, mặt nạ T'Beauty và dầu gội, kem ủ nhân sâm Hàn Quốc. Có phiếu công bố mỹ phẩm của Cục Quản lý Dược.",
    lede: `<p>Phát Lộc có 14 sản phẩm chăm sóc da và tóc, từ 126.000đ đến 550.000đ: bộ chăm sóc da T'Beauty (tẩy trang, sữa rửa mặt, toner, serum, kem dưỡng, gel tẩy da chết, kem chống nắng, mặt nạ) và dòng chăm sóc tóc nhân sâm Hàn Quốc.</p>
<p>Các sản phẩm có phiếu công bố mỹ phẩm của Cục Quản lý Dược, đăng công khai ở mục <a href="../#ho-so">Hồ sơ pháp lý</a>.</p>`,
    guide: `      <h2>Thứ tự chăm sóc da cơ bản</h2>
      <ol>
        <li>Tẩy trang, rồi rửa mặt bằng sữa rửa mặt.</li>
        <li>Toner cân bằng da.</li>
        <li>Serum, sau đó kem dưỡng ẩm.</li>
        <li>Ban ngày: kem chống nắng là bước cuối.</li>
        <li>2–3 lần mỗi tuần: tẩy da chết và đắp mặt nạ.</li>
      </ol>
      <p>Muốn làm quà, xem các túi quà mỹ phẩm trong trang <a href="../qua-tet/">Quà Tết 2027</a> (QTT05, QTT09, QTT15–QTT17).</p>`,
    faq: [
      ["Mỹ phẩm có giấy công bố không?", "Có. Các sản phẩm có phiếu công bố mỹ phẩm của Cục Quản lý Dược và chứng nhận xuất xứ, xem tại mục <a href=\"../#ho-so\">Hồ sơ pháp lý</a>."],
      ["Da nhạy cảm dùng được không?", "Nên thử trước một lượng nhỏ ở vùng da sau tai hoặc cổ tay trong 24 giờ; ngưng dùng nếu thấy đỏ, ngứa."],
      ["Có túi quà mỹ phẩm không?", "Có, các túi quà Tết mỹ phẩm từ 440.000đ đến 1.388.000đ trong trang <a href=\"../qua-tet/\">Quà Tết 2027</a>."]
    ]
  }
];
