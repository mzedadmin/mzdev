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
  headline: "Stop Searching YouTube. Start Learning Now."
  subtext: "Become a better filmmaker today..."
  cta_text: "Join MZed Pro"
  cta_link: "#plan"
  risk_text: "7-day money-back guarantee on annual plans. Cancel monthly anytime."
catalog:
  topper: "Course Library"
  title: "All the courses you need to become a master filmmaker"
  text: "Over 800 lessons featuring trusted..."
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

### Homepage Includes
| Include | Purpose |
|---|---|
| `trusted_by.html` | Scrolling logo bar of trusted brands |
| `stats_strip.html` | 4 key numbers: Courses, Lessons, Hours, Value (course count is dynamic from collection) |
| `course_catalog.html` | Netflix-style horizontal-scroll rows grouped by topic from `_data/course_categories.yml` |
| `course_thumb.html` | Lightweight thumbnail card: image + title + educator |
| `educator_showcase.html` | Top 8 educators from collection (sorted by position) |
| `educator_card_mini.html` | Circular photo + name + subtitle card |
| `cta_banner.html` | Full-width red CTA with risk-reduction text |
| `mzed_pricing.html` | Comparison pricing table with Monthly/Annual columns |

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

- **Single CTA in hero** - Research shows multiple CTAs reduce conversion. One "Join MZed Pro" button with risk-reduction text underneath.
- **Risk-reduction text** at every CTA point (hero, CTA banner, pricing) - "7-day money-back guarantee" / "Cancel anytime" reduces purchase anxiety.
- **Stats strip** instead of large feature sections - Dense number presentation is more impactful and gets visitors to the course catalog faster.
- **Streaming-platform catalog** - Netflix-style horizontal scroll shows breadth of library without overwhelming. Pure CSS scroll-snap, no JS carousel.
- **Real educator cards** instead of static background image - Actual faces and names build more trust than a generic photo.
- **CTA banner after trust section** - Placed after video testimonial + written reviews for maximum trust-to-action conversion.

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
