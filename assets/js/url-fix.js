// Fix absolute URLs for GitHub Pages subdirectory deployment
(function() {
    const baseUrl = '/mzdev';
    
    // Fix navigation links
    document.addEventListener('DOMContentLoaded', function() {
        const links = document.querySelectorAll('a[href^="/"]');
        links.forEach(function(link) {
            const href = link.getAttribute('href');
            // Only fix if it doesn't already start with baseUrl
            if (!href.startsWith(baseUrl)) {
                link.setAttribute('href', baseUrl + href);
            }
        });
        
        // Fix images
        const images = document.querySelectorAll('img[src^="/"], source[srcset^="/"]');
        images.forEach(function(img) {
            const src = img.getAttribute('src') || img.getAttribute('srcset');
            if (src && !src.startsWith(baseUrl)) {
                if (img.hasAttribute('src')) {
                    img.setAttribute('src', baseUrl + src);
                } else {
                    img.setAttribute('srcset', baseUrl + src);
                }
            }
        });
    });
})();