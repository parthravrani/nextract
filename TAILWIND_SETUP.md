# Tailwind CSS Setup for Jekyll

## Quick Start

1. **Install Node.js dependencies:**
   ```bash
   npm install
   ```

2. **Build Tailwind CSS (one-time):**
   ```bash
   npm run build:css
   ```

3. **Build your Jekyll site:**
   ```bash
   bundle exec jekyll build
   ```

4. **Or use the combined build command:**
   ```bash
   npm run build
   ```

## Development Workflow

**Option 1: Combined commands (recommended)**
```bash
# Build CSS + Jekyll site
npm run build

# Build CSS + serve Jekyll (auto-rebuilds)
npm run serve
```

**Option 2: Separate commands**
```bash
# Terminal 1: Watch Tailwind CSS
npm run watch:css

# Terminal 2: Serve Jekyll
bundle exec jekyll serve
```

## How It Works

- **Pre-build approach**: Tailwind CSS is compiled **before** Jekyll builds
- The `tailwind.css` source file contains `@tailwind` directives
- Running `npm run build:css` compiles it to `tailwind.min.css`
- Jekyll serves the pre-compiled `tailwind.min.css` file
- This is simpler and more reliable than Jekyll plugins

## What Changed

- ✅ Removed Tailwind CDN script tag (was causing performance issues)
- ✅ Created `tailwind.config.js` with proper content paths
- ✅ Source file: `assets/css/tailwind.css` (with `@tailwind` directives)
- ✅ Compiled file: `assets/css/tailwind.min.css` (minified CSS)
- ✅ Updated `default.html` to link to compiled CSS
- ✅ Added npm scripts for building CSS

## Important Notes

- **You MUST run `npm run build:css` before deploying** to generate the CSS
- The compiled `tailwind.min.css` file should be committed to git
- For development, use `npm run watch:css` in one terminal and `jekyll serve` in another
- This dramatically improves Core Web Vitals (LCP, CLS) and SEO rankings compared to the CDN version

## Production Deployment

```bash
# 1. Build Tailwind CSS
npm run build:css

# 2. Build Jekyll site
bundle exec jekyll build

# 3. Deploy the _site folder
```

The compiled CSS file (`tailwind.min.css`) will be included in your Jekyll build output.
