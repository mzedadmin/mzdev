/**
 * Scroll Reveal Animation System
 * Remove the <script> tag in default.html to disable.
 *
 * Usage:
 *   data-reveal              — fade-up the element itself
 *   data-reveal-children     — fade-up + stagger direct children
 *   data-reveal-delay="100"  — stagger interval in ms (default 100)
 *   data-reveal-max-delay    — max stagger cap in ms (default 600)
 */
(function () {
  var els = document.querySelectorAll('[data-reveal], [data-reveal-children]');

  // Reduced motion or no IntersectionObserver — reveal immediately
  if (
    window.matchMedia('(prefers-reduced-motion: reduce)').matches ||
    !('IntersectionObserver' in window)
  ) {
    els.forEach(function (el) { el.classList.add('is-revealed'); });
    return;
  }

  function onReveal(entries, observer) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) return;

      var el = entry.target;

      // Set stagger delays on direct children before revealing
      if (el.hasAttribute('data-reveal-children')) {
        var interval = parseInt(el.getAttribute('data-reveal-delay'), 10) || 100;
        var maxDelay = parseInt(el.getAttribute('data-reveal-max-delay'), 10) || 600;
        var children = el.children;
        for (var i = 0; i < children.length; i++) {
          children[i].style.setProperty('--reveal-delay', Math.min(i * interval, maxDelay) + 'ms');
        }
      }

      el.classList.add('is-revealed');
      observer.unobserve(el);
    });
  }

  var observer = new IntersectionObserver(onReveal, {
    rootMargin: '0px 0px -10% 0px',
    threshold: 0
  });

  els.forEach(function (el) { observer.observe(el); });

  // Reveal any remaining elements when user scrolls near the bottom
  // (rootMargin creates a dead zone at the viewport bottom)
  function revealRemaining() {
    var atBottom = (window.innerHeight + window.scrollY) >= (document.body.scrollHeight - 100);
    if (atBottom) {
      els.forEach(function (el) {
        if (!el.classList.contains('is-revealed')) {
          if (el.hasAttribute('data-reveal-children')) {
            var interval = parseInt(el.getAttribute('data-reveal-delay'), 10) || 100;
            var maxDelay = parseInt(el.getAttribute('data-reveal-max-delay'), 10) || 600;
            var children = el.children;
            for (var i = 0; i < children.length; i++) {
              children[i].style.setProperty('--reveal-delay', Math.min(i * interval, maxDelay) + 'ms');
            }
          }
          el.classList.add('is-revealed');
          observer.unobserve(el);
        }
      });
      window.removeEventListener('scroll', revealRemaining);
    }
  }
  window.addEventListener('scroll', revealRemaining, { passive: true });
})();
