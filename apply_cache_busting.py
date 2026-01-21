"""
Cache Busting System for Quantum Merlin Tools
Adds version timestamps to all HTML files to ensure users get latest updates
"""

import os
import re
from datetime import datetime

# Get current timestamp for version
VERSION = datetime.now().strftime('%Y%m%d%H%M%S')

print(f"🔄 Applying cache busting with version: {VERSION}\n")

# Update service worker version
if os.path.exists('sw.js'):
    try:
        with open('sw.js', 'r', encoding='utf-8') as f:
            sw_content = f.read()
        
        sw_content = re.sub(
            r"const CACHE_VERSION = '[^']*';",
            f"const CACHE_VERSION = '{VERSION}';",
            sw_content
        )
        
        with open('sw.js', 'w', encoding='utf-8') as f:
            f.write(sw_content)
        
        print(f"✅ Updated service worker version\n")
    except Exception as e:
        print(f"⚠️  Could not update service worker: {str(e)}\n")

# Get all HTML files
html_files = [f for f in os.listdir('.') if f.endswith('.html')]

updates_count = 0

for filename in html_files:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Add/Update cache control meta tags in head
        meta_cache_tags = f'''    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="0">
    <meta name="version" content="{VERSION}">'''
        
        # Check if cache meta tags already exist
        if 'Cache-Control' in content and 'no-cache' in content:
            # Update existing version
            content = re.sub(
                r'<meta name="version" content="[^"]*">',
                f'<meta name="version" content="{VERSION}">',
                content
            )
        else:
            # Add cache control after charset meta tag
            content = re.sub(
                r'(<meta charset="UTF-8">)',
                f'\\1\n{meta_cache_tags}',
                content
            )
        
        # Add version query string to astronomy-engine library if present
        if 'astronomy-engine' in content:
            content = re.sub(
                r'astronomy\.browser\.min\.js"',
                f'astronomy.browser.min.js?v={VERSION}"',
                content
            )
        
        # Add version query string to share-utils.js
        content = re.sub(
            r'share-utils\.js(\?v=[^"]*)?',
            f'share-utils.js?v={VERSION}',
            content
        )
        
        # Add version query string to tool-tracker.js
        content = re.sub(
            r'tool-tracker\.js(\?v=[^"]*)?',
            f'tool-tracker.js?v={VERSION}',
            content
        )
        
        # Add version query string to Google Fonts (optional, they handle their own caching)
        content = re.sub(
            r'(fonts\.googleapis\.com/css2\?[^"]+)"',
            f'\\1&v={VERSION}"',
            content
        )
        
        # Add version comment at the top of script tags
        if '<script>' in content:
            content = re.sub(
                r'(<script>)',
                f'\\1\n        // Version: {VERSION} - Auto-generated cache buster',
                content,
                count=1
            )
        
        # Only write if content changed
        if content != original_content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Updated: {filename}")
            updates_count += 1
        else:
            print(f"⏭️  Skipped: {filename} (no changes needed)")
            
    except Exception as e:
        print(f"❌ Error processing {filename}: {str(e)}")

print(f"\n🎉 Cache busting complete! Updated {updates_count} files with version {VERSION}")
print(f"\nNext steps:")
print(f"  1. Commit these changes: git add .")
print(f"  2. Push to GitHub: git push")
print(f"  3. Users will get fresh content immediately!")
