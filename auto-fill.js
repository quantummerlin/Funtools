// Simple Auto-Fill System with Multiple Profiles for Quantum Merlin Tools
// Automatically saves and restores form data across all tools

(function() {
    const PROFILES_KEY = 'quantumMerlinProfiles';
    const ACTIVE_KEY = 'quantumMerlinActiveProfile';
    const FIELDS = ['preferredName', 'birthName', 'birthDate', 'birthTime', 'birthPlace'];

    // Get all profiles
    function getProfiles() {
        try {
            const saved = localStorage.getItem(PROFILES_KEY);
            return saved ? JSON.parse(saved) : {};
        } catch (e) {
            return {};
        }
    }

    // Save profiles
    function saveProfiles(profiles) {
        localStorage.setItem(PROFILES_KEY, JSON.stringify(profiles));
    }

    // Get active profile name
    function getActiveProfile() {
        return localStorage.getItem(ACTIVE_KEY) || '';
    }

    // Set active profile
    function setActiveProfile(name) {
        localStorage.setItem(ACTIVE_KEY, name);
    }

    // Load data into form fields
    function loadData(profileName) {
        const profiles = getProfiles();
        const data = profiles[profileName];
        if (!data) return;
        
        FIELDS.forEach(field => {
            const el = document.getElementById(field);
            if (el && data[field]) {
                el.value = data[field];
            }
        });
    }

    // Save current form data to active profile
    function saveData() {
        const profileName = getActiveProfile();
        if (!profileName) return;
        
        const profiles = getProfiles();
        const data = {};
        FIELDS.forEach(field => {
            const el = document.getElementById(field);
            if (el) {
                data[field] = el.value || '';
            }
        });
        profiles[profileName] = data;
        saveProfiles(profiles);
    }

    // Create the profile selector UI
    function createProfileSelector() {
        // Find the form or first input container
        const form = document.querySelector('form') || document.querySelector('.form-section');
        if (!form) return;
        
        // Check if we already added it
        if (document.getElementById('profileSelector')) return;
        
        // Create profile selector HTML
        const container = document.createElement('div');
        container.id = 'profileSelector';
        container.style.cssText = 'margin-bottom: 20px; padding: 15px; background: rgba(20,20,30,0.6); border: 1px solid rgba(6,182,212,0.3); border-radius: 10px;';
        container.innerHTML = `
            <div style="display: flex; gap: 10px; align-items: center; flex-wrap: wrap;">
                <label style="color: #C4B998; font-family: Cinzel, serif;">Profile:</label>
                <select id="profileDropdown" style="flex: 1; min-width: 150px; padding: 8px 12px; background: rgba(10,10,20,0.8); border: 1px solid rgba(6,182,212,0.3); border-radius: 6px; color: #E8E4D9; font-family: inherit;">
                    <option value="">Select or create...</option>
                </select>
                <input type="text" id="newProfileName" placeholder="New profile name" style="padding: 8px 12px; background: rgba(10,10,20,0.8); border: 1px solid rgba(6,182,212,0.3); border-radius: 6px; color: #E8E4D9; width: 140px;">
                <button type="button" id="addProfileBtn" style="padding: 8px 15px; background: linear-gradient(135deg, #06b6d4, #8b5cf6); border: none; border-radius: 6px; color: white; cursor: pointer; font-family: Cinzel, serif;">+ Add</button>
                <button type="button" id="deleteProfileBtn" style="padding: 8px 15px; background: rgba(239,68,68,0.3); border: 1px solid rgba(239,68,68,0.5); border-radius: 6px; color: #ef4444; cursor: pointer; font-family: Cinzel, serif;">🗑️</button>
            </div>
        `;
        
        form.insertBefore(container, form.firstChild);
        
        // Setup event listeners
        const dropdown = document.getElementById('profileDropdown');
        const newNameInput = document.getElementById('newProfileName');
        const addBtn = document.getElementById('addProfileBtn');
        const deleteBtn = document.getElementById('deleteProfileBtn');
        
        // Populate dropdown
        function updateDropdown() {
            const profiles = getProfiles();
            const active = getActiveProfile();
            dropdown.innerHTML = '<option value="">Select or create...</option>';
            Object.keys(profiles).sort().forEach(name => {
                const opt = document.createElement('option');
                opt.value = name;
                opt.textContent = name;
                if (name === active) opt.selected = true;
                dropdown.appendChild(opt);
            });
        }
        
        // Switch profile
        dropdown.addEventListener('change', function() {
            const name = this.value;
            if (name) {
                setActiveProfile(name);
                loadData(name);
            }
        });
        
        // Add new profile
        addBtn.addEventListener('click', function() {
            const name = newNameInput.value.trim();
            if (!name) {
                alert('Please enter a profile name');
                return;
            }
            
            const profiles = getProfiles();
            if (profiles[name]) {
                if (!confirm(`Profile "${name}" exists. Update it with current form data?`)) return;
            }
            
            // Save current form data to new profile
            const data = {};
            FIELDS.forEach(field => {
                const el = document.getElementById(field);
                if (el) data[field] = el.value || '';
            });
            profiles[name] = data;
            saveProfiles(profiles);
            setActiveProfile(name);
            
            newNameInput.value = '';
            updateDropdown();
        });
        
        // Delete profile
        deleteBtn.addEventListener('click', function() {
            const name = getActiveProfile();
            if (!name) {
                alert('No profile selected');
                return;
            }
            if (!confirm(`Delete profile "${name}"?`)) return;
            
            const profiles = getProfiles();
            delete profiles[name];
            saveProfiles(profiles);
            setActiveProfile('');
            
            // Clear form
            FIELDS.forEach(field => {
                const el = document.getElementById(field);
                if (el) el.value = '';
            });
            
            updateDropdown();
        });
        
        updateDropdown();
    }

    // Attach auto-save listeners to all fields
    function setupAutoSave() {
        FIELDS.forEach(field => {
            const el = document.getElementById(field);
            if (el) {
                el.addEventListener('input', saveData);
                el.addEventListener('change', saveData);
            }
        });
    }

    // Initialize when DOM is ready
    function init() {
        createProfileSelector();
        const active = getActiveProfile();
        if (active) {
            loadData(active);
        }
        setupAutoSave();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
