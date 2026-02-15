#!/usr/bin/env python3
"""
Improve styling for code blocks and Related Resources section
"""

from pathlib import Path
import re

def improve_brand_page_styling(brand_file):
    """Add proper styling to brand pages"""
    content = brand_file.read_text(encoding='utf-8')
    
    # Replace Related Resources section with properly styled version
    old_related_section = re.search(
        r'## Related Services\n\n(.*?)(?=\[Start Free Trial|$)',
        content,
        re.DOTALL
    )
    
    if old_related_section:
        # Extract the links
        links = re.findall(r'- \[(.*?)\]\((.*?)\)', old_related_section.group(1))
        
        # Create new styled section
        new_section = '''## Related Resources

<section class="related-resources py-16 bg-gray-50">
  <div class="container mx-auto px-6">
    <div class="grid md:grid-cols-3 gap-8">
      <div>
        <h3 class="text-xl font-bold text-gray-900 mb-4">Platform-Specific Pages</h3>
        <ul class="space-y-3">
'''
        # Add first set of links (platform-specific)
        platform_links = [link for link in links if 'Scraper' in link[0] or 'API' in link[0]][:5]
        for name, url in platform_links:
            new_section += f'          <li><a href="{url}" class="text-blue-600 hover:text-blue-800 font-medium flex items-center gap-2"><i class="ri-arrow-right-s-line"></i>{name}</a></li>\n'
        
        new_section += '''        </ul>
      </div>
      <div>
        <h3 class="text-xl font-bold text-gray-900 mb-4">Geographic Coverage</h3>
        <ul class="space-y-3">
'''
        # Add geographic links
        geo_links = [link for link in links if 'USA' in link[0] or 'India' in link[0] or 'UAE' in link[0]][:3]
        for name, url in geo_links:
            new_section += f'          <li><a href="{url}" class="text-blue-600 hover:text-blue-800 font-medium flex items-center gap-2"><i class="ri-arrow-right-s-line"></i>{name}</a></li>\n'
        
        new_section += '''        </ul>
      </div>
      <div>
        <h3 class="text-xl font-bold text-gray-900 mb-4">Data Intelligence</h3>
        <ul class="space-y-3">
'''
        # Add intelligence links
        intel_links = [link for link in links if 'Intelligence' in link[0]][:3]
        for name, url in intel_links:
            new_section += f'          <li><a href="{url}" class="text-blue-600 hover:text-blue-800 font-medium flex items-center gap-2"><i class="ri-arrow-right-s-line"></i>{name}</a></li>\n'
        
        new_section += '''        </ul>
      </div>
    </div>
  </div>
</section>

'''
        
        # Replace the old section
        content = content.replace(old_related_section.group(0), new_section)
    
    # Improve code block styling - wrap in proper divs
    content = re.sub(
        r'```(\w+)\n(.*?)```',
        r'<div class="code-block bg-gray-900 text-gray-100 p-6 my-6 overflow-x-auto">\n<pre><code class="language-\1">\n\2</code></pre>\n</div>',
        content,
        flags=re.DOTALL
    )
    
    brand_file.write_text(content, encoding='utf-8')

def improve_case_study_styling(case_file):
    """Improve case study page styling"""
    content = case_file.read_text(encoding='utf-8')
    
    # Improve Related Resources section
    content = re.sub(
        r'## Related Resources\n\n(.*?)(?=$)',
        lambda m: '''## Related Resources

<section class="related-resources mt-12 p-8 bg-blue-50 border-l-4 border-blue-600">
  <div class="grid md:grid-cols-3 gap-6">
''' + '\n'.join([
            f'    <div><a href="{url}" class="text-blue-600 hover:text-blue-800 font-bold block"><i class="ri-arrow-right-s-line inline"></i>{name}</a></div>'
            for name, url in re.findall(r'- \[(.*?)\]\((.*?)\)', m.group(1))
        ]) + '\n  </div>\n</section>\n',
        content,
        flags=re.DOTALL
    )
    
    case_file.write_text(content, encoding='utf-8')

def improve_blog_styling(blog_file):
    """Improve blog/intelligence page styling"""
    content = blog_file.read_text(encoding='utf-8')
    
    # Improve Related Resources section
    content = re.sub(
        r'## Related Resources\n\n(.*?)(?=---|\Z)',
        lambda m: '''## Related Resources

<section class="related-resources mt-12 p-8 bg-gray-50">
  <div class="grid md:grid-cols-2 gap-6">
''' + '\n'.join([
            f'    <div><a href="{url}" class="text-blue-600 hover:text-blue-800 font-bold flex items-center gap-2"><i class="ri-arrow-right-s-line"></i>{name}</a></div>'
            for name, url in re.findall(r'- \[(.*?)\]\((.*?)\)', m.group(1))
        ]) + '\n  </div>\n</section>\n\n',
        content,
        flags=re.DOTALL
    )
    
    blog_file.write_text(content, encoding='utf-8')

def main():
    """Improve styling for all pages"""
    script_dir = Path(__file__).parent
    
    print("\n" + "="*60)
    print("Improving Styling & Navigation")
    print("="*60 + "\n")
    
    # Fix brand pages
    print("Fixing Brand Pages...")
    brands_dir = script_dir / "brands"
    for brand_file in brands_dir.glob("*.md"):
        improve_brand_page_styling(brand_file)
        print(f"  ✓ {brand_file.name}")
    
    # Fix case studies
    print("\nFixing Case Studies...")
    case_dir = script_dir / "_case-studies"
    for case_file in case_dir.glob("*.md"):
        improve_case_study_styling(case_file)
        print(f"  ✓ {case_file.name}")
    
    # Fix blog pages
    print("\nFixing Blog/Intelligence Pages...")
    blog_dir = script_dir / "blog"
    for blog_file in blog_dir.glob("*.md"):
        improve_blog_styling(blog_file)
        print(f"  ✓ {blog_file.name}")
    
    print("\n" + "="*60)
    print("✅ Styling Improvements Complete!")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
