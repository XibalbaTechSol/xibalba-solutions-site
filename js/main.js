document.addEventListener('DOMContentLoaded', () => {
    // Navigation Logic
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');

    if (hamburger && navLinks) {
        hamburger.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            hamburger.classList.toggle('active');
        });
    }

    // Form Submission Loading State
    const forms = document.querySelectorAll('form[action]');
    forms.forEach(form => {
        form.addEventListener('submit', (e) => {
            // Find the submit button
            const submitBtn = form.querySelector('button[type="submit"]');

            if (submitBtn) {
                // Update UI to show loading
                submitBtn.innerText = 'Sending...';
                submitBtn.disabled = true;
                submitBtn.style.opacity = '0.7';
                submitBtn.style.cursor = 'not-allowed';
            }
        });
    });
});
