// Course filtering and sorting functionality
document.addEventListener('DOMContentLoaded', function() {
  var filterButtons = document.querySelectorAll('.filter-btn:not(.reset-btn)');
  var resetButton = document.querySelector('.reset-btn');
  var sortButtons = document.querySelectorAll('.sort-btn');
  var cardGroup = document.querySelector('#courses .cs-card-group');
  var courseItems = Array.from(document.querySelectorAll('.course-card-item'));

  // State
  var activeFilters = new Set();
  var currentSort = 'popularity';

  // --- Filtering ---
  filterButtons.forEach(function(button) {
    button.addEventListener('click', function() {
      var topic = this.dataset.topic;

      if (this.classList.toggle('active')) {
        activeFilters.add(topic);
      } else {
        activeFilters.delete(topic);
      }

      // Deactivate "Show All" when a topic is active
      if (activeFilters.size > 0) {
        resetButton.classList.remove('active');
      } else {
        resetButton.classList.add('active');
      }

      updateCourseVisibility();
    });
  });

  if (resetButton) {
    resetButton.addEventListener('click', function() {
      activeFilters.clear();
      filterButtons.forEach(function(btn) { btn.classList.remove('active'); });
      resetButton.classList.add('active');
      updateCourseVisibility();
    });
  }

  function updateCourseVisibility() {
    courseItems.forEach(function(item) {
      var courseTopicsStr = item.getAttribute('data-topics') || '';
      var courseTopics = courseTopicsStr ? courseTopicsStr.split(',').map(function(t) { return t.trim(); }) : [];

      if (activeFilters.size === 0) {
        item.classList.remove('hidden');
      } else {
        var shouldShow = Array.from(activeFilters).some(function(filter) {
          return courseTopics.indexOf(filter) !== -1;
        });
        item.classList.toggle('hidden', !shouldShow);
      }
    });
  }

  // --- Sorting ---
  sortButtons.forEach(function(button) {
    button.addEventListener('click', function() {
      var sortType = this.dataset.sort;
      if (sortType === currentSort) return;

      currentSort = sortType;
      sortButtons.forEach(function(btn) { btn.classList.remove('active'); });
      this.classList.add('active');

      sortCourses(sortType);
    });
  });

  function sortCourses(sortType) {
    var sorted = courseItems.slice();

    if (sortType === 'popularity') {
      sorted.sort(function(a, b) {
        return parseInt(a.dataset.position, 10) - parseInt(b.dataset.position, 10);
      });
    } else if (sortType === 'release') {
      // Newest first by release_date
      sorted.sort(function(a, b) {
        var dateA = a.dataset.release || '1970-01-01';
        var dateB = b.dataset.release || '1970-01-01';
        return dateB < dateA ? -1 : dateB > dateA ? 1 : 0;
      });
    } else if (sortType === 'alpha') {
      sorted.sort(function(a, b) {
        var titleA = (a.dataset.title || '').toLowerCase();
        var titleB = (b.dataset.title || '').toLowerCase();
        return titleA < titleB ? -1 : titleA > titleB ? 1 : 0;
      });
    }

    // Re-append in sorted order (preserves filter/sort containers since they aren't in the array)
    sorted.forEach(function(item) {
      cardGroup.appendChild(item);
    });
  }
});
