"""
Comprehensive fix for all birthName HTML structure issues
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
        
        # Remove the malformed orphaned helper text div
        content = re.sub(
            r'<div class="input-group"><div class="helper-text">(Optional but provides deeper insights into your soul\'s blueprint|As it appears on your birth certificate)</div>[\s\S]*?</div>',
            '',
            content
        )
        
        # Clean up any double line breaks
        content = re.sub(r'\n\n\n+', '\n\n', content)
        
        if content != original_content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Cleaned up: {filename}")
            fixed_count += 1
        else:
            print(f"⏭️  Already clean: {filename}")
            
    except Exception as e:
        print(f"❌ Error processing {filename}: {str(e)}")

print(f"\n🎉 Cleaned up {fixed_count} files")
print("\nNow testing forms...")
