#!/usr/bin/env python3
"""
Fix profile management in all reading tools.
Replace the broken onProfileChange with the proper version that handles creating new profiles.
Also ensure showDeleteProfileDialog is correct.
"""

import os
import re

# Files that need fixing (reading files + soul-urge-calculator which might be broken too)
files_to_fix = [
    'birthday-number-reading.html',
    'personal-year-reading.html', 
    'personal-month-reading.html',
    'maturity-number-reading.html',
    'karmic-debt-reading.html',
    'master-number-reading.html',
    'moon-sign-reading.html',
    'rising-sign-reading.html',
    'soul-urge-calculator.html'
]

# The correct onProfileChange function that handles new profile creation
CORRECT_ON_PROFILE_CHANGE = '''        // Handle profile selection change
        function onProfileChange() {
            const dropdown = document.getElementById('profileSelect');
            const profileName = dropdown.value;
            
            if (profileName) {
                loadProfile(profileName);
            } else {
                // If "Select or type to create..." is chosen, ask for new profile name
                const newName = prompt('Enter a name for the new profile:');
                if (newName && newName.trim()) {
                    const trimmedName = newName.trim();
                    // Create new profile with current form data
                    const userData = {
                        preferredName: document.getElementById('preferredName')?.value || '',
                        birthName: document.getElementById('birthName')?.value || '',
                        birthDate: document.getElementById('birthDate')?.value || '',
                        birthTime: document.getElementById('birthTime')?.value || '',
                        birthPlace: document.getElementById('birthPlace')?.value || ''
                    };
                    
                    const profiles = getAllProfiles();
                    profiles[trimmedName] = userData;
                    localStorage.setItem('quantumMerlinProfiles', JSON.stringify(profiles));
                    localStorage.setItem('quantumMerlinActiveProfile', trimmedName);
                    localStorage.setItem('quantumMerlinUserData', JSON.stringify(userData));
                    
                    updateProfileDropdown();
                }
            }
        }
'''

# The correct loadProfile function
CORRECT_LOAD_PROFILE = '''        // Load a specific profile
        function loadProfile(profileName) {
            const profiles = getAllProfiles();
            const profileData = profiles[profileName];
            
            if (profileData) {
                if (document.getElementById('preferredName') && profileData.preferredName) {
                    document.getElementById('preferredName').value = profileData.preferredName;
                }
                if (document.getElementById('birthName') && profileData.birthName) {
                    document.getElementById('birthName').value = profileData.birthName;
                }
                if (document.getElementById('birthDate') && profileData.birthDate) {
                    document.getElementById('birthDate').value = profileData.birthDate;
                }
                if (document.getElementById('birthTime') && profileData.birthTime) {
                    document.getElementById('birthTime').value = profileData.birthTime;
                }
                if (document.getElementById('birthPlace') && profileData.birthPlace) {
                    document.getElementById('birthPlace').value = profileData.birthPlace;
                }
                
                localStorage.setItem('quantumMerlinUserData', JSON.stringify(profileData));
                localStorage.setItem('quantumMerlinActiveProfile', profileName);
            }
        }
'''

# The correct showDeleteProfileDialog function
CORRECT_DELETE_DIALOG = '''        // Show delete profile dialog
        function showDeleteProfileDialog() {
            const profiles = getAllProfiles();
            const profileNames = Object.keys(profiles).sort();
            
            if (profileNames.length === 0) {
                alert('No saved profiles to remove');
                return;
            }
            
            const activeProfile = localStorage.getItem('quantumMerlinActiveProfile') || '';
            const defaultDelete = activeProfile || profileNames[0];
            
            const profileName = prompt('Enter profile name to remove:\\n\\nSaved profiles:\\n' + profileNames.join('\\n'), defaultDelete);
            if (profileName && profiles[profileName]) {
                if (confirm('Remove profile "' + profileName + '"? This cannot be undone.')) {
                    deleteProfile(profileName);
                    // Clear form if we deleted the active profile
                    if (profileName === activeProfile) {
                        if (document.getElementById('preferredName')) document.getElementById('preferredName').value = '';
                        if (document.getElementById('birthName')) document.getElementById('birthName').value = '';
                        if (document.getElementById('birthDate')) document.getElementById('birthDate').value = '';
                        if (document.getElementById('birthTime')) document.getElementById('birthTime').value = '';
                        if (document.getElementById('birthPlace')) document.getElementById('birthPlace').value = '';
                    }
                }
            } else if (profileName) {
                alert('Profile not found');
            }
        }
'''

# The correct deleteProfile function
CORRECT_DELETE_PROFILE = '''        // Delete a profile
        function deleteProfile(profileName) {
            const profiles = getAllProfiles();
            delete profiles[profileName];
            localStorage.setItem('quantumMerlinProfiles', JSON.stringify(profiles));
            
            const activeProfile = localStorage.getItem('quantumMerlinActiveProfile');
            if (activeProfile === profileName) {
                localStorage.removeItem('quantumMerlinActiveProfile');
            }
            
            updateProfileDropdown();
        }
'''

def fix_file(filepath):
    """Fix profile management in a single file."""
    if not os.path.exists(filepath):
        print(f"  ⚠ File not found: {filepath}")
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    changes = []
    
    # 1. Replace broken onProfileChange with correct version
    old_on_profile_change_pattern = r"// Handle profile selection change\s*\n\s*function onProfileChange\(\) \{.*?^\s*\}"
    if re.search(old_on_profile_change_pattern, content, re.MULTILINE | re.DOTALL):
        # Find the function and its closing brace properly
        match = re.search(r"(// Handle profile selection change\s*\n\s*function onProfileChange\(\) \{)", content)
        if match:
            start = match.start()
            # Find matching closing brace
            brace_count = 0
            found_open = False
            end = start
            for i, char in enumerate(content[start:], start):
                if char == '{':
                    brace_count += 1
                    found_open = True
                elif char == '}':
                    brace_count -= 1
                    if found_open and brace_count == 0:
                        end = i + 1
                        break
            
            if end > start:
                content = content[:start] + CORRECT_ON_PROFILE_CHANGE + content[end:]
                changes.append("Fixed onProfileChange")
    
    # 2. Add loadProfile function if missing
    if 'function loadProfile(' not in content:
        # Insert before onProfileChange
        insert_point = content.find('// Handle profile selection change')
        if insert_point > 0:
            content = content[:insert_point] + CORRECT_LOAD_PROFILE + '\n' + content[insert_point:]
            changes.append("Added loadProfile")
    
    # 3. Fix showDeleteProfileDialog if it's the old version
    if 'showDeleteProfileDialog' in content and 'Enter profile name to remove' not in content:
        # Replace the old version
        match = re.search(r"(// Show dialog to delete current profile\s*\n\s*function showDeleteProfileDialog\(\) \{)", content)
        if not match:
            match = re.search(r"(// Show delete profile dialog\s*\n\s*function showDeleteProfileDialog\(\) \{)", content)
        
        if match:
            start = match.start()
            # Find matching closing brace
            brace_count = 0
            found_open = False
            end = start
            for i, char in enumerate(content[start:], start):
                if char == '{':
                    brace_count += 1
                    found_open = True
                elif char == '}':
                    brace_count -= 1
                    if found_open and brace_count == 0:
                        end = i + 1
                        break
            
            if end > start:
                content = content[:start] + CORRECT_DELETE_DIALOG + content[end:]
                changes.append("Fixed showDeleteProfileDialog")
    
    # 4. Add deleteProfile function if missing
    if 'function deleteProfile(' not in content:
        # Insert after showDeleteProfileDialog
        insert_point = content.find('// Load saved data from localStorage')
        if insert_point > 0:
            content = content[:insert_point] + CORRECT_DELETE_PROFILE + '\n        ' + content[insert_point:]
            changes.append("Added deleteProfile")
    
    # 5. Remove showSaveProfileDialog if it exists (we don't need it anymore)
    if 'function showSaveProfileDialog' in content:
        match = re.search(r"// Show dialog to create new profile\s*\n\s*function showSaveProfileDialog\(\) \{", content)
        if match:
            start = match.start()
            # Find matching closing brace
            brace_count = 0
            found_open = False
            end = start
            for i, char in enumerate(content[start:], start):
                if char == '{':
                    brace_count += 1
                    found_open = True
                elif char == '}':
                    brace_count -= 1
                    if found_open and brace_count == 0:
                        end = i + 1
                        break
            
            if end > start:
                content = content[:start] + content[end:]
                changes.append("Removed unused showSaveProfileDialog")
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✅ {', '.join(changes)}")
        return True
    else:
        print(f"  ℹ️ No changes needed")
        return False

def main():
    print("=" * 60)
    print("Fixing profile management in reading tools")
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
