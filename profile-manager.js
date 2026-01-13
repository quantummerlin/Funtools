// Quantum Merlin Profile Manager
// Manages user profiles across all tools with modern UI

const ProfileManager = {
    // Get all profiles from localStorage
    getProfiles() {
        const profiles = localStorage.getItem('quantumMerlinProfiles');
        return profiles ? JSON.parse(profiles) : [];
    },

    // Get active profile
    getActiveProfile() {
        const activeId = localStorage.getItem('quantumMerlinActiveProfile');
        if (!activeId) return null;
        
        const profiles = this.getProfiles();
        return profiles.find(p => p.id === activeId) || null;
    },

    // Save profiles to localStorage
    saveProfiles(profiles) {
        localStorage.setItem('quantumMerlinProfiles', JSON.stringify(profiles));
    },

    // Set active profile
    setActiveProfile(profileId) {
        localStorage.setItem('quantumMerlinActiveProfile', profileId);
        this.autoFillCurrentPage();
    },

    // Create new profile
    createProfile(data) {
        const profiles = this.getProfiles();
        const newProfile = {
            id: Date.now().toString(),
            name: data.name || 'Unnamed Profile',
            birthDate: data.birthDate || '',
            birthTime: data.birthTime || '',
            birthLocation: data.birthLocation || '',
            latitude: data.latitude || '',
            longitude: data.longitude || '',
            fullName: data.fullName || '',
            createdAt: new Date().toISOString()
        };
        
        profiles.push(newProfile);
        this.saveProfiles(profiles);
        this.setActiveProfile(newProfile.id);
        return newProfile;
    },

    // Update existing profile
    updateProfile(profileId, data) {
        const profiles = this.getProfiles();
        const index = profiles.findIndex(p => p.id === profileId);
        
        if (index !== -1) {
            profiles[index] = { ...profiles[index], ...data };
            this.saveProfiles(profiles);
            
            // If this is the active profile, auto-fill the current page
            if (this.getActiveProfile()?.id === profileId) {
                this.autoFillCurrentPage();
            }
        }
    },

    // Delete profile
    deleteProfile(profileId) {
        const profiles = this.getProfiles();
        const filtered = profiles.filter(p => p.id !== profileId);
        this.saveProfiles(filtered);
        
        // If deleted profile was active, clear active profile
        if (this.getActiveProfile()?.id === profileId) {
            localStorage.removeItem('quantumMerlinActiveProfile');
        }
    },

    // Auto-fill current page with active profile data
    autoFillCurrentPage() {
        const profile = this.getActiveProfile();
        if (!profile) return;

        // Common field mappings
        const fieldMap = {
            'birthDate': profile.birthDate,
            'date': profile.birthDate,
            'date1': profile.birthDate,
            'yourBirthDate': profile.birthDate,
            'birthTime': profile.birthTime,
            'time': profile.birthTime,
            'birthLocation': profile.birthLocation,
            'location': profile.birthLocation,
            'latitude': profile.latitude,
            'longitude': profile.longitude,
            'fullName': profile.fullName,
            'name': profile.fullName,
            'yourName': profile.fullName,
            'preferredName': profile.name,
            'userName': profile.name
        };

        // Fill in all matching fields
        Object.keys(fieldMap).forEach(fieldId => {
            const element = document.getElementById(fieldId);
            if (element && fieldMap[fieldId]) {
                element.value = fieldMap[fieldId];
            }
        });
    },

    // Show profile selector modal
    showProfileSelector() {
        this.createProfileUI();
        document.getElementById('profileModal').classList.add('show');
        document.body.style.overflow = 'hidden';
    },

    // Create profile UI
    createProfileUI() {
        // Remove existing modal if present
        const existingModal = document.getElementById('profileModal');
        if (existingModal) {
            existingModal.remove();
        }

        const profiles = this.getProfiles();
        const activeProfile = this.getActiveProfile();

        const profilesHTML = profiles.map(p => `
            <div class="profile-item ${activeProfile?.id === p.id ? 'active' : ''}" onclick="ProfileManager.selectProfile('${p.id}')">
                <div class="profile-info">
                    <div class="profile-name">${p.name}</div>
                    <div class="profile-details">
                        ${p.birthDate ? `📅 ${new Date(p.birthDate).toLocaleDateString()}` : 'No birth date'}
                        ${p.birthTime ? ` ⏰ ${p.birthTime}` : ''}
                    </div>
                </div>
                <div class="profile-actions">
                    <button onclick="event.stopPropagation(); ProfileManager.editProfile('${p.id}')" class="icon-btn" title="Edit">✏️</button>
                    <button onclick="event.stopPropagation(); ProfileManager.confirmDelete('${p.id}')" class="icon-btn" title="Delete">🗑️</button>
                </div>
            </div>
        `).join('');

        const modalHTML = `
            <div class="modal-overlay" id="profileModal">
                <div class="modal-content profile-modal">
                    <button class="modal-close" onclick="ProfileManager.closeModal()">✕</button>
                    <h2 class="modal-title">👤 Your Profiles</h2>
                    <p class="modal-subtitle">Select a profile to auto-fill your information</p>
                    
                    <div class="profiles-list">
                        ${profiles.length > 0 ? profilesHTML : '<p class="no-profiles">No profiles yet. Create one to save your information!</p>'}
                    </div>
                    
                    <button onclick="ProfileManager.showCreateForm()" class="profile-create-btn">
                        ➕ Create New Profile
                    </button>
                </div>
            </div>
        `;

        document.body.insertAdjacentHTML('beforeend', modalHTML);
    },

    // Show create/edit form
    showCreateForm(profileId = null) {
        const profile = profileId ? this.getProfiles().find(p => p.id === profileId) : null;
        const isEdit = !!profile;

        const formHTML = `
            <div class="modal-overlay show" id="profileFormModal">
                <div class="modal-content profile-modal">
                    <button class="modal-close" onclick="ProfileManager.closeFormModal()">✕</button>
                    <h2 class="modal-title">${isEdit ? '✏️ Edit Profile' : '➕ Create Profile'}</h2>
                    
                    <form id="profileForm" onsubmit="ProfileManager.saveProfile(event, '${profileId || ''}')">
                        <div class="form-group">
                            <label>Profile Name *</label>
                            <input type="text" id="profileName" required placeholder="e.g., My Chart" value="${profile?.name || ''}">
                            <small>A friendly name to identify this profile</small>
                        </div>
                        
                        <div class="form-group">
                            <label>Full Name (for numerology)</label>
                            <input type="text" id="profileFullName" placeholder="e.g., John Michael Smith" value="${profile?.fullName || ''}">
                        </div>
                        
                        <div class="form-group">
                            <label>Birth Date *</label>
                            <input type="date" id="profileBirthDate" required value="${profile?.birthDate || ''}">
                        </div>
                        
                        <div class="form-group">
                            <label>Birth Time (for accurate Rising Sign)</label>
                            <input type="time" id="profileBirthTime" value="${profile?.birthTime || ''}">
                            <small>Optional but recommended for precise astrological readings</small>
                        </div>
                        
                        <div class="form-group">
                            <label>Birth Location</label>
                            <input type="text" id="profileBirthLocation" placeholder="e.g., New York, NY" value="${profile?.birthLocation || ''}">
                        </div>
                        
                        <div class="form-row">
                            <div class="form-group">
                                <label>Latitude</label>
                                <input type="text" id="profileLatitude" placeholder="40.7128" value="${profile?.latitude || ''}">
                            </div>
                            <div class="form-group">
                                <label>Longitude</label>
                                <input type="text" id="profileLongitude" placeholder="-74.0060" value="${profile?.longitude || ''}">
                            </div>
                        </div>
                        
                        <button type="submit" class="submit-btn">${isEdit ? 'Update Profile' : 'Create Profile'}</button>
                    </form>
                </div>
            </div>
        `;

        document.body.insertAdjacentHTML('beforeend', formHTML);
        document.body.style.overflow = 'hidden';
    },

    // Save profile from form
    saveProfile(event, profileId) {
        event.preventDefault();

        const data = {
            name: document.getElementById('profileName').value,
            fullName: document.getElementById('profileFullName').value,
            birthDate: document.getElementById('profileBirthDate').value,
            birthTime: document.getElementById('profileBirthTime').value,
            birthLocation: document.getElementById('profileBirthLocation').value,
            latitude: document.getElementById('profileLatitude').value,
            longitude: document.getElementById('profileLongitude').value
        };

        if (profileId) {
            this.updateProfile(profileId, data);
        } else {
            this.createProfile(data);
        }

        this.closeFormModal();
        this.closeModal();
        this.showProfileSelector();
        
        // Show success message
        this.showToast('Profile saved! ✨');
    },

    // Select a profile
    selectProfile(profileId) {
        this.setActiveProfile(profileId);
        this.closeModal();
        this.showToast('Profile activated! Form fields auto-filled. ✨');
    },

    // Edit profile
    editProfile(profileId) {
        this.closeModal();
        this.showCreateForm(profileId);
    },

    // Confirm delete
    confirmDelete(profileId) {
        const profile = this.getProfiles().find(p => p.id === profileId);
        if (confirm(`Delete profile "${profile?.name}"? This cannot be undone.`)) {
            this.deleteProfile(profileId);
            this.closeModal();
            this.showProfileSelector();
            this.showToast('Profile deleted.');
        }
    },

    // Close main modal
    closeModal() {
        const modal = document.getElementById('profileModal');
        if (modal) {
            modal.remove();
        }
        document.body.style.overflow = '';
    },

    // Close form modal
    closeFormModal() {
        const modal = document.getElementById('profileFormModal');
        if (modal) {
            modal.remove();
        }
        document.body.style.overflow = '';
    },

    // Show toast notification
    showToast(message) {
        const existingToast = document.querySelector('.profile-toast');
        if (existingToast) existingToast.remove();

        const toast = document.createElement('div');
        toast.className = 'profile-toast';
        toast.textContent = message;
        document.body.appendChild(toast);

        setTimeout(() => toast.classList.add('show'), 10);
        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => toast.remove(), 300);
        }, 3000);
    },

    // Initialize profile button on page
    initProfileButton() {
        const container = document.querySelector('.container');
        if (!container) return;

        const activeProfile = this.getActiveProfile();
        const buttonHTML = `
            <button class="profile-btn" onclick="ProfileManager.showProfileSelector()" title="Manage Profiles">
                👤 ${activeProfile ? activeProfile.name : 'Select Profile'}
            </button>
        `;

        container.insertAdjacentHTML('afterbegin', buttonHTML);
    }
};

// Auto-initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    ProfileManager.initProfileButton();
    
    // Auto-fill if there's an active profile
    const activeProfile = ProfileManager.getActiveProfile();
    if (activeProfile) {
        // Small delay to ensure form fields are loaded
        setTimeout(() => {
            ProfileManager.autoFillCurrentPage();
        }, 100);
    }
});
