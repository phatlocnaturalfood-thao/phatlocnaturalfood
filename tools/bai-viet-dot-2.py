# Sinh 4 bài kiến thức đợt 2 (lịch tuần 26/10 và 2/11 trong kế hoạch SEO).
# Giá và tên sản phẩm lấy từ bảng giá P trong index.html, xuất qua node ra JSON.
import json, subprocess, os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
js = r'''const fs=require("fs");const h=fs.readFileSync(process.argv[1],"utf8");
const code=h.slice(h.indexOf("const P = ["),h.indexOf("const DIR ="));const c={};
new Function("ctx",code.replace(/\bconst (P|IMG|R|AN_XA_BONG)\b/g,"var $1")+";ctx.P=P;").call(null,c);
process.stdout.write(JSON.stringify(c.P));'''
P = json.loads(subprocess.check_output(['node', '-e', js, R + 'index.html']))
BY = {p[0]: p for p in P}
SP = {113: 'yen-rut-long-dap-to-100gr', 111: 'yen-tinh-che-1-lop-soi-18-20-tai-100gr', 101: 'yen-tho-to-ab-it-long-100gr',
      129: 'loc-6-hu-yen-vcn-nest-0-8gr', 136: 'nam-dong-trung-ha-thao-loai-cay-100gr', 306: 'gio-qua-phu-quy-dai-cat-qtg06',
      313: 'gio-qua-hoang-gia-qtg13', 338: 'hop-qua-yen-sao-cao-cap-qth24', 323: 'hop-qua-an-lac-qth06', 347: 'tui-qua-xuan-sac-qtt05'}
vnd = lambda n: f"{n:,}".replace(",", ".") + "đ"
import re
def link(i):
    p = BY[i]
    if i in SP: return f'../san-pham/{SP[i]}/'
    m = re.search(r'\b(QT[GHKT]\d{2})\b', p[2])
    return '../#' + (m.group(1).lower() if m else f'sp-{i}')

src = open(R + 'kien-thuc/loi-ich-yen-sao.html', encoding='utf-8').read()
pre = src[:src.index('<meta name="description"')]
mid = src[src.index('<link rel="icon"'):src.index('<main class="article">')]
foot = src[src.index('</main>'):]

def page(slug, desc, title, crumb, h1, body, cta):
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": h1, "description": desc,
          "datePublished": "2026-10-22", "inLanguage": "vi",
          "author": {"@type": "Organization", "name": "Phát Lộc Natural Food"},
          "publisher": {"@type": "Organization", "name": "Phát Lộc Natural Food",
                        "logo": {"@type": "ImageObject", "url": "https://phatlocnaturalfood.com/logo.jpg"}},
          "mainEntityOfPage": f"https://phatlocnaturalfood.com/kien-thuc/{slug}.html"}
    h = (pre + f'<meta name="description" content="{desc}">\n<title>{title} | Phát Lộc Natural Food</title>\n'
         f'<link rel="canonical" href="https://phatlocnaturalfood.com/kien-thuc/{slug}.html">\n'
         f'<meta property="og:type" content="article">\n<meta property="og:title" content="{title}">\n'
         f'<meta property="og:description" content="{desc}">\n<meta property="og:image" content="https://phatlocnaturalfood.com/logo.jpg">\n'
         f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>\n'
         + mid + f'<main class="article">\n  <p class="crumb"><a href="./">Kiến thức</a> / {crumb}</p>\n  <p class="eyebrow">{crumb}</p>\n  <h1>{h1}</h1>\n'
         + body + f'\n  <div class="cta">\n{cta}\n    <a class="btn btn-line" href="./">Xem bài khác</a>\n  </div>\n' + foot)
    open(R + f'kien-thuc/{slug}.html', 'w', encoding='utf-8').write(h)

def li(i, note=''):
    p = BY[i]
    return f'    <li><a href="{link(i)}"><b>{p[2]}</b></a> – {vnd(p[4])}. {p[3]}.{(" " + note) if note else ""}</li>'

# 1. 10 mẫu giỏ quà Tết
top10 = [335, 323, 347, 341, 332, 314, 307, 338, 306, 313]
b1 = f'''  <p class="lede">Mười mẫu quà Tết yến sào 2027 dưới đây trải đều từ 260.000đ đến 5.202.000đ, mỗi mức giá có lựa chọn cho nhân viên, khách hàng, cha mẹ và đối tác. Tất cả dùng yến sào Việt Cường Nhân có bản tự công bố và phiếu kiểm nghiệm.</p>

  <h2>Dưới 1 triệu: quà phát đồng loạt, quà khách hàng</h2>
  <ol>
{li(335, "Yến chưng sẵn uống ngay, hộp có tay xách, hợp phát cho nhân viên.")}
{li(323, "10 hũ yến chưng vị đường phèn hoặc đông trùng, kèm muỗng vàng, hộp giấy cứng sang hơn ở mức dưới 600.000đ.")}
{li(347, "Dành cho phái đẹp: mặt nạ yến và bộ làm sạch da T'Beauty.")}
{li(341, "Yến vụn sạch tự chưng kèm đông trùng, táo đỏ, đường phèn trên khay Tết.")}
  </ol>

  <h2>Từ 1 đến 2 triệu: biếu cha mẹ, khách hàng thân thiết</h2>
  <ol start="5">
{li(332, "Yến tinh chế 25gr để tự chưng và yến hũ dùng ngay trong cùng một hộp.")}
{li(314, "Giỏ quà đủ bộ yến, đông trùng, táo, kỷ tử.")}
{li(307, "50gr yến tinh chế 18–20 tai, mỗi tai một lần chưng, dễ dùng cho người lớn tuổi.")}
  </ol>

  <h2>Trên 2 triệu: biếu sếp, đối tác quan trọng</h2>
  <ol start="8">
{li(338, "Gọn, sang, tập trung vào 100gr yến tinh chế.")}
{li(306, "100gr yến rút lông đắp tổ kèm đông trùng, táo đỏ, yến hũ.")}
{li(313, "Mẫu cao cấp nhất: 150gr yến khô và 50gr đông trùng.")}
  </ol>

  <h2>Cách chọn nhanh</h2>
  <ul>
    <li><b>Người nhận ít thời gian:</b> chọn mẫu có yến chưng sẵn.</li>
    <li><b>Người nhận quen chưng yến:</b> chọn mẫu có yến tinh chế hoặc rút lông.</li>
    <li><b>Mua số lượng cho công ty:</b> từ 20 hộp có chiết khấu và hóa đơn điện tử, xem <a href="../#doanh-nghiep">Quà Tết doanh nghiệp</a>.</li>
  </ul>
  <p>Xem đủ 59 mẫu chia theo ngân sách ở trang <a href="../qua-tet/">Quà Tết yến sào 2027</a>.</p>'''
page('mau-gio-qua-tet-yen-sao-2027',
     '10 mẫu giỏ quà, hộp quà Tết yến sào 2027 đáng chọn từ 260.000đ đến 5.202.000đ: quà cho nhân viên, khách hàng, cha mẹ, sếp và đối tác. Yến sào Việt Cường Nhân có giấy tờ đầy đủ.',
     '10 mẫu giỏ quà Tết yến sào 2027 đáng chọn', 'Quà Tết', '10 mẫu giỏ quà Tết yến sào 2027 đáng chọn', b1,
     '    <a class="btn btn-gold" href="../qua-tet/">Xem đủ 59 mẫu quà Tết</a>')

# 2. Quà Tết biếu sếp
b2 = f'''  <p class="lede">Quà Tết biếu sếp nên trang trọng nhưng không phô trương, dùng được và có nguồn gốc rõ ràng. Yến sào là lựa chọn quen thuộc vì hợp mọi lứa tuổi và dễ dùng cho cả gia đình người nhận. Dưới đây là gợi ý theo 3 mức ngân sách từ 1 đến 5 triệu.</p>

  <h2>Từ 1 đến 2 triệu</h2>
  <ul>
{li(332)}
{li(311)}
{li(307)}
  </ul>

  <h2>Từ 2 đến 3 triệu</h2>
  <ul>
{li(338, "Hộp đỏ khay vàng, gọn và sang.")}
{li(113, "Mua lẻ, đóng hộp quà theo yêu cầu.")}
  </ul>

  <h2>Từ 3 đến 5 triệu</h2>
  <ul>
{li(342)}
{li(306)}
{li(308)}
{li(313)}
  </ul>

  <h2>Lưu ý khi biếu quà Tết</h2>
  <ul>
    <li><b>Thời điểm:</b> thường từ rằm tháng Chạp đến trước 28 Tết; tránh sát giao thừa khi người nhận bận việc gia đình.</li>
    <li><b>Bao bì:</b> giữ nguyên hộp, túi; kèm thiệp viết tay ngắn gọn.</li>
    <li><b>Giấy tờ:</b> sản phẩm có bản tự công bố, phiếu kiểm nghiệm giúp người nhận yên tâm; xem <a href="../#ho-so">Hồ sơ pháp lý</a>.</li>
    <li><b>Giao hộ:</b> có thể giao thẳng đến nhà người nhận, người nhận được kiểm hàng.</li>
  </ul>
  <p>Xem thêm bài <a href="mau-gio-qua-tet-yen-sao-2027.html">10 mẫu giỏ quà Tết yến sào 2027 đáng chọn</a>.</p>'''
page('qua-tet-bieu-sep',
     'Gợi ý quà Tết biếu sếp 2027 theo ngân sách 1–2 triệu, 2–3 triệu, 3–5 triệu: giỏ quà, hộp quà yến sào, đông trùng hạ thảo, kèm lưu ý thời điểm và cách biếu.',
     'Quà Tết biếu sếp 2027: gợi ý theo ngân sách 1–5 triệu', 'Quà Tết', 'Quà Tết biếu sếp: gợi ý theo ngân sách 1–5 triệu', b2,
     '    <a class="btn btn-gold" href="../qua-tet/">Xem quà Tết theo ngân sách</a>')

# 3. Phân biệt yến tinh chế, rút lông, yến thô
b3 = f'''  <p class="lede">Cùng là tổ yến, nhưng yến thô, yến tinh chế và yến rút lông khác nhau ở cách làm sạch, độ nguyên sợi, công sức khi dùng và giá. Bảng dưới so sánh nhanh để chọn đúng loại theo nhu cầu.</p>

  <table class="cmp">
    <thead><tr><th></th><th>Yến thô</th><th>Yến tinh chế</th><th>Yến rút lông</th></tr></thead>
    <tbody>
      <tr><th>Làm sạch</th><td>Chưa nhặt lông</td><td>Đã làm sạch lông, tạp chất</td><td>Nhặt lông bằng tay từng sợi</td></tr>
      <tr><th>Sợi yến</th><td>Nguyên tổ</td><td>Có thể gãy, ép thành tai</td><td>Giữ sợi dài, đắp lại thành tổ</td></tr>
      <tr><th>Khi dùng</th><td>Ngâm, nhặt lông 15–30 phút/tổ</td><td>Ngâm 20–40 phút rồi chưng</td><td>Ngâm 1–2 giờ rồi chưng</td></tr>
      <tr><th>Giá 100gr tại Phát Lộc</th><td>{vnd(1590000)} – {vnd(2150000)}</td><td>{vnd(1680000)} – {vnd(2690000)}</td><td>{vnd(2899000)} – {vnd(4169000)}</td></tr>
      <tr><th>Hợp với</th><td>Người muốn tự xử lý, tiết kiệm</td><td>Dùng hằng ngày</td><td>Làm quà biếu, người muốn sợi đẹp</td></tr>
    </tbody>
  </table>

  <h2>Yến thô</h2>
  <p>Tổ yến còn nguyên như khi khai thác. Giá thấp nhất cùng trọng lượng nhưng hao khoảng 10–20% khi nhặt lông. Tổ AB ít lông nhặt nhanh hơn. Xem <a href="{link(101)}">Yến thô tổ AB ít lông 100gr</a>.</p>

  <h2>Yến tinh chế</h2>
  <p>Tổ yến đã được làm sạch, thường ép thành tai mỏng (1 lớp, 2 lớp) hoặc để dạng vụn. Loại 18–20 tai mỗi tai khoảng 5gr, tiện chia phần. Xem <a href="{link(111)}">Yến tinh chế 1 lớp sợi 18–20 tai</a>.</p>

  <h2>Yến rút lông</h2>
  <p>Nhặt lông bằng tay để giữ sợi dài, rồi đắp hoặc định hình lại thành tổ. Công làm nhiều nhất nên giá cao nhất, chưng lên sợi đẹp, hợp làm quà. Xem <a href="{link(113)}">Yến rút lông đắp tổ 100gr</a>.</p>

  <p>Dù chọn loại nào, hãy kiểm tra bản tự công bố và phiếu kiểm nghiệm; xem bài <a href="phan-biet-yen-sao-that-gia.html">Cách phân biệt yến sào thật – giả</a> và <a href="cach-chung-yen-sao.html">Cách chưng yến sào đường phèn tại nhà</a>.</p>'''
page('yen-tinh-che-rut-long-yen-tho-khac-nhau',
     'Yến thô, yến tinh chế và yến rút lông khác nhau thế nào về cách làm sạch, độ nguyên sợi, công sức khi dùng và giá 100gr. Bảng so sánh giúp chọn đúng loại yến.',
     'Yến tinh chế, yến rút lông, yến thô khác nhau thế nào?', 'Yến sào', 'Yến tinh chế, yến rút lông, yến thô khác nhau thế nào?', b3,
     '    <a class="btn btn-gold" href="../yen-tinh-che/">Xem yến tinh chế</a>\n    <a class="btn btn-line" href="../yen-tho/">Xem yến thô</a>')

# 4. Giá yến sào 100gr
rows = [p for p in P if p[1] in ('Tổ Yến Thô', 'Tổ Yến Đã Nhặt Sạch Lông') and p[3] == '100gr']
rows.sort(key=lambda p: p[4])
trs = '\n'.join(f'      <tr><td><a href="{link(p[0])}">{p[2]}</a></td><td>{"Yến thô" if p[1] == "Tổ Yến Thô" else "Đã làm sạch"}</td><td class="num">{vnd(p[4])}</td></tr>' for p in rows)
b4 = f'''  <p class="lede">Tại Phát Lộc, 100gr yến sào Việt Cường Nhân có giá từ {vnd(rows[0][4])} đến {vnd(rows[-1][4])} tùy loại (cập nhật 22/10/2026). Giá chênh nhau chủ yếu vì độ sạch, độ nguyên sợi và công làm.</p>

  <h2>Bảng giá yến sào 100gr</h2>
  <table class="cmp">
    <thead><tr><th>Sản phẩm</th><th>Loại</th><th class="num">Giá 100gr</th></tr></thead>
    <tbody>
{trs}
    </tbody>
  </table>

  <h2>Vì sao giá yến chênh nhau</h2>
  <ul>
    <li><b>Độ sạch:</b> yến thô rẻ hơn vì chưa nhặt lông, khi làm sạch hao một phần khối lượng.</li>
    <li><b>Độ nguyên sợi:</b> sợi dài, nguyên tổ đắt hơn vụn, sợi ngắn dù dinh dưỡng tương tự.</li>
    <li><b>Công làm:</b> rút lông bằng tay, đắp tổ tốn công nhất.</li>
    <li><b>Giá quá rẻ so với mặt bằng</b> là dấu hiệu cần cẩn trọng, xem <a href="phan-biet-yen-sao-that-gia.html">Cách phân biệt yến sào thật – giả</a>.</li>
  </ul>

  <h2>Cách đọc nhãn yến sào</h2>
  <p>Nhãn thực phẩm bao gói sẵn tại Việt Nam cần có các thông tin bắt buộc theo quy định ghi nhãn hàng hóa. Khi mua yến, kiểm tra:</p>
  <ul>
    <li><b>Tên sản phẩm và loại yến:</b> yến thô, tinh chế, rút lông.</li>
    <li><b>Khối lượng tịnh:</b> 50gr, 100gr…</li>
    <li><b>Tên, địa chỉ cơ sở sản xuất</b> và đơn vị chịu trách nhiệm sản phẩm.</li>
    <li><b>Ngày sản xuất, hạn sử dụng</b> và hướng dẫn bảo quản.</li>
    <li><b>Xuất xứ</b> và số lô nếu có.</li>
  </ul>
  <p>Ngoài nhãn, hỏi người bán bản tự công bố sản phẩm và phiếu kiểm nghiệm. Giấy tờ yến Việt Cường Nhân do Phát Lộc phân phối được đăng tại <a href="../#ho-so">Hồ sơ pháp lý</a>.</p>
  <p class="note">Giá có thể thay đổi theo lô hàng; giá mới nhất luôn hiển thị ở trang <a href="../yen-tinh-che/">Yến tinh chế</a> và <a href="../yen-tho/">Yến thô</a>.</p>'''
page('gia-yen-sao-100gr',
     f'Giá yến sào 100gr mới nhất tại Phát Lộc: từ {vnd(rows[0][4])} đến {vnd(rows[-1][4])} cho yến thô, yến tinh chế, yến rút lông Việt Cường Nhân. Vì sao giá chênh và cách đọc nhãn yến sào.',
     'Giá yến sào 100gr mới nhất và cách đọc nhãn', 'Yến sào', 'Giá yến sào 100gr mới nhất và cách đọc nhãn', b4,
     '    <a class="btn btn-gold" href="../yen-tinh-che/">Xem bảng giá yến tinh chế</a>')

# Trang danh sách bài + sitemap
ix = open(R + 'kien-thuc/index.html', encoding='utf-8').read()
cards = [
  ('mau-gio-qua-tet-yen-sao-2027', 'qua-tet', 'Quà Tết', '10 mẫu giỏ quà Tết yến sào 2027 đáng chọn', 'Mười mẫu quà từ 260.000đ đến 5.202.000đ cho nhân viên, khách hàng, cha mẹ, sếp.'),
  ('qua-tet-bieu-sep', 'qua-tet', 'Quà Tết', 'Quà Tết biếu sếp: gợi ý theo ngân sách 1–5 triệu', 'Giỏ quà, hộp quà yến sào theo 3 mức chi, kèm lưu ý thời điểm và cách biếu.'),
  ('yen-tinh-che-rut-long-yen-tho-khac-nhau', 'yen-sao', 'Yến sào', 'Yến tinh chế, yến rút lông, yến thô khác nhau thế nào?', 'Bảng so sánh cách làm sạch, độ nguyên sợi, công sức và giá 100gr.'),
  ('gia-yen-sao-100gr', 'yen-sao', 'Yến sào', 'Giá yến sào 100gr mới nhất và cách đọc nhãn', 'Bảng giá yến thô, tinh chế, rút lông 100gr và những gì cần xem trên nhãn.'),
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
urls = [f'https://phatlocnaturalfood.com/kien-thuc/{c[0]}.html' for c in cards] + \
       [f'https://phatlocnaturalfood.com/{x}/' for x in ['tao-do', 'nha-dam', 'my-pham']] + \
       [f'https://phatlocnaturalfood.com/san-pham/{s}/' for s in SP.values()]
add = ''.join(f'  <url><loc>{u}</loc><lastmod>2026-10-22</lastmod></url>\n' for u in urls if u not in sm)
sm = sm.replace('</urlset>', add + '</urlset>')
open(R + 'sitemap.xml', 'w', encoding='utf-8').write(sm)
print('ok', len(urls))
