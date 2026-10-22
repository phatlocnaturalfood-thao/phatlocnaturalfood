# Đăng 1 bài kiến thức từ file JSON: python3 tools/dang-bai.py bai.json
# JSON: {"slug","title","desc","crumb","h1","body","cta","faq":[[hỏi, đáp],...],"the_loai":"qua-tet"|"yen-sao","mo_ta_the":"..."}
# - Tạo kien-thuc/<slug>.html (khung, GA4, Pixel, Article + FAQPage)
# - Thêm thẻ bài vào đầu kien-thuc/index.html, thêm URL vào sitemap.xml
# - Đánh dấu bài trong tools/lich-bai.json (theo tieu_de_lich) là da_dang
import json, os, sys, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bai_chung import page, R

b = json.load(open(sys.argv[1], encoding='utf-8'))
slug = b['slug']
assert slug and all(c.isalnum() or c == '-' for c in slug), 'slug chỉ gồm chữ thường không dấu, số, gạch nối'
if os.path.exists(R + f'kien-thuc/{slug}.html'):
    sys.exit(f'Đã có bài {slug}.html – chọn slug khác')
page(slug, b['desc'], b['title'], b['crumb'], b['h1'], b['body'], b['cta'], faq=[tuple(x) for x in b.get('faq', [])])

ix_p = R + 'kien-thuc/index.html'
ix = open(ix_p, encoding='utf-8').read()
card = f'''    <a class="post" href="{slug}.html" data-cat="{b.get('the_loai', 'yen-sao')}">
      <span class="eyebrow">{b['crumb']}</span>
      <h2>{b['h1']}</h2>
      <p>{b.get('mo_ta_the', b['desc'][:140])}</p>
      <span class="more">Đọc bài</span>
    </a>
'''
ix = ix.replace('  <div class="posts" id="posts">\n', '  <div class="posts" id="posts">\n' + card, 1)
open(ix_p, 'w', encoding='utf-8').write(ix)

today = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=7)
sm_p = R + 'sitemap.xml'
sm = open(sm_p, encoding='utf-8').read()
u = f'https://phatlocnaturalfood.com/kien-thuc/{slug}.html'
if u not in sm:
    sm = sm.replace('</urlset>', f'  <url><loc>{u}</loc><lastmod>{today:%Y-%m-%d}</lastmod></url>\n</urlset>')
open(sm_p, 'w', encoding='utf-8').write(sm)

lich_p = R + 'tools/lich-bai.json'
lich = json.load(open(lich_p, encoding='utf-8'))
for r in lich:
    if r['tieu_de'] == b.get('tieu_de_lich'):
        r.update(trang_thai='da_dang', slug=slug, ngay_dang=f'{today:%Y-%m-%d %H:%M}')
        break
else:
    lich.append({"tieu_de": b['h1'], "tu_khoa": b.get('tu_khoa', ''), "link_ve": "", "trang_thai": "da_dang", "slug": slug, "ngay_dang": f'{today:%Y-%m-%d %H:%M}'})
json.dump(lich, open(lich_p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('Đã đăng', u)
