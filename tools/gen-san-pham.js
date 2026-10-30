// Sinh 10 trang sản phẩm chủ lực /san-pham/<slug>/ từ bảng giá trong index.html.
// Chạy: node tools/gen-san-pham.js (chạy sau gen-danh-muc.js nếu đổi giá).
const fs = require("fs");
const path = require("path");
const ROOT = path.join(__dirname, "..");
const SITE = "https://phatlocnaturalfood.com/";

const html = fs.readFileSync(path.join(ROOT, "index.html"), "utf8");
const code = html.slice(html.indexOf("const P = ["), html.indexOf("const DIR ="));
const ctx = {};
new Function("ctx", code.replace(/\bconst (P|IMG|R|AN_XA_BONG)\b/g, "var $1") + "; ctx.P = P; ctx.IMG = IMG;")(ctx);
const { P, IMG } = ctx;
const HET_HANG = ((html.match(/const HET_HANG = \[([^\]]*)\]/) || [])[1] || "").split(",").filter(Boolean).map(Number);

const IMG_V = "?v=21";
const web = f => f.replace(/\.jpg$/, ".webp");
const full = f => "images/san-pham/" + web(f) + (/^(catalog|that|khung|tet)\//.test(f) ? IMG_V : "");
const fullJpg = f => "images/san-pham/" + f;
const thumb = f => "images/san-pham/nho/" + web(f) + (/^(catalog|that|khung|tet)\//.test(f) ? IMG_V : "");
const vnd = n => n.toLocaleString("vi-VN").replace(/,/g, ".") + "đ";
const esc = s => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/"/g, "&quot;");
const QT = /\b(QT[GHKT]\d{2})\b/;
const orderHash = p => { const m = p[2].match(QT); return "#" + (m ? m[1].toLowerCase() : "sp-" + p[0]); };

const SP = require("./san-pham-noi-dung.js");
const DM = Object.fromEntries(require("./danh-muc-noi-dung.js").map(d => [d.slug, d]));
const tpl = fs.readFileSync(path.join(ROOT, "kien-thuc/phan-biet-yen-sao-that-gia.html"), "utf8");
const headTop = tpl.slice(0, tpl.indexOf('<meta name="description"'));
const footer = tpl.slice(tpl.indexOf("<footer>")).replace(/\.\.\/chinh-sach\//g, "../../chinh-sach/");

for (const s of SP) {
  const p = P.find(x => x[0] === s.id);
  const dm = DM[s.dm];
  const url = SITE + "san-pham/" + s.slug + "/";
  const imgs = (IMG[p[0]] || []).slice(0, 6);
  const name = p[1] === "Quà Tết" ? p[2] : `${p[2]} ${p[3]}`;
  const ld = [
    { "@context": "https://schema.org", "@type": "Product", name, description: s.desc, sku: String(p[0]),
      image: imgs.map(f => SITE + fullJpg(f)),
      brand: /Mỹ Phẩm/.test(p[1]) || /T'Beauty/.test(p[3]) ? { "@type": "Brand", name: "T'Beauty" } : { "@type": "Brand", name: "Việt Cường Nhân" },
      offers: { "@type": "Offer", price: p[4], priceCurrency: "VND", availability: HET_HANG.includes(p[0]) ? "https://schema.org/OutOfStock" : "https://schema.org/InStock", url,
        seller: { "@type": "Organization", name: "Phát Lộc Natural Food" } } },
    { "@context": "https://schema.org", "@type": "BreadcrumbList", itemListElement: [
      { "@type": "ListItem", position: 1, name: "Trang chủ", item: SITE },
      { "@type": "ListItem", position: 2, name: dm.crumb, item: SITE + dm.slug + "/" },
      { "@type": "ListItem", position: 3, name, item: url }] },
    { "@context": "https://schema.org", "@type": "FAQPage", mainEntity: s.faq.map(([q, a]) => ({
      "@type": "Question", name: q, acceptedAnswer: { "@type": "Answer", text: a.replace(/<[^>]+>/g, "") } })) }
  ];
  const related = P.filter(x => dm.cats.includes(x[1]) && x[0] !== p[0]).sort((a, b) => Math.abs(a[4] - p[4]) - Math.abs(b[4] - p[4])).slice(0, 4);
  const out = headTop + `<meta name="description" content="${esc(s.desc)}">
<title>${esc(s.title)}</title>
<link rel="canonical" href="${url}">
<meta property="og:type" content="product">
<meta property="og:title" content="${esc(s.title)}">
<meta property="og:description" content="${esc(s.desc)}">
<meta property="og:image" content="${imgs[0] ? SITE + fullJpg(imgs[0]) : SITE + "logo.jpg"}">
<meta property="og:url" content="${url}">
${ld.map(o => `<script type="application/ld+json">${JSON.stringify(o)}</script>`).join("\n")}
<link rel="icon" href="../../mark.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap">
<link rel="stylesheet" href="../../kien-thuc/kt.css">
<link rel="stylesheet" href="../../danh-muc.css">
</head>
<body>

<header class="top">
  <div class="wrap">
    <a class="brand" href="../../" aria-label="Phát Lộc Natural Food">
      <span class="mark"><img src="../../mark-trong.png" alt=""></span>
      <span><b>PHÁT LỘC</b><small>Natural Food · Tinh hoa tạo vị</small></span>
    </a>
    <nav class="menu" aria-label="Chính">
      <a href="../../qua-tet/">Quà Tết 2027</a>
      <a href="../../yen-tinh-che/">Yến tinh chế</a>
      <a href="../../yen-tho/">Yến thô</a>
      <a href="../../nuoc-yen/">Nước yến</a>
      <a href="../../dong-trung-ha-thao/">Đông trùng hạ thảo</a>
      <a href="../../kien-thuc/">Kiến thức</a>
    </nav>
    <a class="btn btn-line" href="../../#dat-hang">Đặt hàng</a>
  </div>
</header>

<main class="dm sp">
  <div class="wrap">
    <p class="crumb"><a href="../../">Trang chủ</a> / <a href="../../${dm.slug}/">${esc(dm.crumb)}</a> / ${esc(p[2])}</p>
    <div class="sp-top">
      <div class="gallery">
        ${imgs[0] ? `<img id="main-img" src="../../${full(imgs[0])}" alt="${esc(name)}" width="900" height="900">` : ""}
        ${imgs.length > 1 ? `<div class="thumbs">${imgs.map((f, i) => `<button type="button" data-src="../../${full(f)}" aria-label="Ảnh ${i + 1}"${i ? "" : ' aria-pressed="true"'}><img src="../../${thumb(f)}" alt="" loading="lazy" width="96" height="96"></button>`).join("")}</div>` : ""}
      </div>
      <div class="info">
        <p class="eyebrow">${esc(dm.crumb)}</p>
        <h1>${esc(p[2])}</h1>
        <p class="spec">${esc(p[3])}</p>
        <p class="price"><b>${vnd(p[4])}</b>${p[5] ? ` <s>${vnd(p[5])}</s>` : ""}</p>
        <ul class="points">
${s.points.map(x => `          <li>${esc(x)}</li>`).join("\n")}
        </ul>
        <div class="buy">
          <a class="btn btn-gold" href="https://zalo.me/0768759419" target="_blank" rel="noopener">Liên hệ</a>
          <a class="btn btn-line" href="https://zalo.me/0768759419" target="_blank" rel="noopener" onclick="if(window.gtag)gtag('event','click_zalo');if(window.fbq)fbq('track','Contact')">Hỏi qua Zalo</a>
        </div>
        <p class="ship">Giao toàn quốc · Kiểm hàng khi nhận · Hotline <a href="tel:0768759419" onclick="if(window.gtag)gtag('event','click_call')">0768 759 419</a></p>
      </div>
    </div>
    <section class="guide">
${s.body}
    </section>
    <section class="faq">
      <h2>Câu hỏi thường gặp</h2>
${s.faq.map(([q, a]) => `      <details><summary>${esc(q)}</summary><p>${a}</p></details>`).join("\n")}
    </section>
    <h2>Sản phẩm cùng nhóm</h2>
    <div class="grid">
${related.map(r => { const f = (IMG[r[0]] || [])[0]; const own = SP.find(x => x.id === r[0]);
  return `      <article class="card">
        ${f ? `<img src="../../${thumb(f)}" alt="${esc(r[2] + " " + r[3])}" loading="lazy" width="480" height="480">` : ""}
        <div class="body">
          <h3>${esc(r[2])}</h3>
          <p class="spec">${esc(r[3])}</p>
          <p class="price"><b>${vnd(r[4])}</b></p>
          <a class="btn btn-line" href="${own ? "../" + own.slug + "/" : "https://zalo.me/0768759419"}"${own ? "" : ' target="_blank" rel="noopener"'}>${own ? "Xem chi tiết" : "Liên hệ"}</a>
        </div>
      </article>`; }).join("\n")}
    </div>
    <p class="also"><a href="../../${dm.slug}/">Xem tất cả ${esc(dm.crumb.toLowerCase())}</a></p>
  </div>
</main>
<script>
document.querySelectorAll(".thumbs button").forEach(b => b.onclick = () => {
  document.getElementById("main-img").src = b.dataset.src;
  document.querySelectorAll(".thumbs button").forEach(x => x.removeAttribute("aria-pressed"));
  b.setAttribute("aria-pressed", "true");
});
</script>

` + footer;
  fs.mkdirSync(path.join(ROOT, "san-pham", s.slug), { recursive: true });
  fs.writeFileSync(path.join(ROOT, "san-pham", s.slug, "index.html"), out);
}
console.log(SP.length, "trang sản phẩm");
