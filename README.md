# Nextract Jekyll Website

This is the Jekyll-powered version of the Nextract website, converted from static HTML to a fully functional Jekyll site with reusable components, SEO optimization, and maintainable architecture.

## 🎯 What's Been Accomplished

✅ **Complete Jekyll Migration**: Successfully converted all HTML pages to Jekyll with proper templating
✅ **Reusable Components**: Created modular includes for header, footer, navigation, and contact sections
✅ **SEO Optimization**: Added Jekyll SEO plugin with proper meta tags and structured data
✅ **Responsive Design**: Preserved all Tailwind CSS styling and responsive behavior
✅ **Dynamic Navigation**: Configuration-driven navigation system with dropdown menus
✅ **Site Configuration**: Centralized site data in `_config.yml` for easy management
✅ **Build System**: Working Jekyll build pipeline with Bundler dependency management

## 📁 Site Structure

```
nextract-jekyll/
├── _layouts/              # Page layouts
│   └── default.html       # Main layout template
├── _includes/             # Reusable components
│   ├── header.html        # Site header and navigation
│   ├── footer.html        # Site footer
│   ├── mobile-menu.html   # Mobile navigation menu
│   └── contact-section.html # Contact CTA section
├── assets/               # Static assets
│   └── js/
│       └── script.js     # JavaScript functionality
├── _config.yml          # Site configuration
├── Gemfile              # Ruby dependencies
├── index.html           # Homepage
├── about.html           # About page
├── solutions.html       # Solutions page
├── industries.html      # Industries page
└── [legal pages]        # Privacy, Terms, SLA, etc.
```

## 🚀 Getting Started

### Prerequisites
- Ruby 3.0+ installed
- Bundler gem installed

### Setup
```bash
# Navigate to the Jekyll site directory
cd /home/parth/Documents/Website/nextract-jekyll

# Install dependencies
bundle install

# Build the site (with clean URLs)
export PATH="$HOME/.local/share/gem/ruby/3.2.0/bin:$PATH"
bundle exec jekyll build

# Serve locally for development
bundle exec jekyll serve --host=0.0.0.0 --port=4000
```

The site will be available at `http://localhost:4000`

### For Production Build
```bash
# Clean build for production
bundle exec jekyll build --config _config.yml

# The generated site will be in the _site/ directory
```

## 🔧 Configuration

### Site Settings
Edit `_config.yml` to update:
- Site metadata (title, description, URL)
- Contact information (phone, email, address)
- Social media links
- Navigation structure
- SEO settings

### Navigation Management
The navigation is dynamically generated from `_config.yml`. To add/modify menu items:

```yaml
navigation:
  - name: "New Page"
    link: "/new-page/"
  - name: "Dropdown Menu"
    link: "#"
    dropdown:
      - name: "Submenu Item"
        link: "/submenu/"
```

### Adding New Pages
1. Create a new HTML file (e.g., `new-page.html`)
2. Add Jekyll front matter:
```yaml
---
layout: default
title: "Page Title"
description: "Page description for SEO"
---
```
3. Add your content using HTML

## 🎨 Styling

The site uses:
- **Tailwind CSS** (via CDN) for utility-first styling
- **Custom CSS** for brand-specific styles (gradients, animations, etc.)
- **Remix Icons** for iconography
- **Google Fonts** (Montserrat) for typography

All styles are preserved from the original design and are mobile-responsive.

## 🔍 SEO Features

- **Jekyll SEO Tag**: Automatic meta tags and structured data
- **Sitemap**: Auto-generated XML sitemap
- **RSS Feed**: Automatic feed generation
- **Canonical URLs**: Proper URL canonicalization
- **Open Graph**: Social media sharing optimization
- **Twitter Cards**: Twitter-specific meta tags

## 📱 Features Included

- **Responsive Design**: Mobile-first approach with breakpoint-based layouts
- **Interactive Navigation**: Dropdown menus and mobile hamburger menu
- **Contact Forms**: Ready-to-integrate contact forms
- **Reveal Animations**: Scroll-based animations for content sections
- **Fast Loading**: Optimized assets and efficient HTML structure

## 🛠️ Development Commands

```bash
# Start development server with auto-rebuild
bundle exec jekyll serve --livereload

# Build for production
bundle exec jekyll build --config _config.yml

# Clean build artifacts
bundle exec jekyll clean

# Check for errors
bundle exec jekyll doctor
```

## 📈 Performance Optimizations

- Minified and compressed assets
- Optimized images and SVGs
- Efficient CSS loading strategy
- Fast JavaScript execution
- SEO-optimized HTML structure

## 🚀 Deployment Options

### Option 1: Static Hosting (Netlify, Vercel)
1. Connect your Git repository
2. Set build command: `bundle exec jekyll build`
3. Set publish directory: `_site`

### Option 2: GitHub Pages
1. Push to GitHub repository
2. Enable GitHub Pages in repository settings
3. Jekyll will build automatically

### Option 3: Manual Deployment
1. Run `bundle exec jekyll build`
2. Upload `_site/` contents to your web server

## 🎯 Key Improvements Over Static HTML

- **Maintainability**: DRY principle with reusable components
- **SEO**: Enhanced search engine optimization
- **Performance**: Optimized build process and assets
- **Scalability**: Easy to add new pages and sections
- **Configuration**: Centralized site management
- **Development**: Hot-reload for efficient development

## 📞 Support

The site maintains the exact visual appearance and functionality of your original HTML website while providing the benefits of a modern Jekyll-powered architecture.

For development questions or modifications, refer to the [Jekyll Documentation](https://jekyllrb.com/docs/).

---

**Ready to use!** Your Nextract website is now powered by Jekyll with full maintainability and modern web development best practices.