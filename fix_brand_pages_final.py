#!/usr/bin/env python3
"""
Final fix for brand pages - fix front matter and breadcrumbs
"""

from pathlib import Path
import re

def fix_brand_page(brand_file):
    """Fix a single brand page"""
    content = brand_file.read_text(encoding='utf-8')
    
    # Fix the closing --- issue and remove .html from breadcrumbs
    content = re.sub(r'url: "([^"]+)\.html"---', r'url: "\1"\n---', content)
    content = re.sub(r'url: "([^"]+)\.html"', r'url: "\1"', content)
    
    brand_file.write_text(content, encoding='utf-8')

def main():
    """Fix all brand pages"""
    script_dir = Path(__file__).parent
    brands_dir = script_dir / "brands"
    
    print("\n" + "="*60)
    print("Final Fix for Brand Pages")
    print("="*60 + "\n")
    
    count = 0
    for brand_file in brands_dir.glob("*.md"):
        fix_brand_page(brand_file)
        count += 1
        print(f"  ✓ Fixed {brand_file.name}")
    
    print(f"\n  Total: {count} brand pages fixed")
    print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    main()
