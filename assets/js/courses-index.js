// Course filtering functionality
document.addEventListener('DOMContentLoaded', function() {
  const filterButtons = document.querySelectorAll('.filter-btn');
  const resetButton = document.querySelector('.reset-btn');
  const courseItems = document.querySelectorAll('.cs-item');

  // Keep track of active filters
  let activeFilters = new Set();

  // Add click event listener to each filter button
  filterButtons.forEach((button) => {
    button.addEventListener('click', function () {
      const topic = this.dataset.topic;

      // Toggle button active state and update activeFilters
      if (this.classList.toggle('active')) {
        activeFilters.add(topic);
      } else {
        activeFilters.delete(topic);
      }

      updateCourseVisibility();
    });
  });

  // Reset button functionality
  if (resetButton) {
    resetButton.addEventListener('click', function () {
      activeFilters.clear();
      filterButtons.forEach((btn) => btn.classList.remove('active'));
      updateCourseVisibility();
    });
  }

  // Function to update course visibility based on active filters
  function updateCourseVisibility() {
    courseItems.forEach((item) => {
      const courseTopicsStr = item.getAttribute('data-topics') || '';
      const courseTopics = courseTopicsStr
        ? courseTopicsStr.split(',').map((t) => t.trim())
        : [];

      if (activeFilters.size === 0) {
        item.classList.remove('hidden');
      } else {
        const shouldShow = [...activeFilters].some((filter) => courseTopics.includes(filter));

        if (shouldShow) {
          item.classList.remove('hidden');
        } else {
          item.classList.add('hidden');
        }
      }
    });
  }
}); 