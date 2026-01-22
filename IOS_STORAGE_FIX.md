# iOS Storage Fix - Documentation

## Problem

Users on iOS Safari were experiencing issues where **wrong readings would appear** or **profile data would get mixed up**. This was caused by several iOS-specific storage limitations:

### Root Causes

1. **Private Browsing Mode**
   - sessionStorage and localStorage are completely disabled
   - Data passed via sessionStorage would be lost immediately
   - Reading results would not appear after generation

2. **Memory Pressure**
   - iOS Safari aggressively clears storage when memory is low
   - Cached data can disappear mid-session
   - Different profiles' data could get confused

3. **Silent Save Failures**
   - iOS Safari sometimes fails to save to storage without throwing errors
   - Data appears to save but isn't actually persisted
   - Leads to stale or wrong data being retrieved later

4. **Cross-Tab/Navigation Issues**
   - sessionStorage doesn't always persist correctly during redirects
   - Race conditions between save and page navigation
   - Data lost during the redirect from calculator → loading → results

## Solution Implemented

### New Files Created

1. **`storage-fix.js`** - Robust storage wrapper with iOS-specific handling
   - Multiple fallback mechanisms (sessionStorage → localStorage backup → in-memory → DOM hidden fields)
   - Save verification (confirms data was actually written)
   - Automatic stale data cleanup
   - iOS detection and special handling

2. **`apply_ios_storage_fix.py`** - Script to apply fixes to all HTML files
   - Injects storage-fix.js into all reading tools
   - Updates navigation code to use safer methods
   - Updates data retrieval to use verified methods

### Updated Files

1. **`auto-fill.js`** - Profile management improvements
   - Added data validation before save
   - Verifies profile exists before loading
   - Prevents empty/corrupted profiles from being saved
   - Checks if data actually changed before saving (avoids unnecessary writes)
   - Returns success/failure status from save operations

2. **All 62 reading/calculator HTML files**
   - Now include storage-fix.js
   - Use `QMStorage.navigateWithReading()` instead of direct sessionStorage
   - Use `QMStorage.getReading()` for reliable retrieval

### How It Works

#### Before (Problematic):
```javascript
// Could fail silently on iOS
sessionStorage.setItem('quantumMerlinReading', JSON.stringify(data));
window.location.href = 'reading-loading.html';
// Data might be lost during redirect on iOS
```

#### After (Fixed):
```javascript
// Multiple fallbacks, verified save, delayed navigation
QMStorage.navigateWithReading(readingData, 'reading-loading.html');
// Handles:
// 1. Saves to sessionStorage (if available)
// 2. Saves to localStorage backup (survives longer on iOS)
// 3. Saves to in-memory fallback
// 4. Saves to hidden DOM element
// 5. Passes via URL if storage completely unavailable
// 6. Delays navigation by 100ms to ensure save completes
```

#### Reading Retrieval:
```javascript
// Checks all fallback locations
const data = QMStorage.getReading();
// Tries in order:
// 1. sessionStorage
// 2. localStorage backup (if recent - within 5 minutes)
// 3. URL parameters
// 4. Hidden DOM elements
// 5. In-memory cache
```

### Profile Data Protection

The updated auto-fill.js now:

- **Validates before saving**: Won't save empty or malformed profiles
- **Checks for changes**: Only saves if data actually changed (reduces storage errors)
- **Verifies after saving**: Confirms data was written correctly
- **Active profile validation**: Ensures active profile actually exists
- **Structure validation**: Prevents corrupted data structures from being saved

Example:
```javascript
function saveProfiles(profiles) {
    // Validate structure
    if (typeof profiles !== 'object' || Array.isArray(profiles)) {
        console.error('Invalid profiles data, not saving');
        return false;
    }
    
    const data = JSON.stringify(profiles);
    localStorage.setItem(PROFILES_KEY, data);
    
    // VERIFY save succeeded (iOS can fail silently)
    const verify = localStorage.getItem(PROFILES_KEY);
    if (verify !== data) {
        console.warn('Save verification failed');
        return false;
    }
    
    return true;
}
```

## What's Fixed

✅ **Private browsing mode** - Readings work via URL fallback  
✅ **Memory pressure** - Multiple storage locations, picks first available  
✅ **Silent failures** - Save verification catches iOS silent failures  
✅ **Race conditions** - 100ms delay ensures save completes before navigation  
✅ **Profile corruption** - Validation prevents invalid data from being saved  
✅ **Stale data** - Automatic cleanup of old data (>5 minutes)  
✅ **Cross-tool consistency** - All 62 tools now use same reliable storage  

## Testing Checklist

### iOS Safari - Normal Mode
- [ ] Generate a reading (e.g., Life Path Calculator)
- [ ] Verify reading appears correctly on results page
- [ ] Save a profile with your data
- [ ] Switch to a different tool
- [ ] Verify profile auto-loads correctly
- [ ] Generate another reading
- [ ] Verify correct reading appears (not previous one)

### iOS Safari - Private Browsing
- [ ] Enable Private Browsing mode
- [ ] Generate a reading
- [ ] Verify reading still appears (via URL fallback)
- [ ] Try to save profile
- [ ] Verify profile saves (to in-memory fallback)
- [ ] Generate second reading
- [ ] Verify correct reading appears

### iOS Safari - Low Memory Simulation
- [ ] Open many tabs to create memory pressure
- [ ] Generate a reading
- [ ] Switch to other tabs
- [ ] Return to results tab
- [ ] Verify reading still displays correctly

## Developer Notes

### Using QMStorage in New Tools

```javascript
// For reading data that needs to survive navigation
QMStorage.saveReading(readingData);
QMStorage.navigateWithReading(readingData, 'target-page.html');

// For retrieving reading data
const readingData = QMStorage.getReading();

// For profile data
QMStorage.saveProfile(profileName, profileData);
const profileData = QMStorage.getProfile(profileName);

// For general storage with fallbacks
QMStorage.setItem('myKey', 'myValue', 'local', false);
const value = QMStorage.getItem('myKey', 'local', false);

// Get diagnostics
console.log(QMStorage.getDiagnostics());
```

### Parameters

- `type`: 'session' or 'local'
- `critical`: boolean - if true, uses URL/DOM fallbacks for critical data

### Diagnostics

You can check storage availability:
```javascript
console.log(QMStorage.getDiagnostics());
// Shows:
// - sessionStorageAvailable
// - localStorageAvailable  
// - isIOS
// - isPrivateBrowsing
// - in-memory cache stats
```

## Files Modified

- **Created:** storage-fix.js (new robust storage wrapper)
- **Created:** apply_ios_storage_fix.py (deployment script)
- **Updated:** auto-fill.js (validation and verification)
- **Updated:** 62 HTML files (injected storage-fix.js and updated navigation)

## Deployment

Already applied! All 62 reading/calculator tools now use the robust storage system.

To re-apply or apply to new files:
```bash
python apply_ios_storage_fix.py
```

## Monitoring

Storage operations now log warnings/errors to console:
- `QMStorage: Save verification failed` - indicates iOS silent failure
- `QMStorage: Backup reading data is stale` - old data auto-cleaned
- `Auto-fill: Failed to save profiles` - validation prevented save
- `Auto-fill: Active profile not found` - auto-corrects invalid state

Check browser console on iOS to see if storage issues are occurring.
