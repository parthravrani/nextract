#!/usr/bin/env python3
"""
SEO Analysis Script for Actowiz Solutions Website
Filters and analyzes e-commerce, quick commerce, and food delivery pages
Uses pattern matching and semantic analysis to identify relevant pages
"""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup
from collections import defaultdict
import json
from datetime import datetime

# Pattern-based matching - using regex patterns to catch variations
ECOMMERCE_PATTERNS = [
    r'\be[\s-]?commerce\b', r'\bonline[\s-]?store', r'\bonline[\s-]?shopping',
    r'\bproduct[\s-]?data', r'\bproduct[\s-]?scraping', r'\bmarketplace',
    r'\bamazon', r'\bebay', r'\bshopify', r'\bwoocommerce', r'\bmagento',
    r'\binventory[\s-]?scraping', r'\bpricing[\s-]?data', r'\bcatalog[\s-]?scraping',
    r'\bmerchant[\s-]?data', r'\bseller[\s-]?data', r'\bdigital[\s-]?shelf',
    r'\bbrand[\s-]?protection', r'\bretail[\s-]?data', r'\bstore[\s-]?data',
    r'\bproduct[\s-]?listing', r'\bmarketplace[\s-]?scraping', r'\be[\s-]?tail',
    r'\bwalmart', r'\btarget', r'\bbest[\s-]?buy', r'\betsy', r'\balibaba',
    r'\bflipkart', r'\bmyntra', r'\bproduct[\s-]?information', r'\bproduct[\s-]?details'
]

QUICK_COMMERCE_PATTERNS = [
    r'\bquick[\s-]?commerce', r'\bq[\s-]?commerce', r'\binstant[\s-]?delivery',
    r'\b15[\s-]?minute', r'\brapid[\s-]?delivery', r'\bgrocery[\s-]?delivery',
    r'\bblinkit', r'\bzepto', r'\bdunzo', r'\brapido', r'\bgrofers',
    r'\bbigbasket', r'\binstacart', r'\bgopuff', r'\bgetir', r'\bjokr',
    r'\bswiggy[\s-]?instamart', r'\bquick[\s-]?grocery', r'\bexpress[\s-]?delivery',
    r'\bhyperlocal', r'\bon[\s-]?demand[\s-]?grocery', r'\bimmediate[\s-]?delivery',
    r'\bultra[\s-]?fast[\s-]?delivery', r'\bminutes[\s-]?delivery'
]

FOOD_DELIVERY_PATTERNS = [
    r'\bfood[\s-]?delivery', r'\brestaurant[\s-]?data', r'\brestaurant[\s-]?scraping',
    r'\bfood[\s-]?ordering', r'\bdelivery[\s-]?app', r'\bzomato', r'\bswiggy',
    r'\buber[\s-]?eats', r'\bdoordash', r'\bgrubhub', r'\bdeliveroo', r'\bfoodpanda',
    r'\bmenulog', r'\bjust[\s-]?eat', r'\brestaurant[\s-]?menu', r'\bdining[\s-]?data',
    r'\bcuisine[\s-]?data', r'\btakeaway', r'\bfood[\s-]?service', r'\bfood[\s-]?app',
    r'\bmeal[\s-]?delivery', r'\bhungry', r'\bpostmates', r'\bcaviar', r'\bseamless',
    r'\brestaurant[\s-]?listing', r'\bfood[\s-]?platform', r'\bmenu[\s-]?scraping'
]

# Platform/company names that indicate categories
ECOMMERCE_PLATFORMS = ['amazon', 'ebay', 'shopify', 'woocommerce', 'magento', 'walmart', 
                       'target', 'bestbuy', 'etsy', 'alibaba', 'flipkart', 'myntra', 
                       'snapdeal', 'paytm', 'meesho', 'nykaa', 'ajio']

QUICK_COMMERCE_PLATFORMS = ['blinkit', 'zepto', 'dunzo', 'rapido', 'grofers', 'bigbasket',
                            'instacart', 'gopuff', 'getir', 'jokr', 'swiggy instamart']

FOOD_DELIVERY_PLATFORMS = ['zomato', 'swiggy', 'ubereats', 'doordash', 'grubhub', 'deliveroo',
                           'foodpanda', 'menulog', 'just eat', 'hungry', 'postmates', 'caviar']

def extract_seo_elements(soup, filepath):
    """Extract SEO elements from HTML"""
    seo_data = {
        'filepath': str(filepath),
        'filename': os.path.basename(filepath),
        'title': '',
        'meta_description': '',
        'meta_keywords': '',
        'h1': [],
        'h2': [],
        'h3': [],
        'og_title': '',
        'og_description': '',
        'canonical': '',
        'schema': [],
        'word_count': 0,
        'internal_links': 0,
        'external_links': 0,
        'images': 0,
        'category': None
    }
    
    # Title
    title_tag = soup.find('title')
    if title_tag:
        seo_data['title'] = title_tag.get_text(strip=True)
    
    # Meta description
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    if meta_desc:
        seo_data['meta_description'] = meta_desc.get('content', '')
    
    # Meta keywords
    meta_keywords = soup.find('meta', attrs={'name': 'keywords'})
    if meta_keywords:
        seo_data['meta_keywords'] = meta_keywords.get('content', '')
    
    # Headings
    for h in soup.find_all(['h1', 'h2', 'h3']):
        text = h.get_text(strip=True)
        if text:
            seo_data[f'h{h.name[1]}'].append(text)
    
    # Open Graph
    og_title = soup.find('meta', property='og:title')
    if og_title:
        seo_data['og_title'] = og_title.get('content', '')
    
    og_desc = soup.find('meta', property='og:description')
    if og_desc:
        seo_data['og_description'] = og_desc.get('content', '')
    
    # Canonical
    canonical = soup.find('link', rel='canonical')
    if canonical:
        seo_data['canonical'] = canonical.get('href', '')
    
    # Schema markup
    schemas = soup.find_all('script', type='application/ld+json')
    for schema in schemas:
        try:
            schema_data = json.loads(schema.string)
            seo_data['schema'].append(schema_data)
        except:
            pass
    
    # Word count (main content)
    body = soup.find('body')
    if body:
        text = body.get_text()
        seo_data['word_count'] = len(text.split())
    
    # Links
    links = soup.find_all('a', href=True)
    for link in links:
        href = link['href']
        if href.startswith('http') and 'actowizsolutions.com' not in href:
            seo_data['external_links'] += 1
        else:
            seo_data['internal_links'] += 1
    
    # Images
    seo_data['images'] = len(soup.find_all('img'))
    
    return seo_data

def count_pattern_matches(text, patterns):
    """Count how many patterns match in the text"""
    count = 0
    matches = []
    for pattern in patterns:
        found = re.findall(pattern, text, re.IGNORECASE)
        if found:
            count += len(found)
            matches.extend(found)
    return count, matches

def categorize_page(filename, title, meta_desc, headings, full_content):
    """Categorize page using pattern matching and semantic analysis"""
    categories = []
    score = {'ecommerce': 0, 'quick_commerce': 0, 'food_delivery': 0}
    evidence = {'ecommerce': [], 'quick_commerce': [], 'food_delivery': []}
    
    # Combine all text for analysis
    all_text = f"{filename} {title} {meta_desc} {' '.join(headings)} {full_content}"
    text_lower = all_text.lower()
    
    # Pattern matching with scoring
    # Filename gets higher weight
    filename_lower = filename.lower()
    ecom_count, ecom_matches = count_pattern_matches(filename_lower, ECOMMERCE_PATTERNS)
    qcom_count, qcom_matches = count_pattern_matches(filename_lower, QUICK_COMMERCE_PATTERNS)
    fdel_count, fdel_matches = count_pattern_matches(filename_lower, FOOD_DELIVERY_PATTERNS)
    
    score['ecommerce'] += ecom_count * 3
    score['quick_commerce'] += qcom_count * 3
    score['food_delivery'] += fdel_count * 3
    evidence['ecommerce'].extend(ecom_matches[:5])
    evidence['quick_commerce'].extend(qcom_matches[:5])
    evidence['food_delivery'].extend(fdel_matches[:5])
    
    # Title gets high weight
    title_lower = title.lower()
    ecom_count, ecom_matches = count_pattern_matches(title_lower, ECOMMERCE_PATTERNS)
    qcom_count, qcom_matches = count_pattern_matches(title_lower, QUICK_COMMERCE_PATTERNS)
    fdel_count, fdel_matches = count_pattern_matches(title_lower, FOOD_DELIVERY_PATTERNS)
    
    score['ecommerce'] += ecom_count * 4
    score['quick_commerce'] += qcom_count * 4
    score['food_delivery'] += fdel_count * 4
    evidence['ecommerce'].extend(ecom_matches[:5])
    evidence['quick_commerce'].extend(qcom_matches[:5])
    evidence['food_delivery'].extend(fdel_matches[:5])
    
    # Headings get medium weight
    headings_text = ' '.join(headings).lower()
    ecom_count, ecom_matches = count_pattern_matches(headings_text, ECOMMERCE_PATTERNS)
    qcom_count, qcom_matches = count_pattern_matches(headings_text, QUICK_COMMERCE_PATTERNS)
    fdel_count, fdel_matches = count_pattern_matches(headings_text, FOOD_DELIVERY_PATTERNS)
    
    score['ecommerce'] += ecom_count * 2
    score['quick_commerce'] += qcom_count * 2
    score['food_delivery'] += fdel_count * 2
    evidence['ecommerce'].extend(ecom_matches[:5])
    evidence['quick_commerce'].extend(qcom_matches[:5])
    evidence['food_delivery'].extend(fdel_matches[:5])
    
    # Full content gets lower weight but broader coverage
    # Sample different parts of content to catch context
    content_samples = [
        text_lower[:5000],  # First 5000 chars
        text_lower[len(text_lower)//2:len(text_lower)//2+5000] if len(text_lower) > 10000 else '',  # Middle
        text_lower[-5000:] if len(text_lower) > 5000 else ''  # Last 5000 chars
    ]
    
    for sample in content_samples:
        if sample:
            ecom_count, ecom_matches = count_pattern_matches(sample, ECOMMERCE_PATTERNS)
            qcom_count, qcom_matches = count_pattern_matches(sample, QUICK_COMMERCE_PATTERNS)
            fdel_count, fdel_matches = count_pattern_matches(sample, FOOD_DELIVERY_PATTERNS)
            
            score['ecommerce'] += ecom_count * 1
            score['quick_commerce'] += qcom_count * 1
            score['food_delivery'] += fdel_count * 1
    
    # Platform name detection (high confidence)
    for platform in ECOMMERCE_PLATFORMS:
        if platform in text_lower:
            score['ecommerce'] += 5
            evidence['ecommerce'].append(f"platform:{platform}")
    
    for platform in QUICK_COMMERCE_PLATFORMS:
        if platform in text_lower:
            score['quick_commerce'] += 5
            evidence['quick_commerce'].append(f"platform:{platform}")
    
    for platform in FOOD_DELIVERY_PLATFORMS:
        if platform in text_lower:
            score['food_delivery'] += 5
            evidence['food_delivery'].append(f"platform:{platform}")
    
    # Context-based semantic matching
    # E-commerce indicators
    if re.search(r'\b(product|item|listing|seller|merchant|marketplace)', text_lower):
        if re.search(r'\b(scraping|data|extract|collect)', text_lower):
            score['ecommerce'] += 2
    
    # Quick commerce indicators (grocery + fast delivery)
    if re.search(r'\b(grocery|grocery|supermarket|store)', text_lower):
        if re.search(r'\b(15|minutes?|instant|rapid|quick|fast)', text_lower):
            score['quick_commerce'] += 3
    
    # Food delivery indicators (restaurant + delivery)
    if re.search(r'\b(restaurant|food|cuisine|menu|dining)', text_lower):
        if re.search(r'\b(delivery|order|takeaway|takeout)', text_lower):
            score['food_delivery'] += 3
    
    # Determine category (threshold-based)
    threshold = 3  # Minimum score to be considered relevant
    max_score = max(score.values())
    
    if max_score >= threshold:
        if score['ecommerce'] >= threshold:
            categories.append('ecommerce')
        if score['quick_commerce'] >= threshold:
            categories.append('quick_commerce')
        if score['food_delivery'] >= threshold:
            categories.append('food_delivery')
    
    # Remove duplicates from evidence
    for cat in evidence:
        evidence[cat] = list(set(evidence[cat]))[:10]
    
    return categories, score, evidence

def analyze_html_file(filepath):
    """Analyze a single HTML file - reads full content"""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        seo_data = extract_seo_elements(soup, filepath)
        
        # Get full content text (body content)
        body = soup.find('body')
        full_content = body.get_text() if body else content
        
        # Get all headings
        all_headings = seo_data['h1'] + seo_data['h2'] + seo_data['h3']
        
        # Categorize using full content and pattern matching
        categories, score, evidence = categorize_page(
            seo_data['filename'],
            seo_data['title'],
            seo_data['meta_description'],
            all_headings,
            full_content
        )
        
        seo_data['category'] = categories
        seo_data['relevance_score'] = score
        seo_data['evidence'] = evidence  # What patterns matched
        
        return seo_data if categories else None
        
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return None

def main():
    base_path = Path("/Volumes/192.168.1.10/Cloned website/https___www.actowizsolutions.com_/www.actowizsolutions.com")
    
    if not base_path.exists():
        print(f"Error: Path {base_path} does not exist")
        return
    
    print("Starting SEO Analysis...")
    print(f"Scanning directory: {base_path}")
    
    # Find all HTML files
    html_files = list(base_path.glob("*.html"))
    total_files = len(html_files)
    print(f"Found {total_files} HTML files")
    
    # Analyze files
    relevant_pages = {
        'ecommerce': [],
        'quick_commerce': [],
        'food_delivery': []
    }
    
    processed = 0
    for html_file in html_files:
        processed += 1
        if processed % 100 == 0:
            print(f"Processed {processed}/{total_files} files...")
        
        result = analyze_html_file(html_file)
        if result:
            for category in result['category']:
                relevant_pages[category].append(result)
    
    print(f"\nAnalysis complete!")
    print(f"E-commerce pages: {len(relevant_pages['ecommerce'])}")
    print(f"Quick commerce pages: {len(relevant_pages['quick_commerce'])}")
    print(f"Food delivery pages: {len(relevant_pages['food_delivery'])}")
    
    # Save results
    output_dir = Path(__file__).parent / "seo_analysis_results"
    output_dir.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    for category, pages in relevant_pages.items():
        if pages:
            output_file = output_dir / f"{category}_pages_{timestamp}.json"
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(pages, f, indent=2, ensure_ascii=False)
            print(f"Saved {len(pages)} {category} pages to {output_file}")
    
    # Generate summary
    summary = {
        'total_files_scanned': total_files,
        'ecommerce_count': len(relevant_pages['ecommerce']),
        'quick_commerce_count': len(relevant_pages['quick_commerce']),
        'food_delivery_count': len(relevant_pages['food_delivery']),
        'total_relevant': sum(len(pages) for pages in relevant_pages.values()),
        'timestamp': timestamp
    }
    
    summary_file = output_dir / f"summary_{timestamp}.json"
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2)
    
    print(f"\nSummary saved to {summary_file}")
    return relevant_pages

if __name__ == "__main__":
    main()
