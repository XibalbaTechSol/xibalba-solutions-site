document.addEventListener('DOMContentLoaded', () => {
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');

    if (hamburger && navLinks) {
        // Initialize accessibility attributes
        if (!navLinks.id) {
            navLinks.id = 'mobile-nav';
        }
        if (!hamburger.hasAttribute('aria-controls')) {
            hamburger.setAttribute('aria-controls', navLinks.id);
        }
        if (!hamburger.hasAttribute('aria-expanded')) {
            hamburger.setAttribute('aria-expanded', 'false');
        }

        hamburger.addEventListener('click', () => {
            const isActive = navLinks.classList.toggle('active');
            hamburger.classList.toggle('active');
            hamburger.setAttribute('aria-expanded', isActive);
        });
    }
});
