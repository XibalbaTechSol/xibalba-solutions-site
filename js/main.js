// The static pages deploy to GitHub Pages; this backend (server.py's /contact) deploys
// separately to Render, since Pages can't run a Python process. Keep this in sync with
// contact.html's <form action> and server.py's ALLOWED_ORIGIN.
const CONTACT_ENDPOINT = 'https://xibalba-solutions-site.onrender.com/contact';

document.addEventListener('DOMContentLoaded', () => {
    console.log('Xibalba Solutions v2.0 — Sovereign Obsidian loaded.');
    // ── Hamburger Menu ──
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');
    const navOverlay = document.querySelector('.nav-overlay');

    function closeMenu() {
        navLinks?.classList.remove('active');
        hamburger?.classList.remove('active');
        hamburger?.setAttribute('aria-expanded', 'false');
        navOverlay?.classList.remove('active');
        document.body.style.overflow = '';
    }

    function openMenu() {
        navLinks?.classList.add('active');
        hamburger?.classList.add('active');
        hamburger?.setAttribute('aria-expanded', 'true');
        navOverlay?.classList.add('active');
        document.body.style.overflow = 'hidden';
    }

    if (hamburger && navLinks) {
        hamburger.addEventListener('click', () => {
            if (navLinks.classList.contains('active')) {
                closeMenu();
            } else {
                openMenu();
            }
        });
    }

    if (navOverlay) {
        navOverlay.addEventListener('click', closeMenu);
    }

    // Close menu on nav link click (mobile)
    document.querySelectorAll('.nav-links a').forEach(link => {
        link.addEventListener('click', closeMenu);
    });

    // ── Navbar scroll effect ──
    const nav = document.querySelector('nav');
    if (nav) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 40) {
                nav.classList.add('scrolled');
            } else {
                nav.classList.remove('scrolled');
            }
        }, { passive: true });
    }

    // ── Scroll-Spy (active nav links) ──
    const sections = document.querySelectorAll('section[id]');
    const navAnchors = document.querySelectorAll('.nav-links a[href^="#"]');

    if (sections.length && navAnchors.length) {
        const observerOptions = {
            root: null,
            rootMargin: '-30% 0px -60% 0px',
            threshold: 0
        };

        const scrollObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const id = entry.target.getAttribute('id');
                    navAnchors.forEach(a => {
                        a.classList.toggle('active', a.getAttribute('href') === `#${id}`);
                    });
                }
            });
        }, observerOptions);

        sections.forEach(section => scrollObserver.observe(section));
    }

    // ── Intersection Observer for scroll animations ──
    const animateElements = document.querySelectorAll('.animate-in');
    if (animateElements.length) {
        const animObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    animObserver.unobserve(entry.target);
                }
            });
        }, {
            root: null,
            rootMargin: '0px',
            threshold: 0.1
        });

        animateElements.forEach(el => animObserver.observe(el));
    }

    // ── Smooth scroll for anchor links ──
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            const targetEl = document.querySelector(targetId);
            if (targetEl) {
                e.preventDefault();
                const navHeight = document.querySelector('nav')?.offsetHeight || 80;
                const targetPosition = targetEl.getBoundingClientRect().top + window.pageYOffset - navHeight;
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // ── Contact form handler ──
    const contactForm = document.querySelector('#contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            
            const btn = contactForm.querySelector('button[type="submit"]');
            const originalText = btn.textContent;
            const formStatus = contactForm.querySelector("#form-status");
            
            // Show loading state
            btn.textContent = 'Synchronizing...';
            btn.disabled = true;

            const formData = new FormData(contactForm);
            
            fetch(CONTACT_ENDPOINT, {
                method: 'POST',
                body: new URLSearchParams(formData)
            })
            .then(response => {
                if (response.ok) {
                    btn.textContent = "Message Sent ✓";
                    if (formStatus) formStatus.textContent = "Your message was sent successfully.";
                    btn.style.background = 'linear-gradient(135deg, #00FF88 0%, #00F2FF 100%)';
                    contactForm.reset();
                } else {
                    throw new Error('Server Error');
                }
            })
            .catch(err => {
                console.error('Contact error:', err);
                btn.textContent = "Relay Failed";
                if (formStatus) formStatus.textContent = "We could not send your message. Please try again or email us directly.";
                btn.style.background = 'var(--color-error)';
            })
            .finally(() => {
                setTimeout(() => {
                    btn.textContent = originalText;
                    btn.style.background = '';
                    btn.disabled = false;
                }, 3000);
            });
        });
    }

    // ── Current year in footer ──
    document.querySelectorAll('.current-year').forEach(el => {
        el.textContent = new Date().getFullYear();
    });

    // Note: this file previously simulated fabricated "live" protocol metrics and a rotating
    // status-text ticker (e.g. "Protocol Node v8.4.2 — ACTIVE") for DOM elements that no longer
    // exist in index.html -- that content was removed as unverifiable/misleading. Removed the
    // dead JS along with it rather than leaving it as inert but confusing leftover code.
});
