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

## 2026-06-22 — Fix store.html + corporate.html issues (claude-code)
- store.html: theme btns now 16px circles w/ direct bg color (removed broken ::after w/ no positioned parent); product card = <h3> name once + muted .product-cat label + price; img array trimmed to 4 confirmed-fashion files (dropped headphones img_1583394838336 + CCCP dups), front/back use distinct imgs.
- corporate.html: section pad 6rem→8-9rem + border-top dividers; hero split flex sizing (h1 left flex:1, subtitle col flex:0 0 300px bottom-right); solution slide bgs swapped fashion→corporate boardroom imgs (opacity .35); slide-content fade-in on .active (wired in updateNav); counters threshold .5→.25 + reduced-motion fallback.
- IMG REALITY: only ONE distinct corporate photo exists (boardroom+skyline, aliased as 4 filenames img_1742585665885/665960/667037 + img_1779700210487 are identical pixels). NO portrait/people photos. Team 8 cards = office-img backdrop + branded overlay + monogram initials (no headshots avail). img_1761315413964=burger, _1758957701419=coffee, _1778731525495=living room — all removed from team.
- Verified: 0 emoji (grep), all 8 referenced imgs exist on disk, shimmer CSS intact both files, 8 team cards/0 leftover <img>. Not opened in browser.
- Left: hero-right sits near right edge (~1096px not exactly x896); team uses monograms not real headshots (none in repo); map is SVG Europe (no landmark raster needed).
