// Simple Auto-Fill System with Multiple Profiles for Quantum Merlin Tools
// Automatically saves and restores form data across all tools
// Supports dual-profile selection for compatibility tools

(function() {
    const PROFILES_KEY = 'quantumMerlinProfiles';
    const ACTIVE_KEY = 'quantumMerlinActiveProfile';
    const FIELDS = ['preferredName', 'birthName', 'birthDate', 'birthTime', 'birthPlace'];
    
    // Field mappings for different tools (maps profile field to possible element IDs)
    const FIELD_MAPPINGS = {
        birthDate: ['birthDate', 'date', 'birthDate1', 'date1'],
        birthTime: ['birthTime', 'time', 'birthTime1', 'time1'],
        birthPlace: ['birthPlace', 'place', 'birthPlace1', 'location', 'birthLocation'],
        preferredName: ['preferredName', 'name', 'name1', 'yourName'],
        birthName: ['birthName', 'fullName']
    };
    
    // Person 2 field mappings for compatibility tools
    const PERSON2_MAPPINGS = {
        birthDate: ['birthDate2', 'date2', 'partnerDate'],
        birthTime: ['birthTime2', 'time2', 'partnerTime'],
        birthPlace: ['birthPlace2', 'place2', 'partnerPlace', 'partnerLocation'],
        preferredName: ['name2', 'partnerName']
    };

    // Check if localStorage is available (blocked in some private browsing modes)
    function isStorageAvailable() {
        try {
            const test = '__storage_test__';
            localStorage.setItem(test, test);
            localStorage.removeItem(test);
            return true;
        } catch (e) {
            return false;
        }
    }

    const storageAvailable = isStorageAvailable();

    // Get all profiles
    function getProfiles() {
        if (!storageAvailable) return {};
        try {
            const saved = localStorage.getItem(PROFILES_KEY);
            return saved ? JSON.parse(saved) : {};
        } catch (e) {
            return {};
        }
    }

    // Save profiles
    function saveProfiles(profiles) {
        if (!storageAvailable) return;
        try {
            localStorage.setItem(PROFILES_KEY, JSON.stringify(profiles));
        } catch (e) {
            // Storage not available or full
        }
    }

    // Get active profile name
    function getActiveProfile() {
        if (!storageAvailable) return '';
        try {
            return localStorage.getItem(ACTIVE_KEY) || '';
        } catch (e) {
            return '';
        }
    }

    // Set active profile
    function setActiveProfile(name) {
        if (!storageAvailable) return;
        try {
            localStorage.setItem(ACTIVE_KEY, name);
        } catch (e) {
            // Storage not available
        }
    }
    
    // Find element by trying multiple possible IDs
    function findElement(possibleIds) {
        for (const id of possibleIds) {
            const el = document.getElementById(id);
            if (el) return el;
        }
        return null;
    }

    // Load data into form fields (person 1 or main form)
    function loadData(profileName, isPerson2 = false) {
        const profiles = getProfiles();
        const data = profiles[profileName];
        if (!data) return;
        
        const mappings = isPerson2 ? PERSON2_MAPPINGS : FIELD_MAPPINGS;
        
        Object.keys(mappings).forEach(field => {
            const el = findElement(mappings[field]);
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
        
        // Save from main/person1 fields
        Object.keys(FIELD_MAPPINGS).forEach(field => {
            const el = findElement(FIELD_MAPPINGS[field]);
            if (el) {
                data[field] = el.value || '';
            }
        });
        
        profiles[profileName] = data;
        saveProfiles(profiles);
    }
    
    // Check if this is a compatibility/dual-person tool
    function isDualPersonTool() {
        return document.getElementById('birthDate2') || 
               document.getElementById('date2') || 
               document.getElementById('name2') ||
               document.querySelector('[id*="person2"]') ||
               document.querySelector('[id*="Partner"]') ||
               document.querySelector('[id*="partner"]');
    }

    // Create the profile selector UI
    function createProfileSelector() {
        // Skip if storage is not available (private browsing mode)
        if (!storageAvailable) return;
        
        // Find the form or first input container
        const form = document.querySelector('form') || document.querySelector('#toolForm') || document.querySelector('.form-section') || document.querySelector('.tool-card');
        if (!form) return;
        
        // Check if we already added it
        if (document.getElementById('profileSelector')) return;
        
        const isDual = isDualPersonTool();
        
        // Create profile selector HTML
        const container = document.createElement('div');
        container.id = 'profileSelector';
        container.style.cssText = 'margin-bottom: 20px; padding: 15px; background: rgba(20,20,30,0.6); border: 1px solid rgba(6,182,212,0.3); border-radius: 10px;';
        
        if (isDual) {
            // Dual-person selector for compatibility tools
            container.innerHTML = `
                <div style="display: flex; gap: 15px; flex-wrap: wrap; margin-bottom: 10px;">
                    <div style="flex: 1; min-width: 200px;">
                        <label style="color: #FFD93D; font-family: Cinzel, serif; font-size: 0.9rem; display: block; margin-bottom: 5px;">👤 Person 1:</label>
                        <select id="profile1Dropdown" style="width: 100%; padding: 10px 12px; background: rgba(10,10,20,0.8); border: 1px solid rgba(255,217,61,0.4); border-radius: 6px; color: #E8E4D9; font-family: inherit;">
                            <option value="">Select profile...</option>
                        </select>
                    </div>
                    <div style="flex: 1; min-width: 200px;">
                        <label style="color: #FF69B4; font-family: Cinzel, serif; font-size: 0.9rem; display: block; margin-bottom: 5px;">💕 Person 2:</label>
                        <select id="profile2Dropdown" style="width: 100%; padding: 10px 12px; background: rgba(10,10,20,0.8); border: 1px solid rgba(255,105,180,0.4); border-radius: 6px; color: #E8E4D9; font-family: inherit;">
                            <option value="">Select profile...</option>
                        </select>
                    </div>
                </div>
                <div style="display: flex; gap: 10px; align-items: center; flex-wrap: wrap; padding-top: 10px; border-top: 1px solid rgba(255,255,255,0.1);">
                    <input type="text" id="newProfileName" placeholder="New profile name" style="flex: 1; min-width: 120px; padding: 8px 12px; background: rgba(10,10,20,0.8); border: 1px solid rgba(6,182,212,0.3); border-radius: 6px; color: #E8E4D9;">
                    <button type="button" id="addProfileBtn" style="padding: 8px 15px; background: linear-gradient(135deg, #06b6d4, #8b5cf6); border: none; border-radius: 6px; color: white; cursor: pointer; font-family: Cinzel, serif; white-space: nowrap;">+ Add</button>
                    <button type="button" id="deleteProfileBtn" style="padding: 8px 15px; background: rgba(239,68,68,0.3); border: 1px solid rgba(239,68,68,0.5); border-radius: 6px; color: #ef4444; cursor: pointer; font-family: Cinzel, serif;">🗑️</button>
                </div>
            `;
        } else {
            // Single person selector
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
        }
        
        form.insertBefore(container, form.firstChild);
        
        // Setup event listeners
        const newNameInput = document.getElementById('newProfileName');
        const addBtn = document.getElementById('addProfileBtn');
        const deleteBtn = document.getElementById('deleteProfileBtn');
        
        // Populate dropdown(s)
        function updateDropdowns() {
            const profiles = getProfiles();
            const active = getActiveProfile();
            const sortedNames = Object.keys(profiles).sort();
            
            if (isDual) {
                const dropdown1 = document.getElementById('profile1Dropdown');
                const dropdown2 = document.getElementById('profile2Dropdown');
                
                [dropdown1, dropdown2].forEach((dd, idx) => {
                    dd.innerHTML = '<option value="">Select profile...</option>';
                    sortedNames.forEach(name => {
                        const opt = document.createElement('option');
                        opt.value = name;
                        opt.textContent = name;
                        if (idx === 0 && name === active) opt.selected = true;
                        dd.appendChild(opt);
                    });
                });
            } else {
                const dropdown = document.getElementById('profileDropdown');
                dropdown.innerHTML = '<option value="">Select or create...</option>';
                sortedNames.forEach(name => {
                    const opt = document.createElement('option');
                    opt.value = name;
                    opt.textContent = name;
                    if (name === active) opt.selected = true;
                    dropdown.appendChild(opt);
                });
            }
        }
        
        if (isDual) {
            // Dual profile event listeners
            const dropdown1 = document.getElementById('profile1Dropdown');
            const dropdown2 = document.getElementById('profile2Dropdown');
            
            dropdown1.addEventListener('change', function() {
                if (this.value) {
                    setActiveProfile(this.value);
                    loadData(this.value, false);
                }
            });
            
            dropdown2.addEventListener('change', function() {
                if (this.value) {
                    loadData(this.value, true);
                }
            });
        } else {
            // Single profile event listener
            const dropdown = document.getElementById('profileDropdown');
            dropdown.addEventListener('change', function() {
                const name = this.value;
                if (name) {
                    setActiveProfile(name);
                    loadData(name);
                }
            });
        }
        
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
            Object.keys(FIELD_MAPPINGS).forEach(field => {
                const el = findElement(FIELD_MAPPINGS[field]);
                if (el) data[field] = el.value || '';
            });
            profiles[name] = data;
            saveProfiles(profiles);
            setActiveProfile(name);
            
            newNameInput.value = '';
            updateDropdowns();
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
            
            updateDropdowns();
        });
        
        updateDropdowns();
    }

    // Attach auto-save listeners to all fields
    function setupAutoSave() {
        // Check all possible field IDs
        const allPossibleIds = [];
        Object.values(FIELD_MAPPINGS).forEach(ids => allPossibleIds.push(...ids));
        
        allPossibleIds.forEach(id => {
            const el = document.getElementById(id);
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
