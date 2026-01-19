#!/usr/bin/env python3
"""
Apply enhanced share buttons to all HTML tool pages.
Replaces the old 3-button layout with a modern 6-button layout including WhatsApp, Email, and SMS.
Also adds the share-utils.js script reference.
"""

import os
import re
from pathlib import Path

# Old share buttons pattern (3 buttons)
OLD_SHARE_BUTTONS = re.compile(
    r'<div class="share-buttons">\s*'
    r'<button class="share-btn" onclick="shareOnTwitter\(\)">[^<]*Twitter</button>\s*'
    r'<button class="share-btn" onclick="shareOnFacebook\(\)">[^<]*Facebook</button>\s*'
    r'<button class="share-btn" onclick="copyLink\(\)">[^<]*Copy Link</button>\s*'
    r'</div>',
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

# Old share functions to remove (we'll keep them in case pages have custom implementations)
OLD_SHARE_FUNCTIONS = re.compile(
    r'function shareOnTwitter\(\)\s*\{[^}]+\}\s*'
    r'function shareOnFacebook\(\)\s*\{[^}]+\}\s*'
    r'function copyLink\(\)\s*\{[^}]+\}',
    re.DOTALL
)

# Script tag to add
SHARE_UTILS_SCRIPT = '<script src="share-utils.js"></script>'

def has_share_utils(content):
    """Check if page already includes share-utils.js"""
    return 'share-utils.js' in content

def add_share_utils_script(content):
    """Add share-utils.js script reference before </head>"""
    if has_share_utils(content):
        return content, False
    
    # Add before </head>
    if '</head>' in content:
        content = content.replace('</head>', f'    {SHARE_UTILS_SCRIPT}\n</head>')
        return content, True
    return content, False

def update_share_buttons(content):
    """Replace old 3-button share layout with new 6-button layout"""
    if 'QMShare.twitter' in content:
        return content, False  # Already updated
    
    # Try to find and replace the old share buttons
    new_content, count = OLD_SHARE_BUTTONS.subn(NEW_SHARE_BUTTONS, content)
    
    if count > 0:
        return new_content, True
    return content, False

def update_css_for_new_buttons(content):
    """Add CSS for emoji-based share buttons if not present"""
    if '.share-btn { min-width:' in content or '.share-btn[title]' in content:
        return content, False
    
    # Find existing share button CSS and enhance it
    old_css = '.share-btn { background: linear-gradient'
    new_css = '''.share-btn { 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border: none;
            color: white;
            padding: 12px 16px;
            border-radius: 12px;
            cursor: pointer;
            font-size: 18px;
            min-width: 50px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        }
        .share-btn:hover {
            transform: translateY(-2px) scale(1.05);
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
        }'''
    
    # Only update if we have the old pattern
    if old_css in content:
        # This is complex, so let's not try to replace inline CSS
        pass
    
    return content, False

def process_file(filepath):
    """Process a single HTML file"""
    filename = filepath.name
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    changes = []
    
    # Add share-utils.js script
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
        print(f"  ⏭️  {filename} - no changes needed")
        return False

def main():
    """Main function to process all HTML files"""
    script_dir = Path(__file__).parent
    
    # Get all HTML files
    html_files = list(script_dir.glob('*.html'))
    
    # Skip certain files
    skip_files = {'index.html', 'advertise.html', 'disclaimer.html', 'forecasts.html', 'privacy.html', 'terms.html', 'reading-loading.html'}
    
    print("\n🔗 Applying Enhanced Share Buttons")
    print("=" * 50)
    
    updated = 0
    skipped = 0
    
    for filepath in sorted(html_files):
        filename = filepath.name
        
        if filename in skip_files:
            continue
        
        # Only process files that have share buttons
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'share-buttons' not in content:
            continue
            
        if process_file(filepath):
            updated += 1
        else:
            skipped += 1
    
    print("=" * 50)
    print(f"✨ Complete! Updated: {updated}, Skipped: {skipped}")
    print("\nShare buttons now include: Twitter/X, Facebook, WhatsApp, Email, SMS, Copy Link")

if __name__ == '__main__':
    main()
