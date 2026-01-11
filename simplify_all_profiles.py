"""
Simplify profile management across all tools.
Remove complex inline code and add simple auto-fill.js include.
"""

import os
import re
import glob

def simplify_tool(filepath):
    """Remove complex profile code and add simple auto-fill.js"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Skip if already has auto-fill.js
    if 'auto-fill.js' in content:
        print(f"  ⏭️  {os.path.basename(filepath)} - already updated")
        return False
    
    # Remove the massive inline profile management code blocks
    # Pattern 1: // ===== PROFILE MANAGEMENT ... // ===== END PROFILE MANAGEMENT =====
    content = re.sub(
        r'// ===== PROFILE MANAGEMENT.*?// ===== END PROFILE MANAGEMENT =====\s*',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Pattern 2: Remove standalone profile functions that might not be in the block
    patterns_to_remove = [
        r'function autoSaveData\(\)\s*\{[^}]+(?:\{[^}]*\}[^}]*)*\}\s*',
        r'function getAllProfiles\(\)\s*\{[^}]+\}\s*',
        r'function updateProfileDropdown\(\)\s*\{[^}]+(?:\{[^}]*\}[^}]*)*\}\s*',
        r'function onProfileChange\(\)\s*\{[^}]+(?:\{[^}]*\}[^}]*)*\}\s*',
        r'function loadProfile\([^)]*\)\s*\{[^}]+(?:\{[^}]*\}[^}]*)*\}\s*',
        r'function removeCurrentProfile\(\)\s*\{[^}]+(?:\{[^}]*\}[^}]*)*\}\s*',
        r'function loadSavedData\(\)\s*\{[^}]+(?:\{[^}]*\}[^}]*)*\}\s*',
        r'function setupAutoSave\(\)\s*\{[^}]+(?:\{[^}]*\}[^}]*)*\}\s*',
        r'// Initialize on page load\s*window\.addEventListener\([\'"]DOMContentLoaded[\'"],\s*function\(\)\s*\{[^}]+\}\);?\s*',
        r'// Profile Management\s*',
        r'// Load saved data on page load\s*window\.addEventListener.*?loadSavedData.*?\);?\s*',
    ]
    
    for pattern in patterns_to_remove:
        content = re.sub(pattern, '', content, flags=re.DOTALL)
    
    # Remove profile dropdown HTML if present
    content = re.sub(
        r'<div class="profile-section">.*?</div>\s*(?=<div|<form|<button)',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Remove profile select elements
    content = re.sub(
        r'<select id="profileSelect".*?</select>\s*',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Remove profile buttons
    content = re.sub(
        r'<button[^>]*onclick="removeCurrentProfile\(\)"[^>]*>.*?</button>\s*',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Add auto-fill.js before </head>
    if '</head>' in content:
        content = content.replace(
            '</head>',
            '    <script src="auto-fill.js"></script>\n</head>'
        )
    
    # Clean up any leftover empty script blocks or excessive whitespace
    content = re.sub(r'<script>\s*</script>', '', content)
    content = re.sub(r'\n{4,}', '\n\n\n', content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✅ {os.path.basename(filepath)} - simplified")
        return True
    else:
        print(f"  ⏭️  {os.path.basename(filepath)} - no changes needed")
        return False

def main():
    print("🧹 Simplifying profile management across all tools...")
    print()
    
    # Get all HTML files
    html_files = glob.glob('*.html')
    
    # Skip certain files
    skip_files = ['tools_index.html', 'advertise.html', 'reading-loading.html', 'reading-result.html', 'index.html', 'test-astronomy.html']
    
    updated = 0
    for filepath in sorted(html_files):
        if os.path.basename(filepath) in skip_files:
            continue
        if simplify_tool(filepath):
            updated += 1
    
    print()
    print(f"✨ Done! Updated {updated} files.")
    print()
    print("New system:")
    print("  • auto-fill.js handles everything")
    print("  • Form data auto-saves on input")
    print("  • Form data auto-loads on page visit")
    print("  • Same data shared across all tools")
    print("  • No dropdowns, no buttons, just works")

if __name__ == '__main__':
    main()
