// Tool Usage Tracker for Quantum Merlin
// Tracks which tools users have used PER PROFILE and suggests unexplored ones

const ToolTracker = (function() {
    const STORAGE_KEY = 'quantumMerlinToolUsage';
    const LEGACY_KEY = 'quantumMerlinToolsUsed'; // For migration
    
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
    
    // Get the active profile ID
    function getActiveProfileId() {
        try {
            const activeId = localStorage.getItem('quantumMerlinActiveProfile');
            return activeId || 'default';
        } catch (e) {
            return 'default';
        }
    }
    
    // Get all usage data
    function getAllUsageData() {
        if (!isStorageAvailable()) return {};
        try {
            const data = localStorage.getItem(STORAGE_KEY);
            if (data) {
                return JSON.parse(data);
            }
            // Migrate from legacy format if exists
            const legacyData = localStorage.getItem(LEGACY_KEY);
            if (legacyData) {
                const legacyTools = JSON.parse(legacyData);
                const migrated = { 'default': {} };
                legacyTools.forEach(tool => {
                    migrated['default'][tool] = { count: 1, lastUsed: Date.now() };
                });
                localStorage.setItem(STORAGE_KEY, JSON.stringify(migrated));
                return migrated;
            }
            return {};
        } catch (e) {
            return {};
        }
    }
    
    // Get used tools for current profile
    function getUsedTools(profileId = null) {
        const pid = profileId || getActiveProfileId();
        const allData = getAllUsageData();
        const profileData = allData[pid] || {};
        return Object.keys(profileData);
    }
    
    // Get usage count for a specific tool
    function getToolUsageCount(toolUrl, profileId = null) {
        const pid = profileId || getActiveProfileId();
        const allData = getAllUsageData();
        const profileData = allData[pid] || {};
        const filename = toolUrl.split('/').pop().split('?')[0];
        return profileData[filename] ? profileData[filename].count : 0;
    }
    
    // Mark a tool as used (increments count)
    function markUsed(toolUrl) {
        if (!isStorageAvailable()) return;
        try {
            const allData = getAllUsageData();
            const pid = getActiveProfileId();
            
            if (!allData[pid]) {
                allData[pid] = {};
            }
            
            const filename = toolUrl.split('/').pop().split('?')[0];
            
            if (!allData[pid][filename]) {
                allData[pid][filename] = { count: 0, lastUsed: 0 };
            }
            
            allData[pid][filename].count++;
            allData[pid][filename].lastUsed = Date.now();
            
            localStorage.setItem(STORAGE_KEY, JSON.stringify(allData));
        } catch (e) {
            // Storage error
        }
    }
    
    // Get unused tools for current profile
    function getUnusedTools(profileId = null) {
        const used = getUsedTools(profileId);
        const unused = [];
        
        for (const [url, info] of Object.entries(allTools)) {
            if (!used.includes(url)) {
                unused.push({ url, ...info });
            }
        }
        
        return unused;
    }
    
    // Priority categories for maximum impact (in order of priority)
    const PRIORITY_CATEGORIES = ['numerology', 'astrology', 'purpose', 'relationship'];
    
    // Get suggested tools (prioritize unused, then least used, with high-impact categories first)
    function getSuggestedTools(count = 3, excludeUrl = null, profileId = null) {
        const pid = profileId || getActiveProfileId();
        const allData = getAllUsageData();
        const profileData = allData[pid] || {};
        
        // Build list with usage counts
        const toolList = [];
        for (const [url, info] of Object.entries(allTools)) {
            if (url === excludeUrl) continue;
            const usage = profileData[url] || { count: 0, lastUsed: 0 };
            // Assign priority score (lower = higher priority)
            const priorityIndex = PRIORITY_CATEGORIES.indexOf(info.category);
            const priorityScore = priorityIndex >= 0 ? priorityIndex : PRIORITY_CATEGORIES.length;
            toolList.push({ url, ...info, usageCount: usage.count, lastUsed: usage.lastUsed, priorityScore });
        }
        
        // Sort by: priority category, then unused first, then least used, then oldest last used
        toolList.sort((a, b) => {
            // Priority categories first
            if (a.priorityScore !== b.priorityScore) return a.priorityScore - b.priorityScore;
            // Unused (count 0) first
            if (a.usageCount === 0 && b.usageCount > 0) return -1;
            if (b.usageCount === 0 && a.usageCount > 0) return 1;
            // Then by count (ascending)
            if (a.usageCount !== b.usageCount) return a.usageCount - b.usageCount;
            // Then by last used (oldest first)
            return a.lastUsed - b.lastUsed;
        });
        
        // Get a mix of priority categories from the prioritized list
        const byCategory = {};
        toolList.forEach(t => {
            if (!byCategory[t.category]) byCategory[t.category] = [];
            byCategory[t.category].push(t);
        });
        
        const result = [];
        // Prioritize these categories in order, then add others
        const priorityOrder = [...PRIORITY_CATEGORIES];
        const otherCategories = Object.keys(byCategory).filter(c => !PRIORITY_CATEGORIES.includes(c));
        const orderedCategories = [...priorityOrder.filter(c => byCategory[c]), ...otherCategories];
        
        // Round-robin from categories (priority categories first)
        let catIndex = 0;
        while (result.length < count && toolList.length > 0) {
            const cat = orderedCategories[catIndex % orderedCategories.length];
            if (byCategory[cat] && byCategory[cat].length > 0) {
                result.push(byCategory[cat].shift());
            }
            catIndex++;
            if (catIndex > orderedCategories.length * count) break;
        }
        
        return result;
    }
    
    // Get progress stats for current profile
    function getProgress(profileId = null) {
        const total = Object.keys(allTools).length;
        const used = getUsedTools(profileId).length;
        return {
            used,
            total,
            percentage: Math.round((used / total) * 100)
        };
    }
    
    // Render "Go Deeper" suggestion section
    function renderGoDeeper(containerId = 'goDeeper', count = 3) {
        const container = document.getElementById(containerId);
        if (!container) return;
        
        const currentPage = window.location.pathname.split('/').pop();
        const suggestions = getSuggestedTools(count, currentPage);
        const progress = getProgress();
        
        if (suggestions.length === 0) {
            container.innerHTML = '<p style="text-align: center; color: #9A8F7A;">You\'ve explored all available tools! 🎉</p>';
            return;
        }
        
        let html = `
            <div class="go-deeper-header">
                <h3>✨ Go Deeper</h3>
                <p>Continue your journey of self-discovery</p>
                <div class="progress-bar-mini">
                    <div class="progress-fill" style="width: ${progress.percentage}%"></div>
                </div>
                <span class="progress-text">${progress.used} of ${progress.total} tools explored</span>
            </div>
            <div class="suggestion-cards">
        `;
        
        suggestions.forEach(tool => {
            const isNew = tool.usageCount === 0;
            html += `
                <a href="${tool.url}" class="suggestion-card ${isNew ? 'new-tool' : ''}">
                    <span class="suggestion-icon">${tool.icon}</span>
                    <span class="suggestion-title">${tool.title}</span>
                    <span class="suggestion-desc">${tool.desc}</span>
                    ${isNew ? '<span class="new-badge">NEW</span>' : ''}
                </a>
            `;
        });
        
        html += '</div>';
        container.innerHTML = html;
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
        getToolUsageCount,
        renderGoDeeper,
        allTools
    };
})();

// Make it globally available
if (typeof window !== 'undefined') {
    window.ToolTracker = ToolTracker;
}
