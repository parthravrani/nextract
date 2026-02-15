#!/usr/bin/env python3
"""
Phase 1: Extract all SEO metadata from HTML files
Extracts title, meta description, headings, filename, and basic info
"""

import os
import json
from pathlib import Path
from bs4 import BeautifulSoup
from datetime import datetime
import re

def extract_metadata(filepath):
    """Extract SEO metadata from a single HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        metadata = {
            'filename': os.path.basename(filepath),
            'filepath': str(filepath),
            'title': '',
            'meta_description': '',
            'meta_keywords': '',
            'og_title': '',
            'og_description': '',
            'canonical': '',
            'h1': [],
            'h2': [],
            'h3': [],
            'h4': [],
            'h5': [],
            'h6': [],
            'url_slug': '',
            'word_count': 0,
            'has_schema': False
        }
        
        # Title
        title_tag = soup.find('title')
        if title_tag:
            metadata['title'] = title_tag.get_text(strip=True)
        
        # Meta description
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if meta_desc:
            metadata['meta_description'] = meta_desc.get('content', '').strip()
        
        # Meta keywords
        meta_keywords = soup.find('meta', attrs={'name': 'keywords'})
        if meta_keywords:
            metadata['meta_keywords'] = meta_keywords.get('content', '').strip()
        
        # Open Graph
        og_title = soup.find('meta', property='og:title')
        if og_title:
            metadata['og_title'] = og_title.get('content', '').strip()
        
        og_desc = soup.find('meta', property='og:description')
        if og_desc:
            metadata['og_description'] = og_desc.get('content', '').strip()
        
        # Canonical
        canonical = soup.find('link', rel='canonical')
        if canonical:
            metadata['canonical'] = canonical.get('href', '').strip()
        
        # All headings
        for level in range(1, 7):
            headings = soup.find_all(f'h{level}')
            for h in headings:
                text = h.get_text(strip=True)
                if text:
                    metadata[f'h{level}'].append(text)
        
        # URL slug from filename (remove .html)
        metadata['url_slug'] = metadata['filename'].replace('.html', '')
        
        # Word count (body content)
        body = soup.find('body')
        if body:
            text = body.get_text()
            metadata['word_count'] = len(text.split())
        
        # Check for schema markup
        schemas = soup.find_all('script', type='application/ld+json')
        metadata['has_schema'] = len(schemas) > 0
        
        return metadata
        
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return None

def main():
    base_path = Path("/Volumes/192.168.1.10/Cloned website/https___www.actowizsolutions.com_/www.actowizsolutions.com")
    
    if not base_path.exists():
        print(f"Error: Path {base_path} does not exist")
        return
    
    print("=" * 60)
    print("Phase 1: Extracting SEO Metadata from All HTML Files")
    print("=" * 60)
    print(f"Scanning directory: {base_path}")
    
    # Find all HTML files
    html_files = list(base_path.glob("*.html"))
    total_files = len(html_files)
    print(f"Found {total_files} HTML files\n")
    
    # Extract metadata from all files
    all_metadata = []
    processed = 0
    errors = 0
    
    for html_file in html_files:
        processed += 1
        if processed % 500 == 0:
            print(f"Processed {processed}/{total_files} files... ({len(all_metadata)} extracted, {errors} errors)")
        
        metadata = extract_metadata(html_file)
        if metadata:
            all_metadata.append(metadata)
        else:
            errors += 1
    
    print(f"\n{'=' * 60}")
    print(f"Extraction Complete!")
    print(f"Total files: {total_files}")
    print(f"Successfully extracted: {len(all_metadata)}")
    print(f"Errors: {errors}")
    print(f"{'=' * 60}\n")
    
    # Save to JSON
    output_dir = Path(__file__).parent / "seo_analysis_results"
    output_dir.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = output_dir / f"all_metadata_{timestamp}.json"
    
    print(f"Saving metadata to: {output_file}")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_metadata, f, indent=2, ensure_ascii=False)
    
    file_size_mb = output_file.stat().st_size / (1024 * 1024)
    print(f"Saved {len(all_metadata)} records ({file_size_mb:.2f} MB)")
    print(f"\nNext step: Review {output_file} and categorize pages")
    
    return output_file

if __name__ == "__main__":
    main()
