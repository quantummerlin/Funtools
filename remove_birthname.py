#!/usr/bin/env python3
"""
Remove birthName fields from all premium tools
Use preferredName for all name-based calculations instead
"""

import re
import os

# List of HTML files that have birthName fields
FILES_TO_UPDATE = [
    'moon-sign-reading.html',
    'rising-sign-reading.html',
    'personal-year-reading.html',
    'personal-month-reading.html',
    'maturity-number-reading.html',
    'master-number-reading.html',
    'karmic-debt-reading.html',
    'birthday-number-reading.html',
    'soul-urge-calculator.html',
    'personality-number-calculator.html',
    'destiny-number-calculator.html',
    'name-number-calculator.html',
    'life-path-calculator.html',
]

def remove_birthname_field(content):
    """Remove the birthName form field and label"""
    # Remove the div containing birthName label and input
    content = re.sub(
        r'<div>\s*<label for="birthName">.*?</label>\s*<input[^>]*id="birthName"[^>]*>\s*</div>\s*',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Also handle the case with spacing variations
    content = re.sub(
        r'\s*<label for="birthName">.*?</label>\s*<input[^>]*id="birthName"[^>]*>\s*',
        '',
        content,
        flags=re.DOTALL
    )
    
    return content

def update_javascript(content):
    """Update JavaScript to remove birthName references"""
    
    # Replace: const birthName = document.getElementById('birthName').value || preferredName;
    # With: const birthName = preferredName;
    content = re.sub(
        r"const birthName = document\.getElementById\('birthName'\)\.value \|\| preferredName;",
        "const birthName = preferredName;",
        content
    )
    
    # Replace birthName in localStorage saves
    content = re.sub(
        r"birthName: document\.getElementById\('birthName'\)(\?)?\.value( \|\| '')?",
        "// birthName removed - using preferredName for all calculations",
        content
    )
    
    # Remove birthName from profile data loading
    content = re.sub(
        r"if \(profileData\.birthName && document\.getElementById\('birthName'\)\) \{\s*document\.getElementById\('birthName'\)\.value = profileData\.birthName;\s*\}",
        "// birthName field removed",
        content
    )
    
    # Remove birthName from localStorage loading
    content = re.sub(
        r"if \(data\.birthName\) document\.getElementById\('birthName'\)\.value = data\.birthName;",
        "// birthName field removed",
        content
    )
    
    content = re.sub(
        r"if \(document\.getElementById\('birthName'\) && data\.birthName\) \{\s*document\.getElementById\('birthName'\)\.value = data\.birthName;\s*\}",
        "// birthName field removed",
        content
    )
    
    # Remove birthName from userData saves
    content = re.sub(
        r"if \(document\.getElementById\('birthName'\)\) \{\s*userData\.birthName = document\.getElementById\('birthName'\)\.value;\s*\}",
        "// birthName field removed",
        content
    )
    
    content = re.sub(
        r"userData\.birthName = document\.getElementById\('birthName'\)\.value;",
        "// birthName field removed",
        content
    )
    
    # Remove clearing birthName
    content = re.sub(
        r"document\.getElementById\('birthName'\)\.value = '';",
        "// birthName field removed",
        content
    )
    
    # Remove birthName from saveUserData
    content = re.sub(
        r"birthName: document\.getElementById\('birthName'\)\.value,",
        "// birthName removed",
        content
    )
    
    return content

def update_helper_text(content):
    """Update helper text to remove birthName references"""
    # Remove helper text mentioning birth name
    content = re.sub(
        r'<div class="helper-text">Use the name that feels most authentic to you - this could be your birth name, chosen name, or nickname</div>',
        '',
        content
    )
    return content

def process_file(filepath):
    """Process a single file"""
    if not os.path.exists(filepath):
        print(f"⚠️  File not found: {filepath}")
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Apply transformations
    content = remove_birthname_field(content)
    content = update_javascript(content)
    content = update_helper_text(content)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Updated: {filepath}")
        return True
    else:
        print(f"ℹ️  No changes: {filepath}")
        return False

def main():
    print("🔧 Removing birthName fields from premium tools...")
    print("=" * 60)
    
    updated_count = 0
    for filename in FILES_TO_UPDATE:
        if process_file(filename):
            updated_count += 1
    
    print("=" * 60)
    print(f"✨ Complete! Updated {updated_count} files")
    print("\n💡 Note: birthName calculations now use preferredName")

if __name__ == '__main__':
    main()
