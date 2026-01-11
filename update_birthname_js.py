"""
Update JavaScript in all tools to save/load birthName field
"""

import os
import re

files_to_update = [
    'birthday-number-reading.html',
    'destiny-number-calculator.html',
    'karmic-debt-reading.html',
    'life-path-calculator.html',
    'master-number-reading.html',
    'maturity-number-reading.html',
    'name-number-calculator.html',
    'personal-month-reading.html',
    'personal-year-reading.html',
    'personality-number-calculator.html',
    'soul-urge-calculator.html'
]

updated_count = 0

for filename in files_to_update:
    if not os.path.exists(filename):
        continue
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Update saveUserData function
        content = re.sub(
            r'(function saveUserData\(\) \{[\s\S]*?const userData = \{[\s\S]*?preferredName: document\.getElementById\(["\']preferredName["\']\)\.value)',
            r'\1,\n                birthName: document.getElementById(\'birthName\').value',
            content
        )
        
        # Update loadUserData function
        content = re.sub(
            r'(if \(data\.preferredName\) document\.getElementById\(["\']preferredName["\']\)\.value = data\.preferredName;)',
            r'\1\n                if (data.birthName) document.getElementById(\'birthName\').value = data.birthName;',
            content
        )
        
        # Update saveProfile function
        content = re.sub(
            r'(const currentData = \{[\s\S]*?preferredName: document\.getElementById\(["\']preferredName["\']\)\?\.value \|\| ["\']["\'])',
            r'\1,\n                birthName: document.getElementById(\'birthName\')?.value || \'\'',
            content
        )
        
        # Update loadProfile function
        content = re.sub(
            r'(if \(profileData\.preferredName && document\.getElementById\(["\']preferredName["\']\)\) \{[\s\S]*?\})',
            r'''\1
            if (profileData.birthName && document.getElementById('birthName')) {
                document.getElementById('birthName').value = profileData.birthName;
            }''',
            content
        )
        
        if content != original_content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Updated JavaScript: {filename}")
            updated_count += 1
        else:
            print(f"⚠️  No JavaScript changes: {filename}")
            
    except Exception as e:
        print(f"❌ Error processing {filename}: {str(e)}")

print(f"\n🎉 Complete! Updated JavaScript in {updated_count} files")
