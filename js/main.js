document.addEventListener('DOMContentLoaded', () => {
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');

    if (hamburger && navLinks) {
        // Accessibility setup
        hamburger.setAttribute('aria-expanded', 'false');
        hamburger.setAttribute('aria-controls', 'mobile-nav');
        navLinks.id = 'mobile-nav';

        hamburger.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            const isActive = hamburger.classList.toggle('active');
            hamburger.setAttribute('aria-expanded', isActive);
        });
    }
});
