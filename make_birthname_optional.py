"""
Make birthName optional and check for JavaScript issues in all forms
"""

import os
import re

files_to_fix = [
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
    'soul-urge-calculator.html',
    'moon-sign-reading.html',
    'rising-sign-reading.html'
]

fixed_count = 0

for filename in files_to_fix:
    if not os.path.exists(filename):
        print(f"⏭️  Skipped: {filename} (not found)")
        continue
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Make birthName optional by removing required attribute
        content = re.sub(
            r'(<input[^>]*id="birthName"[^>]*)\s+required([^>]*>)',
            r'\1\2',
            content
        )
        
        # Also check if there are any escaped quotes in JavaScript
        content = re.sub(
            r"getElementById\(\\'",
            r"getElementById('",
            content
        )
        content = re.sub(
            r"\\'\)",
            r"')",
            content
        )
        content = re.sub(
            r"\\'\\',",
            r"'',",
            content
        )
        
        if content != original_content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Fixed: {filename}")
            fixed_count += 1
        else:
            print(f"⏭️  No changes needed: {filename}")
            
    except Exception as e:
        print(f"❌ Error processing {filename}: {str(e)}")

print(f"\n🎉 Fixed {fixed_count} files - birthName is now optional")
