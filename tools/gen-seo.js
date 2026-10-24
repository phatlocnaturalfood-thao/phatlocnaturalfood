// Sinh JSON-LD danh sách sản phẩm từ mảng P/IMG trong index.html, chèn giữa 2 dấu mốc.
const fs = require('fs'); const f = process.argv[2];
let html = fs.readFileSync(f, 'utf8');
const a = html.indexOf('const P = ['), b = html.indexOf('const lb = document');
const code = html.slice(a, b) + '\n;({P, IMG, full, HET_HANG});';
const {P, IMG, full, HET_HANG} = eval(code);
const BASE = 'https://phatlocnaturalfood.com/';
const items = P.filter(p => p[4]).map((p, i) => ({
  "@type": "ListItem", position: i + 1,
  item: {
    "@type": "Product",
    name: `${p[2]} ${p[3]}`.trim(),
    category: p[1],
    ...(IMG[p[0]] ? { image: BASE + encodeURI(full(IMG[p[0]][0])) } : {}),
    url: BASE + '#sp-' + p[0],
    offers: { "@type": "Offer", price: p[4], priceCurrency: "VND", availability: (typeof HET_HANG !== "undefined" && HET_HANG.includes(p[0])) ? "https://schema.org/OutOfStock" : "https://schema.org/InStock", url: BASE + '#sp-' + p[0],
      seller: { "@type": "Organization", name: "Phát Lộc Natural Food" } }
  }
}));
const ld = { "@context": "https://schema.org", "@type": "ItemList", name: "Bảng giá sản phẩm Phát Lộc Natural Food", numberOfItems: items.length, itemListElement: items };
const block = `<!-- SEO-SAN-PHAM: tự sinh từ mảng P, chạy lại gen.js khi đổi giá -->\n<script type="application/ld+json">\n${JSON.stringify(ld)}\n</script>\n<!-- /SEO-SAN-PHAM -->`;
const re = /<!-- SEO-SAN-PHAM[\s\S]*?<!-- \/SEO-SAN-PHAM -->/;
html = re.test(html) ? html.replace(re, block) : html.replace('</body>', block + '\n</body>');
fs.writeFileSync(f, html); console.log('products', items.length, 'bytes', block.length);
