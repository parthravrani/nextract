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

    legalDropdownButton.addEventListener('click', (event) => {
        event.stopPropagation();
        legalDropdownMenu.classList.toggle('hidden');
    });

    window.addEventListener('click', (event) => {
        if (!legalDropdownContainer.contains(event.target)) {
            legalDropdownMenu.classList.add('hidden');
        }
    });

    mobileMenuButton.addEventListener('click', () => mobileMenu.classList.remove('hidden'));
    closeMenuButton.addEventListener('click', () => mobileMenu.classList.add('hidden'));

    mobileLegalButton.addEventListener('click', () => {
        mobileLegalSubmenu.classList.toggle('hidden');
        mobileLegalIcon.classList.toggle('ri-add-line');
        mobileLegalIcon.classList.toggle('ri-subtract-line');
    });
    
    mobileNavLinks.forEach(link => {
        link.addEventListener('click', () => {
            mobileMenu.classList.add('hidden');
        });
    });

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) entry.target.classList.add('visible');
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
});