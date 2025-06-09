document.addEventListener("DOMContentLoaded", function() {
    // Ensure Fancybox is loaded
    if (typeof Fancybox !== 'undefined') {
      Fancybox.bind("[data-fancybox]", {
        iframe: {
          css: {
            width: '100%',
            height: '45vw',
            maxWidth: '960px',
            maxHeight: '540px',
            borderRadius: '8px',
            backgroundColor: 'black',
          }
        }
      });
    } else {
      console.error("Fancybox is not loaded");
    }
  });