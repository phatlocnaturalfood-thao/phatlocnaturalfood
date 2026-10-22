# Hàm dùng chung cho các script sinh bài kiến thức: bảng giá P, link sản phẩm, khung trang bài.
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

def page(slug, desc, title, crumb, h1, body, cta, faq=None):
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": h1, "description": desc,
          "datePublished": "2026-10-22", "inLanguage": "vi",
          "author": {"@type": "Organization", "name": "Phát Lộc Natural Food"},
          "publisher": {"@type": "Organization", "name": "Phát Lộc Natural Food",
                        "logo": {"@type": "ImageObject", "url": "https://phatlocnaturalfood.com/logo.jpg"}},
          "mainEntityOfPage": f"https://phatlocnaturalfood.com/kien-thuc/{slug}.html"}
    lds = [ld]
    if faq:
        lds.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r'<[^>]+>', '', a)}} for q, a in faq]})
        body += '\n  <h2>Câu hỏi thường gặp</h2>\n' + '\n'.join(f'  <h3>{q}</h3>\n  <p>{a}</p>' for q, a in faq)
    h = (pre + f'<meta name="description" content="{desc}">\n<title>{title} | Phát Lộc Natural Food</title>\n'
         f'<link rel="canonical" href="https://phatlocnaturalfood.com/kien-thuc/{slug}.html">\n'
         f'<meta property="og:type" content="article">\n<meta property="og:title" content="{title}">\n'
         f'<meta property="og:description" content="{desc}">\n<meta property="og:image" content="https://phatlocnaturalfood.com/logo.jpg">\n'
         ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in lds)
         + mid + f'<main class="article">\n  <p class="crumb"><a href="./">Kiến thức</a> / {crumb}</p>\n  <p class="eyebrow">{crumb}</p>\n  <h1>{h1}</h1>\n'
         + body + f'\n  <div class="cta">\n{cta}\n    <a class="btn btn-line" href="./">Xem bài khác</a>\n  </div>\n' + foot)
    open(R + f'kien-thuc/{slug}.html', 'w', encoding='utf-8').write(h)

def li(i, note=''):
    p = BY[i]
    return f'    <li><a href="{link(i)}"><b>{p[2]}</b></a> – {vnd(p[4])}. {p[3]}.{(" " + note) if note else ""}</li>'

