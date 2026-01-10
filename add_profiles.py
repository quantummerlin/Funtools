#!/usr/bin/env python3
"""
Add profile management dropdown to all premium numerology tools
"""

import os
import re

# List of premium tools that have full input forms
PREMIUM_TOOLS = [
    "birthday-number-reading.html",
    "personal-year-reading.html",
    "personal-month-reading.html",
    "maturity-number-reading.html",
    "karmic-debt-reading.html",
    "master-number-reading.html",
    "life-path-calculator.html",
    "destiny-number-calculator.html",
    "soul-urge-calculator.html",
    "personality-number-calculator.html",
    "name-number-calculator.html"
]

# CSS to add for profile dropdown
PROFILE_CSS = """        .profile-controls {
            display: flex;
            gap: 10px;
            align-items: center;
            justify-content: flex-end;
            margin-bottom: 20px;
            flex-wrap: wrap;
        }
        .profile-select {
            flex: 1;
            min-width: 200px;
            padding: 10px 15px;
            border: 2px solid rgba(6, 182, 212, 0.3);
            background: rgba(10, 10, 15, 0.6);
            color: #e0e0e0;
            border-radius: 8px;
            font-size: 0.95em;
            font-family: 'Cinzel', serif;
            cursor: pointer;
        }
        .profile-select:focus {
            outline: none;
            border-color: #06b6d4;
        }
        .profile-btn {
            background: rgba(6, 182, 212, 0.1);
            border: 2px solid rgba(6, 182, 212, 0.3);
            color: #06b6d4;
            padding: 10px 15px;
            font-size: 0.9em;
            border-radius: 8px;
            cursor: pointer;
            font-family: 'Cinzel', serif;
            font-weight: 600;
            transition: all 0.3s;
            white-space: nowrap;
        }
        .profile-btn:hover {
            background: rgba(6, 182, 212, 0.2);
            border-color: #06b6d4;
        }
        .clear-btn {
            background: rgba(236, 72, 153, 0.1);
            border-color: rgba(236, 72, 153, 0.3);
            color: #ec4899;
        }
        .clear-btn:hover {
            background: rgba(236, 72, 153, 0.2);
            border-color: #ec4899;
        }"""

# HTML to replace the current clear data button section
PROFILE_HTML = """            <div class="profile-controls">
                <select id="profileSelect" class="profile-select">
                    <option value="">Select a profile...</option>
                </select>
                <button type="button" class="profile-btn" onclick="showSaveProfileDialog()">💾 Save Profile</button>
                <button type="button" class="profile-btn" onclick="showDeleteProfileDialog()">🗑️ Delete Profile</button>
                <button type="button" class="profile-btn clear-btn" onclick="clearSavedData()">✨ Clear Form</button>
            </div>"""

# JavaScript functions to add
PROFILE_JS = """
        // Profile Management Functions
        function getAllProfiles() {
            const profiles = localStorage.getItem('quantumMerlinProfiles');
            return profiles ? JSON.parse(profiles) : {};
        }

        function saveProfile(profileName) {
            if (!profileName || profileName.trim() === '') {
                alert('Please enter a profile name');
                return;
            }
            
            const currentData = {
                preferredName: document.getElementById('preferredName')?.value || '',
                birthName: document.getElementById('birthName')?.value || '',
                birthDate: document.getElementById('birthDate')?.value || '',
                birthTime: document.getElementById('birthTime')?.value || '',
                birthPlace: document.getElementById('birthPlace')?.value || ''
            };
            
            const profiles = getAllProfiles();
            profiles[profileName] = currentData;
            localStorage.setItem('quantumMerlinProfiles', JSON.stringify(profiles));
            
            localStorage.setItem('quantumMerlinUserData', JSON.stringify(currentData));
            localStorage.setItem('quantumMerlinActiveProfile', profileName);
            
            updateProfileDropdown();
            alert(`Profile "${profileName}" saved! ✨`);
        }

        function loadProfile(profileName) {
            const profiles = getAllProfiles();
            const profileData = profiles[profileName];
            
            if (!profileData) return;
            
            if (profileData.preferredName && document.getElementById('preferredName')) {
                document.getElementById('preferredName').value = profileData.preferredName;
            }
            if (profileData.birthName && document.getElementById('birthName')) {
                document.getElementById('birthName').value = profileData.birthName;
            }
            if (profileData.birthDate && document.getElementById('birthDate')) {
                document.getElementById('birthDate').value = profileData.birthDate;
            }
            if (profileData.birthTime && document.getElementById('birthTime')) {
                document.getElementById('birthTime').value = profileData.birthTime;
            }
            if (profileData.birthPlace && document.getElementById('birthPlace')) {
                document.getElementById('birthPlace').value = profileData.birthPlace;
            }
            
            localStorage.setItem('quantumMerlinUserData', JSON.stringify(profileData));
            localStorage.setItem('quantumMerlinActiveProfile', profileName);
        }

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

        function updateProfileDropdown() {
            const dropdown = document.getElementById('profileSelect');
            if (!dropdown) return;
            
            const profiles = getAllProfiles();
            const activeProfile = localStorage.getItem('quantumMerlinActiveProfile') || '';
            
            dropdown.innerHTML = '<option value="">Select a profile...</option>';
            
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

        function onProfileChange() {
            const dropdown = document.getElementById('profileSelect');
            const profileName = dropdown.value;
            
            if (profileName) {
                loadProfile(profileName);
            }
        }

        function showSaveProfileDialog() {
            const profiles = getAllProfiles();
            const currentActive = localStorage.getItem('quantumMerlinActiveProfile') || '';
            
            let message = 'Enter a name for this profile:';
            if (currentActive) {
                message += `\\n\\nCurrent profile: "${currentActive}"\\nLeave blank to update current profile.`;
            }
            
            const profileName = prompt(message, currentActive);
            
            if (profileName !== null) {
                const finalName = profileName.trim() || currentActive || 'Profile ' + (Object.keys(profiles).length + 1);
                saveProfile(finalName);
            }
        }

        function showDeleteProfileDialog() {
            const profiles = getAllProfiles();
            const profileNames = Object.keys(profiles).sort();
            
            if (profileNames.length === 0) {
                alert('No saved profiles to delete');
                return;
            }
            
            const profileName = prompt(`Enter profile name to delete:\\n\\nSaved profiles:\\n${profileNames.join('\\n')}`);
            if (profileName && profiles[profileName]) {
                if (confirm(`Delete profile "${profileName}"?`)) {
                    deleteProfile(profileName);
                    alert(`Profile "${profileName}" deleted`);
                }
            } else if (profileName) {
                alert('Profile not found');
            }
        }

        // Initialize profile dropdown on page load
        document.addEventListener('DOMContentLoaded', function() {
            updateProfileDropdown();
            
            const dropdown = document.getElementById('profileSelect');
            if (dropdown) {
                dropdown.addEventListener('change', onProfileChange);
            }
        });
"""

print("🔮 Adding Profile Management to Premium Tools...")
print("=" * 60)

updated_count = 0
for tool_file in PREMIUM_TOOLS:
    if not os.path.exists(tool_file):
        print(f"⚠️  {tool_file} not found, skipping...")
        continue
    
    with open(tool_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already updated
    if 'profileSelect' in content:
        print(f"✅ {tool_file} already has profile management")
        continue
    
    # Add CSS before the closing </style> tag
    if PROFILE_CSS not in content:
        content = content.replace('</style>', PROFILE_CSS + '\n    </style>')
    
    # Replace the clear data button section with profile controls
    old_clear_section = r'<div class="clear-data-btn">\s*<button[^>]*onclick="clearSavedData\(\)"[^>]*>.*?</button>\s*</div>'
    content = re.sub(old_clear_section, PROFILE_HTML, content, flags=re.DOTALL)
    
    # Add profile JS before the clearSavedData function
    clear_saved_pattern = r'(\s+// Clear saved data\s+function clearSavedData\(\))'
    if re.search(clear_saved_pattern, content):
        content = re.sub(clear_saved_pattern, PROFILE_JS + r'\1', content)
    else:
        # Alternative: add before closing script tag
        content = content.replace('</script>', PROFILE_JS + '\n    </script>')
    
    with open(tool_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    updated_count += 1
    print(f"✅ Updated {tool_file}")

print("=" * 60)
print(f"✨ Profile management added to {updated_count} tools!")
print("📝 Features:")
print("   • Save named profiles")
print("   • Switch between profiles via dropdown")
print("   • Delete unwanted profiles")
print("   • Profiles persist across all tools")
