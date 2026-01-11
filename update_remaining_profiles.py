#!/usr/bin/env python3
"""
Update remaining reading tools with simplified auto-save profile management.
These tools have the OLD profile UI that needs to be updated to match the new format.
"""

import re
import os

# Files to update
files_to_update = [
    'birthday-number-reading.html',
    'personal-year-reading.html',
    'personal-month-reading.html',
    'maturity-number-reading.html',
    'karmic-debt-reading.html',
    'master-number-reading.html',
    'moon-sign-reading.html',
    'rising-sign-reading.html'
]

# NEW simplified profile UI HTML
NEW_PROFILE_UI = '''
            <!-- Profile Management Section -->
            <div class="profile-section" style="background: rgba(139, 92, 246, 0.08); border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 12px; padding: 15px 20px; margin-bottom: 25px;">
                <div style="display: flex; flex-wrap: wrap; gap: 12px; align-items: center;">
                    <div style="display: flex; align-items: center; gap: 10px; flex: 1; min-width: 200px;">
                        <label style="color: #BF5AF2; font-family: 'Cinzel', serif; white-space: nowrap; font-size: 0.95em;">👤 Profile:</label>
                        <select id="profileSelect" onchange="onProfileChange()" style="flex: 1; background: rgba(0,0,0,0.4); border: 1px solid rgba(191, 90, 242, 0.4); color: #E8E4D9; padding: 10px 14px; border-radius: 8px; font-family: 'Cormorant Garamond', serif; font-size: 1em; cursor: pointer;">
                            <option value="">Select or type to create...</option>
                        </select>
                    </div>
                    <button type="button" onclick="showDeleteProfileDialog()" class="profile-btn" style="background: rgba(236, 72, 153, 0.1); border: 1px solid rgba(236, 72, 153, 0.4); color: #ec4899; padding: 10px 16px; border-radius: 8px; cursor: pointer; font-family: 'Cinzel', serif; font-size: 0.85em; transition: all 0.3s;">
                        🗑️ Remove Profile
                    </button>
                </div>
                <p style="color: #9A8F7A; font-size: 0.8em; margin-top: 10px; margin-bottom: 0;">
                    ✨ Your info auto-saves as you type. Create profiles for friends & family!
                </p>
            </div>
'''

# NEW Profile JS with auto-save functionality
NEW_PROFILE_JS = '''
        // ===== PROFILE MANAGEMENT (Simplified with Auto-Save) =====
        
        // Auto-save data whenever any field changes
        function autoSaveData() {
            const userData = {
                preferredName: document.getElementById('preferredName')?.value || '',
                birthName: document.getElementById('birthName')?.value || '',
                birthDate: document.getElementById('birthDate')?.value || '',
                birthTime: document.getElementById('birthTime')?.value || '',
                birthPlace: document.getElementById('birthPlace')?.value || ''
            };
            localStorage.setItem('quantumMerlinUserData', JSON.stringify(userData));
            
            // Also update active profile if one is selected
            const activeProfile = localStorage.getItem('quantumMerlinActiveProfile');
            if (activeProfile) {
                const profiles = getAllProfiles();
                profiles[activeProfile] = userData;
                localStorage.setItem('quantumMerlinProfiles', JSON.stringify(profiles));
            }
        }
        
        // Get all saved profiles
        function getAllProfiles() {
            const profiles = localStorage.getItem('quantumMerlinProfiles');
            return profiles ? JSON.parse(profiles) : {};
        }
        
        // Update the profile dropdown
        function updateProfileDropdown() {
            const dropdown = document.getElementById('profileSelect');
            if (!dropdown) return;
            
            const profiles = getAllProfiles();
            const activeProfile = localStorage.getItem('quantumMerlinActiveProfile') || '';
            
            dropdown.innerHTML = '<option value="">Select or type to create...</option>';
            
            Object.keys(profiles).sort().forEach(profileName => {
                const option = document.createElement('option');
                option.value = profileName;
                option.textContent = profileName;
                if (profileName === activeProfile) {
                    option.selected = true;
                }
                dropdown.appendChild(option);
            });
        }
        
        // Handle profile selection change
        function onProfileChange() {
            const dropdown = document.getElementById('profileSelect');
            const profileName = dropdown.value;
            
            if (profileName) {
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
        }
        
        // Show dialog to create new profile
        function showSaveProfileDialog() {
            const profileName = prompt('Enter a name for this profile (e.g., "Me", "Partner", "Friend"):');
            if (profileName && profileName.trim()) {
                const currentData = {
                    preferredName: document.getElementById('preferredName')?.value || '',
                    birthName: document.getElementById('birthName')?.value || '',
                    birthDate: document.getElementById('birthDate')?.value || '',
                    birthTime: document.getElementById('birthTime')?.value || '',
                    birthPlace: document.getElementById('birthPlace')?.value || ''
                };
                
                const profiles = getAllProfiles();
                profiles[profileName.trim()] = currentData;
                localStorage.setItem('quantumMerlinProfiles', JSON.stringify(profiles));
                localStorage.setItem('quantumMerlinActiveProfile', profileName.trim());
                localStorage.setItem('quantumMerlinUserData', JSON.stringify(currentData));
                
                updateProfileDropdown();
                alert('Profile "' + profileName.trim() + '" saved! ✨');
            }
        }
        
        // Show dialog to delete current profile
        function showDeleteProfileDialog() {
            const activeProfile = localStorage.getItem('quantumMerlinActiveProfile');
            if (!activeProfile) {
                alert('No profile is currently selected.');
                return;
            }
            
            if (confirm('Delete profile "' + activeProfile + '"? This cannot be undone.')) {
                const profiles = getAllProfiles();
                delete profiles[activeProfile];
                localStorage.setItem('quantumMerlinProfiles', JSON.stringify(profiles));
                localStorage.removeItem('quantumMerlinActiveProfile');
                updateProfileDropdown();
                alert('Profile deleted.');
            }
        }
        
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
        
        // Attach auto-save to all input fields
        function setupAutoSave() {
            const fields = ['preferredName', 'birthName', 'birthDate', 'birthTime', 'birthPlace'];
            fields.forEach(fieldId => {
                const field = document.getElementById(fieldId);
                if (field) {
                    field.addEventListener('input', autoSaveData);
                    field.addEventListener('change', autoSaveData);
                }
            });
        }
        
        // Initialize on page load
        window.addEventListener('DOMContentLoaded', function() {
            loadSavedData();
            setupAutoSave();
        });
        
        // ===== END PROFILE MANAGEMENT =====
'''

def update_file(filepath):
    """Update a single file with the new profile management."""
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Step 1: Replace the old profile controls HTML
    old_profile_pattern = r'<div class="profile-controls">.*?</div>\s*(?=\s*<form|\s*<div class="input)'
    match = re.search(old_profile_pattern, content, re.DOTALL)
    if match:
        content = content[:match.start()] + NEW_PROFILE_UI + content[match.end():]
        print(f"  ✓ Replaced profile-controls HTML")
    else:
        # Try another pattern - profile controls might be right after tool-card
        old_profile_pattern2 = r'(<div class="tool-card">)\s*<div class="profile-controls">.*?</div>'
        match2 = re.search(old_profile_pattern2, content, re.DOTALL)
        if match2:
            content = re.sub(old_profile_pattern2, r'\1' + NEW_PROFILE_UI, content, flags=re.DOTALL)
            print(f"  ✓ Replaced profile-controls HTML (pattern 2)")
        else:
            print(f"  ⚠ Could not find profile-controls to replace")
    
    # Step 2: Remove old profile management JS functions and replace with new ones
    # Find and remove old profile functions
    old_js_patterns = [
        r'// Profile Management Functions\s+function getAllProfiles\(\).*?(?=// Initialize profile dropdown|function calculate|// Calculate|function goBack|$)',
        r'function getAllProfiles\(\).*?(?=function calculate|// Calculate|function goBack|</script>)',
        r'// LocalStorage functions.*?function clearSavedData\(\).*?\}\s*(?=// Load saved data|window\.addEventListener)',
    ]
    
    for pattern in old_js_patterns:
        content = re.sub(pattern, '', content, flags=re.DOTALL)
    
    # Step 3: Remove old DOMContentLoaded listener for profiles
    old_dom_listeners = [
        r"// Initialize profile dropdown on page load\s*document\.addEventListener\('DOMContentLoaded', function\(\) \{.*?\}\);\s*",
        r"// Load saved data on page load\s*window\.addEventListener\('DOMContentLoaded', loadSavedData\);\s*",
    ]
    
    for pattern in old_dom_listeners:
        content = re.sub(pattern, '', content, flags=re.DOTALL)
    
    # Step 4: Insert new profile JS before </script>
    if NEW_PROFILE_JS.strip() not in content:
        content = content.replace('</script>', NEW_PROFILE_JS + '\n    </script>')
        print(f"  ✓ Added new profile JS")
    
    # Step 5: Clean up any duplicate saveUserData calls
    # Make sure we keep only one saveUserData if it still exists (some tools use it in calculateReading)
    
    # Step 6: Remove any leftover saveUserData function and clearSavedData if they exist
    # We'll let autoSaveData handle everything now
    content = re.sub(r'function saveUserData\(\).*?\}\s*(?=function|// )', '', content, flags=re.DOTALL)
    content = re.sub(r'function clearSavedData\(\).*?\}\s*(?=function|// )', '', content, flags=re.DOTALL)
    content = re.sub(r'function loadSavedData\(\).*?\}\s*(?=function|// |// Profile)', '', content, flags=re.DOTALL)
    
    # Step 7: Update any saveUserData() calls to autoSaveData()
    content = content.replace('saveUserData();', 'autoSaveData();')
    content = content.replace('saveUserData()', 'autoSaveData()')
    
    # Clean up multiple blank lines
    content = re.sub(r'\n{4,}', '\n\n\n', content)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✅ Updated: {filepath}")
        return True
    else:
        print(f"  ℹ️ No changes needed: {filepath}")
        return False

def main():
    print("=" * 60)
    print("Updating remaining tools with simplified profile management")
    print("=" * 60)
    
    base_path = os.path.dirname(os.path.abspath(__file__))
    updated_count = 0
    
    for filename in files_to_update:
        filepath = os.path.join(base_path, filename)
        print(f"\nProcessing: {filename}")
        if update_file(filepath):
            updated_count += 1
    
    print("\n" + "=" * 60)
    print(f"Complete! Updated {updated_count} of {len(files_to_update)} files")
    print("=" * 60)

if __name__ == '__main__':
    main()
