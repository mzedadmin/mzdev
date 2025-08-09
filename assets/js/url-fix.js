// Fix absolute URLs for GitHub Pages subdirectory deployment
(function() {
    const baseUrl = '/mzdev';
    
    function fixUrls() {
        // Fix all links starting with /
        const links = document.querySelectorAll('a[href^="/"]');
        links.forEach(function(link) {
            const href = link.getAttribute('href');
            if (href && !href.startsWith(baseUrl) && !href.startsWith('//')) {
                link.setAttribute('href', baseUrl + href);
            }
        });
        
        // Fix all images starting with /
        const images = document.querySelectorAll('img[src^="/"]');
        images.forEach(function(img) {
            const src = img.getAttribute('src');
            if (src && !src.startsWith(baseUrl) && !src.startsWith('//')) {
                img.setAttribute('src', baseUrl + src);
            }
        });
        
        // Fix all source elements (for picture/srcset)
        const sources = document.querySelectorAll('source[srcset^="/"]');
        sources.forEach(function(source) {
            const srcset = source.getAttribute('srcset');
            if (srcset && !srcset.startsWith(baseUrl) && !srcset.startsWith('//')) {
                source.setAttribute('srcset', baseUrl + srcset);
            }
        });
        
        // Fix CSS background images in style attributes
        const elementsWithBgImages = document.querySelectorAll('[style*="background-image"]');
        elementsWithBgImages.forEach(function(el) {
            const style = el.getAttribute('style');
            const updatedStyle = style.replace(/url\(['"]?(\/[^'")]+)['"]?\)/g, function(match, url) {
                if (!url.startsWith(baseUrl) && !url.startsWith('//')) {
                    return match.replace(url, baseUrl + url);
                }
                return match;
            });
            el.setAttribute('style', updatedStyle);
        });
    }
    
    // Run on page load
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', fixUrls);
    } else {
        fixUrls();
    }
})();