// Smooth Auto-Fill System with Auto-Save Profiles for Quantum Merlin Tools
// Automatically saves and restores form data - profiles created from names
// v2.0 - Simplified: just fill in data, it saves automatically

(function() {
    const PROFILES_KEY = 'quantumMerlinProfiles';
    const ACTIVE_KEY = 'quantumMerlinActiveProfile';
    const FIELDS = ['preferredName', 'birthName', 'birthDate', 'birthTime', 'birthPlace'];
    
    // Field mappings for different tools
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

    // Check if localStorage is available
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
        } catch (e) {}
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
        } catch (e) {}
    }
    
    // Find element by trying multiple possible IDs
    function findElement(possibleIds) {
        for (const id of possibleIds) {
            const el = document.getElementById(id);
            if (el) return el;
        }
        return null;
    }

    // Load data into form fields
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

    // Get current form data
    function getFormData() {
        const data = {};
        Object.keys(FIELD_MAPPINGS).forEach(field => {
            const el = findElement(FIELD_MAPPINGS[field]);
            if (el) data[field] = el.value || '';
        });
        return data;
    }

    // Auto-save current form data based on preferredName
    function autoSave() {
        const nameEl = findElement(FIELD_MAPPINGS.preferredName);
        if (!nameEl) return;
        
        const name = nameEl.value.trim();
        if (!name) return; // Need a name to save as profile
        
        const profiles = getProfiles();
        const data = getFormData();
        
        profiles[name] = data;
        saveProfiles(profiles);
        setActiveProfile(name);
        
        // Update dropdown if it exists
        updateDropdowns();
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

    let updateDropdowns = () => {}; // Will be set by createProfileSelector

    // Create the profile selector UI
    function createProfileSelector() {
        if (!storageAvailable) return;
        
        const form = document.querySelector('form') || document.querySelector('#toolForm') || document.querySelector('.form-section') || document.querySelector('.tool-card');
        if (!form) return;
        
        if (document.getElementById('profileSelector')) return;
        
        const isDual = isDualPersonTool();
        
        const container = document.createElement('div');
        container.id = 'profileSelector';
        container.style.cssText = 'margin-bottom: 20px; padding: 15px; background: rgba(20,20,30,0.6); border: 1px solid rgba(6,182,212,0.3); border-radius: 10px;';
        
        if (isDual) {
            container.innerHTML = `
                <div style="font-family: Cinzel, serif; color: #06b6d4; font-size: 0.85rem; margin-bottom: 10px; opacity: 0.8;">
                    💾 Saved Profiles — select to auto-fill, or just start typing to save new
                </div>
                <div style="display: flex; gap: 15px; flex-wrap: wrap;">
                    <div style="flex: 1; min-width: 200px;">
                        <label style="color: #FFD93D; font-family: Cinzel, serif; font-size: 0.9rem; display: block; margin-bottom: 5px;">👤 Person 1:</label>
                        <select id="profile1Dropdown" style="width: 100%; padding: 10px 12px; background: rgba(10,10,20,0.8); border: 1px solid rgba(255,217,61,0.4); border-radius: 6px; color: #E8E4D9; font-family: inherit; cursor: pointer;">
                            <option value="">Load saved profile...</option>
                        </select>
                    </div>
                    <div style="flex: 1; min-width: 200px;">
                        <label style="color: #FF69B4; font-family: Cinzel, serif; font-size: 0.9rem; display: block; margin-bottom: 5px;">💕 Person 2:</label>
                        <select id="profile2Dropdown" style="width: 100%; padding: 10px 12px; background: rgba(10,10,20,0.8); border: 1px solid rgba(255,105,180,0.4); border-radius: 6px; color: #E8E4D9; font-family: inherit; cursor: pointer;">
                            <option value="">Load saved profile...</option>
                        </select>
                    </div>
                </div>
                <div style="margin-top: 10px; padding-top: 10px; border-top: 1px solid rgba(255,255,255,0.1); display: flex; gap: 10px; align-items: center; flex-wrap: wrap;">
                    <label style="color: #9ca3af; font-family: Cinzel, serif; font-size: 0.85rem;">Delete:</label>
                    <select id="deleteProfileSelect" style="flex: 1; min-width: 120px; padding: 8px 12px; background: rgba(10,10,20,0.8); border: 1px solid rgba(239,68,68,0.3); border-radius: 6px; color: #E8E4D9; font-family: inherit;">
                        <option value="">Select profile to delete...</option>
                    </select>
                    <button type="button" id="deleteProfileBtn" style="padding: 8px 15px; background: rgba(239,68,68,0.2); border: 1px solid rgba(239,68,68,0.5); border-radius: 6px; color: #ef4444; cursor: pointer; font-family: Cinzel, serif;">🗑️ Delete</button>
                </div>
            `;
        } else {
            container.innerHTML = `
                <div style="display: flex; gap: 10px; align-items: center; flex-wrap: wrap;">
                    <label style="color: #C4B998; font-family: Cinzel, serif; font-size: 0.9rem;">💾 Saved:</label>
                    <select id="profileDropdown" style="flex: 1; min-width: 150px; padding: 10px 12px; background: rgba(10,10,20,0.8); border: 1px solid rgba(6,182,212,0.3); border-radius: 6px; color: #E8E4D9; font-family: inherit; cursor: pointer;">
                        <option value="">Load saved profile...</option>
                    </select>
                    <button type="button" id="deleteProfileBtn" style="padding: 8px 12px; background: rgba(239,68,68,0.2); border: 1px solid rgba(239,68,68,0.4); border-radius: 6px; color: #ef4444; cursor: pointer; font-family: Cinzel, serif; font-size: 0.85rem;">🗑️</button>
                </div>
                <div style="margin-top: 8px; font-size: 0.8rem; color: #6b7280; font-style: italic;">
                    Enter your name below — data auto-saves as you type
                </div>
            `;
        }
        
        form.insertBefore(container, form.firstChild);
        
        // Populate dropdowns
        updateDropdowns = function() {
            const profiles = getProfiles();
            const sortedNames = Object.keys(profiles).sort();
            const active = getActiveProfile();
            
            if (isDual) {
                const dropdown1 = document.getElementById('profile1Dropdown');
                const dropdown2 = document.getElementById('profile2Dropdown');
                const deleteSelect = document.getElementById('deleteProfileSelect');
                
                if (dropdown1) {
                    const current1 = dropdown1.value;
                    dropdown1.innerHTML = '<option value="">Load saved profile...</option>';
                    sortedNames.forEach(name => {
                        const opt = document.createElement('option');
                        opt.value = name;
                        opt.textContent = name;
                        dropdown1.appendChild(opt);
                    });
                    if (current1 && profiles[current1]) dropdown1.value = current1;
                }
                
                if (dropdown2) {
                    const current2 = dropdown2.value;
                    dropdown2.innerHTML = '<option value="">Load saved profile...</option>';
                    sortedNames.forEach(name => {
                        const opt = document.createElement('option');
                        opt.value = name;
                        opt.textContent = name;
                        dropdown2.appendChild(opt);
                    });
                    if (current2 && profiles[current2]) dropdown2.value = current2;
                }
                
                if (deleteSelect) {
                    deleteSelect.innerHTML = '<option value="">Select profile to delete...</option>';
                    sortedNames.forEach(name => {
                        const opt = document.createElement('option');
                        opt.value = name;
                        opt.textContent = name;
                        deleteSelect.appendChild(opt);
                    });
                }
            } else {
                const dropdown = document.getElementById('profileDropdown');
                if (dropdown) {
                    dropdown.innerHTML = '<option value="">Load saved profile...</option>';
                    sortedNames.forEach(name => {
                        const opt = document.createElement('option');
                        opt.value = name;
                        opt.textContent = name;
                        if (name === active) opt.selected = true;
                        dropdown.appendChild(opt);
                    });
                }
            }
        };
        
        // Event listeners
        if (isDual) {
            const dropdown1 = document.getElementById('profile1Dropdown');
            const dropdown2 = document.getElementById('profile2Dropdown');
            const deleteSelect = document.getElementById('deleteProfileSelect');
            const deleteBtn = document.getElementById('deleteProfileBtn');
            
            if (dropdown1) {
                dropdown1.addEventListener('change', function() {
                    if (this.value) {
                        setActiveProfile(this.value);
                        loadData(this.value, false);
                    }
                });
            }
            
            if (dropdown2) {
                dropdown2.addEventListener('change', function() {
                    if (this.value) {
                        loadData(this.value, true);
                    }
                });
            }
            
            if (deleteBtn && deleteSelect) {
                deleteBtn.addEventListener('click', function() {
                    const name = deleteSelect.value;
                    if (!name) {
                        alert('Please select a profile to delete');
                        return;
                    }
                    if (!confirm(`Delete profile "${name}"?`)) return;
                    
                    const profiles = getProfiles();
                    delete profiles[name];
                    saveProfiles(profiles);
                    
                    if (getActiveProfile() === name) setActiveProfile('');
                    
                    updateDropdowns();
                });
            }
        } else {
            const dropdown = document.getElementById('profileDropdown');
            const deleteBtn = document.getElementById('deleteProfileBtn');
            
            if (dropdown) {
                dropdown.addEventListener('change', function() {
                    if (this.value) {
                        setActiveProfile(this.value);
                        loadData(this.value);
                    }
                });
            }
            
            if (deleteBtn && dropdown) {
                deleteBtn.addEventListener('click', function() {
                    const name = dropdown.value;
                    if (!name) {
                        alert('Please select a profile to delete first');
                        return;
                    }
                    if (!confirm(`Delete profile "${name}"?`)) return;
                    
                    const profiles = getProfiles();
                    delete profiles[name];
                    saveProfiles(profiles);
                    setActiveProfile('');
                    
                    updateDropdowns();
                });
            }
        }
        
        updateDropdowns();
    }

    // Debounce function for auto-save
    function debounce(func, wait) {
        let timeout;
        return function(...args) {
            clearTimeout(timeout);
            timeout = setTimeout(() => func.apply(this, args), wait);
        };
    }

    // Attach auto-save listeners to all fields
    function setupAutoSave() {
        const debouncedSave = debounce(autoSave, 500); // Save 500ms after typing stops
        
        const allPossibleIds = [];
        Object.values(FIELD_MAPPINGS).forEach(ids => allPossibleIds.push(...ids));
        
        allPossibleIds.forEach(id => {
            const el = document.getElementById(id);
            if (el) {
                el.addEventListener('input', debouncedSave);
                el.addEventListener('change', autoSave); // Immediate on dropdown/date change
            }
        });
    }

    // Initialize
    function init() {
        createProfileSelector();
        
        // Load active profile if exists
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
