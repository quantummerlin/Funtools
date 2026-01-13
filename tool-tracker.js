// Tool Usage Tracker for Quantum Merlin
// Tracks which tools users have used and suggests unexplored ones

const ToolTracker = (function() {
    const STORAGE_KEY = 'quantumMerlinToolsUsed';
    
    // All available tools with categories
    const allTools = {
        // Numerology
        'life-path-calculator.html': { title: 'Life Path Number', category: 'numerology', icon: '🔢', desc: 'Discover your soul\'s purpose' },
        'destiny-number-calculator.html': { title: 'Destiny Number', category: 'numerology', icon: '✨', desc: 'Your life mission revealed' },
        'soul-urge-calculator.html': { title: 'Soul Urge Number', category: 'numerology', icon: '💫', desc: 'Your heart\'s deepest desires' },
        'personality-number-calculator.html': { title: 'Personality Number', category: 'numerology', icon: '🎭', desc: 'How the world sees you' },
        'name-number-calculator.html': { title: 'Name Number', category: 'numerology', icon: '📝', desc: 'The power in your name' },
        'birthday-number-reading.html': { title: 'Birthday Number', category: 'numerology', icon: '🎂', desc: 'Your special gift' },
        'karmic-debt-reading.html': { title: 'Karmic Debt', category: 'numerology', icon: '⚖️', desc: 'Past life lessons' },
        'master-number-reading.html': { title: 'Master Numbers', category: 'numerology', icon: '🌟', desc: 'Your spiritual calling' },
        'maturity-number-reading.html': { title: 'Maturity Number', category: 'numerology', icon: '🌳', desc: 'Your future self' },
        'personal-year-reading.html': { title: 'Personal Year', category: 'numerology', icon: '📅', desc: 'This year\'s theme' },
        'personal-month-reading.html': { title: 'Personal Month', category: 'numerology', icon: '🗓️', desc: 'This month\'s energy' },
        'personal-day-number.html': { title: 'Personal Day', category: 'numerology', icon: '☀️', desc: 'Today\'s guidance' },
        'expression-number-reading.html': { title: 'Expression Number', category: 'numerology', icon: '🎯', desc: 'Your natural talents' },
        'hidden-passion-number.html': { title: 'Hidden Passion', category: 'numerology', icon: '🔥', desc: 'Your secret drive' },
        'pinnacle-numbers-reading.html': { title: 'Pinnacle Numbers', category: 'numerology', icon: '🏔️', desc: 'Life cycles revealed' },
        'challenge-numbers-reading.html': { title: 'Challenge Numbers', category: 'numerology', icon: '💪', desc: 'Obstacles to overcome' },
        
        // Astrology - Signs
        'moon-sign-reading.html': { title: 'Moon Sign', category: 'astrology', icon: '🌙', desc: 'Your emotional nature' },
        'rising-sign-reading.html': { title: 'Rising Sign', category: 'astrology', icon: '🌅', desc: 'Your outer personality' },
        'venus-sign-reading.html': { title: 'Venus Sign', category: 'astrology', icon: '💕', desc: 'Your love language' },
        'mars-sign-reading.html': { title: 'Mars Sign', category: 'astrology', icon: '🔥', desc: 'Your drive & passion' },
        'mercury-sign-reading.html': { title: 'Mercury Sign', category: 'astrology', icon: '💭', desc: 'How you think & communicate' },
        'jupiter-sign-reading.html': { title: 'Jupiter Sign', category: 'astrology', icon: '🍀', desc: 'Your path to luck' },
        'saturn-sign-reading.html': { title: 'Saturn Sign', category: 'astrology', icon: '⏳', desc: 'Your karmic lessons' },
        'uranus-sign-reading.html': { title: 'Uranus Sign', category: 'astrology', icon: '⚡', desc: 'Your unique genius' },
        'neptune-sign-reading.html': { title: 'Neptune Sign', category: 'astrology', icon: '🌊', desc: 'Your dreams & intuition' },
        'pluto-sign-reading.html': { title: 'Pluto Sign', category: 'astrology', icon: '🦋', desc: 'Your transformation power' },
        'chiron-reading.html': { title: 'Chiron', category: 'astrology', icon: '💔', desc: 'Your deepest wound & gift' },
        'lilith-reading.html': { title: 'Lilith', category: 'astrology', icon: '🌑', desc: 'Your shadow power' },
        'north-node-reading.html': { title: 'North Node', category: 'astrology', icon: '🧭', desc: 'Your soul\'s direction' },
        'south-node-reading.html': { title: 'South Node', category: 'astrology', icon: '🔮', desc: 'Your past life gifts' },
        'midheaven-reading.html': { title: 'Midheaven', category: 'astrology', icon: '🏆', desc: 'Your career calling' },
        'descendant-reading.html': { title: 'Descendant', category: 'astrology', icon: '👥', desc: 'Who you attract' },
        'part-of-fortune-reading.html': { title: 'Part of Fortune', category: 'astrology', icon: '🎰', desc: 'Where luck finds you' },
        
        // Relationship
        'synastry-reading.html': { title: 'Synastry', category: 'relationship', icon: '💑', desc: 'Planetary connections' },
        'composite-chart-reading.html': { title: 'Composite Chart', category: 'relationship', icon: '💞', desc: 'Your relationship\'s chart' },
        'venus-mars-compatibility.html': { title: 'Venus-Mars', category: 'relationship', icon: '❤️‍🔥', desc: 'Romantic chemistry' },
        'relationship-karma-reading.html': { title: 'Relationship Karma', category: 'relationship', icon: '🔄', desc: 'Past life connections' },
        'soul-contract-reading.html': { title: 'Soul Contract', category: 'relationship', icon: '📜', desc: 'Your soul agreement' },
        
        // Life Purpose
        'dharma-number-reading.html': { title: 'Dharma Number', category: 'purpose', icon: '🕉️', desc: 'Your sacred duty' },
        'life-mission-reading.html': { title: 'Life Mission', category: 'purpose', icon: '🎯', desc: 'Why you\'re here' },
        'vocation-reading.html': { title: 'Vocation', category: 'purpose', icon: '💼', desc: 'Your ideal career' },
        
        // Other
        'chinese-zodiac-calculator.html': { title: 'Chinese Zodiac', category: 'astrology', icon: '🐉', desc: 'Your Chinese animal sign' },
        'chinese-zodiac-reading.html': { title: 'Chinese Reading', category: 'astrology', icon: '🎋', desc: 'Deep Chinese astrology' },
        'element-calculator.html': { title: 'Element', category: 'personality', icon: '🌍', desc: 'Your elemental nature' },
        'aura-color-test.html': { title: 'Aura Color', category: 'personality', icon: '🌈', desc: 'Your energy color' },
        'color-personality-test.html': { title: 'Color Personality', category: 'personality', icon: '🎨', desc: 'Colors reveal you' },
        'brain-type-test.html': { title: 'Brain Type', category: 'personality', icon: '🧠', desc: 'How you think' },
        'stellium-reading.html': { title: 'Stellium', category: 'astrology', icon: '⭐', desc: 'Your concentrated power' },
        'modality-reading.html': { title: 'Modality', category: 'astrology', icon: '🔄', desc: 'Cardinal, Fixed, or Mutable' },
        'void-of-course-moon.html': { title: 'Void Moon', category: 'astrology', icon: '🌑', desc: 'Timing your actions' },
        'mercury-retrograde-checker.html': { title: 'Mercury Retrograde', category: 'astrology', icon: '⚠️', desc: 'Communication chaos' }
    };
    
    // Check if localStorage is available
    function isStorageAvailable() {
        try {
            localStorage.setItem('test', 'test');
            localStorage.removeItem('test');
            return true;
        } catch (e) {
            return false;
        }
    }
    
    // Get used tools
    function getUsedTools() {
        if (!isStorageAvailable()) return [];
        try {
            const data = localStorage.getItem(STORAGE_KEY);
            return data ? JSON.parse(data) : [];
        } catch (e) {
            return [];
        }
    }
    
    // Mark a tool as used
    function markUsed(toolUrl) {
        if (!isStorageAvailable()) return;
        try {
            const used = getUsedTools();
            // Normalize the URL to just the filename
            const filename = toolUrl.split('/').pop().split('?')[0];
            if (!used.includes(filename)) {
                used.push(filename);
                localStorage.setItem(STORAGE_KEY, JSON.stringify(used));
            }
        } catch (e) {
            // Storage error
        }
    }
    
    // Get unused tools
    function getUnusedTools() {
        const used = getUsedTools();
        const unused = [];
        
        for (const [url, info] of Object.entries(allTools)) {
            if (!used.includes(url)) {
                unused.push({ url, ...info });
            }
        }
        
        return unused;
    }
    
    // Get suggested tools (prioritize unused, mix of categories)
    function getSuggestedTools(count = 3, excludeUrl = null) {
        const unused = getUnusedTools();
        const used = getUsedTools();
        
        // Exclude current tool
        let candidates = unused.filter(t => t.url !== excludeUrl);
        
        // If not enough unused, add some used ones
        if (candidates.length < count) {
            const usedTools = used
                .filter(url => url !== excludeUrl && allTools[url])
                .map(url => ({ url, ...allTools[url], alreadyUsed: true }));
            candidates = [...candidates, ...usedTools];
        }
        
        // Shuffle to add variety
        candidates = candidates.sort(() => Math.random() - 0.5);
        
        // Try to get a mix of categories
        const byCategory = {};
        candidates.forEach(t => {
            if (!byCategory[t.category]) byCategory[t.category] = [];
            byCategory[t.category].push(t);
        });
        
        const result = [];
        const categories = Object.keys(byCategory).sort(() => Math.random() - 0.5);
        
        // Round-robin from categories
        let catIndex = 0;
        while (result.length < count && candidates.length > 0) {
            const cat = categories[catIndex % categories.length];
            if (byCategory[cat] && byCategory[cat].length > 0) {
                result.push(byCategory[cat].shift());
            }
            catIndex++;
            // Safety: if we've gone through all categories without adding, break
            if (catIndex > categories.length * 2 && result.length === 0) break;
        }
        
        return result;
    }
    
    // Get progress stats
    function getProgress() {
        const total = Object.keys(allTools).length;
        const used = getUsedTools().length;
        return {
            used,
            total,
            percentage: Math.round((used / total) * 100)
        };
    }
    
    // Auto-track current page on load
    function autoTrack() {
        const currentPage = window.location.pathname.split('/').pop();
        if (allTools[currentPage]) {
            markUsed(currentPage);
        }
    }
    
    // Initialize
    if (typeof window !== 'undefined') {
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', autoTrack);
        } else {
            autoTrack();
        }
    }
    
    return {
        markUsed,
        getUsedTools,
        getUnusedTools,
        getSuggestedTools,
        getProgress,
        allTools
    };
})();

// Make it globally available
if (typeof window !== 'undefined') {
    window.ToolTracker = ToolTracker;
}
