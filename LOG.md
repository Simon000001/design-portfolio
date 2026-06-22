# LOG

## 2026-06-22 — Rebuild showcase/ecommerce.html (MØNA)
- Full rewrite to Awwwards-quality. Single self-contained HTML, all CSS/JS inline.
- Fonts: Fraunces (display, italic accents) + Jost (body). Only external resource.
- Palette: #fafafa/#f5f5f5/#f05a4d/#1a1a1a, airy editorial.
- Fixed flaws: removed ALL emoji (was 👟/📷). Products + UI icons now inline 2px SVG.
- 8 products rendered from JS data, each a distinct designed SVG silhouette placeholder (tote/shirt/cap/mug/tee/wallet/scarf/carafe). Color swatches w/ active state, hover quick-add bumps cart count + toast, wishlist heart toggle.
- Sections: nav(search panel+cart+mobile menu), hero(layered art), product grid, collections band, values(SVG icons), scroll-revealed newsletter(inline email validation + success state), footer.
- IntersectionObserver reveals. Form preventDefault. No href="#" (anchors/buttons). og/twitter meta + inline SVG favicon. Responsive 375–1440.
- Verified: 0 emoji, 0 href="#", balanced tags, only fonts CDN external.
