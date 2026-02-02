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
| `_courses` | 64 files (.md) | Yes | `/courses/:name/` |
| `_educators` | 32 files (.md) | Yes | `/educators/:name/` |
| `_posts` | 175 files (.md) | Yes | `/posts/:title/` |
| `_trusted_by` | 12 files (.md) | No | N/A |
| `_settings` | Pricing/globals | No | N/A |
| `_uploads` | Media files | No | N/A |

### Layouts
- `default.html` - Base layout (nav + footer)
- `course.html` - Individual course pages
- `educator.html` - Individual educator pages
- `post.html` - Blog post pages

### Key Data Files
- `_data/course_categories.yml` - Maps topic tags to display categories for course catalog (10 categories with position ordering)
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

### Educator Frontmatter Structure
```yaml
name: "Educator Name"
subtitle: "Role/Title"
Image: /uploads/photo.jpg
short_bio: "Bio text"
position: 1  # Sort order (lower = first)
```

## Homepage Structure (index.html)

The homepage follows an **Attention > Interest > Trust > Action** conversion funnel.

### Section Order
```
1. Hero (#hero-229)                    ATTENTION
2. Trusted By (#trusted-by)            TRUST
3. Stats Strip (#stats-strip)          INTEREST
4. Course Catalog (#course-catalog)    INTEREST
5. Educator Showcase (#educator-showcase) TRUST
6. Video Testimonial (#video-1683)     TRUST
7. Written Reviews (#reviews-399)      TRUST
8. CTA Banner (#cta-banner)            ACTION
9. Recent Articles (#recent-articles)  SEO/INTEREST
10. FAQ (#faq-1261)                    TRUST
11. Pricing (#plan)                    ACTION
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
| `mzed_pricing.html` | Two side-by-side pricing cards (Monthly/Annual) with shared feature list, trust signal, and dynamic savings badge |

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
10. Producing (5)

Courses appear in multiple categories if they have multiple topics. Categories with 0 matching courses are auto-hidden.

## Conversion Optimization Decisions

- **Value-first headline** - Leads with library scale (800+) and credential authority (World's Top Filmmakers), with "One Subscription." as a bold gold accent line. Research shows outcome/value headlines outperform pain-point framing.
- **Trust signal in hero** - Overlapping educator avatars + 5 stars + "Join 100,000+ filmmakers" follows the modern SaaS social proof pattern (similar to Cursor, Linear, etc.)
- **Credential stacking in subtext** - "Oscar & Emmy Award winners, Hollywood DPs, and top content creators" is specific and aspirational vs generic "best in the industry"
- **Single CTA per section** - Research shows 371% more clicks vs multiple CTAs. "Get MZed Pro" uses a power verb ("Get") that implies receiving value.
- **Risk-reduction text** at CTA banner and pricing points. Hero uses "Stream anywhere. Cancel anytime." as a bold tagline instead.
- **Stats strip** with light gray background and multicolor numbers (red/blue/green/gold) at 4rem — dense number presentation is impactful and flows smoothly from the trusted-by section into the course catalog.
- **Streaming-platform catalog** - Netflix-style horizontal scroll shows breadth of library without overwhelming. Pure CSS scroll-snap, no JS carousel.
- **Real educator cards** instead of static background image - Actual faces and names build more trust than a generic photo.
- **CTA banner after trust section** - Placed after video testimonial + written reviews for maximum trust-to-action conversion.
- **Testimonial section** - Video + written reviews share gray background, creating one unified trust zone. White review cards with box-shadow pop off the background. Gold 5-star ratings on each card add quantitative credibility. Section header uses social proof number ("See why 100,000+ filmmakers choose MZed Pro").
- **Pricing cards** - Two side-by-side cards replace comparison table (both plans have identical features, so table was redundant). Monthly anchors left, annual right with gold border + "Best Value — Save X%" dynamic badge. Shared feature list (6 items in 2-col grid) below cards. Trust signal with educator avatars at bottom.

## Section Background Flow
```
Hero             → dark (video overlay)
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
