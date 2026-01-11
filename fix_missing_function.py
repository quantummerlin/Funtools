#!/usr/bin/env python3
"""
Fix missing loadSavedData function in reading tools.
The update script accidentally removed this function.
"""

import os
import re

# Files that need fixing
files_to_fix = [
    'birthday-number-reading.html',
    'personal-year-reading.html', 
    'personal-month-reading.html',
    'maturity-number-reading.html',
    'karmic-debt-reading.html',
    'master-number-reading.html',
    'moon-sign-reading.html',
    'rising-sign-reading.html'
]

# The missing loadSavedData function
LOAD_SAVED_DATA_FUNCTION = '''
        // Load saved data from localStorage (cross-tool persistence)
        function loadSavedData() {
            const savedData = localStorage.getItem('quantumMerlinUserData');
            if (savedData) {
                const data = JSON.parse(savedData);
                
                if (document.getElementById('preferredName') && data.preferredName) {
                    document.getElementById('preferredName').value = data.preferredName;
                }
                if (document.getElementById('birthName') && data.birthName) {
                    document.getElementById('birthName').value = data.birthName;
                }
                if (document.getElementById('birthDate') && data.birthDate) {
                    document.getElementById('birthDate').value = data.birthDate;
                }
                if (document.getElementById('birthTime') && data.birthTime) {
                    document.getElementById('birthTime').value = data.birthTime;
                }
                if (document.getElementById('birthPlace') && data.birthPlace) {
                    document.getElementById('birthPlace').value = data.birthPlace;
                }
            }
            
            // Update profile dropdown
            updateProfileDropdown();
        }
'''

def fix_file(filepath):
    """Fix a single file by adding the missing loadSavedData function."""
    if not os.path.exists(filepath):
        print(f"  ⚠ File not found: {filepath}")
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if function is already properly defined
    if 'function loadSavedData()' in content:
        print(f"  ✓ Already has loadSavedData function")
        return False
    
    # Find the broken pattern and replace it
    # Pattern: "// Load saved data from localStorage (cross-tool persistence)\n        // Update profile dropdown"
    broken_pattern = r"// Load saved data from localStorage \(cross-tool persistence\)\s*\n\s*// Update profile dropdown\s*\n\s*updateProfileDropdown\(\);\s*\n\s*\}"
    
    if re.search(broken_pattern, content):
        # Remove the broken remnant and add full function
        content = re.sub(broken_pattern, '', content)
        
        # Find where to insert - before setupAutoSave function
        insert_pattern = r"(\s*// Attach auto-save to all input fields)"
        content = re.sub(insert_pattern, LOAD_SAVED_DATA_FUNCTION + r'\n\1', content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✅ Fixed: {os.path.basename(filepath)}")
        return True
    else:
        # Try alternative approach - insert before setupAutoSave
        if 'function setupAutoSave()' in content and 'function loadSavedData()' not in content:
            insert_pattern = r"(\s*// Attach auto-save to all input fields)"
            if re.search(insert_pattern, content):
                content = re.sub(insert_pattern, LOAD_SAVED_DATA_FUNCTION + r'\n\1', content)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  ✅ Fixed (alt): {os.path.basename(filepath)}")
                return True
        
        print(f"  ⚠ Could not find pattern to fix")
        return False

def main():
    print("=" * 60)
    print("Fixing missing loadSavedData function in reading tools")
    print("=" * 60)
    
    base_path = os.path.dirname(os.path.abspath(__file__))
    fixed_count = 0
    
    for filename in files_to_fix:
        filepath = os.path.join(base_path, filename)
        print(f"\nProcessing: {filename}")
        if fix_file(filepath):
            fixed_count += 1
    
    print("\n" + "=" * 60)
    print(f"Fixed {fixed_count} of {len(files_to_fix)} files")
    print("=" * 60)

if __name__ == '__main__':
    main()
