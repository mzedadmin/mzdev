# MZed Dev Site - Project Reference

## Overview

Marketing/landing site for MZed, an online education platform for filmmakers and photographers. Built with Jekyll + Siteleaf CMS. All content must stay Siteleaf-editable (frontmatter-driven with defaults).

- **URL (local):** `http://localhost:4000/mzdev/`
- **URL (production):** `https://mzedadmin.github.io/mzdev`
- **Base URL:** `/mzdev`
- **Serve command:** `bundle exec jekyll serve`
- **Build command:** `bundle exec jekyll build`

## Architecture

### Collections
| Collection | Count | Output | Path |
|---|---|---|---|
| `_courses` | 66 files (.md) | Yes | `/courses/:name/` |
| `_educators` | 32 files (.md) | Yes | `/educators/:name/` |
| `_sessions` | 4 files (.md) | Yes | `/sessions/:name/` |
| `_posts` | 175 files (.md) | Yes | `/posts/:title/` |
| `_testimonials` | 3 files (.md) | No | N/A |
| `_trusted_by` | 12 files (.md) | No | N/A |
| `_settings` | Pricing/globals | No | N/A |
| `_uploads` | Media files | No | N/A |

### Layouts
- `default.html` - Base layout (nav + footer)
- `course.html` - Individual course pages
- `educator.html` - Individual educator pages
- `session.html` - Individual session pages (simplified course layout: hero, summary, educator, pricing — no lessons/reviews/related)
- `post.html` - Blog post pages

### Key Data Files
- `_data/course_categories.yml` - Maps topic tags to display categories for course catalog (11 categories with position ordering)
- `_data/hero_videos.yml` - Background video config for hero section (active ID + video list)
- `_data/prices.json` - Pricing data (`mzed-monthly`, `mzed-annual`)

### SCSS Structure
- `_sass/core-styles.scss` - CSS variables, fonts, global `.cs-topper`, `.cs-title`, `.cs-text`, `.cs-button-solid` styles
- `_sass/homepage.scss` - All homepage section styles
- `_sass/course.scss` - Course page + pricing section (`#plan`) styles
- `_sass/course-card.scss` - Course card component
- `_sass/courses.scss` - Courses listing page
- `_sass/educator.scss` - Individual educator page
- `_sass/educators.scss` - Educators listing page
- `_sass/nav.scss` - MZed nav (sticky/fixed, transparent homepage with scroll-to-solid, solid inner pages, mobile hamburger)
- `_sass/footer.scss` - MZed footer (newsletter, link grid, legal bar)
- `_sass/creators.scss` - Creators/Teach page (hero, creator stats strip, why-teach grid)
- `_sass/sessions.scss` - Sessions listing page, session card component, session detail page
- `_sass/news-card.scss` - News/blog card component
- `_sass/post.scss` - Blog post page

### CSS Variables (from core-styles.scss)
```css
--primary: #ea3e33;        /* Red */
--primaryLight: #fbb01a;   /* Gold/yellow */
--secondary: #5db4e4;      /* Blue */
--secondaryLight: #95c456;  /* Green */
--headerColor: #333;
--bodyTextColor: #4e4e4e;
--bodyTextColorWhite: #fafafa;
--bodyFontSize: 1.1rem;
--headerFontSize: clamp(2rem, 5vw, 3rem);
--sectionPadding: clamp(3.75rem, 7.82vw, 6.25rem) 1rem;
```

### Course Frontmatter Structure
Courses use nested YAML with `Course Card` prefix:
```yaml
title: "Course Name"
position: 1              # Sort order for popularity (lower = more popular)
release_date: 2025-01-13 # YYYY-MM-DD, used for Release Date sort on courses page
Course Card:
  Title: "Course Name"
  Image: /uploads/image.jpg
  Educator: "Educator Name"
  Topics:
    - cinematography
    - filmmaking
    - lighting
```
Topics are lowercase, hyphenated strings. A course can have multiple topics.

### Post Frontmatter Structure
```yaml
title: "Post Title"
date: 2025-01-01 00:00:00 Z
image: "/assets/images/posts/image.jpg"
layout: post
blog_category: "Educational"  # One of: "Educational", "MZed News", "New Course"
```

### Educator Frontmatter Structure
```yaml
name: "Educator Name"
subtitle: "Role/Title"
Image: /uploads/photo.jpg
short_bio: "Bio text"
position: 1  # Sort order (lower = first)
```

### Session Frontmatter Structure
```yaml
title: "Session Name"
date: 2026-02-18 00:00:00 Z   # Must be past/present date (Jekyll skips future dates)
session_date: 2026-03-15 18:00:00 Z  # Actual session date for display
image: "/assets/images/courses/..."
educator: "Educator Name"
description: "Short description"
duration: "90 min"
status: upcoming               # One of: "upcoming", "live", "past"
position: 1                    # Sort order
Session Page:
  Main Title: "Session Title"
  Main Text: "Longer description"
  Main Image: "/assets/images/..."
```
**Important:** Jekyll's `future: false` (default) prevents documents with future `date` from being published. Use `date` for Jekyll internals (set to current/past date) and `session_date` for the actual event date displayed to users.

## Homepage Structure (index.html)

The homepage follows an **Attention > Interest > Trust > Action** conversion funnel.

### Section Order
```
1. Hero (#hero-229)                    ATTENTION
2. Just Added (#just-added)            INTEREST (latest course + session)
3. Trusted By (#trusted-by)            TRUST
4. Stats Strip (#stats-strip)          INTEREST
5. Course Catalog (#course-catalog)    INTEREST
6. Educator Showcase (#educator-showcase) TRUST
7. Video Testimonial (#video-1683)     TRUST
8. Written Reviews (#reviews-399)      TRUST
9. CTA Banner (#cta-banner)            ACTION
10. Recent Articles (#recent-articles) SEO/INTEREST
11. FAQ (#faq-1261)                    TRUST
12. Pricing (#plan)                    ACTION
```

### Homepage Frontmatter (Siteleaf-editable)
```yaml
hero:
  headline: "800+ Lessons from the World's Top Filmmakers."
  headline2: "One Subscription."              # Rendered in gold accent color
  subtext: "60+ courses from Oscar & Emmy Award winners, Hollywood DPs, and top content creators."
  subtext2: "Stream anywhere. Cancel anytime." # Rendered bold with tagline styling
  cta_text: "Get MZed Pro"
  cta_link: "#plan"
  social_proof: "Join 100,000+ filmmakers"     # Shown with avatar stack + stars
catalog:
  topper: "Course Library"
  title: "All the courses you need to become a master filmmaker"
  text: "Over 800 lessons featuring trusted, high-quality course videos..."
educators_section:
  topper: "World-Class Educators"
  title: "Learn from the best educators in the business"
  text: "Our educators include some of the best-known..."
cta_banner:
  title: "Start learning from the best today"
  text: "Join thousands of filmmakers already learning with MZed Pro."
  cta_text: "Join MZed Pro"
  risk_text: "7-day money-back guarantee on annual plans. Cancel monthly anytime."
```

### Hero Structure
The hero uses a column flex layout with visual hierarchy:
- **headline** (font-weight: 300, white) + **headline2** wrapped in `.cs-title-accent` (font-weight: 700, gold/primaryLight)
- **subtext** (0.85 opacity, max-width: 36rem) + **subtext2** wrapped in `.cs-text-tagline` (font-weight: 600, letter-spacing)
- CTA button (18px font, 56px horizontal padding)
- Trust signal: 5 overlapping educator avatar circles + gold stars + social proof text (pulled from `_educators` collection, sorted by position, limit 5)

### Homepage Includes
| Include | Purpose |
|---|---|
| `trusted_by.html` | Scrolling logo bar — "Trusted by teams at" (50s animation) |
| `stats_strip.html` | 4 key numbers: Courses, Lessons, Hours, Value (course count is dynamic from collection) |
| `course_catalog.html` | Netflix-style horizontal-scroll rows grouped by topic from `_data/course_categories.yml` |
| `course_thumb.html` | Lightweight thumbnail card: image + title + educator |
| `educator_showcase.html` | Top 8 educators from collection (sorted by position) |
| `educator_card_mini.html` | Circular photo + name + subtitle card |
| `cta_banner.html` | Full-width red CTA with risk-reduction text |
| `testimonial_card.html` | Review card: stars + quote + photo + name/job (used by `_testimonials` collection) |
| `mzed_pricing.html` | Two side-by-side pricing cards (Annual/Monthly, annual first) with "MZed Pro membership includes:" heading, shared feature list, trust signal, Gift section, and dynamic savings badge |

### Course Catalog Categories
Defined in `_data/course_categories.yml`, sorted by `position`:
1. Cinematography (23 courses)
2. Filmmaking (41)
3. Lighting (14)
4. Editing & Post-Production (13)
5. Color Grading (6)
6. Visual Storytelling (16)
7. Directing (8)
8. Photography (6)
9. Audio & Podcasting (4)
10. AI (new)
11. Producing (5)

Courses appear in multiple categories if they have multiple topics. Categories with 0 matching courses are auto-hidden.

## Conversion Optimization Decisions

- **Value-first headline** - Leads with library scale (800+) and credential authority (World's Top Filmmakers), with "One Subscription." as a bold gold accent line. Research shows outcome/value headlines outperform pain-point framing.
- **Trust signal in hero** - Overlapping educator avatars + 5 stars + "Join 100,000+ filmmakers" follows the modern SaaS social proof pattern (similar to Cursor, Linear, etc.)
- **Credential stacking in subtext** - "Oscar & Emmy Award winners, Hollywood DPs, and top content creators" is specific and aspirational vs generic "best in the industry"
- **Single CTA per section** - Research shows 371% more clicks vs multiple CTAs. "Get MZed Pro" uses a power verb ("Get") that implies receiving value.
- **Risk-reduction text** at CTA banner and pricing points. Hero uses "Stream anywhere. Cancel anytime." as a bold tagline instead.
- **Stats strip** with light gray background and multicolor numbers (red/blue/green/gold) at 4rem — courses, lessons, and hours are computed dynamically from course frontmatter; course value is hardcoded. Dense number presentation is impactful and flows smoothly from the trusted-by section into the course catalog.
- **Streaming-platform catalog** - Netflix-style horizontal scroll shows breadth of library without overwhelming. Pure CSS scroll-snap, no JS carousel.
- **Real educator cards** instead of static background image - Actual faces and names build more trust than a generic photo.
- **CTA banner after trust section** - Placed after video testimonial + written reviews for maximum trust-to-action conversion. Copy uses value anchoring ("$10,000+ in course value — less than $1/day") with "One subscription." on its own line for emphasis.
- **FAQ section** - 7 conversion-focused questions in single column, ordered by decision funnel (What is it → What's included → Educators → Value comparison → Mobile/offline → Renewal pricing → Cancellation). First item auto-expanded. Inline JS toggle scoped to `#faq-1261`.
- **Testimonial section** - Video + written reviews share gray background, creating one unified trust zone. White review cards with box-shadow pop off the background. Gold 5-star ratings on each card add quantitative credibility. Section header uses social proof number ("See why 100,000+ filmmakers choose MZed Pro").
- **Pricing cards** - Two side-by-side cards (annual left, monthly right). Annual card has gold border + "Best Value — Save X%" dynamic badge. "MZed Pro membership includes:" heading above shared feature list (6 items in 2-col grid). Trust signal with educator avatars. Gift section at bottom with link.

## Section Background Flow
```
Hero             → dark (video overlay)
Just Added       → #fff (white)
Trusted By       → #f7f7f7 (light gray)
Stats Strip      → #f7f7f7 (light gray)
Course Catalog   → #14142b (dark navy)
Educators        → #fff (white)
Video            → #f7f7f7 (light gray)
Reviews          → #f7f7f7 (light gray)
CTA Banner       → var(--primary) (red)
Recent Articles  → #f7f7f7 (light gray)
FAQ              → #fff (white)
Pricing          → #fff (white)
```

## Change Log

### 2025-02-01: Homepage Conversion Optimization
**Created:**
- `_data/course_categories.yml`
- `_includes/course_catalog.html`, `course_thumb.html`
- `_includes/educator_showcase.html`, `educator_card_mini.html`
- `_includes/stats_strip.html`
- `_includes/cta_banner.html`

**Modified:**
- `index.html` - Restructured sections, added Siteleaf-editable frontmatter, removed old sections (#sbs-1585, #services-1729, #RPsbs-600, #RPsbsr-600, #latest-courses)
- `_sass/homepage.scss` - Removed ~700 lines of old section styles, added styles for stats-strip, course-catalog, educator-showcase, cta-banner, recent-articles, risk-text
- `_sass/course.scss` - Added `.cs-risk-text` styles in pricing section
- `_includes/mzed_pricing.html` - Added "Cancel anytime" / "7-day money-back guarantee" under CTA buttons

### 2025-02-01: Homepage Visual Enhancements
**Modified:**
- `index.html` - Hero: new conversion-optimized copy (value-first headline, credential-stacking subtext, "Get MZed Pro" CTA), trust signal component with educator avatars + stars + social proof, split headline/subtext into two-part frontmatter fields with `.cs-title-accent` and `.cs-text-tagline` spans. FAQ: removed SVG waves background.
- `_includes/trusted_by.html` - Changed label from "Trusted by" to "Trusted by teams at"
- `_sass/homepage.scss` - Hero: column flex layout, font-weight 300 headline + 700 gold accent, larger subtext (22px max) and button (18px), trust signal with overlapping avatar stack. Trusted by: slowed animation 30s→50s. Stats strip: dark bg (#1a1a2e), gold numbers (primaryLight), dividers. Course catalog: compacted padding/gaps/thumbnails (13rem max). Educator showcase: compacted padding/gaps/photos (6rem max). Video: added #f7f7f7 background. Reviews: border-radius 16px→4px. FAQ: changed from dark (#14142b) to white background with standard text colors, removed wave background styles.

### 2025-02-01: Pricing Section Redesign
**Modified:**
- `_includes/mzed_pricing.html` - Complete rewrite from 3-column comparison table to two side-by-side pricing cards. Dynamic Liquid savings badge, shared 6-item feature list, trust signal with educator avatars + stars.
- `_sass/course.scss` - Replaced ~460 lines of comparison table + toggle styles with ~170 lines of card-based styles. Mobile-first with cards stacked (annual first), side-by-side at tablet+. Removed dead toggle script and CSS animations.

### 2025-02-01: Testimonial & Stats Section Enhancements
**Modified:**
- `index.html` - Reviews: added 5-star gold ratings to all 3 review cards. Video section: updated topper to "Member Reviews" and headline to "See why 100,000+ filmmakers choose MZed Pro".
- `_sass/homepage.scss` - Reviews: gray background (#f7f7f7), white cards with box-shadow, hidden quote icons, larger star ratings (1.5rem), gray profile borders. Stats strip: light gray bg (#f7f7f7), multicolor numbers (red/blue/green/gold via nth-child), increased size to 4rem, dark text labels, dark dividers.

### 2025-02-01: CTA, Articles, FAQ & Dynamic Stats
**Modified:**
- `index.html` - CTA banner: updated copy to value-anchoring ("60+ courses. 800+ lessons. One subscription." with line break, "$10,000+ in course value"). Recent Articles: updated topper ("Filmmaking Insights"), title ("Tips, Techniques & Industry News"), subtext, and button text. FAQ: complete rewrite from 10 questions in two columns to 7 conversion-focused questions in single column with inline toggle JS. Added "What happens after my first year?" FAQ item ($199/year renewal). Fixed "255 hours" → "375 hours" inconsistency.
- `_includes/stats_strip.html` - Lessons and hours now computed dynamically via Liquid loops over `site.courses` collection. Course value updated to "$10,000+".
- `_includes/mzed_pricing.html` - Updated feature list: course value to "$10,000+", lesson count to "840+", educator description to match hero copy.
- `_sass/homepage.scss` - FAQ: removed `.cs-wrapper` styles, removed tablet two-column breakpoint, updated container max-width to 800px for single column, tightened vertical spacing (gap, button padding, answer padding). Educator showcase: added title bottom margin for spacing.

### 2025-02-01: Testimonials Collection
**Created:**
- `_testimonials/` collection (3 files: ryan-connolly, cooper-demar, drazen-stader) with name, job, position, image, review fields
- `_includes/testimonial_card.html` — reusable review card component
- `assets/images/testimonials/` — 11 reviewer photos downloaded from CDN, stored locally with descriptive filenames

**Modified:**
- `_config.yml` — Added `testimonials` collection (output: false)
- `index.html` — Reviews section: replaced 3 hardcoded cards with Liquid loop over `_testimonials` sorted by position. Trust signal avatars use 5 hand-picked reviewer photos (local images). Review card alignment fix (`.cs-flex-group` margin-top: auto pushes reviewer info to bottom).
- `_includes/mzed_pricing.html` — Trust signal avatars use same 5 reviewer photos (local images).
- `_sass/homepage.scss` — Reviews: removed `justify-content: center` from `.cs-item`, added `margin-top: auto` to `.cs-flex-group` for consistent card alignment.

### 2025-02-01: Courses Listing Page Overhaul
**Modified:**
- `courses/index.html` — New frontmatter header copy ("Course Library" / dynamic course+lesson counts / subtext with line break). Replaced `mzed_stats.html` with `stats_strip.html` for consistent branding. Filter labels: "Browse by Topic" / "Show All". Topics reordered by popularity (Cinematography first, Podcasting last).
- `_sass/course-card.scss` — Compact cards: hidden inline description (`display: none`), smaller title (1.15rem), educator (0.875rem), tighter padding/gap. Stats bar changed from dark (`var(--headerColor)`) to light (`#f7f7f7`) with dark text. Hover overlay redesigned: dark background with course description (1.2rem, 5-line clamp) and "Go to Course →" link.
- `_sass/courses.scss` — Removed ~135 lines of `#mzed-summary-stats` styles. Tighter grid gap (`clamp(0.75rem, 1.5vw, 1.25rem)`). 4-col desktop breakpoint moved from 1300px to 1024px. Filter redesigned: pill buttons replaced with underline tabs (no backgrounds/borders, red underline on active, lighter inactive text #aaa, 0.875rem). 90% width on desktop to fit all topics in one row. Mobile gap increased for wrapped line readability.
- `_includes/course_card.html` — Overlay now includes course description text and arrow on "Go to Course →".
- `_includes/mzed_stats.html` — Updated "$9000+" to "$10,000+" (still used on course detail pages).

### 2025-02-01: Educators Page Overhaul
**Modified:**
- `educators/index.html` — New frontmatter header copy ("Our Educators" / "Learn from the Best Filmmakers in the Business" / credential-stacking subtext). Added `stats_strip.html` and `mzed_pricing.html` below grid. Removed Siteleaf `{% assign page %}` line.
- `_includes/educator_card.html` — Stripped down: removed course thumbnails grid and inline bio. Added course count badge ("8 Courses"). Hover overlay redesigned: dark background with short_bio (6-line clamp) and "View Educator →" link.
- `_sass/educators.scss` — Complete rewrite: removed border-radius (matches course cards), square photos (`aspect-ratio: 1/1`), compact info (1.15rem name, 0.875rem subtitle), dark hover overlay with bio, tighter grid gap, 4-col at 1024px. Removed all course thumbnail styles (~80 lines).
- `_layouts/educator.html` — Swapped `mzed_stats.html` → `stats_strip.html`.
- `_includes/course_card_mini.html` — Overlay updated: description + "Go to Course →" arrow.
- `_sass/educator.scss` — Show full course descriptions on educator detail page (`display: block`, no clamp). Hide overlay description since it's already visible inline.
- `_educators/*.md` (8 files) — Removed escaped quotes (`\"` → `"`) in bios. Converted Rubidium Wu bio from flow scalar to `|-` block scalar.

### 2025-02-01: Course Detail Page Overhaul
**Modified:**
- `_layouts/course.html` — Swapped `mzed_stats.html` → `stats_strip.html` for consistent branding. Updated recommended courses subtext to match site voice ("Explore more from the MZed library — 60+ courses...").
- `_includes/course_pricing.html` — Complete rewrite from toggle/table layout to 3-card design. Cards: Course Purchase (one-time price, dark CTA, "Lifetime access"), Monthly ($49/month, outline CTA, "Cancel anytime"), Annual ($29/month billed annually, gold border, "Best Value" badge, "7-day money-back guarantee"). Shared 6-item feature list with updated copy ($10,000+, Oscar & Emmy). Trust signal with 5 reviewer avatars + stars. Price lookup from `_settings` collection with sale support, fallback $100.
- `_sass/course.scss` — Added `.cs-card-course` (order: -2 on mobile, dark button style) and `.cs-card-group-three` modifier (33.33% width at tablet, 19rem max at desktop). Course purchase card appears first on mobile, all three side-by-side at 768px+. Reviews section: red background → #f7f7f7, green topper → red, white cards with box-shadow, removed border-radius.
- `_includes/course_lessons.html` — Fixed lesson descriptions rendering as multiple `<p>` tags per paragraph. YAML `|-` block scalars preserve line wraps; `newline_to_br | split` was creating separate paragraphs for each line. Now outputs single `<p>` per description using `replace: '<br />', ' '`.
- `_includes/course_review.html` — No changes (styling handled in course.scss).

### 2025-02-01: Course Detail Page Polish
**Modified:**
- `_layouts/course.html` — Recommended courses: reframed as "Included with MZed Pro" / "More Courses You'll Love" with dynamic course count (`site.courses.size - 1`). Reviews: "Course Reviews" → "Reviews", "What Viewers are Saying" → "What Students Are Saying". What You'll Learn: replaced dead `<a href="#">` wrappers with `<div>` elements.

### 2025-02-01: Course Summary Scroll-Reveal Animation
**Modified:**
- `_sass/course.scss` — Added scroll-reveal animation styles to `#sbs-1015`: text elements (`.cs-topper`, `.cs-title`, `.cs-text`, `.cs-button-12`) start hidden (`opacity: 0`, `translateY(1.5rem)`) with 0.6s ease-out transitions and staggered delays (0s/0.15s/0.3s/0.45s). `.is-visible` class reveals them. Includes `prefers-reduced-motion: reduce` media query to skip animation.
- `_layouts/course.html` — Added inline Intersection Observer script after `#sbs-1015` section. Observes `.cs-topper` element with `rootMargin: '0px 0px -10% 0px'` so animation triggers when text is clearly in viewport, not just peeking in. Falls back to immediate visibility if IntersectionObserver is unsupported.

### 2025-02-01: What You'll Learn Icon Hover Fix
**Modified:**
- `_sass/course.scss` — Added `filter: brightness(0) invert(1)` on `.cs-icon` inside `#services-1304 .cs-item:hover` so SVG icons turn white on dark hover background. Added `transition: filter 0.3s` on `.cs-icon` for smooth change.

### 2025-02-01: Site-Wide Scroll-Reveal Animation System
Standalone, opt-in scroll-reveal system using `data-reveal` attributes. Two new files (SCSS + JS) that can each be disabled by removing a single line. Elements fade up with staggered timing as they enter the viewport. Respects `prefers-reduced-motion`, has `<noscript>` fallback, and a scroll-to-bottom fallback for elements near the page end.

**Usage:** `data-reveal` on an element → fades up on scroll. `data-reveal-children` on a container → direct children stagger in. `data-reveal-delay="100"` sets stagger interval (default 100ms). Max stagger capped at 600ms for large grids.

**Disabling:** Remove `@use 'scroll-reveal'` from `main.scss` and/or `<script>` tag from `default.html`.

**Created:**
- `_sass/scroll-reveal.scss` — Hidden/revealed states via `[data-reveal]` attribute selectors, child stagger via `--reveal-delay` CSS custom property, `prefers-reduced-motion` override.
- `assets/js/scroll-reveal.js` — Single IntersectionObserver (`rootMargin: 0px 0px -10% 0px`), stagger delay injection on children, 600ms max-delay cap, reduced-motion/no-JS fallbacks, scroll-to-bottom fallback.

**Modified:**
- `assets/css/main.scss` — Added `@use 'scroll-reveal'`.
- `_layouts/default.html` — Added `<script>` for `scroll-reveal.js` and `<noscript>` fallback.
- `_layouts/course.html` — Removed inline `#sbs-1015` scroll-reveal script (migrated to new system). Added `data-reveal-children` to `#sbs-1015 .cs-content`. Added `data-reveal`/`data-reveal-children` to `#services-1304`, `#reviews-567`, `#recommended-courses`.
- `_sass/course.scss` — Removed 34 lines of `#sbs-1015`-specific reveal CSS (now handled by `scroll-reveal.scss`).
- `index.html` — Added reveal attributes to `#video-1683 .cs-content`, `#reviews-399 .cs-card-group`, `#recent-articles` content + news cards, `#faq-1261` content + FAQ items.
- `_includes/stats_strip.html` — `data-reveal-children` on `.stats-list`.
- `_includes/course_catalog.html` — `data-reveal` on `.cs-content` and each `.catalog-row`.
- `_includes/educator_showcase.html` — `data-reveal` on `.cs-content`, `data-reveal-children` on `.educator-grid`.
- `_includes/cta_banner.html` — `data-reveal` on `.cs-container`.
- `_includes/mzed_pricing.html` — `data-reveal` on `.cs-content`, `data-reveal-children` on `.cs-card-group`.
- `_layouts/educator.html` — `data-reveal` on `#educator-courses .cs-content`, `data-reveal-children` on `.cs-card-group`.
- `courses/index.html` — `data-reveal` on header `.cs-content`.
- `educators/index.html` — `data-reveal` on `.cs-content`, `data-reveal-children` on `.cs-card-group`.
- `news/index.html` — `data-reveal` on `.cs-content`, `data-reveal-children` on `.news-card-group`.
- `_layouts/post.html` — `data-reveal` on `.post-container`.

### 2025-02-02: Production Nav & Footer
Replaced `#tempnav` with a production-quality nav and footer matching mzed.com's look and feel. Both wrapped in `{% if site.mzed_chrome %}` kill switch — set `mzed_chrome: false` in `_config.yml` to disable.

**Nav:** Sticky/fixed on all pages. Transparent on homepage (white text over hero, transitions to solid white on scroll via `mzed-nav--scrolled` class), solid white with bottom border on inner pages. `.mzed-nav-spacer` (70px) on inner pages offsets fixed positioning. Inline SVG MZed logo, left-aligned links (Courses, Educators, Sessions, Blog, Teach, Gift), right-aligned "Join MZed Pro" CTA + "Log in" button. Mobile hamburger with animated X toggle and dropdown menu. BEM class structure (`.mzed-nav`, `--transparent`/`--solid`/`--scrolled` modifiers).

**Footer:** Newsletter section (light gray bg, email input + subscribe button). 4-column link grid (MZed, Support, Learn About topics from `course_categories.yml`, Connect with social icons). Legal bar with copyright, Terms/Privacy links, "Empowering Filmmakers" tagline. Responsive: 1-col → 2-col → 4-col.

**Created:**
- `_includes/mzed_nav.html` — Nav with homepage detection (`page.url == '/'`), inline SVG logo, desktop links + actions, mobile hamburger with inline toggle script.
- `_includes/mzed_footer.html` — Newsletter form, 4-column link grid with dynamic topic links from `course_categories.yml`, social icon SVGs (Facebook, X, Instagram, YouTube), legal bar.
- `_sass/nav.scss` — BEM styles, `--transparent`/`--solid` variants, mobile menu, desktop breakpoint at 48rem.
- `_sass/footer.scss` — Newsletter, link grid (responsive 1→2→4 col), social icons with hover, legal bar.

**Modified:**
- `_config.yml` — Added `mzed_chrome: true` kill switch.
- `_layouts/default.html` — Replaced `#tempnav` with conditional `mzed_nav.html` include, added conditional `mzed_footer.html` before scripts.
- `assets/css/main.scss` — Added `@use 'nav'` and `@use 'footer'`.
- `_sass/core-styles.scss` — Removed `#tempnav` styles (~33 lines).
- `news/index.html` — Added `mzed_pricing.html` include above footer.

### 2025-02-02: Creators "Teach on MZed" Page
New page at `/creators/` pitching content creators to license their educational filmmaking content to MZed.

**Page structure:** Hero with dark overlay background image → Creator Stats Strip (dark blue bg, gold text: $1M+ paid, Oscar & Emmy educators, educator count) → Why MZed (6 value prop cards) → CTA Banner (mailto:creators@mzed.com).

**Created:**
- `creators/index.html` — Page with hero, creator stats strip, why-teach section, CTA banner include.
- `_sass/creators.scss` — `#creator-hero` (dark overlay + background image), `#creator-stats` (dark navy bg, gold numbers, 3 stats with dividers), `#why-teach` (card grid 1→2→3 col).

**Modified:**
- `assets/css/main.scss` — Added `@use 'creators'`.
- `_includes/cta_banner.html` — Made `href` configurable via `page.cta_banner.cta_link` frontmatter with `#plan` default fallback.
- `_includes/mzed_nav.html` — Added "Teach" link (`/creators/`) to both desktop nav links and mobile menu.

### 2025-02-02: Safari CSS Fixes (aspect-ratio + height: 100%)
Fixed Safari rendering bugs where card images collapsed to thin strips or zero height across multiple pages.

**Root cause 1:** `aspect-ratio` on non-replaced elements (`<picture>`, `<div>`) inside flex column containers doesn't compute height correctly in Safari. **Fix:** Moved `aspect-ratio` onto the `<img>` element (a replaced element where Safari handles it correctly). Removed `aspect-ratio` from all container elements.

**Root cause 2:** `height: 100%` on grid items with flex column children causes Safari to constrain and compress flex children. **Fix:** Removed `height: 100%` from card items — grid's default `align-items: stretch` handles equal-height cards without it.

**Root cause 3:** Course detail hero `.cs-big-link` used `aspect-ratio` with flex centering for the play button. **Fix:** Changed to `padding-top: 56.25%` with absolutely positioned `.cs-background` and explicit `top/left/transform` centering on `.cs-picture` play button.

**Modified:**
- `_sass/course-card.scss` — Removed `height: 100%` from `.course-card-item`. Changed `.course-card-picture` from `aspect-ratio: 16/9` container to simple wrapper; moved `aspect-ratio: 16/9` onto `img` with `height: auto; display: block`.
- `_sass/educators.scss` — Same pattern: removed `aspect-ratio: 1/1` from `.educator-card-picture` container, added `aspect-ratio: 1/1` to `img`.
- `_sass/homepage.scss` — Same pattern for `.course-thumb-picture` in course catalog.
- `_sass/courses.scss` — Removed redundant `aspect-ratio` overrides at tablet/desktop breakpoints.
- `_sass/news-card.scss` — Removed `height: 100%` from `.news-card-item`.
- `_sass/course.scss` — Changed `.cs-big-link` from `aspect-ratio: 16/9` to `padding-top: 56.25%`. Changed `.cs-background` from `position: relative` to `position: absolute`. Added explicit centering (`top: 50%; left: 50%; transform: translate(-50%, -50%)`) to `.cs-picture` play button, updated hover to preserve centering.

### 2026-02-18: Sticky Nav & Updated Navigation
**Modified:**
- `_includes/mzed_nav.html` — Nav items updated: Courses (was "Our Courses"), Educators (was "Our Educators"), Sessions (new), Blog (was "News"), Teach, Gift (moved to last). Added scroll listener for homepage transparent→solid transition (`mzed-nav--scrolled` class at 50px scroll).
- `_sass/nav.scss` — Changed both `--transparent` and `--solid` variants from `position: absolute`/`relative` to `position: fixed`. Added `--scrolled` state styles (white bg, dark text, border, box-shadow). Added `.mzed-nav-spacer` (70px) for inner page offset.
- `_layouts/default.html` — Added `.mzed-nav-spacer` div after nav for non-homepage pages.

**Created:**
- `sessions/index.html` — Placeholder page at `/sessions/` with "Coming Soon" messaging and pricing section.

### 2026-02-18: Homepage Enhancements
**Modified:**
- `index.html` — Added "What's New? ↓" link in hero after trust signal, linking to `#just-added`. Added new "Just Added" section between hero and Trusted By showing latest course (by position) + sessions placeholder in 2-col grid.
- `_sass/homepage.scss` — Hero: added viewport-height-based positioning (`min-height: 85vh`, `align-items: flex-end` on tall screens ≥700px height + ≥768px width) so text sits lower and faces in video are visible. Added `.cs-whats-new` gold link styles. Added `#just-added` section styles (white bg, 2-col grid at tablet, card with image/badge/info, hover lift).
- `_sass/homepage.scss` — Video thumbnail hover zoom reduced from `scale(1.1)` to `scale(1.03)`.
- `_sass/course.scss` — Video thumbnail hover zoom reduced from `scale(1.1)` to `scale(1.03)` across all course page video links.

### 2026-02-18: Stats Count-Up Animation
**Modified:**
- `_includes/stats_strip.html` — Stats numbers now use `data-count`, `data-prefix`, `data-suffix` attributes. Added inline JS with IntersectionObserver that triggers a fast count-up animation (ease-out cubic, 1.2s duration) from 0 to the final number when stats enter viewport. Numbers are formatted with `toLocaleString()` for comma separators.

### 2026-02-18: Course Catalog Random Sort & AI Category
**Modified:**
- `_includes/course_catalog.html` — Added inline JS (Fisher-Yates shuffle) that randomizes course thumbnail order within each category row on every page load.
- `_data/course_categories.yml` — Added "AI" category (topic: `ai`, position: 10). Bumped "Producing" to position 11.
- `courses/index.html` — Added "AI +" filter button (last position, after Podcasting).

### 2026-02-18: Pricing Section Updates
**Modified:**
- `_includes/mzed_pricing.html` — Swapped card order: Annual card first (left), Monthly second (right). Added "MZed Pro membership includes:" heading above feature list. Added Gift section at bottom (icon, title, description, "Learn about gifting →" link).
- `_sass/course.scss` — Removed CSS `order` overrides for card positioning (source order now controls layout). Added `.cs-features-heading` styles. Added `.cs-gift-section` styles (bordered box, gold link).

### 2026-02-18: Courses Page Sort By Feature
**Modified:**
- `courses/index.html` — Added "Sort By" section with connected pill-group: Popularity (default), Release Date, Alphabetical. Topic filters redesigned from underline tabs to pill buttons with rounded borders and "+" suffix. "Show All" now first and starts active.
- `_includes/course_card.html` — Added `data-position`, `data-title`, `data-release` attributes to course card `<li>` elements for client-side sorting.
- `assets/js/courses-index.js` — Complete rewrite: handles both topic filtering and sorting. Popularity sorts by `position`, Release Date sorts by `release_date` (newest first), Alphabetical sorts by title A-Z. Filter and sort work together.
- `_sass/courses.scss` — Filter buttons: pill style with `border: 1.5px solid var(--primary)`, `border-radius: 2rem`, red fill on active. Sort buttons: connected pill group with shared border and segmented control style.
- `_courses/*.md` (all 66 files) — Added `release_date: YYYY-MM-DD` field to frontmatter with real release dates. Updated `position` values: Ollie Kenchington's 10 courses set to positions 1-10 (most popular), other courses bumped to avoid collisions.

### 2026-02-18: New Courses Added
**Created:**
- `_courses/the-efficient-filmmaker-video-masking.md` — "The Efficient Filmmaker: AI Video Masking for the Rest of Us" by Mascha Deikova (7 lessons, 1h 4m). Topics: editing, color-grading, ai.
- `_courses/ai-video-for-filmmakers.md` — "Directing the Future: Ethical AI Video for Filmmakers" by Drew Geraci (11 lessons, 2h 35m). Topics: filmmaking, ai.
- `_courses/the-efficient-filmmaker-scan-and-plan.md` — "The Efficient Filmmaker: Scan and Plan" by Mascha Deikova (6 lessons, 51m). Topics: filmmaking, ai.
- Course thumbnail images downloaded from MZed CDN for all three courses.

**Modified:**
- `_courses/the-efficient-filmmaker-subtitle-mastery.md` — Added `ai` topic.

### 2026-02-18: Educators Page "Become an Educator" Section
**Modified:**
- `educators/index.html` — Added `#become-educator` section between educator grid and stats strip. Light gray background, centered text with "Share Your Knowledge" topper, "Become an MZed Educator" headline, description, and "Learn More" button linking to `/creators/`.
- `_sass/educators.scss` — Added `#become-educator` styles (centered, max-width 800px, `#f7f7f7` background).

### 2026-02-18: Blog Categories & Filtering
**Modified:**
- `_posts/*.markdown` (all 175 files) — Added `blog_category` field to frontmatter. Categories: "Educational" (113 posts), "MZed News" (40 posts), "New Course" (24 posts).
- `_includes/news_card.html` — Added `data-category` attribute and `.news-card--{category}` class to `<li>`. Added colored category badge (`.news-card-category`) in meta area next to date.
- `news/index.html` — Added category filter UI: connected pill-group (All | MZed News | Educational | New Course). Added inline JS for filtering cards by category.
- `_sass/news-card.scss` — Category color system: MZed News = red (`--primary`), Educational = blue (`--secondary`), New Course = green (`--secondaryLight`). Each category gets colored top border on card + colored badge. Blog filter styles: connected pill group with per-category active colors. Hidden state with `!important` to override grid specificity.

### 2026-02-18: Teach Page Updates
**Modified:**
- `creators/index.html` — Removed "Over $1M paid to MZed educators" trust text from hero. Removed entire Topic Board section (Supabase form, vote list, sort toggle) and all associated inline JS (~230 lines). Added `#creator-stats` section after hero with 3 stats: $1M+ paid, Oscar & Emmy educators, dynamic educator count from `site.educators.size`. Hero CTA now links to `#why-teach` instead of removed topic board.
- `_sass/creators.scss` — Removed `.cs-trust-signal`/`.cs-trust-text` styles from hero. Removed all `#topic-board` styles (~185 lines: form, input, submit, status, sort buttons, topic list, vote buttons, empty state). Added `#creator-stats` styles: dark navy background (`#14142b`), gold numbers (`var(--primaryLight)`), 3-stat horizontal layout with dividers at tablet+, stacked on mobile.

### 2026-02-18: Sessions Collection & Pages
New `_sessions` collection for live webinars and on-demand sessions. Listing page at `/sessions/` similar to courses page. Detail pages at `/sessions/:name/` similar to course detail but without lessons, reviews, or related courses.

**Session cards** show: thumbnail (16:9), status badge (Upcoming = blue, Live = red, Replay = green), date, title, educator, description (3-line clamp), stats bar.

**Session detail page** includes: hero image, summary section (side-by-side image + content on desktop with meta bar: educator, duration, date, status), educator section (reuses `about_educator.html`), stats strip, and pricing.

**Important gotcha:** Jekyll's default `future: false` prevents documents with future dates from being written to `_site`. Sessions use `date` (set to current/past) for Jekyll internals and `session_date` for the actual event date displayed to users.

**Created:**
- `_sessions/` — 4 placeholder sessions: Lighting Masterclass Live (Shane Hurlbut), Color Grading Workflows (Ollie Kenchington), Documentary Storytelling Q&A (Philip Bloom), AI Tools for Filmmakers (Drew Geraci).
- `_includes/session_card.html` — Session card component with status badge, date, description.
- `_layouts/session.html` — Session detail layout: hero, summary with meta bar, educator, stats strip, pricing.
- `_sass/sessions.scss` — All session styles: listing page grid (1→2→3 col responsive), session cards, status badge colors, detail page layout (side-by-side at desktop).

**Modified:**
- `_config.yml` — Added `sessions` collection (`output: true`, `permalink: /sessions/:name/`), added default layout/permalink for sessions type.
- `sessions/index.html` — Full rewrite from placeholder to real listing page with header, session card grid, stats strip, and pricing.
- `assets/css/main.scss` — Added `@use 'sessions'`.

### 2026-02-18: Course Detail Page Section Reorder & Visual Breakers
Restructured course detail page section order for better flow. Added photo breakers between sections using Additional Images. Reorganized pricing with split perks and gift section.

**New section order:**
1. Course Summary (`#sbs-1015`) — "About the Course", CTA changed to "Start watching"
2. Photo breaker (all Additional Images)
3. Course Stats (dark bar)
4. Trailer (`#mz-hero` — moved down from top)
5. What You'll Learn (`#services-1304`)
6. Photo breaker (second half of Additional Images)
7. Lessons
8. Photo breaker (full set of Additional Images)
9. Reviews
10. Educator (moved after Reviews)
11. Recommended Courses
12. Stats Strip
13. Pricing

**Visual breakers** (`.cs-photo-breaker`): Horizontal-scroll image strips using `page['Course Page']['Additional Images']` placed between major sections. Reuses same scroll-snap pattern as the original `.cs-image-group`. Three instances: after summary (full set), between What You'll Learn and Lessons (second half), between Lessons and Reviews (full set). Skipped entirely if no Additional Images exist.

**Modified:**
- `_layouts/course.html` — Reordered all sections. Moved hero/trailer below course stats. Moved educator after reviews. Changed CTA button text "Start watching with MZed Pro" → "Start watching". Added Liquid logic to split Additional Images array (`half = img_count / 2`) and render three `.cs-photo-breaker` divs at different positions. Removed original `.cs-image-group` from inside `#sbs-1015`.
- `_includes/course_pricing.html` — Reordered cards: Monthly (left) → Annual (middle, gold border + badge) → Course Purchase (right). Replaced single shared feature list with split `.cs-perks-group` containing two `.cs-perks-column` divs: `.cs-perks-pro` (6 items, "MZed Pro membership includes:") and `.cs-perks-course` (4 items: lifetime access, all lessons, certificate, stream on any device). Added gift section (icon, title, description, "Learn about gifting →" link) after perks, before trust signal.
- `_sass/course.scss` — Added `.cs-photo-breaker` styles (horizontal flex scroll, snap, 40% items on mobile, equal flex at tablet+). Added `.cs-perks-group` styles: single container with `rgba(255,255,255,0.07)` background and `0.75rem` border-radius. Mobile: stacked with horizontal divider (`.cs-perks-pro` has `border-bottom`). Tablet+: side-by-side with vertical divider (`.cs-perks-pro` has `border-right`), Pro side `flex: 2` with 2-col feature grid, Course side `flex: 1` with 1-col grid and `justify-content: center`. `.cs-perks-heading` styled as subtle uppercase label (`0.85rem`, `opacity: 0.55`, `letter-spacing: 0.05em`).

### 2026-02-18: Course Detail Page — Split Hero Redesign
Replaced full-bleed overlay hero with MasterClass-style split layout: image left, text right on dark background. Removed separate trailer section (`#mz-hero`) — trailer is now an inline "Watch Trailer" link in the hero meta line that opens Fancybox lightbox. Added new `#about-course` section for the full course description.

**New hero (`#sbs-1015`) — split layout:**
- Image (left, 55% at tablet+): `Course Card Image`, full-height `object-fit: cover`, no overlay/filter needed
- Content (right, 45%): dark `#1a1a1a` background, vertically centered, centered text
- Title: `clamp(2rem, 5vw, 3rem)`, font-weight 700, white, letter-spacing 0.02em
- Educator: uppercase, letter-spacing 0.08em, 60% white opacity
- Description: `Course Card Description` (short tagline)
- Meta line: "X Lessons · Xh Xm · Watch Trailer" (trailer link opens Fancybox)
- CTA: "Get Full Access" using existing `.cs-button-12` style with arrow icon
- Mobile: stacked vertically (image top, text below)

**New section (`#about-course`):**
- Placed after first photo breaker, before Course Stats
- Side-by-side at tablet+ (image 45%, text 55%), stacked on mobile
- Image: `Course Page Main Image`, `border-radius: 0.5rem`, `aspect-ratio: 16/10`
- Text: `Course Page Main Title` + `Main Text` (full description paragraphs)
- `data-reveal-children` for scroll animation

**Updated section order:**
1. **Course Hero** (`#sbs-1015`) — split layout, image left + text right
2. Photo breaker (all Additional Images, `brightness(0.7) saturate(0.8)` filter)
3. **About the Course** (`#about-course`) — Main Image + Main Text (NEW)
4. Course Stats (dark bar)
5. What You'll Learn (`#services-1304`)
6. Photo breaker (second half)
7. Lessons
8. Photo breaker (full set)
9. Reviews
10. Educator
11. Recommended Courses
12. Stats Strip
13. Pricing

**Modified:**
- `_layouts/course.html` — Rewrote hero as split layout with `<picture>` + `.cs-content` side by side. Removed `#mz-hero` trailer section entirely. Added `#about-course` section after first photo breaker. Moved `educator_name` assignment to top of template. Meta line includes lesson count, runtime, and Fancybox trailer link.
- `_sass/course.scss` — Replaced `#sbs-1015` overlay styles with split layout (flex-direction column on mobile, row at 48rem+). Removed all `#mz-hero` / `.cs-big-link` styles (~95 lines). Added `#about-course` styles (white bg, flex row at tablet+, image 45% with border-radius). Added `filter: brightness(0.7) saturate(0.8)` to `.cs-photo-breaker` images. Removed `margin-top` from `.cs-button-12`.
