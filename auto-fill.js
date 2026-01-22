// Streamlined Auto-Fill System for Quantum Merlin Tools
// Auto-saves as you type - minimal UI, maximum convenience
// v3.0 - Ultra-streamlined: tiny dropdown, auto-save, nothing else

(function() {
    const PROFILES_KEY = 'quantumMerlinProfiles';
    const ACTIVE_KEY = 'quantumMerlinActiveProfile';
    
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
    if (!storageAvailable) return;

    function getProfiles() {
        try {
            const data = localStorage.getItem(PROFILES_KEY);
            if (!data) return {};
            const profiles = JSON.parse(data);
            // Validate structure to prevent corrupted data
            if (typeof profiles !== 'object' || Array.isArray(profiles)) {
                console.warn('Auto-fill: Corrupted profiles data, resetting');
                return {};
            }
            return profiles;
        } catch (e) { 
            console.warn('Auto-fill: Failed to load profiles', e);
            return {}; 
        }
    }

    function saveProfiles(profiles) {
        try { 
            // Validate before saving
            if (typeof profiles !== 'object' || Array.isArray(profiles)) {
                console.error('Auto-fill: Invalid profiles data, not saving');
                return false;
            }
            const data = JSON.stringify(profiles);
            localStorage.setItem(PROFILES_KEY, data);
            // Verify save succeeded (iOS Safari can fail silently)
            const verify = localStorage.getItem(PROFILES_KEY);
            if (verify !== data) {
                console.warn('Auto-fill: Save verification failed');
                return false;
            }
            return true;
        } catch (e) {
            console.warn('Auto-fill: Failed to save profiles', e);
            return false;
        }
    }

    function getActiveProfile() {
        try { 
            const name = localStorage.getItem(ACTIVE_KEY) || '';
            // Verify this profile actually exists
            if (name) {
                const profiles = getProfiles();
                if (!profiles[name]) {
                    console.warn('Auto-fill: Active profile not found, clearing');
                    setActiveProfile('');
                    return '';
                }
            }
            return name;
        } catch (e) { 
            return ''; 
        }
    }

    function setActiveProfile(name) {
        try { 
            localStorage.setItem(ACTIVE_KEY, name);
            return true;
        } catch (e) {
            console.warn('Auto-fill: Failed to set active profile', e);
            return false;
        }
    }
    
    function findElement(possibleIds) {
        for (const id of possibleIds) {
            const el = document.getElementById(id);
            if (el) return el;
        }
        return null;
    }

    function loadData(profileName, isPerson2 = false) {
        const profiles = getProfiles();
        const data = profiles[profileName];
        if (!data) return;
        
        const mappings = isPerson2 ? PERSON2_MAPPINGS : FIELD_MAPPINGS;
        Object.keys(mappings).forEach(field => {
            const el = findElement(mappings[field]);
            if (el && data[field]) el.value = data[field];
        });
    }

    function getFormData() {
        const data = {};
        Object.keys(FIELD_MAPPINGS).forEach(field => {
            const el = findElement(FIELD_MAPPINGS[field]);
            if (el) data[field] = el.value || '';
        });
        return data;
    }

    function autoSave() {
        const nameEl = findElement(FIELD_MAPPINGS.preferredName);
        if (!nameEl) return;
        
        const name = nameEl.value.trim();
        if (!name) return;
        
        const newData = getFormData();
        
        // Validate data before saving
        if (!newData.birthDate && !newData.birthTime && !newData.birthPlace) {
            // Don't save empty profiles
            return;
        }
        
        const profiles = getProfiles();
        
        // Check if data actually changed to avoid unnecessary saves
        if (profiles[name] && JSON.stringify(profiles[name]) === JSON.stringify(newData)) {
            return; // No changes, skip save
        }
        
        profiles[name] = newData;
        
        const saved = saveProfiles(profiles);
        if (saved) {
            setActiveProfile(name);
            updateDropdowns();
        } else {
            console.warn('Auto-fill: Failed to auto-save profile');
        }
    }
    
    function isDualPersonTool() {
        return document.getElementById('birthDate2') || 
               document.getElementById('date2') || 
               document.getElementById('name2') ||
               document.querySelector('[id*="person2"]') ||
               document.querySelector('[id*="Partner"]') ||
               document.querySelector('[id*="partner"]');
    }

    let updateDropdowns = () => {};

    function createProfileSelector() {
        const form = document.querySelector('form') || document.querySelector('#toolForm') || document.querySelector('.form-section') || document.querySelector('.tool-card');
        if (!form || document.getElementById('profileSelector')) return;
        
        const isDual = isDualPersonTool();
        const container = document.createElement('div');
        container.id = 'profileSelector';
        container.style.cssText = 'margin-bottom: 15px; padding: 10px 12px; background: rgba(10,10,20,0.4); border: 1px solid rgba(6,182,212,0.2); border-radius: 8px;';
        
        if (isDual) {
            container.innerHTML = `
                <div style="display: flex; gap: 12px; flex-wrap: wrap; align-items: center;">
                    <div style="display: flex; align-items: center; gap: 6px; flex: 1; min-width: 140px;">
                        <span style="color: #FFD93D; font-size: 0.8rem;">👤</span>
                        <select id="profile1Dropdown" style="flex: 1; padding: 6px 8px; background: rgba(10,10,20,0.8); border: 1px solid rgba(255,217,61,0.3); border-radius: 5px; color: #E8E4D9; font-size: 0.85rem; cursor: pointer;">
                            <option value="">Load profile...</option>
                        </select>
                    </div>
                    <div style="display: flex; align-items: center; gap: 6px; flex: 1; min-width: 140px;">
                        <span style="color: #FF69B4; font-size: 0.8rem;">💕</span>
                        <select id="profile2Dropdown" style="flex: 1; padding: 6px 8px; background: rgba(10,10,20,0.8); border: 1px solid rgba(255,105,180,0.3); border-radius: 5px; color: #E8E4D9; font-size: 0.85rem; cursor: pointer;">
                            <option value="">Load profile...</option>
                        </select>
                    </div>
                    <button type="button" id="deleteProfileBtn" title="Delete a profile" style="padding: 4px 8px; background: transparent; border: 1px solid rgba(239,68,68,0.3); border-radius: 4px; color: #ef4444; cursor: pointer; font-size: 0.75rem; opacity: 0.6; transition: opacity 0.2s;">✕</button>
                </div>
            `;
        } else {
            container.innerHTML = `
                <div style="display: flex; gap: 8px; align-items: center;">
                    <span style="color: #6b7280; font-size: 0.8rem;">💾</span>
                    <select id="profileDropdown" style="flex: 1; padding: 6px 10px; background: rgba(10,10,20,0.8); border: 1px solid rgba(6,182,212,0.25); border-radius: 5px; color: #E8E4D9; font-size: 0.85rem; cursor: pointer;">
                        <option value="">Load saved profile...</option>
                    </select>
                    <button type="button" id="deleteProfileBtn" title="Delete selected profile" style="padding: 4px 8px; background: transparent; border: 1px solid rgba(239,68,68,0.3); border-radius: 4px; color: #ef4444; cursor: pointer; font-size: 0.75rem; opacity: 0.6; transition: opacity 0.2s;">✕</button>
                </div>
            `;
        }
        
        form.insertBefore(container, form.firstChild);
        
        // Style the delete button hover
        const delBtn = container.querySelector('#deleteProfileBtn');
        if (delBtn) {
            delBtn.addEventListener('mouseenter', () => delBtn.style.opacity = '1');
            delBtn.addEventListener('mouseleave', () => delBtn.style.opacity = '0.6');
        }
        
        updateDropdowns = function() {
            const profiles = getProfiles();
            const names = Object.keys(profiles).sort();
            const active = getActiveProfile();
            
            if (isDual) {
                const d1 = document.getElementById('profile1Dropdown');
                const d2 = document.getElementById('profile2Dropdown');
                
                [d1, d2].forEach((d, i) => {
                    if (!d) return;
                    const current = d.value;
                    d.innerHTML = '<option value="">Load profile...</option>';
                    names.forEach(n => {
                        const opt = document.createElement('option');
                        opt.value = n;
                        opt.textContent = n;
                        d.appendChild(opt);
                    });
                    if (current && profiles[current]) d.value = current;
                });
            } else {
                const d = document.getElementById('profileDropdown');
                if (d) {
                    d.innerHTML = '<option value="">Load saved profile...</option>';
                    names.forEach(n => {
                        const opt = document.createElement('option');
                        opt.value = n;
                        opt.textContent = n;
                        if (n === active) opt.selected = true;
                        d.appendChild(opt);
                    });
                }
            }
        };
        
        // Event listeners
        if (isDual) {
            const d1 = document.getElementById('profile1Dropdown');
            const d2 = document.getElementById('profile2Dropdown');
            
            if (d1) d1.addEventListener('change', function() {
                if (this.value) { setActiveProfile(this.value); loadData(this.value, false); }
            });
            if (d2) d2.addEventListener('change', function() {
                if (this.value) loadData(this.value, true);
            });
        } else {
            const d = document.getElementById('profileDropdown');
            if (d) d.addEventListener('change', function() {
                if (this.value) { setActiveProfile(this.value); loadData(this.value); }
            });
        }
        
        // Delete button
        const deleteBtn = document.getElementById('deleteProfileBtn');
        if (deleteBtn) {
            deleteBtn.addEventListener('click', function() {
                const profiles = getProfiles();
                const names = Object.keys(profiles).sort();
                if (names.length === 0) {
                    alert('No profiles to delete');
                    return;
                }
                
                const name = prompt('Enter profile name to delete:\n\nSaved: ' + names.join(', '));
                if (!name) return;
                if (!profiles[name]) {
                    alert('Profile not found');
                    return;
                }
                
                delete profiles[name];
                saveProfiles(profiles);
                if (getActiveProfile() === name) setActiveProfile('');
                updateDropdowns();
            });
        }
        
        updateDropdowns();
    }

    function debounce(func, wait) {
        let timeout;
        return function(...args) {
            clearTimeout(timeout);
            timeout = setTimeout(() => func.apply(this, args), wait);
        };
    }

    function setupAutoSave() {
        const debouncedSave = debounce(autoSave, 500);
        const allIds = [];
        Object.values(FIELD_MAPPINGS).forEach(ids => allIds.push(...ids));
        
        allIds.forEach(id => {
            const el = document.getElementById(id);
            if (el) {
                el.addEventListener('input', debouncedSave);
                el.addEventListener('change', autoSave);
            }
        });
    }

    function init() {
        createProfileSelector();
        const active = getActiveProfile();
        if (active) loadData(active);
        setupAutoSave();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
