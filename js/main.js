document.addEventListener('DOMContentLoaded', () => {
    console.log('Xibalba Solutions v2.0 — Sovereign Obsidian loaded.');

    // ── Hamburger Menu ──
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');
    const navOverlay = document.querySelector('.nav-overlay');

    function closeMenu() {
        navLinks?.classList.remove('active');
        hamburger?.classList.remove('active');
        navOverlay?.classList.remove('active');
        hamburger?.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
    }

    function openMenu() {
        navLinks?.classList.add('active');
        hamburger?.classList.add('active');
        navOverlay?.classList.add('active');
        hamburger?.setAttribute('aria-expanded', 'true');
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
            
            // Show loading state
            btn.textContent = 'Synchronizing...';
            btn.disabled = true;

            const formData = new FormData(contactForm);
            
            fetch('/contact', {
                method: 'POST',
                body: new URLSearchParams(formData)
            })
            .then(response => {
                if (response.ok) {
                    btn.textContent = 'Message Sent ✓';
                    btn.style.background = 'linear-gradient(135deg, #00FF88 0%, #00F2FF 100%)';
                    contactForm.reset();
                } else {
                    throw new Error('Server Error');
                }
            })
            .catch(err => {
                console.error('Contact error:', err);
                btn.textContent = 'Relay Failed';
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

    // ── Live Protocol Simulation ──
    const metrics = {
        entropy: { el: document.querySelector('#metric-entropy .metric-trend'), base: 0.4, prefix: '↑ ' },
        grounding: { el: document.querySelector('#metric-grounding .metric-trend'), base: 0, prefix: '~ ', text: 'STABLE' },
        sacrifice: { el: document.querySelector('#metric-sacrifice .metric-trend'), base: 1.2, prefix: '↑ ' }
    };

    function updateLiveMetrics() {
        if (metrics.entropy.el) {
            const val = (metrics.entropy.base + (Math.random() * 0.1 - 0.05)).toFixed(1);
            metrics.entropy.el.textContent = `${metrics.entropy.prefix}${val}%`;
        }
        if (metrics.grounding.el) {
            const chance = Math.random();
            if (chance > 0.8) {
                metrics.grounding.el.textContent = '↑ 0.1%';
                metrics.grounding.el.className = 'metric-trend text-success';
            } else if (chance < 0.2) {
                metrics.grounding.el.textContent = '↓ 0.1%';
                metrics.grounding.el.className = 'metric-trend text-error';
            } else {
                metrics.grounding.el.textContent = '~ STABLE';
                metrics.grounding.el.className = 'metric-trend text-warning';
            }
        }
        if (metrics.sacrifice.el) {
            const val = (metrics.sacrifice.base + (Math.random() * 0.2 - 0.1)).toFixed(1);
            metrics.sacrifice.el.textContent = `${metrics.sacrifice.prefix}${val}%`;
        }
    }

    if (metrics.entropy.el || metrics.grounding.el || metrics.sacrifice.el) {
        setInterval(updateLiveMetrics, 3000);
    }

    // ── Status Text Typing Effect ──
    const statusTextEl = document.querySelector('.status-text');
    if (statusTextEl) {
        const texts = [
            'Protocol Node v8.4.2 — ACTIVE',
            'L2 Settlement — VERIFIED',
            'Sovereign Identity — ENCRYPTED',
            'Entropy Buffer — STABLE'
        ];
        let index = 0;
        
        function rotateStatusText() {
            statusTextEl.style.opacity = '0';
            setTimeout(() => {
                index = (index + 1) % texts.length;
                statusTextEl.textContent = texts[index];
                statusTextEl.style.opacity = '1';
            }, 500);
        }
        
        setInterval(rotateStatusText, 5000);
    }
});
