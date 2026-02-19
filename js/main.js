document.addEventListener('DOMContentLoaded', () => {
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');

    if (hamburger && navLinks) {
        hamburger.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            hamburger.classList.toggle('active');
        });
    }

    // Add loading state to forms
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        // Only target forms that have an action (standard submission) to avoid interfering with SPA-like forms
        if (form.getAttribute('action')) {
            form.addEventListener('submit', (e) => {
                const btn = form.querySelector('button[type="submit"]');
                if (btn && !btn.disabled) {
                    // Store original text if needed, but for now just change it
                    btn.innerText = 'Sending...';
                    btn.disabled = true;
                    btn.style.opacity = '0.7';
                    btn.style.cursor = 'wait';
                }
            });
        }
    });
});
