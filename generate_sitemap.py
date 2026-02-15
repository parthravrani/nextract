#!/usr/bin/env python3
"""
Generate XML sitemaps for Nextract website
"""

from pathlib import Path
from datetime import datetime
import xml.etree.ElementTree as ET

def create_sitemap(urls, filename):
    """Create an XML sitemap"""
    urlset = ET.Element('urlset', xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    
    for url_data in urls:
        url_elem = ET.SubElement(urlset, 'url')
        
        loc = ET.SubElement(url_elem, 'loc')
        loc.text = url_data['loc']
        
        lastmod = ET.SubElement(url_elem, 'lastmod')
        lastmod.text = url_data.get('lastmod', datetime.now().strftime('%Y-%m-%d'))
        
        changefreq = ET.SubElement(url_elem, 'changefreq')
        changefreq.text = url_data.get('changefreq', 'weekly')
        
        priority = ET.SubElement(url_elem, 'priority')
        priority.text = str(url_data.get('priority', 0.5))
    
    tree = ET.ElementTree(urlset)
    ET.indent(tree, space="  ")
    tree.write(filename, encoding='utf-8', xml_declaration=True)
    print(f"✓ Created {filename}")

def main():
    """Generate all sitemaps"""
    base_url = "https://nextract.dev"
    script_dir = Path(__file__).parent
    
    # Main pages
    main_urls = [
        {'loc': f'{base_url}/', 'changefreq': 'daily', 'priority': 1.0},
        # Note: this site uses "pretty" URLs (trailing slash). Keep sitemap locs aligned.
        {'loc': f'{base_url}/scrava/', 'changefreq': 'weekly', 'priority': 0.9},
        {'loc': f'{base_url}/products/', 'changefreq': 'weekly', 'priority': 0.9},
        {'loc': f'{base_url}/services/', 'changefreq': 'weekly', 'priority': 0.9},
        {'loc': f'{base_url}/industries/', 'changefreq': 'weekly', 'priority': 0.8},
        {'loc': f'{base_url}/case-studies/', 'changefreq': 'weekly', 'priority': 0.7},
        {'loc': f'{base_url}/blog/', 'changefreq': 'weekly', 'priority': 0.7},
        {'loc': f'{base_url}/apis/', 'changefreq': 'weekly', 'priority': 0.7},
        {'loc': f'{base_url}/scrapers/', 'changefreq': 'weekly', 'priority': 0.7},
        {'loc': f'{base_url}/datasets/', 'changefreq': 'weekly', 'priority': 0.6},
        {'loc': f'{base_url}/solutions/', 'changefreq': 'weekly', 'priority': 0.6},
        {'loc': f'{base_url}/about/', 'changefreq': 'monthly', 'priority': 0.6},
        {'loc': f'{base_url}/contact/', 'changefreq': 'monthly', 'priority': 0.6},
        {'loc': f'{base_url}/privacy/', 'changefreq': 'monthly', 'priority': 0.3},
        {'loc': f'{base_url}/terms/', 'changefreq': 'monthly', 'priority': 0.3},
    ]
    
    # Category pages (High priority)
    category_urls = [
        {'loc': f'{base_url}/e-commerce/', 'changefreq': 'weekly', 'priority': 0.9},
        {'loc': f'{base_url}/quick-commerce/', 'changefreq': 'weekly', 'priority': 0.9},
        {'loc': f'{base_url}/food-delivery/', 'changefreq': 'weekly', 'priority': 0.9},
    ]
    
    # Brand pages
    brand_pages = list((script_dir / 'brands').glob('*.md'))
    brand_urls = [
        {
            'loc': f'{base_url}/brands/{page.stem}/',
            'changefreq': 'weekly',
            'priority': 0.8
        }
        for page in brand_pages
    ]
    
    # Geographic pages
    geographic_pages = list((script_dir / 'geographic').glob('*.html'))
    geographic_urls = [
        {
            'loc': f'{base_url}/geographic/{page.name}',
            'changefreq': 'weekly',
            'priority': 0.7
        }
        for page in geographic_pages
    ]
    
    # Service pages
    service_pages = list((script_dir / '_services').glob('*.md'))
    service_urls = [
        {
            'loc': f'{base_url}/services/{page.stem}/',
            'changefreq': 'monthly',
            'priority': 0.7
        }
        for page in service_pages
    ]
    
    # API pages
    api_pages = list((script_dir / '_apis').glob('*.md'))
    api_urls = [
        {
            'loc': f'{base_url}/apis/{page.stem}/',
            'changefreq': 'monthly',
            'priority': 0.7
        }
        for page in api_pages
    ]
    
    # Scraper pages
    scraper_pages = list((script_dir / '_scrapers').glob('*.md'))
    scraper_urls = [
        {
            'loc': f'{base_url}/scrapers/{page.stem}/',
            'changefreq': 'monthly',
            'priority': 0.6
        }
        for page in scraper_pages
    ]
    
    # Case study pages
    case_study_pages = list((script_dir / '_case-studies').glob('*.md'))
    case_study_urls = [
        {
            'loc': f'{base_url}/case-studies/{page.stem}/',
            'changefreq': 'monthly',
            'priority': 0.6
        }
        for page in case_study_pages
    ]
    
    # Intelligence pages
    intelligence_pages = list((script_dir / '_intelligence').glob('*.md'))
    intelligence_urls = [
        {
            'loc': f'{base_url}/intelligence/{page.stem}/',
            'changefreq': 'monthly',
            'priority': 0.6
        }
        for page in intelligence_pages
    ]
    
    # Industry pages
    industry_pages = list((script_dir / '_industries').glob('*.md'))
    industry_urls = [
        {
            'loc': f'{base_url}/industries/{page.stem}/',
            'changefreq': 'monthly',
            'priority': 0.7
        }
        for page in industry_pages
    ]
    
    # Blog/Intelligence articles
    blog_pages = list((script_dir / '_blog').glob('*.md'))
    blog_urls = [
        {
            'loc': f'{base_url}/blog/{page.stem}/',
            'changefreq': 'weekly',
            'priority': 0.6
        }
        for page in blog_pages
    ]
    
    # Create separate sitemaps
    print("\n" + "="*60)
    print("Generating Sitemaps...")
    print("="*60 + "\n")
    
    create_sitemap(main_urls, script_dir / 'sitemap-main.xml')
    create_sitemap(category_urls, script_dir / 'sitemap-categories.xml')
    create_sitemap(brand_urls, script_dir / 'sitemap-brands.xml')
    create_sitemap(geographic_urls, script_dir / 'sitemap-geographic.xml')
    create_sitemap(service_urls, script_dir / 'sitemap-services.xml')
    create_sitemap(api_urls, script_dir / 'sitemap-apis.xml')
    create_sitemap(scraper_urls, script_dir / 'sitemap-scrapers.xml')
    create_sitemap(case_study_urls, script_dir / 'sitemap-case-studies.xml')
    create_sitemap(intelligence_urls, script_dir / 'sitemap-intelligence.xml')
    create_sitemap(industry_urls, script_dir / 'sitemap-industries.xml')
    create_sitemap(blog_urls, script_dir / 'sitemap-blog.xml')
    
    # Create sitemap index
    print()
    sitemapindex = ET.Element('sitemapindex', xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    
    sitemap_files = [
        'sitemap-main.xml',
        'sitemap-categories.xml',
        'sitemap-brands.xml',
        'sitemap-geographic.xml',
        'sitemap-services.xml',
        'sitemap-apis.xml',
        'sitemap-scrapers.xml',
        'sitemap-case-studies.xml',
        'sitemap-intelligence.xml',
        'sitemap-industries.xml',
        'sitemap-blog.xml',
    ]
    
    for sitemap_file in sitemap_files:
        sitemap_elem = ET.SubElement(sitemapindex, 'sitemap')
        loc = ET.SubElement(sitemap_elem, 'loc')
        loc.text = f'{base_url}/{sitemap_file}'
        lastmod = ET.SubElement(sitemap_elem, 'lastmod')
        lastmod.text = datetime.now().strftime('%Y-%m-%d')
    
    tree = ET.ElementTree(sitemapindex)
    ET.indent(tree, space="  ")
    tree.write(script_dir / 'sitemap.xml', encoding='utf-8', xml_declaration=True)
    print(f"✓ Created sitemap.xml (index)\n")
    
    # Summary
    print("="*60)
    print("Sitemap Generation Complete!")
    print("="*60)
    print(f"Main pages: {len(main_urls)}")
    print(f"Category pages: {len(category_urls)}")
    print(f"Brand pages: {len(brand_urls)}")
    print(f"Geographic pages: {len(geographic_urls)}")
    print(f"Service pages: {len(service_urls)}")
    print(f"API pages: {len(api_urls)}")
    print(f"Scraper pages: {len(scraper_urls)}")
    print(f"Case studies: {len(case_study_urls)}")
    print(f"Intelligence pages: {len(intelligence_urls)}")
    print(f"Industry pages: {len(industry_urls)}")
    print(f"Blog articles: {len(blog_urls)}")
    print(f"\nTotal URLs: {len(main_urls) + len(category_urls) + len(brand_urls) + len(geographic_urls) + len(service_urls) + len(api_urls) + len(scraper_urls) + len(case_study_urls) + len(intelligence_urls) + len(industry_urls) + len(blog_urls)}")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
