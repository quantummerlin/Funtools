// Astronomy Calculation Cache for Quantum Merlin
// Caches moon phases, planetary positions, and other calculations to reduce computation

const AstroCache = (function() {
    const CACHE_KEY = 'quantumMerlinAstroCache';
    const CACHE_DURATION = 60 * 60 * 1000; // 1 hour in milliseconds
    
    // Get cached data
    function getCache() {
        try {
            const cache = localStorage.getItem(CACHE_KEY);
            if (!cache) return {};
            const parsed = JSON.parse(cache);
            // Clean expired entries
            const now = Date.now();
            Object.keys(parsed).forEach(key => {
                if (parsed[key].expires < now) {
                    delete parsed[key];
                }
            });
            return parsed;
        } catch (e) {
            return {};
        }
    }
    
    // Save cache
    function saveCache(cache) {
        try {
            localStorage.setItem(CACHE_KEY, JSON.stringify(cache));
        } catch (e) {
            // Storage full, clear old cache
            localStorage.removeItem(CACHE_KEY);
        }
    }
    
    // Generate cache key from date (rounds to nearest hour for moon phases)
    function dateKey(date, precision = 'hour') {
        const d = new Date(date);
        if (precision === 'day') {
            return `${d.getFullYear()}-${d.getMonth()}-${d.getDate()}`;
        }
        return `${d.getFullYear()}-${d.getMonth()}-${d.getDate()}-${d.getHours()}`;
    }
    
    // Get or calculate moon phase
    function getMoonPhase(date, calculator) {
        const key = `moon_phase_${dateKey(date)}`;
        const cache = getCache();
        
        if (cache[key] && cache[key].expires > Date.now()) {
            return cache[key].data;
        }
        
        // Calculate and cache
        const result = calculator(date);
        cache[key] = {
            data: result,
            expires: Date.now() + CACHE_DURATION
        };
        saveCache(cache);
        return result;
    }
    
    // Get or calculate moon sign
    function getMoonSign(date, calculator) {
        const key = `moon_sign_${dateKey(date)}`;
        const cache = getCache();
        
        if (cache[key] && cache[key].expires > Date.now()) {
            return cache[key].data;
        }
        
        const result = calculator(date);
        cache[key] = {
            data: result,
            expires: Date.now() + CACHE_DURATION
        };
        saveCache(cache);
        return result;
    }
    
    // Get or calculate sun sign
    function getSunSign(date, calculator) {
        const key = `sun_sign_${dateKey(date, 'day')}`;
        const cache = getCache();
        
        if (cache[key] && cache[key].expires > Date.now()) {
            return cache[key].data;
        }
        
        const result = calculator(date);
        cache[key] = {
            data: result,
            expires: Date.now() + CACHE_DURATION * 24 // Cache for 24 hours
        };
        saveCache(cache);
        return result;
    }
    
    // Get or calculate Mercury retrograde status
    function getMercuryStatus(date, calculator) {
        const key = `mercury_${dateKey(date, 'day')}`;
        const cache = getCache();
        
        if (cache[key] && cache[key].expires > Date.now()) {
            return cache[key].data;
        }
        
        const result = calculator(date);
        cache[key] = {
            data: result,
            expires: Date.now() + CACHE_DURATION * 24 // Cache for 24 hours
        };
        saveCache(cache);
        return result;
    }
    
    // Get or calculate void of course moon
    function getVoidMoon(date, calculator) {
        const key = `void_moon_${dateKey(date)}`;
        const cache = getCache();
        
        if (cache[key] && cache[key].expires > Date.now()) {
            return cache[key].data;
        }
        
        const result = calculator(date);
        cache[key] = {
            data: result,
            expires: Date.now() + CACHE_DURATION
        };
        saveCache(cache);
        return result;
    }
    
    // Generic cache function for any calculation
    function getOrCalculate(cacheKey, calculator, durationMs = CACHE_DURATION) {
        const cache = getCache();
        
        if (cache[cacheKey] && cache[cacheKey].expires > Date.now()) {
            return cache[cacheKey].data;
        }
        
        const result = calculator();
        cache[cacheKey] = {
            data: result,
            expires: Date.now() + durationMs
        };
        saveCache(cache);
        return result;
    }
    
    // Clear all cached data
    function clearCache() {
        localStorage.removeItem(CACHE_KEY);
    }
    
    // Get cache stats
    function getCacheStats() {
        const cache = getCache();
        const entries = Object.keys(cache).length;
        const size = JSON.stringify(cache).length;
        return { entries, sizeBytes: size };
    }
    
    return {
        getMoonPhase,
        getMoonSign,
        getSunSign,
        getMercuryStatus,
        getVoidMoon,
        getOrCalculate,
        clearCache,
        getCacheStats
    };
})();

// Make available globally
if (typeof window !== 'undefined') {
    window.AstroCache = AstroCache;
}
