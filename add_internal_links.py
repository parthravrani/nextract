#!/usr/bin/env python3
"""
Add strategic internal linking to pages for SEO
"""

from pathlib import Path
import re

# Internal linking structure
LINK_STRUCTURE = {
    "e-commerce": {
        "category_page": "/e-commerce.html",
        "related_brands": [
            {"name": "Amazon US", "url": "/brands/amazon-us-scraper.html"},
            {"name": "Walmart", "url": "/brands/walmart-scraper.html"},
            {"name": "eBay", "url": "/brands/ebay-scraper.html"},
            {"name": "Shopify", "url": "/brands/shopify-scraper.html"},
            {"name": "Flipkart", "url": "/brands/flipkart-scraper.html"},
            {"name": "Target", "url": "/brands/target-scraper.html"},
            {"name": "Best Buy", "url": "/brands/best-buy-scraper.html"},
        ],
        "geographic": [
            {"name": "E-commerce USA", "url": "/geographic/ecommerce-usa.html"},
            {"name": "E-commerce India", "url": "/geographic/ecommerce-india.html"},
            {"name": "E-commerce UAE", "url": "/geographic/ecommerce-uae.html"},
        ],
        "related_intelligence": [
            {"name": "E-commerce Intelligence", "url": "/intelligence/e-commerce-intelligence.html"},
            {"name": "Price Intelligence", "url": "/intelligence/price-intelligence.html"},
        ]
    },
    "quick-commerce": {
        "category_page": "/quick-commerce.html",
        "related_brands": [
            {"name": "Blinkit", "url": "/brands/blinkit-scraper.html"},
            {"name": "Zepto", "url": "/brands/zepto-scraper.html"},
            {"name": "Instacart", "url": "/brands/instacart-scraper.html"},
            {"name": "Swiggy Instamart", "url": "/brands/swiggy-instamart-scraper.html"},
            {"name": "BigBasket", "url": "/brands/bigbasket-scraper.html"},
            {"name": "Amazon Fresh", "url": "/brands/amazon-fresh-scraper.html"},
        ],
        "geographic": [
            {"name": "Quick Commerce India", "url": "/geographic/quick-commerce-india.html"},
            {"name": "Quick Commerce USA", "url": "/geographic/quick-commerce-usa.html"},
        ],
        "related_intelligence": [
            {"name": "Market Intelligence", "url": "/intelligence/market-intelligence.html"},
            {"name": "Price Intelligence", "url": "/intelligence/price-intelligence.html"},
        ]
    },
    "food-delivery": {
        "category_page": "/food-delivery.html",
        "related_brands": [
            {"name": "Swiggy", "url": "/brands/swiggy-scraper.html"},
            {"name": "Zomato", "url": "/brands/zomato-scraper.html"},
            {"name": "DoorDash", "url": "/brands/doordash-scraper.html"},
            {"name": "Uber Eats", "url": "/brands/uber-eats-scraper.html"},
            {"name": "GrubHub", "url": "/brands/grubhub-scraper.html"},
        ],
        "geographic": [
            {"name": "Food Delivery India", "url": "/geographic/food-delivery-india.html"},
            {"name": "Food Delivery USA", "url": "/geographic/food-delivery-usa.html"},
        ],
        "related_intelligence": [
            {"name": "Restaurant Intelligence", "url": "/intelligence/restaurant-intelligence.html"},
            {"name": "Market Intelligence", "url": "/intelligence/market-intelligence.html"},
        ]
    }
}

def generate_internal_links_section(category):
    """Generate internal links HTML section"""
    if category not in LINK_STRUCTURE:
        return ""
    
    links = LINK_STRUCTURE[category]
    
    html = '\n<section class="internal-links" style="margin-top: 60px; padding: 40px 0; border-top: 1px solid #e0e0e0;">\n'
    html += '  <div class="container">\n'
    html += '    <h2>Related Resources</h2>\n'
    html += '    <div class="link-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 30px; margin-top: 30px;">\n'
    
    # Brand links
    html += '      <div class="link-column">\n'
    html += '        <h3>Platform-Specific Pages</h3>\n'
    html += '        <ul style="list-style: none; padding: 0;">\n'
    for brand in links["related_brands"][:5]:
        html += f'          <li><a href="{brand["url"]}">{brand["name"]} Scraper</a></li>\n'
    html += '        </ul>\n'
    html += '      </div>\n'
    
    # Geographic links
    html += '      <div class="link-column">\n'
    html += '        <h3>Geographic Coverage</h3>\n'
    html += '        <ul style="list-style: none; padding: 0;">\n'
    for geo in links["geographic"]:
        html += f'          <li><a href="{geo["url"]}">{geo["name"]}</a></li>\n'
    html += '        </ul>\n'
    html += '      </div>\n'
    
    # Intelligence links
    html += '      <div class="link-column">\n'
    html += '        <h3>Data Intelligence</h3>\n'
    html += '        <ul style="list-style: none; padding: 0;">\n'
    for intel in links["related_intelligence"]:
        html += f'          <li><a href="{intel["url"]}">{intel["name"]}</a></li>\n'
    html += '        </ul>\n'
    html += '      </div>\n'
    
    html += '    </div>\n'
    html += '  </div>\n'
    html += '</section>\n'
    
    return html

def add_internal_links_to_html_pages():
    """Add internal links to main HTML category pages"""
    script_dir = Path(__file__).parent
    
    pages = [
        ("e-commerce.html", "e-commerce"),
        ("quick-commerce.html", "quick-commerce"),
        ("food-delivery.html", "food-delivery"),
    ]
    
    print("\n" + "="*60)
    print("Adding Internal Links to HTML Pages...")
    print("="*60 + "\n")
    
    for filename, category in pages:
        filepath = script_dir / filename
        
        if not filepath.exists():
            print(f"  ⚠ Skipping {filename} (not found)")
            continue
        
        content = filepath.read_text(encoding='utf-8')
        
        # Check if links already added
        if 'class="internal-links"' in content:
            print(f"  ✓ {filename} already has internal links")
            continue
        
        # Add internal links before </main> tag
        links_section = generate_internal_links_section(category)
        content = content.replace('</main>', f'{links_section}</main>')
        
        filepath.write_text(content, encoding='utf-8')
        print(f"  ✓ Added internal links to {filename}")
    
    print()

def generate_breadcrumbs_for_brand_pages():
    """Add breadcrumb navigation to brand pages"""
    script_dir = Path(__file__).parent
    brands_dir = script_dir / "brands"
    
    print("="*60)
    print("Adding Breadcrumbs to Brand Pages...")
    print("="*60 + "\n")
    
    # Map brand slugs to categories
    brand_categories = {
        "amazon-us": "e-commerce",
        "walmart": "e-commerce",
        "ebay": "e-commerce",
        "shopify": "e-commerce",
        "flipkart": "e-commerce",
        "target": "e-commerce",
        "best-buy": "e-commerce",
        "etsy": "e-commerce",
        "zalando": "e-commerce",
        "noon": "e-commerce",
        "blinkit": "quick-commerce",
        "zepto": "quick-commerce",
        "instacart": "quick-commerce",
        "bigbasket": "quick-commerce",
        "amazon-fresh": "quick-commerce",
        "swiggy-instamart": "quick-commerce",
        "gorillas": "quick-commerce",
        "getir": "quick-commerce",
        "gopuff": "quick-commerce",
        "whole-foods": "quick-commerce",
        "kroger": "quick-commerce",
        "swiggy": "food-delivery",
        "zomato": "food-delivery",
        "doordash": "food-delivery",
        "uber-eats": "food-delivery",
        "grubhub": "food-delivery",
        "deliveroo": "food-delivery",
        "just-eat": "food-delivery",
        "talabat": "food-delivery",
        "postmates": "food-delivery",
        "grabfood": "food-delivery",
    }
    
    count = 0
    for brand_file in brands_dir.glob("*.md"):
        slug = brand_file.stem.replace('-scraper', '')
        category = brand_categories.get(slug)
        
        if not category:
            continue
        
        content = brand_file.read_text(encoding='utf-8')
        
        # Check if breadcrumbs already exist
        if 'breadcrumbs:' in content:
            continue
        
        # Extract front matter
        match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
        if not match:
            continue
        
        front_matter = match.group(1)
        body = match.group(2)
        
        # Add breadcrumbs to front matter
        category_name = category.replace('-', ' ').title()
        category_url = f"/{category}.html"
        
        breadcrumb_yaml = f"""breadcrumbs:
  - name: "Home"
    url: "/"
  - name: "{category_name}"
    url: "{category_url}"
  - name: "{slug.replace('-', ' ').title()}"
    url: "/brands/{brand_file.stem}.html"
"""
        
        new_content = f"---\n{front_matter}\n{breadcrumb_yaml}---\n{body}"
        brand_file.write_text(new_content, encoding='utf-8')
        count += 1
    
    print(f"  ✓ Added breadcrumbs to {count} brand pages\n")

def main():
    """Main function"""
    add_internal_links_to_html_pages()
    generate_breadcrumbs_for_brand_pages()
    
    print("="*60)
    print("✅ Internal Linking Complete!")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
