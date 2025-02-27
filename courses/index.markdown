---
title: Courses
permalink: "/courses/"
layout: default
description: Browse our full catalog of MZed courses taught by award-winning filmmakers
  and industry professionals.
canonical_url: https://www.mzed.com/courses
custom_css:
- "/assets/css/courses.css"
- "/assets/css/courses-index.css"
custom_js:
- "/assets/js/courses-index.js"
head: |
  <!-- Preload Fonts -->
  <link
    rel="preload"
    as="font"
    type="font/woff2"
    href="{{ '/assets/fonts/roboto-v29-latin-regular.woff2' | relative_url }}"
    crossorigin
  />
  <link
    rel="preload"
    as="font"
    type="font/woff2"
    href="{{ '/assets/fonts/roboto-v29-latin-700.woff2' | relative_url }}"
    crossorigin
  />
mzed_pro_section:
  topper: Access All the Courses
  title: Only Available with MZed Pro!
  description: Join the leading online education membership for filmmakers, and get
    instant access to our entire library.
  lessons_count: 750+
  lessons_label: Lessons
  courses_count: 57+
  courses_label: Courses
  educators_count: 50+
  educators_label: World-Class Educators
pricing:
  headline: Ready to Get Started with <span class="title-highlight">MZed Pro?</span>
  description: Make a commitment to becoming a better filmmaker, today. Seven-day
    money-back guarantee
  terms_link: https://www.mzed.com/terms-of-service#section-6
  terms_text: view full terms here
  monthly_title: Monthly Membership
  annual_title: Annual Membership
  price_label: Monthly price
  monthly_price: "$49/month"
  annual_price: "$29/month"
  billed_annually_text: "(billed annually)"
  monthly_cta_url: https://www.mzed.com/subscription/checkout?plan=monthly
  monthly_cta_text: Join Now
  annual_cta_url: https://www.mzed.com/subscription/checkout?plan=yearly
  annual_cta_text: Join Now
  features:
  - text: Unlimited access to all courses
  - text: Learn from Academy Award and Pulitzer Prize winning educators
  - text: Offline download and viewing with the MZed iOS app
---

<main id="main">
  <!-- ============================================ -->
  <!--                Courses                       -->
  <!-- ============================================ -->

  <section id="services-1169">
    <div class="cs-container">
      <div class="cs-content">
        <span class="cs-topper">MZed Library</span>
        <div class="cs-title">Our Courses</div>
        <p class="cs-text">
          MZed course topics include all areas of filmmaking including cinematography,
          directing, editing, screenwriting, lighting, color grading, and more.
        </p>
      </div>
      <ul class="cs-card-group">
        <!-- Topics -->
        <div class="filter-container">
          <div class="filter-title">Filter Courses by Topic</div>
          <div class="filter-buttons">
            <button class="filter-btn" data-topic="audio">Audio</button>
            <button class="filter-btn" data-topic="cinematography">Cinematography</button>
            <button class="filter-btn" data-topic="color-grading">Color Grading</button>
            <button class="filter-btn" data-topic="directing">Directing</button>
            <button class="filter-btn" data-topic="editing">Editing</button>
            <button class="filter-btn" data-topic="filmmaking">Filmmaking</button>
            <button class="filter-btn" data-topic="lighting">Lighting</button>
            <button class="filter-btn" data-topic="photography">Photography</button>
            <button class="filter-btn" data-topic="producing">Producing</button>
            <button class="filter-btn" data-topic="screenwriting">Screenwriting</button>
            <button class="filter-btn" data-topic="visual-storytelling">
              Visual Storytelling
            </button>
            <button class="filter-btn" data-topic="podcasting">Podcasting</button>
            <button class="filter-btn reset-btn">Reset Filters</button>
          </div>
        </div>

        {% assign sorted_courses = site.courses | sort: "position", "last" %}
        {% for course in sorted_courses %}
          <li class="cs-item" data-topics="{{ course.topics | join: ',' }}">
            <picture class="cs-picture">
              <!--Mobile Image-->
              <source
                media="(max-width: 600px)"
                srcset="{{ course.image | relative_url }}"
              />
              <!--Tablet and above Image-->
              <source
                media="(min-width: 601px)"
                srcset="{{ course.image | relative_url }}"
              />
              <img
                loading="lazy"
                decoding="async"
                src="{{ course.image | relative_url }}"
                alt="{{ course.title }} by {{ course.educator }}"
                width="413"
                height="240"
                aria-hidden="true"
              />
            </picture>
            <div class="cs-info">
              <h3 class="cs-h3">{{ course.title }}</h3>
              <h4 class="cs-topper cs-educator">{{ course.educator }}</h4>
              <p class="cs-item-text">
                {{ course.description }}
              </p>
              <a
                href="{{ course.url | relative_url }}"
                class="cs-link"
              >
                Watch this course
                <img
                  class="cs-arrow"
                  loading="lazy"
                  decoding="async"
                  src="{{ '/assets/icons/red-arrow-right.svg' | relative_url }}"
                  alt="icon"
                  width="20"
                  height="20"
                  aria-hidden="true"
                />
              </a>
            </div>
            <div class="course-card-stats">
              {% if course.lessons %}
                <span class="course-card-stat">
                  <span class="course-card-stat-text">{{ course.lessons }} Lessons</span>
                </span>
              {% endif %}
              
              {% if course.runtime %}
                <span class="course-card-stat">
                  <span class="course-card-stat-text">{{ course.runtime }}</span>
                </span>
              {% endif %}
            </div>
          </li>
        {% endfor %}
      </ul>
    </div>
  </section>

  <!-- MZed Pro Section -->
  {% include mzed_pro_section.html section=page.mzed_pro_section %}

  <!-- Pricing Section -->
  {% include pricing_section.html pricing=page.pricing %}
</main>

