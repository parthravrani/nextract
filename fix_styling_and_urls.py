#!/usr/bin/env python3
"""
Fix styling, layouts, and URLs for all new pages
"""

from pathlib import Path
import re

def fix_brand_pages():
    """Update brand pages with proper layout and clean URLs"""
    script_dir = Path(__file__).parent
    brands_dir = script_dir / "brands"
    
    print("\n" + "="*60)
    print("Fixing Brand Pages...")
    print("="*60 + "\n")
    
    for brand_file in brands_dir.glob("*.md"):
        content = brand_file.read_text(encoding='utf-8')
        
        # Extract front matter
        match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
        if not match:
            continue
        
        front_matter = match.group(1)
        body = match.group(2)
        
        # Change layout to product-page
        front_matter = re.sub(r'layout: product-page', 'layout: product-page', front_matter)
        if 'layout:' not in front_matter:
            front_matter = f"layout: product-page\n{front_matter}"
        
        # Fix URLs in body - remove .html extensions
        body = re.sub(r'\.html(?=["\']|\))', '', body)
        body = re.sub(r'/brands/([^"\']+)-scraper', r'/brands/\1-scraper', body)
        
        # Fix Start Free Trial links
        body = re.sub(r'\[Start Free Trial\]\(#\)', '[Start Free Trial](/contact)', body)
        body = re.sub(r'\[API Documentation\]\(#\)', '[API Documentation](/products)', body)
        body = re.sub(r'\[Contact Sales\]\(#\)', '[Contact Sales](/contact)', body)
        
        # Write updated content
        new_content = f"---\n{front_matter}---\n{body}"
        brand_file.write_text(new_content, encoding='utf-8')
        print(f"  ✓ Fixed {brand_file.name}")
    
    print()

def fix_geographic_pages():
    """Update geographic pages with clean URLs"""
    script_dir = Path(__file__).parent
    geo_dir = script_dir / "geographic"
    
    print("="*60)
    print("Fixing Geographic Pages...")
    print("="*60 + "\n")
    
    for geo_file in geo_dir.glob("*.html"):
        content = geo_file.read_text(encoding='utf-8')
        
        # Fix URLs - remove .html extensions
        content = re.sub(r'\.html(?=["\'])', '', content)
        
        # Fix CTA links
        content = re.sub(r'href="#"', 'href="/contact"', content)
        
        geo_file.write_text(content, encoding='utf-8')
        print(f"  ✓ Fixed {geo_file.name}")
    
    print()

def fix_case_study_pages():
    """Update case study pages with clean URLs"""
    script_dir = Path(__file__).parent
    case_studies_dir = script_dir / "_case-studies"
    
    print("="*60)
    print("Fixing Case Study Pages...")
    print("="*60 + "\n")
    
    for case_file in case_studies_dir.glob("*.md"):
        content = case_file.read_text(encoding='utf-8')
        
        # Fix URLs - remove .html extensions
        content = re.sub(r'\.html(?=["\']|\))', '', content)
        
        # Fix CTA links
        content = re.sub(r'\[Start Free Trial\]\(#\)', '[Start Free Trial](/contact)', content)
        content = re.sub(r'\[Schedule Demo\]\(#\)', '[Schedule Demo](https://calendly.com/parthravrani/30min)', content)
        content = re.sub(r'\[View All Case Studies\]\(/case-studies\.html\)', '[View All Case Studies](/case-studies)', content)
        
        case_file.write_text(content, encoding='utf-8')
        print(f"  ✓ Fixed {case_file.name}")
    
    print()

def fix_blog_pages():
    """Update blog/intelligence pages with clean URLs"""
    script_dir = Path(__file__).parent
    blog_dir = script_dir / "blog"
    
    print("="*60)
    print("Fixing Blog/Intelligence Pages...")
    print("="*60 + "\n")
    
    for blog_file in blog_dir.glob("*.md"):
        content = blog_file.read_text(encoding='utf-8')
        
        # Fix URLs - remove .html extensions
        content = re.sub(r'\.html(?=["\']|\))', '', content)
        
        # Fix CTA links
        content = re.sub(r'\[Start Free Trial\]\(#\)', '[Start Free Trial](/contact)', content)
        content = re.sub(r'\[Schedule Demo\]\(#\)', '[Schedule Demo](https://calendly.com/parthravrani/30min)', content)
        content = re.sub(r'\[Contact Sales\]\(#\)', '[Contact Sales](/contact)', content)
        
        blog_file.write_text(content, encoding='utf-8')
        print(f"  ✓ Fixed {blog_file.name}")
    
    print()

def fix_internal_links():
    """Fix internal links added to category pages"""
    script_dir = Path(__file__).parent
    
    print("="*60)
    print("Fixing Internal Links on Category Pages...")
    print("="*60 + "\n")
    
    pages = ["e-commerce.html", "quick-commerce.html", "food-delivery.html"]
    
    for page_name in pages:
        page_file = script_dir / page_name
        if not page_file.exists():
            continue
        
        content = page_file.read_text(encoding='utf-8')
        
        # Fix URLs in internal links section - remove .html
        content = re.sub(r'href="/brands/([^"]+)\.html"', r'href="/brands/\1"', content)
        content = re.sub(r'href="/geographic/([^"]+)\.html"', r'href="/geographic/\1"', content)
        content = re.sub(r'href="/intelligence/([^"]+)\.html"', r'href="/intelligence/\1"', content)
        
        page_file.write_text(content, encoding='utf-8')
        print(f"  ✓ Fixed {page_name}")
    
    print()

def update_config():
    """Add new collections to _config.yml"""
    script_dir = Path(__file__).parent
    config_file = script_dir / "_config.yml"
    
    print("="*60)
    print("Updating _config.yml...")
    print("="*60 + "\n")
    
    content = config_file.read_text(encoding='utf-8')
    
    # Check if we need to add new collections
    if 'brands:' not in content:
        # Find the collections section
        collections_match = re.search(r'(collections:.*?)(exclude:)', content, re.DOTALL)
        if collections_match:
            collections_section = collections_match.group(1)
            
            # Add new collections before exclude
            new_collections = """  brands:
    output: true
    permalink: /brands/:name/
  geographic:
    output: true
    permalink: /geographic/:name/
  blog:
    output: true
    permalink: /blog/:name/
  
# """
            
            content = content.replace(collections_match.group(2), new_collections + collections_match.group(2))
            
            config_file.write_text(content, encoding='utf-8')
            print("  ✓ Added brands, geographic, and blog collections")
    else:
        print("  ✓ Collections already configured")
    
    print()

def main():
    """Run all fixes"""
    print("\n" + "="*60)
    print("🔧 FIXING STYLING, LAYOUTS & URLs")
    print("="*60)
    
    update_config()
    fix_brand_pages()
    fix_geographic_pages()
    fix_case_study_pages()
    fix_blog_pages()
    fix_internal_links()
    
    print("="*60)
    print("✅ All Fixes Applied!")
    print("="*60)
    print("\nRebuild Jekyll with: bundle exec jekyll build")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
