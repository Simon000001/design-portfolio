
## 2026-06-26 — Full portfolio redesign to terminal/e-ink aesthetic
- Redesigned index.html from minimal Inter-based white to IBM Plex Mono monospace terminal theme
- Based on Figma design (v1): e-ink diffused with dot-matrix texture, grayscale #ffffff/#dcdcdc/#1e1e1e, color-coded pill tags
- Terminal boot hero with typewriter animation (whoami/pwd/cat about.md sequence)
- 7 new content sections: Engineering projects, Research, Art/Photography, Videos, Education/Experience, Side Quests, Footer (socails)
- Preserved: 11 design clones with viewer overlay, Design Style Survey, Inspiration tool link
- All showcase/*.html files untouched — loaded via iframe

## 2026-06-25 — Add 5 diverse design showcase pages (multi-agent orchestration)
- Research agents found 10 award-winning sites across 5 new aesthetic categories
- Built 5 clones via parallel delegate_task build agents:
  - **madrepunk.html**: Brutalist/anti-design — dark navy #040014, asymmetric grid, Bebas Neue + Inter
  - **obys.html**: Swiss/international — white #fafafa, blue #0082f3 + red #ea384c, Inter
  - **redcollar.html**: Glassmorphism/frosted UI — deep purple #0c041f, backdrop-filter blur panels
  - **fitosauna.html**: Dark earthy tech — espresso #27221A, gold #D2942D, layered parallax
  - **dobre.html**: Editorial minimal studio — off-white #F7F8EC, sage gray #CDCEC4
- Visual audit agent verified batch 1: 0 console errors, 0 emoji, all images working, screenshots taken
- Playwright screenshots captured for all 5 thumbnails
- index.html updated: "Eleven website design projects", 5 new entries in designs[]
- Pushed to GitHub: https://simon000001.github.io/design-portfolio/

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

## 2026-06-22 — corporate.html EN + offices redesign, business.html polish (claude-code)
- corporate.html: full ES→EN (nav/hero/about/solutions/stats/team/CTA/footer). Functional EN/ES toggle via data-es attrs + setLang(); EN default. Hero/about headings rebuilt+re-revealed on toggle. Removed fake SVG Europe map → 3-card "Our Presence" grid (London/Madrid/Frankfurt): photo header (single skyline img_1779700210487 at 18/50/82% bg-position for variety) + gradient + city name + address/phone rows w/ SVG pin+phone icons, white cards, hover lift+shadow.
- business.html: scroll-progress bar (#scrollProgress, gradient, rAF width), nav.scrolled shadow on scroll, hero img parallax (translateY*0.12+scale1.05, reduced-motion guarded), feature-card hover translateY+scale(1.02), trusted logos staggered logoIn keyframe (backwards fill keeps hover), nav-cta/cta-btn hover lift+shadow, ::selection #D1E3FF. Smooth scroll already present (hardened href==='#' guard).
- IMG REALITY unchanged: no real city skylines in repo; offices reuse the one boardroom+skyline shot at 3 crops (honest best-available).
- Verified: node --check both inline scripts OK; 0 emoji (grep); all 4 corp imgs exist; section tags balanced (6/6, 9/9); no Spanish in visible text (only in data-es attrs); DOM ids resolve. NOT browser-rendered (headless chrome launch gated by approval).
- Left: ES toggle covers curated strings (slide h2 names/dropdown same both langs, intentionally untranslated); office phones are plausible placeholders; live browser console-error check not run.

## 2026-06-22 — index.html: real site previews + nav arrow polish (claude-code)
- Replaced cringe browser-chrome mockups w/ per-site CSS preview illustrations via buildPreview(id): Fauna(navy+nav pills+"Capable,safe,fun."+blue btn), Monolith(cream+dark sidebar+001+2 rects), Outfit(white+3 theme circles+Bag(0)+3 squares), Escape Coffee(cream+serif headline+Origin/Type/Process cards), Crav(beige+red CRAV+angled card+★), Tresmares(white+"Impulso para crecer"+red dot+PRIVATE EQUITY swatch). Removed .thumb-inner/.mock-* CSS + lighten() (dead).
- All 6 card descs rewritten design-focused; dropped "Awwwards SOTD".
- viewer-nav: 48→56px, bg .08→.15, border .25, font 24px, box-shadow, prev/next 16→24px from edge, Unicode →/← swapped for SVG chevrons. Mobile override 46px+20px svg.
- Verified: grep clean (0 thumb-inner/mock-/lighten/&#8592). NOT browser-rendered.
- Left: none.

## 2026-06-22 — index.html: real screenshots + cleaner nav arrows (claude-code)
- Cards now use <img src="showcase/images/thumb-{id}.jpg"> (object-fit:cover, fills thumb; accent bg = fallback). Removed buildPreview()/cafeCard() + dead .preview CSS. (no lighten() existed this rev).
- viewer-nav: 56→48px, bg .08→.12, border .25→.2, box-shadow removed entirely, hover .3→.22; SVG stroke-width 2.2→2.5. Mobile 46px override untouched.
- Verified: grep clean (0 buildPreview/cafeCard/lighten/.preview/mock-); all 6 thumb-*.jpg exist on disk. NOT browser-rendered.
- Left: none.
