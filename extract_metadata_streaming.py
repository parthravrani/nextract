#!/usr/bin/env python3
"""
Extract metadata from HTML files and append to JSON one by one
Memory optimized - doesn't load all data into memory
Saves after each file
"""

import os
import json
from pathlib import Path
from bs4 import BeautifulSoup

def extract_metadata(filepath):
    """Extract title, meta description, and tags from HTML file"""
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
            'h1': [],
            'h2': [],
            'h3': []
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
        
        # Headings
        for h in soup.find_all('h1'):
            text = h.get_text(strip=True)
            if text:
                metadata['h1'].append(text)
        
        for h in soup.find_all('h2'):
            text = h.get_text(strip=True)
            if text:
                metadata['h2'].append(text)
        
        for h in soup.find_all('h3'):
            text = h.get_text(strip=True)
            if text:
                metadata['h3'].append(text)
        
        return metadata
        
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return None

def get_processed_files(tracking_file):
    """Get set of already processed filenames"""
    processed = set()
    if tracking_file.exists():
        try:
            with open(tracking_file, 'r', encoding='utf-8') as f:
                for line in f:
                    filename = line.strip()
                    if filename:
                        processed.add(filename)
        except:
            pass
    return processed

def mark_file_processed(tracking_file, filename):
    """Mark a file as processed"""
    with open(tracking_file, 'a', encoding='utf-8') as f:
        f.write(filename + '\n')

def append_to_json(output_file, metadata):
    """Efficiently append a record to JSON array without loading all data"""
    if not output_file.exists():
        # Create new file with opening bracket
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('[\n')
            json.dump(metadata, f, ensure_ascii=False)
            f.write('\n]')
    else:
        # Read last few bytes to check if we need to add comma
        with open(output_file, 'rb') as f:
            f.seek(0, 2)  # Seek to end
            file_size = f.tell()
            
            # Read last 100 bytes to check format
            if file_size > 100:
                f.seek(file_size - 100)
            else:
                f.seek(0)
            last_bytes = f.read().decode('utf-8', errors='ignore')
        
        # Remove closing bracket
        with open(output_file, 'r+', encoding='utf-8') as f:
            content = f.read()
            # Remove trailing whitespace and closing bracket
            content = content.rstrip().rstrip(']').rstrip()
            
            # Write back with comma if not empty, then new record, then closing bracket
            f.seek(0)
            f.truncate()
            if content and not content.endswith('['):
                f.write(content.rstrip() + ',\n')
            elif not content.endswith('['):
                f.write('[\n')
            
            # Write new record
            json_str = json.dumps(metadata, ensure_ascii=False)
            f.write('  ' + json_str + '\n]')

def main():
    base_path = Path("/Volumes/192.168.1.10/Cloned website/https___www.actowizsolutions.com_/www.actowizsolutions.com")
    output_file = Path(__file__).parent / "all_metadata.json"
    tracking_file = Path(__file__).parent / "processed_files.txt"
    
    if not base_path.exists():
        print(f"Error: Path {base_path} does not exist")
        return
    
    print("Starting metadata extraction (Memory Optimized)...")
    print(f"Source: {base_path}")
    print(f"Output: {output_file}")
    print("-" * 60)
    
    # Find all HTML files
    html_files = list(base_path.glob("*.html"))
    total_files = len(html_files)
    print(f"Found {total_files} HTML files\n")
    
    # Get already processed files (just filenames, not full data)
    processed_files = get_processed_files(tracking_file)
    processed_count = len(processed_files)
    
    if processed_count > 0:
        print(f"Found {processed_count} already processed files")
        print(f"Resuming from file {processed_count + 1}...\n")
    else:
        print("Starting fresh extraction\n")
    
    # Process files one by one
    new_processed = 0
    errors = 0
    
    for i, html_file in enumerate(html_files, 1):
        filename = os.path.basename(html_file)
        
        # Skip if already processed
        if filename in processed_files:
            continue
        
        # Extract metadata
        metadata = extract_metadata(html_file)
        
        if metadata:
            # Append to JSON file efficiently
            append_to_json(output_file, metadata)
            
            # Mark as processed
            mark_file_processed(tracking_file, filename)
            processed_files.add(filename)  # Keep in memory set for quick lookup
            
            new_processed += 1
            
            # Progress update every 50 files
            if new_processed % 50 == 0:
                total_processed = len(processed_files)
                print(f"Processed {new_processed} new files... Total: {total_processed}/{total_files}")
        else:
            errors += 1
        
        # Final status
        if i == total_files:
            total_processed = len(processed_files)
            print(f"\n{'=' * 60}")
            print(f"Complete!")
            print(f"Total files: {total_files}")
            print(f"Successfully extracted: {total_processed}")
            print(f"Errors: {errors}")
            print(f"Output saved to: {output_file}")
            print(f"{'=' * 60}")

if __name__ == "__main__":
    main()
