#!/usr/bin/env python3
"""
Apply PWA meta tags to all HTML files for maximum PWA experience
"""
import os
import re
from pathlib import Path

# PWA meta tags to add (right after theme-color or after viewport)
PWA_META_TAGS = '''    <meta name="theme-color" content="#bf5af2">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="Quantum Merlin">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="application-name" content="Quantum Merlin">
    <meta name="msapplication-TileColor" content="#bf5af2">
    <meta name="msapplication-navbutton-color" content="#bf5af2">
    <meta name="format-detection" content="telephone=no">
    <link rel="apple-touch-icon" href="RetroMerlin.jpg">
    <link rel="manifest" href="manifest.json">'''

# Files to skip
SKIP_FILES = {
    'reading-loading.html',  # Redirect page
    'apply_pwa_meta.py',
}

def process_html_file(filepath):
    """Add PWA meta tags to an HTML file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Check if already has apple-mobile-web-app-capable
        if 'apple-mobile-web-app-capable' in content:
            return False, "Already has PWA meta tags"
        
        # Strategy 1: Replace existing theme-color meta tag
        if '<meta name="theme-color"' in content:
            # Remove any existing manifest link and apple-touch-icon first
            content = re.sub(r'\s*<link rel="manifest"[^>]*>\n?', '', content)
            content = re.sub(r'\s*<link rel="apple-touch-icon"[^>]*>\n?', '', content)
            
            # Replace theme-color with full PWA block
            content = re.sub(
                r'<meta name="theme-color"[^>]*>',
                PWA_META_TAGS,
                content
            )
        
        # Strategy 2: Add after viewport meta tag
        elif '<meta name="viewport"' in content:
            # Remove any existing manifest link and apple-touch-icon first
            content = re.sub(r'\s*<link rel="manifest"[^>]*>\n?', '', content)
            content = re.sub(r'\s*<link rel="apple-touch-icon"[^>]*>\n?', '', content)
            
            # Add after viewport
            content = re.sub(
                r'(<meta name="viewport"[^>]*>)',
                r'\1\n' + PWA_META_TAGS,
                content
            )
        
        # Strategy 3: Add after charset
        elif '<meta charset=' in content:
            content = re.sub(
                r'(<meta charset=[^>]*>)',
                r'\1\n' + PWA_META_TAGS + '\n    <link rel="manifest" href="manifest.json">',
                content
            )
        else:
            return False, "Could not find insertion point"
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, "Added PWA meta tags"
        
        return False, "No changes made"
        
    except Exception as e:
        return False, f"Error: {e}"

def main():
    workspace = Path('.')
    html_files = list(workspace.glob('*.html'))
    
    updated = 0
    skipped = 0
    failed = 0
    
    print("=" * 60)
    print("APPLYING PWA META TAGS TO ALL HTML FILES")
    print("=" * 60)
    
    for filepath in sorted(html_files):
        if filepath.name in SKIP_FILES:
            print(f"⏭️  SKIP: {filepath.name}")
            skipped += 1
            continue
        
        success, message = process_html_file(filepath)
        
        if success:
            print(f"✅ {filepath.name}: {message}")
            updated += 1
        elif "Already has" in message:
            print(f"⏭️  SKIP: {filepath.name} - {message}")
            skipped += 1
        else:
            print(f"❌ {filepath.name}: {message}")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"SUMMARY: Updated {updated}, Skipped {skipped}, Failed {failed}")
    print("=" * 60)

if __name__ == "__main__":
    main()
