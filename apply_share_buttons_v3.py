#!/usr/bin/env python3
"""
Standardize all share buttons to use SVG icons.
Removes Image share button that doesn't work properly.
"""

import os
import re
import glob

# Standard SVG share buttons (6 buttons, no Image)
STANDARD_SHARE_BUTTONS = '''<div class="share-buttons">
                <button class="share-btn" onclick="QMShare.twitter()" title="Share on X (Twitter)"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg></button>
                <button class="share-btn" onclick="QMShare.facebook()" title="Share on Facebook"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg></button>
                <button class="share-btn" onclick="QMShare.whatsapp()" title="Share on WhatsApp"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg></button>
                <button class="share-btn" onclick="QMShare.email()" title="Share via Email"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg></button>
                <button class="share-btn" onclick="QMShare.sms()" title="Share via SMS"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm-2 12H6v-2h12v2zm0-3H6V9h12v2zm0-3H6V6h12v2z"/></svg></button>
                <button class="share-btn" onclick="QMShare.copyLink()" title="Copy Link"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/></svg></button>
            </div>'''

# Pattern to match the entire share-buttons div (handles emoji and SVG versions)
SHARE_BUTTONS_PATTERN = re.compile(
    r'<div class="share-buttons">\s*'
    r'(?:<button[^>]*>[^<]*(?:<svg[^>]*>.*?</svg>)?[^<]*</button>\s*)+'
    r'</div>',
    re.DOTALL
)

# Alternative pattern for inconsistent whitespace
SHARE_BUTTONS_PATTERN2 = re.compile(
    r'<div class="share-buttons">.*?</div>',
    re.DOTALL
)


def update_share_buttons(filepath):
    """Update share buttons in a file to use standard SVG format."""
    try:
        # Try UTF-8 first
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        try:
            # Try with Windows encoding
            with open(filepath, 'r', encoding='cp1252') as f:
                content = f.read()
        except Exception as e:
            print(f"❌ Could not read {filepath}: {e}")
            return False
    
    # Check if file has share-buttons
    if 'share-buttons' not in content:
        return 'no-buttons'
    
    # Check if already uses SVG (and doesn't have image button)
    if 'viewBox="0 0 24 24"' in content and 'shareAsImage' not in content:
        # Check if it has all 6 buttons (not 7 with image)
        svg_count = content.count('viewBox="0 0 24 24"')
        if svg_count == 6:
            return 'already-good'
    
    original = content
    
    # Try to replace share buttons
    match = SHARE_BUTTONS_PATTERN2.search(content)
    if match:
        # Get the indentation
        line_start = content.rfind('\n', 0, match.start()) + 1
        indent = ''
        for char in content[line_start:match.start()]:
            if char in ' \t':
                indent += char
            else:
                break
        
        # Adjust indentation in the replacement
        replacement = STANDARD_SHARE_BUTTONS
        if indent:
            # Replace leading spaces in each line
            lines = replacement.split('\n')
            adjusted_lines = []
            for i, line in enumerate(lines):
                if i == 0:
                    adjusted_lines.append(line)  # First line uses existing indent
                else:
                    # Remove default indent (16 spaces) and add file's indent
                    stripped = line.lstrip()
                    if stripped:
                        adjusted_lines.append(indent + stripped)
                    else:
                        adjusted_lines.append(line)
            replacement = '\n'.join(adjusted_lines)
        
        content = content[:match.start()] + replacement + content[match.end():]
    
    if content != original:
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        except Exception as e:
            print(f"❌ Could not write {filepath}: {e}")
            return False
    
    return 'unchanged'


def main():
    print("🔧 Standardizing share buttons across all tools...")
    print("=" * 60)
    
    # Get all HTML files in root
    html_files = glob.glob('*.html')
    
    updated = 0
    already_good = 0
    no_buttons = 0
    unchanged = 0
    failed = 0
    
    for filepath in sorted(html_files):
        result = update_share_buttons(filepath)
        
        if result == True:
            print(f"✅ Updated: {filepath}")
            updated += 1
        elif result == 'already-good':
            print(f"✓ Already standard: {filepath}")
            already_good += 1
        elif result == 'no-buttons':
            # Silent skip for files without share buttons
            no_buttons += 1
        elif result == 'unchanged':
            print(f"⚠️  Unchanged (check manually): {filepath}")
            unchanged += 1
        else:
            failed += 1
    
    print("=" * 60)
    print(f"\n🎉 Share button standardization complete!")
    print(f"   ✅ Updated to SVG: {updated}")
    print(f"   ✓ Already standard: {already_good}")
    print(f"   📄 No share buttons: {no_buttons}")
    print(f"   ⚠️  Needs manual check: {unchanged}")
    print(f"   ❌ Failed: {failed}")


if __name__ == '__main__':
    main()
