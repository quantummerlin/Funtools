"""
Fix malformed HTML structure caused by birthName field insertion
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
    'soul-urge-calculator.html'
]

fixed_count = 0

for filename in files_to_fix:
    if not os.path.exists(filename):
        continue
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix the malformed structure around birthName
        # Look for the pattern where birthName div was improperly inserted
        content = re.sub(
            r'(<div class="input-group">[\s\S]*?<label for="preferredName">.*?</label>[\s\S]*?<input[^>]*id="preferredName"[^>]*>[\s\S]*?<div class="helper-text">.*?</div>)[\s\S]*?(<div class="input-group">[\s\S]*?<label for="birthName">.*?</label>[\s\S]*?<input[^>]*id="birthName"[^>]*>[\s\S]*?<div class="helper-text">.*?</div>[\s\S]*?</div>)[\s\S]*?(</div>[\s\S]*?<div class="input-group"><div class="helper-text">)',
            r'\1\n\n                    \2\n                    </div>\n\n                    <div class="input-group">',
            content,
            count=1
        )
        
        # Remove orphaned helper text div
        content = re.sub(
            r'<div class="input-group"><div class="helper-text">As it appears on your birth certificate</div>[\s\S]*?</div>',
            '',
            content
        )
        
        if content != original_content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Fixed HTML structure: {filename}")
            fixed_count += 1
        else:
            print(f"⏭️  No structural issues: {filename}")
            
    except Exception as e:
        print(f"❌ Error processing {filename}: {str(e)}")

print(f"\n🎉 Fixed {fixed_count} files")
