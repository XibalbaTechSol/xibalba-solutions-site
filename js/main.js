document.addEventListener('DOMContentLoaded', () => {
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');

    if (hamburger && navLinks) {
        hamburger.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            hamburger.classList.toggle('active');
            // Accessibility: Update aria-expanded
            const isExpanded = hamburger.classList.contains('active');
            hamburger.setAttribute('aria-expanded', isExpanded);
        });
    }

    // UX Improvement: Loading state for form submissions
    document.addEventListener('submit', (e) => {
        const form = e.target;
        // Only target forms that perform a standard navigation/POST (have an action attribute)
        // This avoids interfering with SPA-style forms that handle submission via JS
        if (form.tagName === 'FORM' && form.getAttribute('action')) {
            const submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn && !submitBtn.disabled) {
                // Store original text to restore if needed (e.g. on bfcache restore)
                submitBtn.dataset.originalText = submitBtn.innerText;
                submitBtn.innerText = 'Sending...';
                submitBtn.style.width = `${submitBtn.offsetWidth}px`; // Prevent layout shift
                submitBtn.disabled = true;
            }
        }
    });

    // Restore button state when navigating back to the page
    window.addEventListener('pageshow', (event) => {
        // event.persisted indicates the page was loaded from the bfcache
        if (event.persisted) {
            document.querySelectorAll('button[type="submit"][disabled]').forEach(btn => {
                btn.disabled = false;
                if (btn.dataset.originalText) {
                    btn.innerText = btn.dataset.originalText;
                }
            });
        }
    });
});
