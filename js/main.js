document.addEventListener('DOMContentLoaded', () => {
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');

    if (hamburger && navLinks) {
        // Initialize aria-expanded state based on initial active class
        const isActive = navLinks.classList.contains('active');
        hamburger.setAttribute('aria-expanded', isActive);

        hamburger.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            const isNowActive = hamburger.classList.toggle('active');
            hamburger.setAttribute('aria-expanded', isNowActive);
        });
    }
});
