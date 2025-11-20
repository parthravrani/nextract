document.addEventListener('DOMContentLoaded', () => {
    const legalDropdownButton = document.getElementById('legal-dropdown-button');
    const legalDropdownMenu = document.getElementById('legal-dropdown-menu');
    const legalDropdownContainer = document.getElementById('legal-dropdown-container');
    const mobileMenu = document.getElementById('mobile-menu');
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const closeMenuButton = document.getElementById('close-menu-button');
    const mobileLegalButton = document.getElementById('mobile-legal-button');
    const mobileLegalSubmenu = document.getElementById('mobile-legal-submenu');
    const mobileLegalIcon = document.getElementById('mobile-legal-icon');
    const mobileNavLinks = document.querySelectorAll('.mobile-nav-link');
    const accordionItems = document.querySelectorAll('.accordion-item');

    // Accordion functionality (only if accordion items exist)
    accordionItems.forEach(item => {
        const header = item.querySelector('.accordion-header');
        if (header) {
            header.addEventListener('click', () => {
                // Close other open items
                accordionItems.forEach(otherItem => {
                    if (otherItem !== item && otherItem.classList.contains('active')) {
                        otherItem.classList.remove('active');
                        const otherIcon = otherItem.querySelector('.accordion-icon');
                        if (otherIcon) {
                            otherIcon.classList.replace('ri-subtract-line', 'ri-add-line');
                        }
                    }
                });

                // Toggle the clicked item
                item.classList.toggle('active');
                const icon = item.querySelector('.accordion-icon');
                if (icon) {
                    if (item.classList.contains('active')) {
                        icon.classList.replace('ri-add-line', 'ri-subtract-line');
                    } else {
                        icon.classList.replace('ri-subtract-line', 'ri-add-line');
                    }
                }
            });
        }
    });

    // Legal dropdown functionality (only if elements exist)
    if (legalDropdownButton && legalDropdownMenu) {
        legalDropdownButton.addEventListener('click', (event) => {
            event.stopPropagation();
            legalDropdownMenu.classList.toggle('hidden');
        });
    }

    if (legalDropdownContainer && legalDropdownMenu) {
        window.addEventListener('click', (event) => {
            if (!legalDropdownContainer.contains(event.target)) {
                legalDropdownMenu.classList.add('hidden');
            }
        });
    }

    // Mobile menu functionality (only if elements exist)
    if (mobileMenuButton && mobileMenu) {
        mobileMenuButton.addEventListener('click', () => mobileMenu.classList.remove('hidden'));
    }

    if (closeMenuButton && mobileMenu) {
        closeMenuButton.addEventListener('click', () => mobileMenu.classList.add('hidden'));
    }

    if (mobileLegalButton && mobileLegalSubmenu && mobileLegalIcon) {
        mobileLegalButton.addEventListener('click', () => {
            mobileLegalSubmenu.classList.toggle('hidden');
            mobileLegalIcon.classList.toggle('ri-add-line');
            mobileLegalIcon.classList.toggle('ri-subtract-line');
        });
    }
    
    mobileNavLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (mobileMenu) {
                mobileMenu.classList.add('hidden');
            }
        });
    });

    // Scroll reveal animation
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                
                // Animate progress bar when visible
                const progressBar = entry.target.querySelector('.progress-bar');
                if (progressBar) {
                    setTimeout(() => {
                        progressBar.style.width = '100%';
                    }, 300);
                }
                
                // Animate counters when visible
                const counters = entry.target.querySelectorAll('.counter');
                counters.forEach(counter => {
                    const target = parseInt(counter.getAttribute('data-target')) || 0;
                    if (target > 0 && !counter.classList.contains('counted')) {
                        counter.classList.add('counted');
                        animateCounter(counter, target);
                    }
                });
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
    
    // Counter animation function
    function animateCounter(element, target) {
        const duration = 2000; // 2 seconds
        const increment = target / (duration / 16); // 60fps
        let current = 0;
        
        const updateCounter = () => {
            current += increment;
            if (current < target) {
                const displayValue = Math.floor(current);
                if (target >= 100) {
                    element.textContent = displayValue.toLocaleString() + 'M+';
                } else if (target >= 10) {
                    element.textContent = displayValue + '+';
                } else {
                    element.textContent = displayValue.toFixed(1) + '%';
                }
                requestAnimationFrame(updateCounter);
            } else {
                if (target >= 100) {
                    element.textContent = target.toLocaleString() + 'M+';
                } else if (target >= 10) {
                    element.textContent = target + '+';
                } else {
                    element.textContent = target.toFixed(1) + '%';
                }
            }
        };
        
        updateCounter();
    }
    
    // Animate stats on page load if they're already visible
    const statCards = document.querySelectorAll('.stat-card');
    statCards.forEach(card => {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.transform = 'scale(1.05)';
                    setTimeout(() => {
                        entry.target.style.transform = 'scale(1)';
                    }, 200);
                }
            });
        }, { threshold: 0.5 });
        observer.observe(card);
    });
    
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href !== '#' && href.length > 1) {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                    // Close mobile menu if open
                    if (mobileMenu && !mobileMenu.classList.contains('hidden')) {
                        mobileMenu.classList.add('hidden');
                    }
                }
            }
        });
    });
    
    // Navbar scroll effect
    const header = document.getElementById('main-header');
    const scrollIndicator = document.getElementById('scroll-indicator');
    let lastScroll = 0;
    
    if (header && scrollIndicator) {
        window.addEventListener('scroll', () => {
            const currentScroll = window.pageYOffset;
            const documentHeight = document.documentElement.scrollHeight - window.innerHeight;
            const scrollPercentage = (currentScroll / documentHeight) * 100;
            
            // Update scroll indicator
            scrollIndicator.style.width = scrollPercentage + '%';
            
            // Add scrolled class for shadow effect
            if (currentScroll > 10) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
            
            lastScroll = currentScroll;
        });
    }
    
    // Enhanced dropdown menu animation
    if (legalDropdownMenu) {
        legalDropdownButton.addEventListener('mouseenter', () => {
            legalDropdownMenu.classList.remove('hidden');
            legalDropdownMenu.classList.add('animate-fade-in');
        });
        
        legalDropdownContainer.addEventListener('mouseleave', () => {
            setTimeout(() => {
                if (!legalDropdownContainer.matches(':hover')) {
                    legalDropdownMenu.classList.add('hidden');
                }
            }, 200);
        });
    }
    
    // Form validation and feedback
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        const inputs = form.querySelectorAll('input[type="text"], input[type="email"], textarea');
        inputs.forEach(input => {
            input.addEventListener('blur', function() {
                if (this.value.trim() !== '') {
                    this.classList.add('success');
                    this.classList.remove('error');
                } else if (this.hasAttribute('required')) {
                    this.classList.add('error');
                    this.classList.remove('success');
                }
            });
            
            input.addEventListener('input', function() {
                if (this.classList.contains('error') && this.value.trim() !== '') {
                    this.classList.remove('error');
                    this.classList.add('success');
                }
            });
        });
        
        form.addEventListener('submit', function(e) {
            let isValid = true;
            inputs.forEach(input => {
                if (input.hasAttribute('required') && input.value.trim() === '') {
                    input.classList.add('error');
                    isValid = false;
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                // Show error message
                const errorMsg = document.createElement('p');
                errorMsg.className = 'text-red-400 text-sm mt-2';
                errorMsg.textContent = 'Please fill in all required fields.';
                if (!form.querySelector('.text-red-400')) {
                    form.appendChild(errorMsg);
                }
            }
        });
    });
    
    // Add floating labels effect
    const formInputs = document.querySelectorAll('.form-input');
    formInputs.forEach(input => {
        input.addEventListener('focus', function() {
            this.parentElement.classList.add('focused');
        });
        input.addEventListener('blur', function() {
            if (this.value === '') {
                this.parentElement.classList.remove('focused');
            }
        });
    });
});