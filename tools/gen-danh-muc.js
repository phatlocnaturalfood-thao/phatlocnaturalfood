// Sinh các trang danh mục SEO (/qua-tet/, /yen-tinh-che/, ...) từ bảng giá P và ảnh IMG trong index.html.
// Chạy lại mỗi khi đổi giá hoặc thêm sản phẩm: node tools/gen-danh-muc.js
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
const thumb = f => "images/san-pham/nho/" + f.replace(/\.jpg$/, ".webp") + (/^(catalog|that|khung|tet)\//.test(f) ? IMG_V : "");
const jpg = f => "images/san-pham/" + f;
const vnd = n => n ? n.toLocaleString("vi-VN").replace(/,/g, ".") + "đ" : "Liên hệ";
const esc = s => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/"/g, "&quot;");
const QT = /\b(QT[GHKT]\d{2})\b/;
const orderLink = p => { const m = p[2].match(QT); return "../#" + (m ? m[1].toLowerCase() : "sp-" + p[0]); };

const tpl = fs.readFileSync(path.join(ROOT, "kien-thuc/phan-biet-yen-sao-that-gia.html"), "utf8");
const headTop = tpl.slice(0, tpl.indexOf('<meta name="description"'));
const footer = tpl.slice(tpl.indexOf("<footer>"));

const PAGES = require("./danh-muc-noi-dung.js");
const SP = Object.fromEntries(require("./san-pham-noi-dung.js").map(x => [x.id, x.slug]));

function card(p) {
  const img = IMG[p[0]] ? IMG[p[0]][0] : null;
  return `      <article class="card">
        ${img ? `<img src="../${thumb(img)}" alt="${esc(p[2] + " " + p[3])}" loading="lazy" width="480" height="480">` : ""}
        <div class="body">
          <h3>${SP[p[0]] ? `<a href="../san-pham/${SP[p[0]]}/">${esc(p[2])}</a>` : esc(p[2])}</h3>
          <p class="spec">${esc(p[3])}</p>
          <p class="price"><b>${vnd(p[4])}</b>${p[5] ? ` <s>${vnd(p[5])}</s>` : ""}</p>
          ${HET_HANG.includes(p[0]) ? `<span class="btn btn-line" aria-disabled="true" style="opacity:.55">Hết hàng</span>` : `<a class="btn btn-line" href="https://zalo.me/0768759419" target="_blank" rel="noopener">Liên hệ</a>`}
        </div>
      </article>`;
}

function build(pg) {
  const url = SITE + pg.slug + "/";
  const items = P.filter(p => pg.cats.includes(p[1]));
  if (pg.sort) items.sort((a, b) => a[4] - b[4]);
  const groups = pg.groups ? pg.groups.map(([name, f]) => [name, items.filter(f)]).filter(g => g[1].length) : [[null, items]];
  const prices = items.map(p => p[4]).filter(Boolean);
  const ld = [
    { "@context": "https://schema.org", "@type": "BreadcrumbList", itemListElement: [
      { "@type": "ListItem", position: 1, name: "Trang chủ", item: SITE },
      { "@type": "ListItem", position: 2, name: pg.crumb, item: url }] },
    { "@context": "https://schema.org", "@type": "CollectionPage", name: pg.h1, description: pg.desc, url,
      mainEntity: { "@type": "ItemList", numberOfItems: items.length, itemListElement: items.map((p, i) => ({
        "@type": "ListItem", position: i + 1, item: {
          "@type": "Product", name: p[2] + " " + p[3], image: IMG[p[0]] ? SITE + jpg(IMG[p[0]][0]) : undefined,
          brand: /Yến|Đông Trùng|Quà Tết/.test(p[1]) ? { "@type": "Brand", name: "Việt Cường Nhân" } : undefined,
          offers: { "@type": "Offer", price: p[4], priceCurrency: "VND", availability: HET_HANG.includes(p[0]) ? "https://schema.org/OutOfStock" : "https://schema.org/InStock", url: SITE + orderLink(p).slice(3) } } })) } },
    { "@context": "https://schema.org", "@type": "FAQPage", mainEntity: pg.faq.map(([q, a]) => ({
      "@type": "Question", name: q, acceptedAnswer: { "@type": "Answer", text: a.replace(/<[^>]+>/g, "") } })) }
  ];
  const og = items[0] && IMG[items[0][0]] ? SITE + jpg(IMG[items[0][0]][0]) : SITE + "logo.jpg";
  const out = headTop + `<meta name="description" content="${esc(pg.desc)}">
<title>${esc(pg.title)}</title>
<link rel="canonical" href="${url}">
<meta property="og:type" content="website">
<meta property="og:title" content="${esc(pg.title)}">
<meta property="og:description" content="${esc(pg.desc)}">
<meta property="og:image" content="${og}">
<meta property="og:url" content="${url}">
${ld.map(o => `<script type="application/ld+json">${JSON.stringify(o)}</script>`).join("\n")}
<link rel="icon" href="../mark.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap">
<link rel="stylesheet" href="../kien-thuc/kt.css">
<link rel="stylesheet" href="../danh-muc.css">
</head>
<body>

<header class="top">
  <div class="wrap">
    <a class="brand" href="../" aria-label="Phát Lộc Natural Food">
      <span class="mark"><img src="../mark-trong.png" alt=""></span>
      <span><b>PHÁT LỘC</b><small>Natural Food · Tinh hoa tạo vị</small></span>
    </a>
    <nav class="menu" aria-label="Chính">
${PAGES.slice(0, 5).map(x => `      <a href="../${x.slug}/"${x.slug === pg.slug ? ' aria-current="page"' : ""}>${x.menu}</a>`).join("\n")}
      <a href="../kien-thuc/">Kiến thức</a>
    </nav>
    <a class="btn btn-line" href="../#dat-hang">Đặt hàng</a>
  </div>
</header>

<main class="dm">
  <div class="wrap">
    <p class="crumb"><a href="../">Trang chủ</a> / ${esc(pg.crumb)}</p>
    <p class="eyebrow">${esc(pg.eyebrow)}</p>
    <h1>${esc(pg.h1)}</h1>
    <div class="lede">${pg.lede}</div>
    <p class="facts"><span>${items.length} sản phẩm</span><span>Từ ${vnd(Math.min(...prices))} đến ${vnd(Math.max(...prices))}</span><span>Giao toàn quốc, kiểm hàng khi nhận</span></p>
${groups.map(([name, list]) => `${name ? `    <h2 class="grp">${esc(name)} <small>${list.length} mẫu</small></h2>\n` : ""}    <div class="grid">
${list.map(card).join("\n")}
    </div>`).join("\n")}
    <section class="guide">
${pg.guide}
    </section>
    <section class="faq">
      <h2>Câu hỏi thường gặp</h2>
${pg.faq.map(([q, a]) => `      <details><summary>${esc(q)}</summary><p>${a}</p></details>`).join("\n")}
    </section>
    <div class="cta">
      <a class="btn btn-gold" href="https://zalo.me/0768759419" target="_blank" rel="noopener" onclick="if(window.gtag)gtag('event','click_zalo');if(window.fbq)fbq('track','Contact')">Nhắn Zalo 0768 759 419</a>
      <a class="btn btn-line" href="tel:0768759419" onclick="if(window.gtag)gtag('event','click_call');if(window.fbq)fbq('track','Contact')">Gọi 0768 759 419</a>
      <a class="btn btn-line" href="../chung-nhan/#ho-so">Xem hồ sơ pháp lý</a>
    </div>
    <p class="also">Xem thêm: ${PAGES.filter(x => x.slug !== pg.slug).map(x => `<a href="../${x.slug}/">${x.menu}</a>`).join(" · ")}</p>
  </div>
</main>

` + footer.replace(/\.\.\/chinh-sach\//g, "../chinh-sach/");
  fs.mkdirSync(path.join(ROOT, pg.slug), { recursive: true });
  fs.writeFileSync(path.join(ROOT, pg.slug, "index.html"), out);
  return [pg.slug, items.length];
}

console.log(PAGES.map(build));
