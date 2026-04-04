document.addEventListener('DOMContentLoaded', () => {
    console.log("Xibalba Solutions: Sovereign Obsidian Edition loaded.");
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');
    const themeToggle = document.querySelector('#theme-toggle');

    // Hamburger Menu
    if (hamburger && navLinks) {
        hamburger.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            hamburger.classList.toggle('active');
            const isActive = hamburger.classList.contains('active');
            hamburger.setAttribute('aria-expanded', isActive ? 'true' : 'false');
        });
    }

    // Theme Toggle (Obsidian Default)
    if (themeToggle) {
        // Initial setup
        const savedTheme = localStorage.getItem('theme') || 'obsidian';
        if (savedTheme === 'light') {
            document.body.classList.add('theme-light');
        }

        themeToggle.addEventListener('click', () => {
            document.body.classList.toggle('theme-light');
            const theme = document.body.classList.contains('theme-light') ? 'light' : 'obsidian';
            localStorage.setItem('theme', theme);
            console.log(`Transmission mode switched: ${theme}`);
        });
    }
});
