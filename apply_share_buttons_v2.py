#!/usr/bin/env python3
"""
Apply enhanced share buttons to ALL HTML files - more robust version.
Handles different HTML patterns (buttons and anchor tags).
"""

import os
import re
from pathlib import Path

# Pattern for anchor tag based share buttons (3 or more buttons)
ANCHOR_SHARE_PATTERN = re.compile(
    r'(<div class="share-buttons">\s*)'
    r'(<a\s+href="#"[^>]*onclick="shareOnTwitter\(\)[^"]*"[^>]*>[^<]*</a>\s*)'
    r'(<a\s+href="#"[^>]*onclick="shareOnFacebook\(\)[^"]*"[^>]*>[^<]*</a>\s*)'
    r'(<a\s+href="#"[^>]*onclick="copyLink\(\)[^"]*"[^>]*>[^<]*</a>\s*)'
    r'(</div>)',
    re.IGNORECASE | re.DOTALL
)

# New enhanced share buttons HTML (6 buttons)
NEW_SHARE_BUTTONS = '''<div class="share-buttons">
                <button class="share-btn" onclick="QMShare.twitter()" title="Share on Twitter/X">𝕏</button>
                <button class="share-btn" onclick="QMShare.facebook()" title="Share on Facebook">📘</button>
                <button class="share-btn" onclick="QMShare.whatsapp()" title="Share on WhatsApp">💬</button>
                <button class="share-btn" onclick="QMShare.email()" title="Share via Email">✉️</button>
                <button class="share-btn" onclick="QMShare.sms()" title="Share via SMS">📱</button>
                <button class="share-btn" onclick="QMShare.copyLink()" title="Copy Link">📋</button>
            </div>'''

# Script tag to add
SHARE_UTILS_SCRIPT = '<script src="share-utils.js"></script>'

def has_share_utils(content):
    """Check if page already includes share-utils.js"""
    return 'share-utils.js' in content

def add_share_utils_script(content):
    """Add share-utils.js script reference before </head>"""
    if has_share_utils(content):
        return content, False
    
    if '</head>' in content:
        content = content.replace('</head>', f'    {SHARE_UTILS_SCRIPT}\n</head>')
        return content, True
    return content, False

def update_share_buttons(content):
    """Replace old share buttons with new ones"""
    if 'QMShare.twitter' in content:
        return content, False  # Already updated
    
    # Try anchor pattern
    new_content, count = ANCHOR_SHARE_PATTERN.subn(NEW_SHARE_BUTTONS, content)
    if count > 0:
        return new_content, True
    
    return content, False

def process_file(filepath):
    """Process a single HTML file"""
    filename = filepath.name
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Only process files with old share buttons
    if 'shareOnTwitter' not in content or 'QMShare.twitter' in content:
        return False
    
    changes = []
    
    # Add share-utils.js script if needed
    content, added_script = add_share_utils_script(content)
    if added_script:
        changes.append('added share-utils.js')
    
    # Update share buttons
    content, updated_buttons = update_share_buttons(content)
    if updated_buttons:
        changes.append('updated share buttons')
    
    if changes:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✅ {filename} - {', '.join(changes)}")
        return True
    else:
        # File has old buttons but pattern didn't match - report it
        print(f"  ⚠️  {filename} - has old share buttons but pattern didn't match")
        return False

def main():
    """Main function"""
    script_dir = Path(__file__).parent
    html_files = list(script_dir.glob('*.html'))
    
    print("\n🔗 Applying Enhanced Share Buttons (Round 2)")
    print("=" * 50)
    
    updated = 0
    
    for filepath in sorted(html_files):
        if process_file(filepath):
            updated += 1
    
    print("=" * 50)
    print(f"✨ Complete! Updated: {updated}")

if __name__ == '__main__':
    main()
