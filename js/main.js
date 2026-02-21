document.addEventListener('DOMContentLoaded', () => {
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');

    if (hamburger && navLinks) {
        hamburger.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            hamburger.classList.toggle('active');

            const isActive = navLinks.classList.contains('active');
            hamburger.setAttribute('aria-expanded', isActive);

            // Lock body scroll when menu is open
            document.body.style.overflow = isActive ? 'hidden' : '';
        });

        // Close menu when clicking a link
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navLinks.classList.remove('active');
                hamburger.classList.remove('active');
                hamburger.setAttribute('aria-expanded', 'false');
                document.body.style.overflow = '';
            });
        });
    }

    // Set aria-current="page" and active class for current page
    const currentPath = window.location.pathname;
    const links = document.querySelectorAll('.nav-links a');

    links.forEach(link => {
        const href = link.getAttribute('href');
        if (!href) return;

        // Match the link href with the current path
        const isMatch =
            currentPath.endsWith(href) ||
            (currentPath === '/' && href === 'index.html') ||
            (href === 'index.html' && currentPath.endsWith('/')) ||
            (currentPath.endsWith('/') && href === 'index.html');

        if (isMatch) {
            link.setAttribute('aria-current', 'page');
            link.classList.add('active');
        }
    });
});
