document.addEventListener('DOMContentLoaded', () => {
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');

    if (hamburger && navLinks) {
        // Accessibility initialization
        if (!navLinks.id) {
            navLinks.id = 'mobile-nav';
        }

        // Ensure aria-controls points to the correct element ID
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
