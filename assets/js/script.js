// Scroll animations
document.addEventListener('DOMContentLoaded', function() {
    // Intersection Observer for scroll animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observe all elements with reveal class
    const revealElements = document.querySelectorAll('.reveal, .card-style, section > div');
    revealElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
        observer.observe(el);
    });

    // Header scroll effect
    const header = document.getElementById('main-header');
    if (header) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        });
    }

    // Mobile menu toggle
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');
    const closeMenuButton = document.getElementById('close-menu-button');

    if (mobileMenuButton && mobileMenu) {
        mobileMenuButton.addEventListener('click', function() {
            mobileMenu.classList.remove('hidden');
        });
    }

    if (closeMenuButton && mobileMenu) {
        closeMenuButton.addEventListener('click', function() {
            mobileMenu.classList.add('hidden');
        });
    }

    // Legal dropdown toggle (desktop)
    const legalDropdownButton = document.getElementById('legal-dropdown-button');
    const legalDropdownMenu = document.getElementById('legal-dropdown-menu');
    
    if (legalDropdownButton && legalDropdownMenu) {
        legalDropdownButton.addEventListener('click', function(e) {
            e.stopPropagation();
            legalDropdownMenu.classList.toggle('hidden');
        });

        // Close dropdown when clicking outside
        document.addEventListener('click', function(e) {
            if (!legalDropdownButton.contains(e.target) && !legalDropdownMenu.contains(e.target)) {
                legalDropdownMenu.classList.add('hidden');
            }
        });
    }

    // Mobile legal dropdown toggle
    const mobileLegalButton = document.getElementById('mobile-legal-button');
    const mobileLegalSubmenu = document.getElementById('mobile-legal-submenu');
    const mobileLegalIcon = document.getElementById('mobile-legal-icon');

    if (mobileLegalButton && mobileLegalSubmenu) {
        mobileLegalButton.addEventListener('click', function() {
            mobileLegalSubmenu.classList.toggle('hidden');
            if (mobileLegalIcon) {
                mobileLegalIcon.classList.toggle('rotate-45');
            }
        });
    }

    // Form validation
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const inputs = form.querySelectorAll('input[required], textarea[required]');
            let isValid = true;

            inputs.forEach(input => {
                if (!input.value.trim()) {
                    isValid = false;
                    input.classList.add('error');
                } else {
                    input.classList.remove('error');
                    input.classList.add('success');
                }
            });

            if (!isValid) {
                e.preventDefault();
            }
        });
    });

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href !== '#' && href.length > 1) {
                const target = document.querySelector(href);
                if (target) {
                    e.preventDefault();
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });
});
