// Simple Auto-Fill System for Quantum Merlin Tools
// Automatically saves and restores form data across all tools

(function() {
    const STORAGE_KEY = 'quantumMerlinUserData';
    const FIELDS = ['preferredName', 'birthName', 'birthDate', 'birthTime', 'birthPlace'];

    // Load saved data into form fields
    function loadData() {
        try {
            const saved = localStorage.getItem(STORAGE_KEY);
            if (!saved) return;
            
            const data = JSON.parse(saved);
            FIELDS.forEach(field => {
                const el = document.getElementById(field);
                if (el && data[field]) {
                    el.value = data[field];
                }
            });
        } catch (e) {
            console.warn('Failed to load saved data:', e);
        }
    }

    // Save current form data
    function saveData() {
        try {
            const data = {};
            FIELDS.forEach(field => {
                const el = document.getElementById(field);
                if (el) {
                    data[field] = el.value || '';
                }
            });
            localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
        } catch (e) {
            console.warn('Failed to save data:', e);
        }
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
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function() {
            loadData();
            setupAutoSave();
        });
    } else {
        loadData();
        setupAutoSave();
    }
})();
