#!/usr/bin/env python3
"""
Add Google Analytics code to all HTML files in the funtools directory.
"""
import os
import re
from pathlib import Path

# Your GA4 tracking ID
GA_TRACKING_ID = "G-VW4LGE7L1T"

# The GA code to insert
GA_CODE = f'''    <!-- Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id={GA_TRACKING_ID}"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){{dataLayer.push(arguments);}}
        gtag('js', new Date());
        gtag('config', '{GA_TRACKING_ID}');
    </script>
    <!-- End Google Analytics -->
'''

def add_ga_to_file(filepath):
    """Add GA code to a single HTML file if not already present."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if GA is already present
        if GA_TRACKING_ID in content:
            print(f"  Skipped (already has GA): {filepath.name}")
            return False
        
        # Find the <head> tag and insert GA code right after it
        # Match <head> with optional attributes
        head_pattern = r'(<head[^>]*>)'
        match = re.search(head_pattern, content, re.IGNORECASE)
        
        if match:
            # Insert GA code right after <head>
            insert_pos = match.end()
            new_content = content[:insert_pos] + '\n' + GA_CODE + content[insert_pos:]
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"  Added GA to: {filepath.name}")
            return True
        else:
            print(f"  No <head> tag found in: {filepath.name}")
            return False
            
    except Exception as e:
        print(f"  Error processing {filepath.name}: {e}")
        return False

def main():
    # Get the directory where this script is located
    script_dir = Path(__file__).parent
    
    # Find all HTML files
    html_files = list(script_dir.glob('*.html'))
    
    print(f"Found {len(html_files)} HTML files")
    print("-" * 50)
    
    added_count = 0
    skipped_count = 0
    
    for html_file in sorted(html_files):
        if add_ga_to_file(html_file):
            added_count += 1
        else:
            skipped_count += 1
    
    print("-" * 50)
    print(f"Done! Added GA to {added_count} files, skipped {skipped_count} files")

if __name__ == "__main__":
    main()
