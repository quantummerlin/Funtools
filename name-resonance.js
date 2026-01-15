/**
 * Birth Name Resonance Analysis
 * 
 * The name given at birth carries the intention, hope, and energy of those who named you.
 * This module analyzes the numerological and spiritual significance of a birth name,
 * adding depth and meaning to readings.
 */

const NameResonance = {
    // Pythagorean numerology letter values
    letterValues: {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
        'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 6, 'P': 7, 'Q': 8, 'R': 9,
        'S': 1, 'T': 2, 'U': 3, 'V': 4, 'W': 5, 'X': 6, 'Y': 7, 'Z': 8
    },

    vowels: 'AEIOU',

    // Reduce to single digit (preserving master numbers)
    reduceToSingle: function(num) {
        while (num > 9 && num !== 11 && num !== 22 && num !== 33) {
            num = String(num).split('').reduce((a, b) => a + parseInt(b), 0);
        }
        return num;
    },

    // Get letter value
    getLetterValue: function(letter) {
        return this.letterValues[letter.toUpperCase()] || 0;
    },

    // Calculate Expression Number (full name)
    calculateExpressionNumber: function(name) {
        const sum = name.toUpperCase().split('')
            .reduce((total, char) => total + this.getLetterValue(char), 0);
        return this.reduceToSingle(sum);
    },

    // Calculate Soul Urge (vowels only)
    calculateSoulUrge: function(name) {
        const sum = name.toUpperCase().split('')
            .reduce((total, char) => 
                this.vowels.includes(char) ? total + this.getLetterValue(char) : total, 0);
        return this.reduceToSingle(sum);
    },

    // Calculate Personality Number (consonants only)
    calculatePersonality: function(name) {
        const sum = name.toUpperCase().split('')
            .reduce((total, char) => 
                !this.vowels.includes(char) && /[A-Z]/.test(char) ? total + this.getLetterValue(char) : total, 0);
        return this.reduceToSingle(sum);
    },

    // Name resonance meanings
    expressionMeanings: {
        1: "independence, leadership, and pioneering spirit",
        2: "diplomacy, harmony, and partnership",
        3: "creativity, expression, and joy",
        4: "stability, structure, and dedication",
        5: "freedom, adventure, and transformation",
        6: "nurturing, responsibility, and love",
        7: "wisdom, spirituality, and introspection",
        8: "power, abundance, and achievement",
        9: "compassion, humanitarianism, and completion",
        11: "illumination, intuition, and spiritual insight",
        22: "master building, practical idealism, and legacy creation",
        33: "master teaching, healing, and unconditional love"
    },

    // Intentions behind naming
    namingIntentions: {
        1: "The one who named you envisioned a leader—someone who would forge their own path and inspire others through courage. They wanted you to stand confidently in your own truth.",
        2: "The one who named you envisioned a peacemaker—someone who would bring people together and create harmony. They wanted you to be a bridge between hearts.",
        3: "The one who named you envisioned a creative spirit—someone who would bring joy and beauty into the world. They wanted your voice to uplift and inspire.",
        4: "The one who named you envisioned a builder—someone who would create lasting foundations and be someone others could rely upon. They wanted stability for your life.",
        5: "The one who named you envisioned a free spirit—someone who would embrace life's adventures and adapt to change with grace. They wanted you to experience life fully.",
        6: "The one who named you envisioned a nurturer—someone who would care deeply for family and community. They wanted you to create a loving home wherever you go.",
        7: "The one who named you envisioned a seeker—someone who would pursue wisdom and understand life's deeper mysteries. They wanted you to find spiritual truth.",
        8: "The one who named you envisioned an achiever—someone who would attain success and use power wisely. They wanted abundance and influence for your life.",
        9: "The one who named you envisioned a humanitarian—someone who would serve the greater good and leave the world better. They wanted you to make a meaningful difference.",
        11: "The one who named you sensed something extraordinary—a soul destined for spiritual illumination. They intuited your role as a beacon of higher consciousness.",
        22: "The one who named you sensed something extraordinary—a soul destined to build lasting contributions. They intuited your capacity to turn dreams into reality on a grand scale.",
        33: "The one who named you sensed something extraordinary—a soul destined for profound service. They intuited your capacity to heal and teach through unconditional love."
    },

    // First letter energy meanings
    firstLetterEnergy: {
        'A': "initiative and ambition",
        'B': "sensitivity and cooperation",
        'C': "creativity and communication",
        'D': "determination and practicality",
        'E': "curiosity and versatility",
        'F': "responsibility and nurturing",
        'G': "analytical thinking and wisdom-seeking",
        'H': "material success and authority",
        'I': "humanitarian ideals and completion",
        'J': "leadership and originality",
        'K': "intuition and spiritual insight",
        'L': "creativity and self-expression",
        'M': "industriousness and foundation-building",
        'N': "imagination and adventure",
        'O': "nurturing and domestic harmony",
        'P': "wisdom and philosophical depth",
        'Q': "power and material mastery",
        'R': "compassion and healing service",
        'S': "emotional intensity and charm",
        'T': "growth and cooperation",
        'U': "creativity and artistic expression",
        'V': "inspiration and reliability",
        'W': "freedom and restlessness",
        'X': "creativity and self-sacrifice",
        'Y': "wisdom and independence",
        'Z': "optimism and faith"
    },

    /**
     * Generate a full birth name resonance analysis
     * @param {string} birthName - The name given at birth
     * @param {string} preferredName - The name the person identifies with (optional)
     * @returns {object} Analysis object with HTML content and data
     */
    generateAnalysis: function(birthName, preferredName = null) {
        if (!birthName || birthName.trim() === '') {
            return null;
        }

        const cleanName = birthName.trim();
        const expressionNum = this.calculateExpressionNumber(cleanName);
        const soulUrge = this.calculateSoulUrge(cleanName);
        const personality = this.calculatePersonality(cleanName);
        const firstLetter = cleanName.charAt(0).toUpperCase();

        const expressionMeaning = this.expressionMeanings[expressionNum] || this.expressionMeanings[this.reduceToSingle(expressionNum)];
        const intention = this.namingIntentions[expressionNum] || this.namingIntentions[this.reduceToSingle(expressionNum)];
        const firstLetterMeaning = this.firstLetterEnergy[firstLetter] || "unique qualities";

        // Check if name has changed
        const nameChanged = preferredName && preferredName.trim().toLowerCase() !== cleanName.toLowerCase();

        let html = `
            <div class="name-resonance-section">
                <p><strong>✨ The Resonance of Your Birth Name:</strong></p>
                <p>The name <strong>"${cleanName}"</strong> carries an Expression Number of <strong>${expressionNum}</strong>, resonating with the energy of ${expressionMeaning}.</p>
                <p>${intention}</p>
                <p>Beginning with the letter "${firstLetter}", your name was imbued with the initial energy of ${firstLetterMeaning}. This sets the tone for how you first present yourself to the world.</p>
        `;

        if (nameChanged) {
            const newExpression = this.calculateExpressionNumber(preferredName);
            const newMeaning = this.expressionMeanings[newExpression] || this.expressionMeanings[this.reduceToSingle(newExpression)];
            html += `
                <p><em>Interestingly, the name you now identify with, "${preferredName.trim()}", carries an Expression Number of ${newExpression}, resonating with ${newMeaning}. This evolution in your name reflects your soul's journey and the qualities you've grown into or are cultivating.</em></p>
            `;
        }

        html += `</div>`;

        return {
            html: html,
            data: {
                birthName: cleanName,
                expressionNumber: expressionNum,
                soulUrge: soulUrge,
                personality: personality,
                firstLetter: firstLetter,
                nameChanged: nameChanged
            }
        };
    },

    /**
     * Generate a shorter inline resonance mention
     * @param {string} birthName - The name given at birth
     * @returns {string} A brief resonance statement
     */
    generateBriefResonance: function(birthName) {
        if (!birthName || birthName.trim() === '') {
            return '';
        }

        const cleanName = birthName.trim();
        const expressionNum = this.calculateExpressionNumber(cleanName);
        const expressionMeaning = this.expressionMeanings[expressionNum] || this.expressionMeanings[this.reduceToSingle(expressionNum)];

        return `The name "${cleanName}" given to you at birth carries the resonance of ${expressionMeaning}, influencing how this energy manifests in your life.`;
    },

    /**
     * Get just the expression number and meaning for a name
     * @param {string} name - Any name
     * @returns {object} Number and meaning
     */
    getNameEnergy: function(name) {
        if (!name || name.trim() === '') {
            return null;
        }
        const num = this.calculateExpressionNumber(name.trim());
        return {
            number: num,
            meaning: this.expressionMeanings[num] || this.expressionMeanings[this.reduceToSingle(num)]
        };
    }
};

// Make available globally
if (typeof window !== 'undefined') {
    window.NameResonance = NameResonance;
}
