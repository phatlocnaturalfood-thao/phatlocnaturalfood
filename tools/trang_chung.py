"""Sinh các trang con dùng chung giao diện trang chủ (bố cục giống vietcuongnhan.com, từ 30/10/2026):
/gioi-thieu/, /chung-nhan/, /doanh-nghiep/.
Lấy CSS, header, footer, nút nổi, mã đo lường từ index.html: đổi giao diện trang chủ rồi chạy lại là đồng bộ.
Chạy: python3 tools/trang_chung.py
Nội dung từng trang: tools/noi-dung/*.html (Chứng nhận, Doanh nghiệp) và hàm gioi_thieu() bên dưới.
"""
import os, re, json, html as H
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/"
SITE = "https://phatlocnaturalfood.com"
IDX = open(R + "index.html", encoding="utf-8").read()
ND = R + "tools/noi-dung/"

def cut(a, b, s=IDX, keep_b=True):
    i = s.index(a); j = s.index(b, i)
    return s[i:j + (len(b) if keep_b else 0)]

TRACK = cut("<!-- Google tag", '<meta name="viewport"', keep_b=False)
STYLE1 = cut("<style>body{margin:0}", "</style>")
FONTS = cut('<link rel="preconnect" href="https://fonts.googleapis.com">', 'display=swap">')
STYLE2 = IDX[IDX.index("<style>", IDX.index(FONTS)):]
STYLE2 = STYLE2[:STYLE2.index("</style>") + 8]
up = lambda s: re.sub(r'(href|src)="(?!https?:|#|/|tel:|mailto:|\.\./)', r'\1="../', s)
FOOTER = up(cut("<footer>", "</footer>"))
FAB = cut('<div class="fab"', "</div>")
BRAND = re.search(r'<span><b>PHÁT LỘC</b>.*?</span></span>|<span><b>PHÁT LỘC</b><small>[^<]*</small></span>', IDX).group(0)
CLICK = '''<script>document.addEventListener("click", e => { const a = e.target.closest('a[href*="zalo.me"], a[href^="tel:"]'); if (a) { try { gtag("event", a.href.includes("zalo") ? "click_zalo" : "click_call"); } catch {} try { fbq("track", "Contact"); } catch {} } });</script>'''
EXTRA_CSS = """<style>
.intro { padding-block: 44px 8px; display: grid; gap: 10px; }
.intro h1 { font-size: clamp(32px, 5.5vw, 48px); color: var(--emerald-2); }
.intro p { margin: 0; color: var(--muted); max-width: 70ch; }
.eyebrow { font-size: 12px; letter-spacing: .14em; text-transform: uppercase; color: var(--gold); font-weight: 700; margin: 0; }
.info { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px; }
.info div { background: var(--paper); border: 1px solid var(--line); border-top: 3px solid var(--emerald-2); border-radius: 12px; padding: 16px 18px; }
.info h3 { font-size: 18px; color: var(--emerald-2); margin-bottom: 8px; }
.info p, .info li { margin: 0 0 6px; color: var(--muted); font-size: 14.5px; }
.info ul { margin: 0; padding-left: 18px; }
</style>"""

def header(active):
    items = [("../gioi-thieu/", "Giới thiệu", "gt"), ("../#san-pham", "Sản phẩm", ""), ("../chung-nhan/", "Chứng nhận &amp; Cam kết", "cn"),
             ("../kien-thuc/", "Kiến thức", "kt")]
    nav = "\n".join(f'      <a href="{h}"{" aria-current=\"page\"" if k == active and k else ""}>{t}</a>' for h, t, k in items)
    return f'''<header class="top">
  <div class="wrap">
    <a class="brand" href="../" aria-label="Phát Lộc Natural Food">
      <span class="mark"><img src="../mark-trong.png" alt=""></span>
      {BRAND}
    </a>
    <nav class="menu" id="menu" aria-label="Chính" onclick="if(event.target.closest('a')){{const h=this.closest('header');h.classList.remove('open');h.querySelector('.nav-t').setAttribute('aria-expanded','false')}}">
{nav}
    </nav>
    <button type="button" class="nav-t" aria-label="Mở menu" aria-expanded="false" aria-controls="menu" onclick="const h=this.closest('header');this.setAttribute('aria-expanded',h.classList.toggle('open'))"><span></span><span></span><span></span></button>
    <a class="btn btn-line" href="../#dat-hang">Liên hệ</a>
  </div>
</header>'''

def shell(path, title, desc, active, body, ld=None, script=""):
    url = f"{SITE}/{path}"
    lds = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in (ld or []))
    return f'''<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
{TRACK}<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{H.escape(title)} | Phát Lộc Natural Food</title>
<meta name="description" content="{H.escape(desc)}">
<link rel="canonical" href="{url}">
<link rel="icon" href="../mark.jpg">
<meta property="og:type" content="website">
<meta property="og:title" content="{H.escape(title)}">
<meta property="og:description" content="{H.escape(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/logo.jpg">
{lds}{STYLE1}
{FONTS}
{STYLE2}
{EXTRA_CSS}
</head>
<body>
{header(active)}

{body}

{FOOTER}

{FAB}
{CLICK}
{script}
</body>
</html>
'''

LB_DOCS = '''<dialog class="lb" id="lb" aria-label="Giấy tờ">
  <img id="lb-img" alt="">
  <div class="bar"><button type="button" id="lb-prev">Trước</button><span id="lb-n"></span><button type="button" id="lb-next">Sau</button><button type="button" id="lb-x">Đóng</button></div>
</dialog>
<script>
''' + open(ND + "docs.js", encoding="utf-8").read().replace("`ho-so/", "`../ho-so/").replace('["ho-so/', '["../ho-so/') + '''
const lb = document.getElementById("lb"), lbImg = document.getElementById("lb-img"), prev = document.getElementById("lb-prev"), next = document.getElementById("lb-next");
let gal = [], gi = 0;
function lbShow() { lbImg.src = gal[gi][0]; lbImg.alt = gal[gi][1]; document.getElementById("lb-n").textContent = gal.length > 1 ? `${gal[gi][1]}` : gal[gi][1]; prev.hidden = next.hidden = gal.length < 2; }
document.addEventListener("click", e => { const d = e.target.closest("[data-doc]"); if (d && DOCS[d.dataset.doc]) { gal = DOCS[d.dataset.doc]; gi = 0; lbShow(); lb.showModal(); } });
prev.onclick = () => { gi = (gi + gal.length - 1) % gal.length; lbShow(); };
next.onclick = () => { gi = (gi + 1) % gal.length; lbShow(); };
document.getElementById("lb-x").onclick = () => lb.close();
lb.addEventListener("click", e => { if (e.target === lb) lb.close(); });
</script>'''

def write(path, html):
    os.makedirs(R + path, exist_ok=True)
    open(R + path + "index.html", "w", encoding="utf-8").write(html)
    print("Đã tạo", path)

def chung_nhan():
    c = open(ND + "chung-nhan.html", encoding="utf-8").read()
    c += '''
<section class="block" style="padding-top:0">
  <div class="wrap" style="display:flex;flex-wrap:wrap;gap:10px">
    <a class="btn btn-gold" href="../#san-pham">Xem bảng giá sản phẩm</a>
    <a class="btn btn-line" href="../gioi-thieu/">Giới thiệu Phát Lộc</a>
    <a class="btn btn-line" href="https://zalo.me/0768759419" target="_blank" rel="noopener">Nhắn Zalo 0768 759 419</a>
  </div>
</section>'''
    ld = [{"@context": "https://schema.org", "@type": "WebPage", "name": "Chứng nhận & Cam kết – Phát Lộc Natural Food", "url": f"{SITE}/chung-nhan/",
           "about": {"@type": "Organization", "name": "Công ty TNHH Sản xuất Phát Lộc Natural Food", "url": SITE}}]
    write("chung-nhan/", shell("chung-nhan/", "Chứng nhận & Cam kết",
        "Phát Lộc phân phối yến sào Việt Cường Nhân theo giấy ủy quyền; nhà máy đạt ISO 22000:2018, HACCP, GMP; bản tự công bố, phiếu kiểm nghiệm Eurofins. Xem bản scan giấy tờ.",
        "cn", c, ld, script=LB_DOCS))

def doanh_nghiep():
    c = open(ND + "doanh-nghiep.html", encoding="utf-8").read()
    gift = open(ND + "qua-tet-trang-chu.html", encoding="utf-8").read()
    # Khối giới thiệu quà Tết: nút lọc mẫu trên trang chủ đổi thành liên kết trang Quà Tết
    gift = re.sub(r'<button class="btn btn-line" type="button" data-showcat="Quà Tết">([^<]*)</button>', r'<a class="btn btn-line" href="../qua-tet/">\1</a>', gift)
    gift = re.sub(r'<a class="btn btn-gold" href="[^"]*doanh-nghiep[^"]*">([^<]*)</a>', r'<a class="btn btn-gold" href="#bao-gia">\1</a>', gift)
    gift = re.sub(r'<div class="box">.*?</div>\n  </div>\n</section>', '</div>\n</section>', gift, flags=re.S) if False else gift
    gift = re.sub(r'<div class="price" id="feat-price" data-id="338"><b>([^<]*)</b></div>\s*<button class="btn btn-gold" type="button" data-pick="338">([^<]*)</button>',
                  r'<div class="price"><b>\1</b></div>\n      <a class="btn btn-gold" href="../san-pham/hop-qua-yen-sao-cao-cap-qth24/">Xem hộp quà này</a>', gift)
    c = c.replace('<form class="f" id="b2b-form"', '<form class="f" id="b2b-form" style="scroll-margin-top:90px"', 1).replace('id="doanh-nghiep"', 'id="bao-gia"', 1)
    js = open(ND + "doanh-nghiep.js", encoding="utf-8").read()
    endpoint = re.search(r'const ORDER_ENDPOINT = "[^"]*";', IDX).group(0)
    body = gift.replace('id="qua-tet"', 'id="qua-tet-2027"') + "\n" + c
    ld = [{"@context": "https://schema.org", "@type": "WebPage", "name": "Quà Tết doanh nghiệp 2027 – Phát Lộc Natural Food", "url": f"{SITE}/doanh-nghiep/"}]
    write("doanh-nghiep/", shell("doanh-nghiep/", "Quà Tết doanh nghiệp 2027: báo giá theo số lượng",
        "Đặt quà Tết yến sào số lượng cho công ty: 59 mẫu giỏ, hộp, khay quà; chiết khấu từ 20 hộp, hóa đơn điện tử, giao theo danh sách. Gửi yêu cầu báo giá trong ngày.",
        "", body, ld, script=f"<script>\n{endpoint}\n{js}</script>"))

def gioi_thieu():
    body = '''<section class="block">
  <div class="wrap">
    <div class="intro" style="padding-top:0">
      <p class="eyebrow">Về chúng tôi</p>
      <h1>Giới thiệu Phát Lộc Natural Food</h1>
      <p>Phát Lộc Natural Food là cửa hàng yến sào, đông trùng hạ thảo và quà biếu tại 511/9 Bùi Thị Xuân, Phường Tân Đông Hiệp, TP. Hồ Chí Minh. Chúng tôi phân phối yến sào thương hiệu Việt Cường Nhân theo giấy ủy quyền, cùng nấm đông trùng hạ thảo, táo đỏ, nha đam, nước yến chưng sẵn và mỹ phẩm từ yến.</p>
    </div>
    <div class="info" style="margin-top:22px">
      <div><h3>Thông tin doanh nghiệp</h3><ul>
        <li><b>CÔNG TY TNHH SẢN XUẤT PHÁT LỘC NATURAL FOOD</b></li>
        <li>Mã số doanh nghiệp: 3703421984, cấp ngày 26/12/2025 tại Phòng Đăng ký kinh doanh, Sở Tài chính TP. Hồ Chí Minh</li>
        <li>Địa chỉ: 511/9 Bùi Thị Xuân, Phường Tân Đông Hiệp, TP. Hồ Chí Minh</li>
        <li>Người đại diện: Bà Phạm Thị Thu Thảo, Giám đốc</li>
      </ul></div>
      <div><h3>Liên hệ</h3><ul>
        <li>Hotline, Zalo: <a href="https://zalo.me/0768759419" target="_blank" rel="noopener">0768 759 419</a></li>
        <li>Email: phatlocnaturalfood@gmail.com</li>
        <li>Giờ mở cửa: 7:30–21:00 tất cả các ngày</li>
        <li>Fanpage: <a href="https://www.facebook.com/1415830271609330" target="_blank" rel="noopener">Phát Lộc Natural Food</a></li>
      </ul></div>
      <div><h3>Nguồn hàng</h3><ul>
        <li>Phân phối yến sào Việt Cường Nhân theo giấy ủy quyền của Công ty TNHH TM-DV Việt Cường Nhân</li>
        <li>Nhà máy đạt ISO 22000:2018, HACCP, GMP</li>
        <li>Có bản tự công bố, phiếu kiểm nghiệm Eurofins. <a href="../chung-nhan/#ho-so">Xem giấy tờ</a></li>
      </ul></div>
    </div>
    <div class="info" style="margin-top:16px">
      <div><h3>Sản phẩm</h3><p>Tổ yến thô, yến tinh chế, yến rút lông, nước yến chưng sẵn, nấm đông trùng hạ thảo, táo đỏ Tân Cương, thạch nha đam, mỹ phẩm T'Beauty và hơn 50 mẫu quà Tết. <a href="../#san-pham">Xem bảng giá</a></p></div>
      <div><h3>Mua hàng</h3><p>Giao toàn quốc: TP.HCM 1–2 ngày, tỉnh 2–5 ngày. Được kiểm hàng trước khi thanh toán, thanh toán COD hoặc chuyển khoản, có hóa đơn điện tử. <a href="../chinh-sach/doi-tra.html">Chính sách đổi trả</a></p></div>
      <div><h3>Quà Tết doanh nghiệp</h3><p>Nhận đặt quà Tết số lượng cho công ty, chiết khấu từ 20 hộp, giao theo danh sách. <a href="../doanh-nghiep/">Gửi yêu cầu báo giá</a></p></div>
    </div>
    <p style="margin:22px 0 0;font-size:13px;color:var(--muted)">Thực phẩm này không phải là thuốc và không có tác dụng thay thế thuốc chữa bệnh.</p>
    <div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:18px">
      <a class="btn btn-gold" href="../#san-pham">Xem sản phẩm</a>
      <a class="btn btn-line" href="../chung-nhan/">Chứng nhận &amp; Cam kết</a>
    </div>
  </div>
</section>'''
    ld = [{"@context": "https://schema.org", "@type": "AboutPage", "name": "Giới thiệu Phát Lộc Natural Food", "url": f"{SITE}/gioi-thieu/"}]
    write("gioi-thieu/", shell("gioi-thieu/", "Giới thiệu Phát Lộc Natural Food",
        "Phát Lộc Natural Food: cửa hàng yến sào, đông trùng hạ thảo, quà biếu tại Tân Đông Hiệp, TP.HCM. Phân phối yến sào Việt Cường Nhân theo ủy quyền, giao toàn quốc.",
        "gt", body, ld))

if __name__ == "__main__":
    gioi_thieu(); chung_nhan(); doanh_nghiep()
