// Profile Management System for Quantum Merlin Tools
// Add this to any tool that uses localStorage

// Get all saved profiles
function getAllProfiles() {
    const profiles = localStorage.getItem('quantumMerlinProfiles');
    return profiles ? JSON.parse(profiles) : {};
}

// Save current data as a named profile
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
    
    // Also save as current active data
    localStorage.setItem('quantumMerlinUserData', JSON.stringify(currentData));
    localStorage.setItem('quantumMerlinActiveProfile', profileName);
    
    updateProfileDropdown();
    alert(`Profile "${profileName}" saved! ✨`);
}

// Load a specific profile
function loadProfile(profileName) {
    const profiles = getAllProfiles();
    const profileData = profiles[profileName];
    
    if (!profileData) {
        alert('Profile not found');
        return;
    }
    
    // Fill in the form fields
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
    
    // Save as current active data
    localStorage.setItem('quantumMerlinUserData', JSON.stringify(profileData));
    localStorage.setItem('quantumMerlinActiveProfile', profileName);
}

// Delete a profile
function deleteProfile(profileName) {
    if (!confirm(`Are you sure you want to delete profile "${profileName}"?`)) {
        return;
    }
    
    const profiles = getAllProfiles();
    delete profiles[profileName];
    localStorage.setItem('quantumMerlinProfiles', JSON.stringify(profiles));
    
    // If this was the active profile, clear it
    const activeProfile = localStorage.getItem('quantumMerlinActiveProfile');
    if (activeProfile === profileName) {
        localStorage.removeItem('quantumMerlinActiveProfile');
    }
    
    updateProfileDropdown();
    alert(`Profile "${profileName}" deleted`);
}

// Update the profile dropdown
function updateProfileDropdown() {
    const dropdown = document.getElementById('profileSelect');
    if (!dropdown) return;
    
    const profiles = getAllProfiles();
    const activeProfile = localStorage.getItem('quantumMerlinActiveProfile') || '';
    
    // Clear existing options except the first
    dropdown.innerHTML = '<option value="">Select a profile...</option>';
    
    // Add profile options
    Object.keys(profiles).forEach(profileName => {
        const option = document.createElement('option');
        option.value = profileName;
        option.textContent = profileName;
        if (profileName === activeProfile) {
            option.selected = true;
        }
        dropdown.appendChild(option);
    });
}

// Handle profile dropdown change
function onProfileChange() {
    const dropdown = document.getElementById('profileSelect');
    const profileName = dropdown.value;
    
    if (profileName) {
        loadProfile(profileName);
    }
}

// Show save profile dialog
function showSaveProfileDialog() {
    const profileName = prompt('Enter a name for this profile:');
    if (profileName) {
        saveProfile(profileName);
    }
}

// Show delete profile dialog
function showDeleteProfileDialog() {
    const profiles = getAllProfiles();
    const profileNames = Object.keys(profiles);
    
    if (profileNames.length === 0) {
        alert('No profiles to delete');
        return;
    }
    
    const profileName = prompt(`Enter profile name to delete:\n\n${profileNames.join('\n')}`);
    if (profileName && profiles[profileName]) {
        deleteProfile(profileName);
    } else if (profileName) {
        alert('Profile not found');
    }
}

// Initialize profile system
function initProfileSystem() {
    updateProfileDropdown();
    
    // Add event listener to dropdown if it exists
    const dropdown = document.getElementById('profileSelect');
    if (dropdown) {
        dropdown.addEventListener('change', onProfileChange);
    }
}

// Call this on page load
if (typeof window !== 'undefined') {
    window.addEventListener('DOMContentLoaded', initProfileSystem);
}
