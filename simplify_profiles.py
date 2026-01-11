import os
import re

TOOLS = [
    'life-path-calculator.html',
    'destiny-number-calculator.html',
    'soul-urge-calculator.html',
    'personality-number-calculator.html',
    'name-number-calculator.html',
    'birthday-number-reading.html',
    'personal-year-reading.html',
    'personal-month-reading.html',
    'maturity-number-reading.html',
    'karmic-debt-reading.html',
    'master-number-reading.html',
    'moon-sign-reading.html',
    'rising-sign-reading.html'
]

# New simplified profile UI - just dropdown and delete button
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

# New JavaScript with auto-save
NEW_PROFILE_JS = '''
        // ===== ENHANCED PROFILE MANAGEMENT WITH AUTO-SAVE =====
        
        // Get all saved profiles
        function getAllProfiles() {
            const profiles = localStorage.getItem('quantumMerlinProfiles');
            return profiles ? JSON.parse(profiles) : {};
        }
        
        // Auto-save current form data
        function autoSaveData() {
            const userData = {
                preferredName: document.getElementById('preferredName')?.value || '',
                birthName: document.getElementById('birthName')?.value || '',
                birthDate: document.getElementById('birthDate')?.value || '',
                birthTime: document.getElementById('birthTime')?.value || '',
                birthPlace: document.getElementById('birthPlace')?.value || ''
            };
            
            // Always save to current user data for cross-tool persistence
            localStorage.setItem('quantumMerlinUserData', JSON.stringify(userData));
            
            // If there's an active profile, update it too
            const activeProfile = localStorage.getItem('quantumMerlinActiveProfile');
            if (activeProfile) {
                const profiles = getAllProfiles();
                profiles[activeProfile] = userData;
                localStorage.setItem('quantumMerlinProfiles', JSON.stringify(profiles));
            }
        }
        
        // Load a profile into the form
        function loadProfile(profileName) {
            const profiles = getAllProfiles();
            const profileData = profiles[profileName];
            
            if (!profileData) return;
            
            if (document.getElementById('preferredName')) {
                document.getElementById('preferredName').value = profileData.preferredName || '';
            }
            if (document.getElementById('birthName')) {
                document.getElementById('birthName').value = profileData.birthName || '';
            }
            if (document.getElementById('birthDate')) {
                document.getElementById('birthDate').value = profileData.birthDate || '';
            }
            if (document.getElementById('birthTime')) {
                document.getElementById('birthTime').value = profileData.birthTime || '';
            }
            if (document.getElementById('birthPlace')) {
                document.getElementById('birthPlace').value = profileData.birthPlace || '';
            }
            
            // Update current user data
            localStorage.setItem('quantumMerlinUserData', JSON.stringify(profileData));
            localStorage.setItem('quantumMerlinActiveProfile', profileName);
        }
        
        // Delete a profile
        function deleteProfile(profileName) {
            const profiles = getAllProfiles();
            delete profiles[profileName];
            localStorage.setItem('quantumMerlinProfiles', JSON.stringify(profiles));
            
            // If we deleted the active profile, clear it
            const activeProfile = localStorage.getItem('quantumMerlinActiveProfile');
            if (activeProfile === profileName) {
                localStorage.removeItem('quantumMerlinActiveProfile');
            }
            
            updateProfileDropdown();
        }
        
        // Update the profile dropdown with saved profiles
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
        
        // Show delete profile dialog
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

def update_tool(filename):
    filepath = os.path.join(os.getcwd(), filename)
    
    if not os.path.exists(filepath):
        print(f"  ⏭️ Skipping {filename} - not found")
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 1. Replace old profile UI with new simplified one
    old_profile_pattern = r'<!-- Profile Management Section -->\s*<div class="profile-section"[^>]*>.*?</div>\s*</div>\s*<p[^>]*>.*?</p>\s*</div>'
    content = re.sub(old_profile_pattern, NEW_PROFILE_UI.strip(), content, flags=re.DOTALL)
    
    # 2. Replace old profile JavaScript with new auto-save version
    old_js_pattern = r'// ===== ENHANCED PROFILE MANAGEMENT =====.*?// ===== END PROFILE MANAGEMENT ====='
    content = re.sub(old_js_pattern, NEW_PROFILE_JS.strip(), content, flags=re.DOTALL)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✅ Updated {filename}")
        return True
    else:
        print(f"  ⏭️ No changes: {filename}")
        return False

def main():
    print("Simplifying profile management with auto-save...")
    print("=" * 50)
    
    updated = 0
    for tool in TOOLS:
        if update_tool(tool):
            updated += 1
    
    print("=" * 50)
    print(f"Updated {updated} of {len(TOOLS)} tools")

if __name__ == '__main__':
    main()
