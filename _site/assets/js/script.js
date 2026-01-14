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

    // Header stays fixed - no hide/show on scroll
    const header = document.getElementById('main-header');
    if (header) {
        // Keep navbar always visible and fixed
        header.style.transform = 'translateY(0)';
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

    // Dropdown toggle (desktop) - handles all dropdowns
    const dropdownContainers = document.querySelectorAll('.dropdown-container');
    
    dropdownContainers.forEach(container => {
        const button = container.querySelector('.dropdown-button');
        const menu = container.querySelector('.dropdown-menu');
        
        if (button && menu) {
            button.addEventListener('click', function(e) {
                e.stopPropagation();
                
                // Close all other dropdowns
                dropdownContainers.forEach(otherContainer => {
                    if (otherContainer !== container) {
                        const otherMenu = otherContainer.querySelector('.dropdown-menu');
                        if (otherMenu) {
                            otherMenu.classList.add('hidden');
                        }
                    }
                });
                
                // Toggle current dropdown
                menu.classList.toggle('hidden');
            });
        }
    });

    // Close dropdowns when clicking outside
    document.addEventListener('click', function(e) {
        dropdownContainers.forEach(container => {
            const menu = container.querySelector('.dropdown-menu');
            if (menu && !container.contains(e.target)) {
                menu.classList.add('hidden');
            }
        });
    });

    // Mobile dropdown toggle - handles all mobile dropdowns
    const mobileDropdownContainers = document.querySelectorAll('.mobile-dropdown-container');
    
    mobileDropdownContainers.forEach(container => {
        const button = container.querySelector('.mobile-dropdown-button');
        const submenu = container.querySelector('.mobile-dropdown-submenu');
        const icon = button.querySelector('i');
        
        if (button && submenu) {
            button.addEventListener('click', function() {
                // Close all other mobile dropdowns
                mobileDropdownContainers.forEach(otherContainer => {
                    if (otherContainer !== container) {
                        const otherSubmenu = otherContainer.querySelector('.mobile-dropdown-submenu');
                        const otherIcon = otherContainer.querySelector('.mobile-dropdown-button i');
                        if (otherSubmenu) {
                            otherSubmenu.classList.add('hidden');
                        }
                        if (otherIcon) {
                            otherIcon.classList.remove('rotate-45');
                        }
                    }
                });
                
                // Toggle current dropdown
                submenu.classList.toggle('hidden');
                if (icon) {
                    icon.classList.toggle('rotate-45');
                }
            });
        }
    });

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

    // FAQ Accordion functionality
    const accordionItems = document.querySelectorAll('.accordion-item');
    accordionItems.forEach(item => {
        const header = item.querySelector('.accordion-header');
        const content = item.querySelector('.accordion-content');
        const icon = item.querySelector('.accordion-icon');
        
        if (header && content) {
            header.addEventListener('click', function() {
                const isActive = item.classList.contains('active');
                
                // Close all accordions
                accordionItems.forEach(otherItem => {
                    otherItem.classList.remove('active');
                });
                
                // Open clicked accordion if it wasn't active
                if (!isActive) {
                    item.classList.add('active');
                }
            });
        }
    });

    // Contact Modal functionality
    const chatButton = document.getElementById('chat-button');
    const contactModal = document.getElementById('contact-modal');
    const closeModal = document.getElementById('close-modal');
    const contactFormModal = document.getElementById('contact-form-modal');

    if (chatButton && contactModal) {
        // Open modal
        chatButton.addEventListener('click', function() {
            contactModal.classList.remove('hidden');
            document.body.style.overflow = 'hidden'; // Prevent background scrolling
        });

        // Close modal
        if (closeModal) {
            closeModal.addEventListener('click', function() {
                contactModal.classList.add('hidden');
                document.body.style.overflow = ''; // Restore scrolling
            });
        }

        // Close modal when clicking outside
        contactModal.addEventListener('click', function(e) {
            if (e.target === contactModal) {
                contactModal.classList.add('hidden');
                document.body.style.overflow = ''; // Restore scrolling
            }
        });

        // Close modal on Escape key
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && !contactModal.classList.contains('hidden')) {
                contactModal.classList.add('hidden');
                document.body.style.overflow = ''; // Restore scrolling
            }
        });

        // Handle form submission
        if (contactFormModal) {
            contactFormModal.addEventListener('submit', function(e) {
                // Form will submit normally via Formspree
                // After successful submission, you can close the modal
                // This is handled by Formspree's redirect or success message
                setTimeout(function() {
                    // Optional: Show success message or close modal after a delay
                    // contactModal.classList.add('hidden');
                    // document.body.style.overflow = '';
                }, 1000);
            });
        }
    }
});
