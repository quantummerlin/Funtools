"""
Add birthName field back to all tools with forms
The birth name carries the energy that was put into your being
"""

import os
import re

# Files that need birthName field added
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

birthname_field = '''
                    <div class="input-group">
                        <label for="birthName">Birth Name</label>
                        <input type="text" id="birthName" required>
                        <div class="helper-text">The name given to you at birth - carries the energy of your naming</div>
                    </div>
'''

updated_count = 0

for filename in files_to_update:
    if not os.path.exists(filename):
        print(f"⏭️  Skipped: {filename} (not found)")
        continue
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if birthName already exists
        if 'id="birthName"' in content:
            print(f"✅ Already has birthName: {filename}")
            continue
        
        # Find preferredName input and add birthName after it
        pattern = r'(<div class="input-group">[\s\S]*?<label for="preferredName">.*?</label>[\s\S]*?</div>)'
        
        def add_birthname(match):
            return match.group(1) + birthname_field
        
        new_content = re.sub(pattern, add_birthname, content, count=1)
        
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ Updated: {filename}")
            updated_count += 1
        else:
            print(f"⚠️  Pattern not found: {filename}")
            
    except Exception as e:
        print(f"❌ Error processing {filename}: {str(e)}")

print(f"\n🎉 Complete! Updated {updated_count} files")
print("\nNext: Update JavaScript to save/load birthName in each file")
