// Tool Usage Tracker for Quantum Merlin
// Version 2.0 - Enhanced with contextual recommendations
// Tracks which tools users have used PER PROFILE and suggests unexplored ones

const ToolTracker = (function() {
    const STORAGE_KEY = 'quantumMerlinToolUsage';
    const LEGACY_KEY = 'quantumMerlinToolsUsed'; // For migration
    
    // Tool relationships for contextual recommendations
    const toolRelationships = {
        // Numerology connections
        'life-path-calculator.html': ['destiny-number-calculator.html', 'soul-urge-calculator.html', 'personal-year-reading.html', 'maturity-number-reading.html'],
        'destiny-number-calculator.html': ['life-path-calculator.html', 'expression-number-reading.html', 'karmic-debt-reading.html', 'dharma-number-reading.html'],
        'soul-urge-calculator.html': ['personality-number-calculator.html', 'hidden-passion-number.html', 'life-path-calculator.html'],
        'personality-number-calculator.html': ['soul-urge-calculator.html', 'name-number-calculator.html', 'expression-number-reading.html'],
        'name-number-calculator.html': ['destiny-number-calculator.html', 'expression-number-reading.html', 'personality-number-calculator.html'],
        'karmic-debt-reading.html': ['master-number-reading.html', 'life-path-calculator.html', 'challenge-numbers-reading.html'],
        'master-number-reading.html': ['karmic-debt-reading.html', 'life-path-calculator.html', 'pinnacle-numbers-reading.html'],
        'personal-year-reading.html': ['personal-month-reading.html', 'personal-day-number.html', 'pinnacle-numbers-reading.html'],
        'personal-month-reading.html': ['personal-year-reading.html', 'personal-day-number.html'],
        'personal-day-number.html': ['personal-month-reading.html', 'personal-year-reading.html'],
        'maturity-number-reading.html': ['life-path-calculator.html', 'destiny-number-calculator.html', 'pinnacle-numbers-reading.html'],
        'pinnacle-numbers-reading.html': ['challenge-numbers-reading.html', 'maturity-number-reading.html', 'personal-year-reading.html'],
        'challenge-numbers-reading.html': ['pinnacle-numbers-reading.html', 'karmic-debt-reading.html', 'life-path-calculator.html'],
        'expression-number-reading.html': ['name-number-calculator.html', 'hidden-passion-number.html', 'soul-urge-calculator.html'],
        'hidden-passion-number.html': ['expression-number-reading.html', 'soul-urge-calculator.html', 'personality-number-calculator.html'],
        'birthday-number-reading.html': ['life-path-calculator.html', 'personal-year-reading.html', 'destiny-number-calculator.html'],
        
        // Astrology connections
        'moon-sign-reading.html': ['rising-sign-reading.html', 'venus-sign-reading.html', 'mercury-sign-reading.html', 'synastry-reading.html'],
        'rising-sign-reading.html': ['moon-sign-reading.html', 'midheaven-reading.html', 'descendant-reading.html'],
        'venus-sign-reading.html': ['mars-sign-reading.html', 'venus-mars-compatibility.html', 'synastry-reading.html', 'moon-sign-reading.html'],
        'mars-sign-reading.html': ['venus-sign-reading.html', 'venus-mars-compatibility.html', 'pluto-sign-reading.html'],
        'mercury-sign-reading.html': ['moon-sign-reading.html', 'mercury-retrograde-checker.html', 'rising-sign-reading.html'],
        'jupiter-sign-reading.html': ['saturn-sign-reading.html', 'north-node-reading.html', 'part-of-fortune-reading.html'],
        'saturn-sign-reading.html': ['jupiter-sign-reading.html', 'karmic-debt-reading.html', 'pluto-sign-reading.html', 'chiron-reading.html'],
        'uranus-sign-reading.html': ['neptune-sign-reading.html', 'pluto-sign-reading.html', 'north-node-reading.html'],
        'neptune-sign-reading.html': ['uranus-sign-reading.html', 'pluto-sign-reading.html', 'lilith-reading.html'],
        'pluto-sign-reading.html': ['saturn-sign-reading.html', 'lilith-reading.html', 'chiron-reading.html'],
        'chiron-reading.html': ['lilith-reading.html', 'saturn-sign-reading.html', 'north-node-reading.html'],
        'lilith-reading.html': ['chiron-reading.html', 'pluto-sign-reading.html', 'neptune-sign-reading.html'],
        'north-node-reading.html': ['south-node-reading.html', 'life-mission-reading.html', 'dharma-number-reading.html'],
        'south-node-reading.html': ['north-node-reading.html', 'karmic-debt-reading.html', 'saturn-sign-reading.html'],
        'midheaven-reading.html': ['rising-sign-reading.html', 'vocation-reading.html', 'saturn-sign-reading.html'],
        'descendant-reading.html': ['rising-sign-reading.html', 'venus-sign-reading.html', 'synastry-reading.html'],
        'part-of-fortune-reading.html': ['jupiter-sign-reading.html', 'north-node-reading.html', 'midheaven-reading.html'],
        'stellium-reading.html': ['modality-reading.html', 'moon-sign-reading.html', 'rising-sign-reading.html'],
        'modality-reading.html': ['stellium-reading.html', 'rising-sign-reading.html'],
        'void-of-course-moon.html': ['moon-sign-reading.html', 'mercury-retrograde-checker.html'],
        'mercury-retrograde-checker.html': ['mercury-sign-reading.html', 'void-of-course-moon.html'],
        'chinese-zodiac-calculator.html': ['chinese-zodiac-reading.html', 'element-calculator.html'],
        'chinese-zodiac-reading.html': ['chinese-zodiac-calculator.html', 'element-calculator.html'],
        
        // Relationship connections
        'synastry-reading.html': ['composite-chart-reading.html', 'venus-mars-compatibility.html', 'relationship-karma-reading.html'],
        'composite-chart-reading.html': ['synastry-reading.html', 'relationship-karma-reading.html', 'soul-contract-reading.html'],
        'venus-mars-compatibility.html': ['synastry-reading.html', 'venus-sign-reading.html', 'mars-sign-reading.html'],
        'relationship-karma-reading.html': ['soul-contract-reading.html', 'synastry-reading.html', 'south-node-reading.html'],
        'soul-contract-reading.html': ['relationship-karma-reading.html', 'north-node-reading.html', 'life-mission-reading.html'],
        'love-compatibility-reading.html': ['venus-mars-compatibility.html', 'synastry-reading.html', 'soul-mate-analysis.html'],
        'soul-mate-analysis.html': ['love-compatibility-reading.html', 'synastry-reading.html', 'relationship-karma-reading.html'],
        'relationship-life-path.html': ['love-compatibility-reading.html', 'life-path-calculator.html', 'soul-contract-reading.html'],
        
        // Life Purpose connections
        'dharma-number-reading.html': ['life-mission-reading.html', 'north-node-reading.html', 'destiny-number-calculator.html'],
        'life-mission-reading.html': ['dharma-number-reading.html', 'north-node-reading.html', 'vocation-reading.html'],
        'vocation-reading.html': ['midheaven-reading.html', 'life-mission-reading.html', 'saturn-sign-reading.html'],
        
        // Astrology extras
        'element-calculator.html': ['modality-reading.html', 'chinese-zodiac-reading.html'],
        'moon-phase-calculator.html': ['moon-sign-reading.html', 'void-of-course-moon.html'],
        'birthstone-finder.html': ['birth-flower-finder.html', 'element-calculator.html'],
        'birth-flower-finder.html': ['birthstone-finder.html', 'element-calculator.html'],
        
        // Forecasts
        'cosmic-daily-forecast.html': ['cosmic-weekly-forecast.html', 'personal-day-number.html'],
        'cosmic-weekly-forecast.html': ['cosmic-daily-forecast.html', 'cosmic-monthly-forecast.html'],
        'cosmic-monthly-forecast.html': ['cosmic-weekly-forecast.html', 'cosmic-yearly-forecast.html'],
        'cosmic-yearly-forecast.html': ['cosmic-monthly-forecast.html', 'decade-forecast.html'],
        'decade-forecast.html': ['cosmic-yearly-forecast.html', 'pinnacle-numbers-reading.html'],
        
        // Life Cycles
        'age-calculator.html': ['birthday-countdown.html', 'life-progress.html'],
        'birthday-countdown.html': ['age-calculator.html', 'personal-year-reading.html'],
        'life-progress.html': ['age-calculator.html', 'decade-forecast.html']
    };
    
    // All available tools with categories
    const allTools = {
        // Numerology (16 tools)
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
        'pinnacle-numbers-reading.html': { title: 'Pinnacle Numbers', category: 'numerology', icon: '🏔️', desc: 'Life phases revealed' },
        'challenge-numbers-reading.html': { title: 'Challenge Numbers', category: 'numerology', icon: '💪', desc: 'Obstacles to overcome' },
        
        // Compatibility (7 tools) - renamed from Relationship
        'love-compatibility-reading.html': { title: 'Deep Love Compatibility', category: 'compatibility', icon: '💕', desc: 'Complete love analysis' },
        'venus-mars-compatibility.html': { title: 'Venus-Mars', category: 'compatibility', icon: '❤️‍🔥', desc: 'Romantic chemistry' },
        'soul-mate-analysis.html': { title: 'Soul Mate Connection', category: 'compatibility', icon: '💫', desc: 'True soul mate signs' },
        'relationship-life-path.html': { title: 'Relationship Life Path', category: 'compatibility', icon: '🛤️', desc: 'Life paths in love' },
        'synastry-reading.html': { title: 'Synastry', category: 'compatibility', icon: '💑', desc: 'Planetary connections' },
        'composite-chart-reading.html': { title: 'Composite Chart', category: 'compatibility', icon: '💞', desc: 'Your relationship\'s chart' },
        'relationship-karma-reading.html': { title: 'Relationship Karma', category: 'compatibility', icon: '🔄', desc: 'Past life connections' },
        
        // Life Purpose (6 tools)
        'north-node-reading.html': { title: 'North Node', category: 'purpose', icon: '🧭', desc: 'Your soul\'s direction' },
        'south-node-reading.html': { title: 'South Node', category: 'purpose', icon: '🔮', desc: 'Your past life gifts' },
        'life-mission-reading.html': { title: 'Life Mission', category: 'purpose', icon: '🎯', desc: 'Why you\'re here' },
        'dharma-number-reading.html': { title: 'Dharma Number', category: 'purpose', icon: '🕉️', desc: 'Your sacred duty' },
        'vocation-reading.html': { title: 'Vocation', category: 'purpose', icon: '💼', desc: 'Your ideal career' },
        'soul-contract-reading.html': { title: 'Soul Contract', category: 'purpose', icon: '📜', desc: 'Your soul agreement' },
        
        // Astrology (21 tools) - Ordered: Rising → Moon → Personal → Social → Outer → Points → Patterns → Extras
        'rising-sign-reading.html': { title: 'Rising Sign', category: 'astrology', icon: '🌅', desc: 'Your outer personality' },
        'moon-sign-reading.html': { title: 'Moon Sign', category: 'astrology', icon: '🌙', desc: 'Your emotional nature' },
        'mercury-sign-reading.html': { title: 'Mercury Sign', category: 'astrology', icon: '💭', desc: 'How you think' },
        'venus-sign-reading.html': { title: 'Venus Sign', category: 'astrology', icon: '💕', desc: 'Your love language' },
        'mars-sign-reading.html': { title: 'Mars Sign', category: 'astrology', icon: '🔥', desc: 'Your drive & passion' },
        'jupiter-sign-reading.html': { title: 'Jupiter Sign', category: 'astrology', icon: '🍀', desc: 'Your path to luck' },
        'saturn-sign-reading.html': { title: 'Saturn Sign', category: 'astrology', icon: '⏳', desc: 'Your karmic lessons' },
        'uranus-sign-reading.html': { title: 'Uranus Sign', category: 'astrology', icon: '⚡', desc: 'Your unique genius' },
        'neptune-sign-reading.html': { title: 'Neptune Sign', category: 'astrology', icon: '🌊', desc: 'Your dreams & intuition' },
        'pluto-sign-reading.html': { title: 'Pluto Sign', category: 'astrology', icon: '🦋', desc: 'Your transformation power' },
        'chiron-reading.html': { title: 'Chiron', category: 'astrology', icon: '💔', desc: 'Your deepest wound & gift' },
        'lilith-reading.html': { title: 'Lilith', category: 'astrology', icon: '🌑', desc: 'Your shadow power' },
        'midheaven-reading.html': { title: 'Midheaven', category: 'astrology', icon: '🏆', desc: 'Your career calling' },
        'descendant-reading.html': { title: 'Descendant', category: 'astrology', icon: '👥', desc: 'Who you attract' },
        'part-of-fortune-reading.html': { title: 'Part of Fortune', category: 'astrology', icon: '🎰', desc: 'Where luck finds you' },
        'stellium-reading.html': { title: 'Stellium', category: 'astrology', icon: '⭐', desc: 'Your concentrated power' },
        'modality-reading.html': { title: 'Modality', category: 'astrology', icon: '🔄', desc: 'Cardinal, Fixed, or Mutable' },
        'moon-phase-calculator.html': { title: 'Moon Phase', category: 'astrology', icon: '🌓', desc: 'Your birth moon phase' },
        'void-of-course-moon.html': { title: 'Void Moon', category: 'astrology', icon: '🌑', desc: 'Timing your actions' },
        'mercury-retrograde-checker.html': { title: 'Mercury Retrograde', category: 'astrology', icon: '⚠️', desc: 'Communication chaos' },
        'chinese-zodiac-reading.html': { title: 'Chinese Zodiac', category: 'astrology', icon: '🐉', desc: 'Your animal sign' },
        
        // Forecasts (5 cosmic tools - removed numerology forecasts)
        'cosmic-daily-forecast.html': { title: 'Cosmic Daily', category: 'forecasts', icon: '✨', desc: 'Complete daily guidance' },
        'cosmic-weekly-forecast.html': { title: 'Cosmic Weekly', category: 'forecasts', icon: '🌟', desc: 'Your week ahead' },
        'cosmic-monthly-forecast.html': { title: 'Cosmic Monthly', category: 'forecasts', icon: '🌙', desc: 'Monthly cosmic guide' },
        'cosmic-yearly-forecast.html': { title: 'Cosmic Yearly', category: 'forecasts', icon: '🎆', desc: 'Year-long forecast' },
        'decade-forecast.html': { title: 'Decade Forecast', category: 'forecasts', icon: '📊', desc: 'Long-term life cycles' },
        
        // Life Cycles (3 tools)
        'age-calculator.html': { title: 'Cosmic Age', category: 'life', icon: '⏰', desc: 'Your cosmic timeline' },
        'birthday-countdown.html': { title: 'Solar Return', category: 'life', icon: '🎂', desc: 'Countdown to rebirth' },
        'life-progress.html': { title: 'Life Journey', category: 'life', icon: '📈', desc: 'Your progress through time' }
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
    const PRIORITY_CATEGORIES = ['numerology', 'astrology', 'purpose', 'compatibility', 'forecasts', 'life'];
    
    // Category display names
    const CATEGORY_NAMES = {
        'numerology': 'Numerology',
        'astrology': 'Astrology',
        'purpose': 'Life Purpose',
        'compatibility': 'Compatibility',
        'forecasts': 'Forecasts',
        'life': 'Life Cycles'
    };
    
    // Get related tools for a given tool (contextual recommendations)
    function getRelatedTools(toolUrl) {
        const filename = toolUrl.split('/').pop().split('?')[0];
        return toolRelationships[filename] || [];
    }
    
    // Get the category of a tool
    function getToolCategory(toolUrl) {
        const filename = toolUrl.split('/').pop().split('?')[0];
        return allTools[filename] ? allTools[filename].category : null;
    }
    
    // Get suggested tools with contextual awareness
    // Priority: 1) Related unused tools, 2) Same category unused, 3) Other priority categories unused, 4) Least used
    function getSuggestedTools(count = 3, excludeUrl = null, profileId = null, contextToolUrl = null) {
        const pid = profileId || getActiveProfileId();
        const allData = getAllUsageData();
        const profileData = allData[pid] || {};
        
        // Normalize exclude URL
        const excludeFilename = excludeUrl ? excludeUrl.split('/').pop().split('?')[0] : null;
        const contextFilename = contextToolUrl ? contextToolUrl.split('/').pop().split('?')[0] : excludeFilename;
        
        // Get related tools for context
        const relatedToolUrls = contextFilename ? getRelatedTools(contextFilename) : [];
        const currentCategory = contextFilename && allTools[contextFilename] ? allTools[contextFilename].category : null;
        
        // Build list with usage counts and recommendation reasons
        const toolList = [];
        for (const [url, info] of Object.entries(allTools)) {
            if (url === excludeFilename) continue;
            
            const usage = profileData[url] || { count: 0, lastUsed: 0 };
            const isRelated = relatedToolUrls.includes(url);
            const isSameCategory = currentCategory && info.category === currentCategory;
            const priorityIndex = PRIORITY_CATEGORIES.indexOf(info.category);
            const priorityScore = priorityIndex >= 0 ? priorityIndex : PRIORITY_CATEGORIES.length;
            
            // Determine recommendation reason
            let reason = '';
            let reasonPriority = 10;
            
            if (isRelated && usage.count === 0) {
                reason = 'Related to your reading';
                reasonPriority = 0;
            } else if (isSameCategory && usage.count === 0) {
                reason = `More ${CATEGORY_NAMES[info.category] || info.category}`;
                reasonPriority = 1;
            } else if (usage.count === 0) {
                reason = 'New for you';
                reasonPriority = 2;
            } else if (isRelated) {
                reason = 'Complements your journey';
                reasonPriority = 3;
            } else if (isSameCategory) {
                reason = 'Explore further';
                reasonPriority = 4;
            } else {
                reason = 'Discover more';
                reasonPriority = 5;
            }
            
            toolList.push({ 
                url, 
                ...info, 
                usageCount: usage.count, 
                lastUsed: usage.lastUsed, 
                priorityScore,
                isRelated,
                isSameCategory,
                reason,
                reasonPriority,
                categoryName: CATEGORY_NAMES[info.category] || info.category
            });
        }
        
        // Sort by: reason priority, then usage (unused first), then category priority
        toolList.sort((a, b) => {
            // Related unused first
            if (a.reasonPriority !== b.reasonPriority) return a.reasonPriority - b.reasonPriority;
            // Unused first
            if (a.usageCount === 0 && b.usageCount > 0) return -1;
            if (b.usageCount === 0 && a.usageCount > 0) return 1;
            // Priority categories
            if (a.priorityScore !== b.priorityScore) return a.priorityScore - b.priorityScore;
            // Then by count (ascending)
            if (a.usageCount !== b.usageCount) return a.usageCount - b.usageCount;
            // Then by last used (oldest first)
            return a.lastUsed - b.lastUsed;
        });
        
        // Get a diverse mix - prefer one from each reason type
        const result = [];
        const usedReasons = new Set();
        const usedCategories = new Set();
        
        // First pass: get diverse suggestions
        for (const tool of toolList) {
            if (result.length >= count) break;
            
            // Prioritize diversity in reasons and categories
            const reasonKey = tool.reason;
            const catKey = tool.category;
            
            // Always take related tools
            if (tool.isRelated && tool.usageCount === 0) {
                result.push(tool);
                usedReasons.add(reasonKey);
                usedCategories.add(catKey);
            } else if (!usedReasons.has(reasonKey) || !usedCategories.has(catKey)) {
                result.push(tool);
                usedReasons.add(reasonKey);
                usedCategories.add(catKey);
            }
        }
        
        // Second pass: fill remaining slots
        if (result.length < count) {
            for (const tool of toolList) {
                if (result.length >= count) break;
                if (!result.includes(tool)) {
                    result.push(tool);
                }
            }
        }
        
        return result.slice(0, count);
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
    
    // Render "Go Deeper" suggestion section with enhanced UI
    function renderGoDeeper(containerId = 'goDeeper', count = 3, contextToolUrl = null) {
        const container = document.getElementById(containerId);
        if (!container) return;
        
        const currentPage = window.location.pathname.split('/').pop();
        const contextUrl = contextToolUrl || currentPage;
        const suggestions = getSuggestedTools(count, currentPage, null, contextUrl);
        const progress = getProgress();
        
        if (suggestions.length === 0) {
            container.innerHTML = `
                <div class="go-deeper-header">
                    <h3>🎉 Journey Complete!</h3>
                    <p>You've explored all available tools. Your cosmic knowledge is truly impressive!</p>
                    <div class="progress-bar-mini">
                        <div class="progress-fill" style="width: 100%"></div>
                    </div>
                    <span class="progress-text">${progress.total} of ${progress.total} tools explored</span>
                </div>
            `;
            return;
        }
        
        // Determine intro text based on whether there are related/new tools
        const hasRelated = suggestions.some(t => t.isRelated && t.usageCount === 0);
        const hasNew = suggestions.some(t => t.usageCount === 0);
        let introText = 'Continue your journey of self-discovery';
        
        if (hasRelated) {
            introText = 'These readings complement what you just discovered';
        } else if (hasNew) {
            introText = 'Explore new dimensions of your cosmic blueprint';
        }
        
        let html = `
            <div class="go-deeper-header">
                <h3>✨ Go Deeper</h3>
                <p>${introText}</p>
                <div class="progress-bar-mini">
                    <div class="progress-fill" style="width: ${progress.percentage}%"></div>
                </div>
                <span class="progress-text">${progress.used} of ${progress.total} tools explored</span>
            </div>
            <div class="suggestion-cards">
        `;
        
        suggestions.forEach(tool => {
            const isNew = tool.usageCount === 0;
            const isRelated = tool.isRelated && isNew;
            const cardClass = isNew ? (isRelated ? 'new-tool related-tool' : 'new-tool') : '';
            
            // Determine which badge to show
            let badge = '';
            if (isNew) {
                badge = '<span class="new-badge">NEW</span>';
            } else if (tool.isRelated) {
                badge = '<span class="recommended-badge">★</span>';
            }
            
            html += `
                <a href="${tool.url}" class="suggestion-card ${cardClass}">
                    <span class="category-badge ${tool.category}">${tool.categoryName}</span>
                    ${badge}
                    <span class="suggestion-icon">${tool.icon}</span>
                    <span class="suggestion-reason">${tool.reason}</span>
                    <span class="suggestion-title">${tool.title}</span>
                    <span class="suggestion-desc">${tool.desc}</span>
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
        getRelatedTools,
        getToolCategory,
        renderGoDeeper,
        allTools,
        CATEGORY_NAMES
    };
})();

// Make it globally available
if (typeof window !== 'undefined') {
    window.ToolTracker = ToolTracker;
}
