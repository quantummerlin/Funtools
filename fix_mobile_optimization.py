#!/usr/bin/env python3
"""
Fix mobile optimization and centering across all HTML tool pages.
Updates container styles to be properly responsive and centered.
"""

import os
import re
from pathlib import Path

def fix_container_styles(content, filename):
    """Add width: 100% and padding to container styles for mobile"""
    changes = []
    
    # Pattern: .container { max-width: Xpx; margin: 0 auto; }
    old_pattern = r'\.container\s*\{\s*max-width:\s*(\d+)px;\s*margin:\s*0\s+auto;\s*\}'
    
    def replacement(match):
        max_width = match.group(1)
        return f'.container {{ max-width: {max_width}px; width: 100%; margin: 0 auto; padding: 0 15px; }}'
    
    new_content, count = re.subn(old_pattern, replacement, content)
    if count > 0:
        changes.append(f'fixed container ({count})')
    
    return new_content, changes

def ensure_text_center(content):
    """Ensure headers and results are properly centered"""
    changes = []
    
    # Make sure .header has text-align: center
    if '.header {' in content and 'text-align: center' not in content.split('.header {')[1].split('}')[0]:
        # Header exists but might not be centered - this is complex, skip for now
        pass
    
    return content, changes

def add_mobile_viewport_meta(content):
    """Ensure proper viewport meta tag exists"""
    if 'viewport' not in content:
        # Add viewport meta after charset
        content = content.replace(
            '<meta charset="UTF-8">',
            '<meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">'
        )
        return content, ['added viewport meta']
    return content, []

def process_file(filepath):
    """Process a single HTML file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    all_changes = []
    
    # Fix container styles
    content, changes = fix_container_styles(content, filepath.name)
    all_changes.extend(changes)
    
    # Add viewport if missing
    content, changes = add_mobile_viewport_meta(content)
    all_changes.extend(changes)
    
    if all_changes:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✅ {filepath.name} - {', '.join(all_changes)}")
        return True
    
    return False

def main():
    script_dir = Path(__file__).parent
    html_files = list(script_dir.glob('*.html'))
    
    # Skip certain files
    skip_files = {'index.html', 'tools_index.html', 'advertise.html'}
    
    print("\n📱 Fixing Mobile Optimization & Centering")
    print("=" * 50)
    
    updated = 0
    
    for filepath in sorted(html_files):
        if filepath.name in skip_files:
            continue
        
        if process_file(filepath):
            updated += 1
    
    print("=" * 50)
    print(f"✨ Complete! Updated: {updated} files")

if __name__ == '__main__':
    main()
