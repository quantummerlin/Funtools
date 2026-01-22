/**
 * Quantum Merlin Storage Fix for iOS Issues
 * Addresses sessionStorage/localStorage reliability problems on iOS Safari
 * 
 * Issues this fixes:
 * 1. iOS Safari private browsing - storage completely disabled
 * 2. iOS memory pressure - storage cleared unexpectedly
 * 3. Cross-tab/navigation issues - data lost during redirects
 * 4. Race conditions - data saved but not retrieved correctly
 */

const QMStorage = (function() {
    'use strict';
    
    // Test storage availability
    function testStorage(type) {
        const storage = type === 'session' ? window.sessionStorage : window.localStorage;
        try {
            const testKey = '__qm_test__';
            storage.setItem(testKey, 'test');
            const retrieved = storage.getItem(testKey);
            storage.removeItem(testKey);
            return retrieved === 'test';
        } catch (e) {
            return false;
        }
    }
    
    const storageAvailable = {
        session: testStorage('session'),
        local: testStorage('local')
    };
    
    // In-memory fallback for when storage is unavailable
    const memoryStorage = {
        session: {},
        local: {}
    };
    
    // URL parameter fallback (for critical data like readings)
    function saveToUrl(key, value) {
        try {
            // Store in hidden form field as backup
            let input = document.getElementById(`__qm_backup_${key}`);
            if (!input) {
                input = document.createElement('input');
                input.type = 'hidden';
                input.id = `__qm_backup_${key}`;
                document.body.appendChild(input);
            }
            input.value = value;
            return true;
        } catch (e) {
            console.warn('QMStorage: URL backup failed', e);
            return false;
        }
    }
    
    function getFromUrl(key) {
        try {
            // Check URL parameters first
            const urlParams = new URLSearchParams(window.location.search);
            const urlData = urlParams.get(key);
            if (urlData) return decodeURIComponent(urlData);
            
            // Check hidden form field backup
            const input = document.getElementById(`__qm_backup_${key}`);
            if (input && input.value) return input.value;
            
            return null;
        } catch (e) {
            return null;
        }
    }
    
    /**
     * Set item with multiple fallbacks
     * @param {string} key - Storage key
     * @param {string} value - Value to store
     * @param {string} type - 'session' or 'local'
     * @param {boolean} critical - If true, use URL fallback for critical data
     */
    function setItem(key, value, type = 'local', critical = false) {
        const storage = type === 'session' ? window.sessionStorage : window.localStorage;
        const memType = type === 'session' ? memoryStorage.session : memoryStorage.local;
        
        let success = false;
        
        // Try primary storage
        if (storageAvailable[type]) {
            try {
                storage.setItem(key, value);
                // Verify it was saved (iOS sometimes fails silently)
                const verify = storage.getItem(key);
                if (verify === value) {
                    success = true;
                } else {
                    console.warn(`QMStorage: ${type}Storage verification failed for ${key}`);
                }
            } catch (e) {
                console.warn(`QMStorage: ${type}Storage.setItem failed`, e);
            }
        }
        
        // Always save to memory fallback
        memType[key] = value;
        
        // For critical data (readings), also save to URL/DOM
        if (critical) {
            saveToUrl(key, value);
        }
        
        return success || critical;
    }
    
    /**
     * Get item with multiple fallbacks
     * @param {string} key - Storage key
     * @param {string} type - 'session' or 'local'
     * @param {boolean} critical - If true, check URL fallback
     */
    function getItem(key, type = 'local', critical = false) {
        const storage = type === 'session' ? window.sessionStorage : window.localStorage;
        const memType = type === 'session' ? memoryStorage.session : memoryStorage.local;
        
        // Try primary storage first
        if (storageAvailable[type]) {
            try {
                const value = storage.getItem(key);
                if (value !== null) {
                    // Also update memory cache
                    memType[key] = value;
                    return value;
                }
            } catch (e) {
                console.warn(`QMStorage: ${type}Storage.getItem failed`, e);
            }
        }
        
        // Try URL fallback for critical data
        if (critical) {
            const urlValue = getFromUrl(key);
            if (urlValue !== null) {
                // Cache it in memory
                memType[key] = urlValue;
                return urlValue;
            }
        }
        
        // Fall back to memory storage
        return memType[key] || null;
    }
    
    /**
     * Remove item from all storage locations
     */
    function removeItem(key, type = 'local') {
        const storage = type === 'session' ? window.sessionStorage : window.localStorage;
        const memType = type === 'session' ? memoryStorage.session : memoryStorage.local;
        
        if (storageAvailable[type]) {
            try {
                storage.removeItem(key);
            } catch (e) {
                console.warn(`QMStorage: ${type}Storage.removeItem failed`, e);
            }
        }
        
        delete memType[key];
        
        // Remove URL backup
        const input = document.getElementById(`__qm_backup_${key}`);
        if (input) input.remove();
    }
    
    /**
     * Save reading data with maximum reliability
     */
    function saveReading(readingData) {
        const dataStr = JSON.stringify(readingData);
        
        // Use multiple strategies
        setItem('quantumMerlinReading', dataStr, 'session', true);
        
        // Also save to localStorage as backup (survives page reloads better on iOS)
        setItem('quantumMerlinReading_backup', dataStr, 'local', false);
        setItem('quantumMerlinReading_timestamp', Date.now().toString(), 'local', false);
        
        return true;
    }
    
    /**
     * Get reading data with maximum reliability
     */
    function getReading() {
        // Try sessionStorage first (critical = true enables URL fallback)
        let data = getItem('quantumMerlinReading', 'session', true);
        
        if (!data) {
            // Try localStorage backup
            data = getItem('quantumMerlinReading_backup', 'local', false);
            
            if (data) {
                // Check if it's recent (within last 5 minutes)
                const timestamp = parseInt(getItem('quantumMerlinReading_timestamp', 'local', false) || '0');
                const age = Date.now() - timestamp;
                
                if (age > 5 * 60 * 1000) {
                    // Too old, don't use it
                    console.warn('QMStorage: Backup reading data is stale');
                    return null;
                }
            }
        }
        
        return data;
    }
    
    /**
     * Navigate with reading data (iOS-safe)
     */
    function navigateWithReading(readingData, targetUrl) {
        saveReading(readingData);
        
        // Small delay to ensure save completes on iOS
        setTimeout(() => {
            // If storage is completely unavailable, pass via URL
            if (!storageAvailable.session && !storageAvailable.local) {
                const encoded = encodeURIComponent(JSON.stringify(readingData));
                window.location.href = `${targetUrl}?data=${encoded}`;
            } else {
                window.location.href = targetUrl;
            }
        }, 100);
    }
    
    /**
     * Save profile data with validation
     */
    function saveProfile(profileName, profileData) {
        if (!profileName || !profileData) {
            console.error('QMStorage: Invalid profile data');
            return false;
        }
        
        try {
            // Get all profiles
            const profiles = JSON.parse(getItem('quantumMerlinProfiles', 'local', false) || '{}');
            
            // Add validation - ensure we're not corrupting existing data
            if (profiles[profileName] && JSON.stringify(profiles[profileName]) === JSON.stringify(profileData)) {
                // No changes, skip save
                return true;
            }
            
            profiles[profileName] = profileData;
            
            const success = setItem('quantumMerlinProfiles', JSON.stringify(profiles), 'local', false);
            
            if (success) {
                // Update active profile
                setItem('quantumMerlinActiveProfile', profileName, 'local', false);
                // Also update current user data for cross-tool compatibility
                setItem('quantumMerlinUserData', JSON.stringify(profileData), 'local', false);
            }
            
            return success;
        } catch (e) {
            console.error('QMStorage: Failed to save profile', e);
            return false;
        }
    }
    
    /**
     * Get profile data with validation
     */
    function getProfile(profileName) {
        try {
            const profiles = JSON.parse(getItem('quantumMerlinProfiles', 'local', false) || '{}');
            return profiles[profileName] || null;
        } catch (e) {
            console.error('QMStorage: Failed to get profile', e);
            return null;
        }
    }
    
    /**
     * Clear old/stale data to prevent confusion
     */
    function clearStaleData() {
        // Clear old reading backups older than 5 minutes
        try {
            const timestamp = parseInt(getItem('quantumMerlinReading_timestamp', 'local', false) || '0');
            const age = Date.now() - timestamp;
            
            if (age > 5 * 60 * 1000) {
                removeItem('quantumMerlinReading_backup', 'local');
                removeItem('quantumMerlinReading_timestamp', 'local');
            }
        } catch (e) {
            console.warn('QMStorage: Failed to clear stale data', e);
        }
    }
    
    /**
     * Get storage diagnostics
     */
    function getDiagnostics() {
        return {
            sessionStorageAvailable: storageAvailable.session,
            localStorageAvailable: storageAvailable.local,
            inMemorySessionKeys: Object.keys(memoryStorage.session).length,
            inMemoryLocalKeys: Object.keys(memoryStorage.local).length,
            userAgent: navigator.userAgent,
            isIOS: /iPad|iPhone|iPod/.test(navigator.userAgent),
            isPrivateBrowsing: !storageAvailable.session && !storageAvailable.local
        };
    }
    
    // Initialize: clean up stale data on load
    clearStaleData();
    
    // Public API
    return {
        setItem,
        getItem,
        removeItem,
        saveReading,
        getReading,
        navigateWithReading,
        saveProfile,
        getProfile,
        clearStaleData,
        getDiagnostics,
        available: storageAvailable
    };
})();

// Make available globally
window.QMStorage = QMStorage;

// Log diagnostics in development
if (window.location.hostname === 'localhost' || window.location.hostname.includes('127.0.0.1')) {
    console.log('QMStorage initialized:', QMStorage.getDiagnostics());
}
