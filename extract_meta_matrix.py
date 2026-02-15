#!/usr/bin/env python3
"""
Extract title and description from all markdown files and create SEO metadata matrix
"""

import os
import re
from pathlib import Path

def extract_frontmatter(file_path):
    """Extract YAML frontmatter from markdown file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file has frontmatter
        if not content.startswith('---'):
            return None, None
        
        # Extract frontmatter (between first --- and second ---)
        match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if not match:
            return None, None
        
        frontmatter_text = match.group(1)
        
        # Parse title and description using regex (simple YAML parsing)
        title = None
        description = None
        
        # Match title: "value" or title: value
        title_match = re.search(r'^title:\s*(.+)$', frontmatter_text, re.MULTILINE)
        if title_match:
            title = title_match.group(1).strip()
            # Remove quotes if present
            if title.startswith('"') and title.endswith('"'):
                title = title[1:-1]
            elif title.startswith("'") and title.endswith("'"):
                title = title[1:-1]
        
        # Match description: "value" or description: value (may span multiple lines)
        desc_match = re.search(r'^description:\s*(.+?)(?=\n\w+:|$)', frontmatter_text, re.MULTILINE | re.DOTALL)
        if desc_match:
            description = desc_match.group(1).strip()
            # Remove quotes if present
            if description.startswith('"') and description.endswith('"'):
                description = description[1:-1]
            elif description.startswith("'") and description.endswith("'"):
                description = description[1:-1]
            # Clean up multi-line descriptions
            description = re.sub(r'\n\s+', ' ', description)
        
        return title or '', description or ''
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None, None

def main():
    """Main function to extract metadata from all markdown files"""
    base_dir = Path(__file__).parent
    md_files = []
    
    # Find all markdown files
    for md_file in base_dir.rglob('*.md'):
        # Skip certain directories/files
        if any(skip in str(md_file) for skip in ['node_modules', '.git', '_site', 'vendor']):
            continue
        md_files.append(md_file)
    
    # Sort files by path
    md_files.sort()
    
    # Extract metadata
    metadata_list = []
    for md_file in md_files:
        relative_path = md_file.relative_to(base_dir)
        result = extract_frontmatter(md_file)
        
        # Only include files with frontmatter (result is not None)
        if result is not None:
            title, description = result
            title_length = len(title) if title else 0
            metadata_list.append({
                'file_path': str(relative_path),
                'title': title or '',
                'description': description or '',
                'title_length': title_length
            })
    
    # Generate markdown table
    from datetime import datetime
    output_lines = [
        "# SEO Metadata Matrix",
        "",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "This matrix contains all title and description metadata from markdown files for SEO audit.",
        "",
        "| File Path | Title Length | Current Title | Current Description | 2026 Audit Notes | Proposed New Title | Proposed New Desc |",
        "|-----------|-------------|---------------|---------------------|------------------|-------------------|-------------------|"
    ]
    
    for meta in metadata_list:
        # Escape pipe characters and newlines in content for markdown table
        file_path = meta['file_path'].replace('|', '\\|')
        title = meta['title'].replace('|', '\\|').replace('\n', ' ').replace('\r', ' ')
        description = meta['description'].replace('|', '\\|').replace('\n', ' ').replace('\r', ' ')
        title_length = str(meta['title_length'])
        
        # Use full description (no truncation)
        output_lines.append(
            f"| `{file_path}` | {title_length} | {title} | {description} | | | |"
        )
    
    # Write to file
    output_file = base_dir / 'SEO_META_MATRIX.md'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_lines))
    
    print(f"✅ Generated SEO_META_MATRIX.md with {len(metadata_list)} files")
    print(f"📄 Output file: {output_file}")

if __name__ == '__main__':
    main()
