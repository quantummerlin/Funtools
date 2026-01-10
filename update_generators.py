#!/usr/bin/env python3
"""
Update generator scripts to not include birthName fields
"""

import re
import os

GENERATOR_FILES = [
    'generate_premium_tools.py',
    'generate_birthday_personalyear.py',
    'generate_month_maturity.py', 
    'generate_karmic_master.py',
    'generate_moon_sign.py',
    'generate_rising_sign.py',
]

def update_generator(filepath):
    """Remove birthName field generation from generator scripts"""
    if not os.path.exists(filepath):
        print(f"⚠️  File not found: {filepath}")
        return False
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Remove birthName label and input in templates
    content = re.sub(
        r'<label for="birthName">.*?</label>\s*<input[^>]*id="birthName"[^>]*>',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Remove helper text mentioning birth name
    content = re.sub(
        r'<div class="helper-text">.*?birth name.*?</div>',
        '',
        content,
        flags=re.DOTALL | re.IGNORECASE
    )
    
    # Update JavaScript generation
    content = re.sub(
        r"const birthName = document\.getElementById\('birthName'\)\.value \|\| preferredName;",
        "const birthName = preferredName;",
        content
    )
    
    # Remove birthName from profile saves
    content = re.sub(
        r"birthName: document\.getElementById\('birthName'\)(\?)?\.value( \|\| '')?",
        "// birthName removed",
        content
    )
    
    # Remove birthName loading
    content = re.sub(
        r"if \(data\.birthName\) document\.getElementById\('birthName'\)\.value = data\.birthName;",
        "// birthName removed",
        content
    )
    
    content = re.sub(
        r"if \(document\.getElementById\('birthName'\) && data\.birthName\) \{\{?\s*document\.getElementById\('birthName'\)\.value = data\.birthName;\s*\}\}?",
        "// birthName removed",
        content
    )
    
    content = re.sub(
        r"if \(profileData\.birthName && document\.getElementById\('birthName'\)\) \{\{?\s*document\.getElementById\('birthName'\)\.value = profileData\.birthName;\s*\}\}?",
        "// birthName removed",
        content
    )
    
    # Remove userData birthName
    content = re.sub(
        r"userData\.birthName = document\.getElementById\('birthName'\)\.value;",
        "// birthName removed",
        content
    )
    
    content = re.sub(
        r"if \(document\.getElementById\('birthName'\)\) \{\{?\s*userData\.birthName = document\.getElementById\('birthName'\)\.value;\s*\}\}?",
        "// birthName removed",
        content
    )
    
    # Remove saveUserData birthName
    content = re.sub(
        r"birthName: document\.getElementById\('birthName'\)\.value,",
        "// birthName removed",
        content
    )
    
    # Remove clearing birthName
    content = re.sub(
        r"document\.getElementById\('birthName'\)\.value = '';",
        "// birthName removed",
        content
    )
    
    # Update any template strings mentioning birth name in readings
    content = re.sub(
        r'Your (full )?birth name carries',
        'Your name carries',
        content
    )
    
    content = re.sub(
        r'birth name carries',
        'name carries',
        content
    )
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Updated: {filepath}")
        return True
    else:
        print(f"ℹ️  No changes: {filepath}")
        return False

def main():
    print("🔧 Updating generator scripts...")
    print("=" * 60)
    
    updated = 0
    for filename in GENERATOR_FILES:
        if update_generator(filename):
            updated += 1
    
    print("=" * 60)
    print(f"✨ Updated {updated} generator scripts")
    print("\n💡 Future generated tools will use preferredName only")

if __name__ == '__main__':
    main()
