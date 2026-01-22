# Quantum Merlin Website - Comprehensive Rebranding Guide

> **Last Updated:** January 21, 2026  
> **Site URL:** https://quantummerlin.com/classic  
> **Total Tools:** 58 (16 Numerology + 21 Astrology + 7 Compatibility + 6 Life Purpose + 5 Forecasts + 3 Life Cycles)

---

## Table of Contents

1. [Site Overview](#1-site-overview)
2. [Site Structure](#2-site-structure)
3. [User Flows](#3-user-flows)
4. [Core Features](#4-core-features)
5. [Key Files Reference](#5-key-files-reference)
6. [Branding Elements - Complete Checklist](#6-branding-elements---complete-checklist)
7. [Third-Party Dependencies](#7-third-party-dependencies)
8. [Tool Categories - Complete List](#8-tool-categories---complete-list)
9. [Rebranding Implementation Steps](#9-rebranding-implementation-steps)

---

## 1. Site Overview

### Brand Identity
- **Name:** Quantum Merlin
- **Tagline:** "Ancient Patterns. Modern Interfaces."
- **Description:** Maps time, numbers, and celestial cycles into clear moments for aligned action — blending ancient pattern wisdom with modern interface clarity.
- **Theme:** Merlin/Arthur Mythology + 80s Tron Aesthetic (neon colors, dark backgrounds)

### Color Palette
```css
/* Primary Brand Colors */
--text-accent-gold: #FFD93D;      /* Mystical gold */
--text-accent-cyan: #00F5FF;      /* Tron cyan */
--text-accent-magenta: #FF00FF;   /* Tron magenta */
--text-accent-purple: #BF5AF2;    /* Mystical purple */
--theme-color: #bf5af2;           /* PWA theme color */
--bg-primary: #0a0a0f;            /* Dark background */
```

### Fonts (Google Fonts)
- **Cinzel Decorative** - Headers, titles (mystical feel)
- **Cinzel** - Subheadings, buttons
- **Cormorant Garamond** - Body text

---

## 2. Site Structure

### Main Pages

| File | Purpose |
|------|---------|
| `index.html` | Redirect page → redirects to `tools_index.html` |
| `tools_index.html` | **Main Hub** - All tools organized by category |
| `privacy.html` | Privacy Policy |
| `terms.html` | Terms of Service |
| `disclaimer.html` | Entertainment Disclaimer |
| `advertise.html` | Advertising information |
| `forecasts.html` | Forecasts landing page |

### Tool Pages (58 Total)

All tools follow a consistent naming convention: `[tool-name].html`

Example structure:
- Input form with profile management
- Calculate button
- Results display with cosmic loader animation
- Share buttons
- Related tool suggestions
- Legal footer with feedback link

---

## 3. User Flows

### Primary User Flow
```
Landing (index.html)
    ↓ (auto-redirect)
Tools Hub (tools_index.html)
    ↓ (Welcome Modal for new users)
    ↓
Category Selection (collapsed sections)
    ↓
Tool Selection (click tool card)
    ↓
Tool Page (e.g., life-path-calculator.html)
    ↓ (enter birth data / auto-fill from profile)
Calculate → Cosmic Loader Animation → Results Display
    ↓
Share Results (Twitter, Facebook, WhatsApp, Email, SMS, Copy Link)
    ↓
Explore Related Tools (contextual suggestions)
    ↓
Return to Hub (← back button)
```

### Profile Flow
```
First Visit:
    User enters birth data → Auto-saved with preferred name
    ↓
Return Visit:
    Profile auto-loads from localStorage
    ↓
    Can switch profiles via dropdown
    ↓
    Profile data persists across all tools
```

---

## 4. Core Features

### 4.1 Profile Management System

**localStorage Keys:**
```javascript
'quantumMerlinProfiles'       // All saved profiles (JSON object)
'quantumMerlinActiveProfile'  // Currently active profile name
'quantumMerlinUserData'       // Current form data
```

**Profile Data Structure:**
```javascript
{
    preferredName: "John",
    birthName: "John Smith",      // Optional, for name numerology
    birthDate: "1990-05-15",
    birthTime: "14:30",           // Optional, for rising sign/moon sign
    birthPlace: "New York, USA",  // Optional, for location-based calcs
    timezone: "America/New_York"
}
```

**Key Files:**
- `profile-manager.js` - Core profile CRUD operations
- `auto-fill.js` - Auto-fill and streamlined profile UI

### 4.2 Tool Progress Tracking

**localStorage Keys:**
```javascript
'quantumMerlinToolUsage'    // Per-profile tool usage data
'quantumMerlinFavorites'    // User's favorited tools
```

**Key File:** `tool-tracker.js`

**Features:**
- Tracks which tools each profile has used
- Shows "NEW" badge on unexplored tools
- Journey progress bar on main hub
- Contextual tool recommendations
- Favorites system (starred tools)

### 4.3 Welcome Modal (First-Time Visitors)

**localStorage Keys:**
```javascript
'quantumMerlinWelcomed'     // Flag for welcome modal shown
```

**Content Highlights:**
- No Sign-Up required
- 100% Free
- No Data Collection (stays on device)
- Enter Once, Explore All (auto-fill)
- Save to Home Screen prompt

**Location:** Bottom of `tools_index.html`

### 4.4 Cosmic Loader Animation

**File:** `cosmic-loader.js`

Shows "Consulting the Cosmic Patterns" animation with:
- Animated mystical orb
- Sequential loading messages
- Ad placeholder space
- Smooth fade transition to results

### 4.5 Share Functionality

**File:** `share-utils.js`

**Share Platforms:**
- Twitter/X
- Facebook
- WhatsApp
- Email
- SMS
- Copy Link to Clipboard
- Native Share API (mobile)

**Configuration:**
```javascript
baseUrl: 'https://quantummerlin.com/classic/'
hashtags: 'quantummerlin,numerology'
```

### 4.6 PWA Capabilities

**PWA Files:**
| File | Purpose |
|------|---------|
| `manifest.json` | PWA manifest with app info |
| `sw.js` | Service Worker for caching |
| `favicon.svg` | Vector favicon |
| `RetroMerlin.jpg` | App icon (512x512) |

**PWA Features:**
- Install to home screen
- Standalone display mode
- Offline-capable (basic caching)
- Theme color integration
- Shortcuts to popular tools

---

## 5. Key Files Reference

### JavaScript Files

| File | Purpose |
|------|---------|
| `tool-tracker.js` | Tool usage tracking, recommendations, journey progress |
| `profile-manager.js` | Profile CRUD operations |
| `auto-fill.js` | Auto-fill system, streamlined profile UI |
| `cosmic-loader.js` | Loading animation between calculate and results |
| `share-utils.js` | Social sharing functionality |
| `astro-cache.js` | Caching for astronomical calculations |
| `name-resonance.js` | Name-based calculations |

### CSS Files

| File | Purpose |
|------|---------|
| `quantum-merlin-styles.css` | Main design system CSS |
| `go-deeper.css` | Styles for "go deeper" sections |

### Python Build Scripts

| File | Purpose |
|------|---------|
| `apply_branding.py` | Apply branding across all HTML files |
| `apply_quantum_branding.py` | Quantum Merlin specific branding |
| `apply_cache_busting.py` | Add version params to assets |
| `apply_og_meta.py` | Add Open Graph meta tags |
| `apply_pwa_meta.py` | Add PWA meta tags |
| `apply_share_buttons.py` | Add share buttons to tools |
| `add_footer_feedback.py` | Add feedback footer |
| `add_profiles.py` | Add profile management |
| `apply_cosmic_loader.py` | Add cosmic loader |

### Configuration Files

| File | Purpose |
|------|---------|
| `manifest.json` | PWA manifest |
| `sw.js` | Service worker |
| `CNAME` | Custom domain (quantummerlin.com/classic) |
| `robots.txt` | Search engine directives |
| `sitemap.xml` | Sitemap for SEO |
| `ads.txt` | Ads configuration |
| `_headers` | HTTP headers (Cloudflare/Netlify) |

---

## 6. Branding Elements - Complete Checklist

### 6.1 Text/String Replacements

#### Brand Name: "Quantum Merlin"
**Appears in:**

1. **Page Titles** (all 58+ HTML files)
   ```html
   <title>Tool Name | Quantum Merlin</title>
   ```

2. **PWA Meta Tags** (all HTML files)
   ```html
   <meta name="apple-mobile-web-app-title" content="Quantum Merlin">
   <meta name="application-name" content="Quantum Merlin">
   ```

3. **Open Graph / Twitter Meta** (all HTML files)
   ```html
   <meta property="og:title" content="Quantum Merlin | Ancient Patterns. Modern Interfaces.">
   <meta name="twitter:title" content="Quantum Merlin | Ancient Patterns. Modern Interfaces.">
   ```

4. **JSON-LD Schema** (all HTML files)
   ```json
   "name": "Quantum Merlin"
   "provider": { "name": "Quantum Merlin" }
   ```

5. **manifest.json**
   ```json
   "name": "Quantum Merlin - Ancient Patterns. Modern Interfaces."
   "short_name": "Quantum Merlin"
   "id": "quantum-merlin-pwa"
   ```

6. **Service Worker** (`sw.js`)
   ```javascript
   const CACHE_NAME = `quantum-merlin-v${CACHE_VERSION}`;
   ```

7. **JavaScript Files**
   - `tool-tracker.js` - Comment header
   - `cosmic-loader.js` - Comment header
   - `share-utils.js` - Comment header, hashtags
   - `auto-fill.js` - Comment header
   - `profile-manager.js` - Comment header

8. **Header/Logo** (all tool pages + hub)
   ```html
   <h1>QUANTUM MERLIN</h1>
   <img src="RetroMerlin.jpg" alt="Quantum Merlin" class="wizard-logo">
   ```

9. **PWA Loader Text** (`tools_index.html`)
   ```html
   <div class="pwa-loader-text">QUANTUM MERLIN</div>
   ```

10. **Welcome Modal** (`tools_index.html`)
    ```html
    <h2 class="welcome-title">Welcome to Quantum Merlin</h2>
    ```

11. **Footer Copyright** (all HTML files)
    ```html
    <p class="copyright">&copy; 2026 Quantum Merlin. For entertainment purposes only.</p>
    ```

12. **Back Button Text** (all tool pages)
    ```html
    <button class="back-btn" onclick="goBack()">← Quantum Merlin Hub</button>
    ```

13. **Footer Text** (`tools_index.html`)
    ```html
    <p>© 2026 Quantum Merlin | Revealing patterns already in motion</p>
    ```

14. **Privacy Policy Content** (`privacy.html`)
    - Multiple references to "Quantum Merlin" in body text

15. **CSS File** (`quantum-merlin-styles.css`)
    - Filename itself contains brand
    - Comment header

### 6.2 Domain/URL Replacements

#### Domain: `quantummerlin.com/classic`

**Appears in:**

1. **CNAME file**
   ```
   quantummerlin.com/classic
   ```

2. **Canonical URLs** (all HTML files)
   ```html
   <link rel="canonical" href="https://quantummerlin.com/classic/[page].html">
   ```

3. **Open Graph URLs** (all HTML files)
   ```html
   <meta property="og:url" content="https://quantummerlin.com/classic/[page].html">
   <meta property="og:image" content="https://quantummerlin.com/classic/RetroMerlin.jpg">
   <meta name="twitter:url" content="https://quantummerlin.com/classic/[page].html">
   <meta name="twitter:image" content="https://quantummerlin.com/classic/RetroMerlin.jpg">
   ```

4. **JSON-LD Schema** (all HTML files)
   ```json
   "url": "https://quantummerlin.com/classic/[page].html"
   "provider": { "url": "https://quantummerlin.com/classic" }
   ```

5. **share-utils.js**
   ```javascript
   baseUrl: 'https://quantummerlin.com/classic/'
   ```

### 6.3 Email Addresses

| Email | Purpose | Location |
|-------|---------|----------|
| `fixit@quantummerlin.com` | Bug reports/feedback | All footers, welcome modal |
| `ads@quantummerlin.com` | Advertising inquiries | `tools_index.html` |
| `privacy@quantummerlin.com` | Privacy concerns | `privacy.html` |

### 6.4 External Accounts/Links

| Service | URL | Location |
|---------|-----|----------|
| Buy Me a Coffee | `https://buymeacoffee.com/quantummerlin` | All footers |

### 6.5 localStorage Keys (IMPORTANT!)

All localStorage keys contain brand name and should be updated for rebranding:

```javascript
// Profile System
'quantumMerlinProfiles'
'quantumMerlinActiveProfile'
'quantumMerlinUserData'

// Tool Tracking
'quantumMerlinToolUsage'
'quantumMerlinFavorites'

// Welcome Modal
'quantumMerlinWelcomed'
```

**Files containing localStorage keys:**
- `tool-tracker.js`
- `profile-manager.js`
- `auto-fill.js`
- All 58+ HTML tool files (inline scripts)
- Python generator scripts

⚠️ **WARNING:** Changing localStorage keys will reset user data! Consider a migration script.

### 6.6 Files to Rename

| Current Name | Contains Brand |
|--------------|----------------|
| `quantum-merlin-styles.css` | ✓ Rename or keep |
| `apply_quantum_branding.py` | ✓ Rename |

### 6.7 Images/Assets

| File | Purpose | Action Needed |
|------|---------|---------------|
| `RetroMerlin.jpg` | Main logo/icon (512x512) | Replace with new logo |
| `favicon.svg` | Vector favicon | Update design if needed |

---

## 7. Third-Party Dependencies

### External Libraries (CDN)

| Library | Version | Purpose | Used In |
|---------|---------|---------|---------|
| **astronomy-engine** | 2.1.19 | Planetary calculations | Moon sign, rising sign, planets, forecasts |
| **SunCalc** | 1.9.0 | Sun/moon calculations | Moon phase, cosmic forecasts |
| **html2canvas** | 1.4.1 | Screenshot for sharing | share-utils.js (lazy loaded) |
| **Google Fonts** | N/A | Typography | All pages |

### CDN URLs
```html
<!-- astronomy-engine -->
<script src="https://cdn.jsdelivr.net/npm/astronomy-engine@2.1.19/astronomy.browser.min.js"></script>

<!-- SunCalc -->
<script src="https://cdn.jsdelivr.net/npm/suncalc@1.9.0/suncalc.js"></script>

<!-- html2canvas (lazy loaded) -->
script.src = 'https://cdn.jsdelivr.net/npm/html2canvas@1.4.1/dist/html2canvas.min.js';

<!-- Google Fonts -->
<link href="https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@400;700;900&family=Cinzel:wght@400;500;600;700;800;900&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&display=swap" rel="stylesheet">
```

### Third-Party Services

| Service | Purpose | Configuration |
|---------|---------|---------------|
| GitHub Pages | Hosting | Via CNAME |
| Super Ninja Analytics | Analytics | Script in tools_index.html |

---

## 8. Tool Categories - Complete List

### 🔢 Numerology (16 tools)

| File | Title | Description |
|------|-------|-------------|
| `life-path-calculator.html` | Life Path Number | Calculate life path and reveal purpose |
| `destiny-number-calculator.html` | Destiny Number | Life's mission revealed |
| `soul-urge-calculator.html` | Soul Urge Number | Heart's deepest desires |
| `personality-number-calculator.html` | Personality Number | How the world sees you |
| `name-number-calculator.html` | Name Number | Power in your name |
| `birthday-number-reading.html` | Birthday Number | Your special gift |
| `expression-number-reading.html` | Expression Number | Natural talents |
| `hidden-passion-number.html` | Hidden Passion | Secret drive |
| `karmic-debt-reading.html` | Karmic Debt | Past life lessons (13, 14, 16, 19) |
| `master-number-reading.html` | Master Numbers | Spiritual calling (11, 22, 33) |
| `maturity-number-reading.html` | Maturity Number | Future self |
| `personal-year-reading.html` | Personal Year | This year's theme |
| `personal-month-reading.html` | Personal Month | This month's energy |
| `personal-day-number.html` | Personal Day | Today's guidance |
| `pinnacle-numbers-reading.html` | Pinnacle Numbers | Life phases |
| `challenge-numbers-reading.html` | Challenge Numbers | Obstacles to overcome |

### ⭐ Astrology (21 tools)

| File | Title | Description |
|------|-------|-------------|
| `rising-sign-reading.html` | Rising Sign | Outer personality (Ascendant) |
| `moon-sign-reading.html` | Moon Sign | Emotional nature |
| `mercury-sign-reading.html` | Mercury Sign | How you think |
| `venus-sign-reading.html` | Venus Sign | Love language |
| `mars-sign-reading.html` | Mars Sign | Drive & passion |
| `jupiter-sign-reading.html` | Jupiter Sign | Path to luck |
| `saturn-sign-reading.html` | Saturn Sign | Karmic lessons |
| `uranus-sign-reading.html` | Uranus Sign | Unique genius |
| `neptune-sign-reading.html` | Neptune Sign | Dreams & intuition |
| `pluto-sign-reading.html` | Pluto Sign | Transformation power |
| `chiron-reading.html` | Chiron | Deepest wound & gift |
| `lilith-reading.html` | Lilith | Shadow power |
| `midheaven-reading.html` | Midheaven | Career calling |
| `descendant-reading.html` | Descendant | Who you attract |
| `part-of-fortune-reading.html` | Part of Fortune | Where luck finds you |
| `stellium-reading.html` | Stellium | Concentrated power |
| `modality-reading.html` | Modality | Cardinal/Fixed/Mutable |
| `moon-phase-calculator.html` | Moon Phase | Birth moon phase |
| `void-of-course-moon.html` | Void Moon | Timing actions |
| `mercury-retrograde-checker.html` | Mercury Retrograde | Communication chaos |
| `chinese-zodiac-reading.html` | Chinese Zodiac | Animal sign |

### 💕 Compatibility (7 tools)

| File | Title | Description |
|------|-------|-------------|
| `love-compatibility-reading.html` | Deep Love Compatibility | Complete love analysis |
| `venus-mars-compatibility.html` | Venus-Mars | Romantic chemistry |
| `soul-mate-analysis.html` | Soul Mate Connection | True soul mate signs |
| `relationship-life-path.html` | Relationship Life Path | Life paths in love |
| `synastry-reading.html` | Synastry | Planetary connections |
| `composite-chart-reading.html` | Composite Chart | Relationship's chart |
| `relationship-karma-reading.html` | Relationship Karma | Past life connections |

### 🎯 Life Purpose (6 tools)

| File | Title | Description |
|------|-------|-------------|
| `north-node-reading.html` | North Node | Soul's direction |
| `south-node-reading.html` | South Node | Past life gifts |
| `life-mission-reading.html` | Life Mission | Why you're here |
| `dharma-number-reading.html` | Dharma Number | Sacred duty |
| `vocation-reading.html` | Vocation | Ideal career |
| `soul-contract-reading.html` | Soul Contract | Soul agreements |

### 📅 Forecasts (5 tools)

| File | Title | Description |
|------|-------|-------------|
| `cosmic-daily-forecast.html` | Cosmic Daily | Complete daily guidance |
| `cosmic-weekly-forecast.html` | Cosmic Weekly | Week ahead |
| `cosmic-monthly-forecast.html` | Cosmic Monthly | Monthly cosmic guide |
| `cosmic-yearly-forecast.html` | Cosmic Yearly | Year-long forecast |
| `decade-forecast.html` | Decade Forecast | Long-term life cycles |

### 📊 Life Cycles (3 tools)

| File | Title | Description |
|------|-------|-------------|
| `age-calculator.html` | Cosmic Age | Cosmic timeline |
| `birthday-countdown.html` | Solar Return | Countdown to rebirth |
| `life-progress.html` | Life Journey | Progress through time |

---

## 9. Rebranding Implementation Steps

### Phase 1: Preparation

1. **Choose new brand name**
2. **Create new logo** (512x512 JPG/PNG for PWA icon, SVG for favicon)
3. **Set up new domain** and email addresses
4. **Create new social accounts** (Buy Me a Coffee, etc.)

### Phase 2: Core File Updates

```bash
# Priority Order:
1. manifest.json         # PWA identity
2. CNAME                 # Domain
3. sw.js                 # Service worker cache name
4. quantum-merlin-styles.css  # Rename file
5. share-utils.js        # Base URL, hashtags
6. tool-tracker.js       # localStorage keys, comments
7. profile-manager.js    # localStorage keys, comments
8. auto-fill.js          # localStorage keys, comments
9. cosmic-loader.js      # Comments
```

### Phase 3: HTML Updates (Create Script)

```python
# Recommended: Create apply_new_branding.py script to:
# 1. Replace "Quantum Merlin" with new brand name
# 2. Replace domain URLs
# 3. Replace email addresses
# 4. Replace Buy Me a Coffee link
# 5. Update copyright year if needed
```

### Phase 4: localStorage Migration (Optional)

```javascript
// Add to auto-fill.js or create migration script
// Migrate existing user data to new keys
function migrateLocalStorage() {
    const oldKeys = ['quantumMerlinProfiles', 'quantumMerlinActiveProfile', ...];
    const newKeys = ['newBrandProfiles', 'newBrandActiveProfile', ...];
    
    oldKeys.forEach((oldKey, i) => {
        const data = localStorage.getItem(oldKey);
        if (data) {
            localStorage.setItem(newKeys[i], data);
            // Optionally: localStorage.removeItem(oldKey);
        }
    });
}
```

### Phase 5: Assets

1. Replace `RetroMerlin.jpg` with new logo
2. Update `favicon.svg` if needed
3. Update any other brand imagery

### Phase 6: SEO & External

1. Update `sitemap.xml` with new domain
2. Update `robots.txt` if needed
3. Set up 301 redirects from old domain
4. Update any external listings

### Phase 7: Testing

1. Test PWA installation
2. Test all localStorage functionality
3. Test sharing on all platforms
4. Test all tools calculate correctly
5. Verify SEO meta tags

---

## Quick Reference: Search & Replace

| Find | Replace With |
|------|--------------|
| `Quantum Merlin` | `[NEW BRAND NAME]` |
| `quantummerlin` | `[newbrandname]` |
| `quantum-merlin` | `[new-brand-name]` |
| `quantumMerlin` | `[newBrandName]` |
| `QUANTUM MERLIN` | `[NEW BRAND NAME]` |
| `quantummerlin.com/classic` | `[new.domain.com]` |
| `RetroMerlin.jpg` | `[new-logo.jpg]` |
| `fixit@quantummerlin.com` | `[support@newdomain.com]` |
| `ads@quantummerlin.com` | `[ads@newdomain.com]` |
| `privacy@quantummerlin.com` | `[privacy@newdomain.com]` |
| `buymeacoffee.com/quantummerlin` | `[buymeacoffee.com/newbrand]` |

---

## File Count Summary

| Category | Count |
|----------|-------|
| HTML Tool Pages | 58 |
| Main/Legal Pages | 5 |
| JavaScript Files | 7 |
| CSS Files | 2 |
| PWA Files | 2 |
| Config Files | 5 |
| Python Scripts | ~20 |
| **Total Files to Review** | ~100 |

---

*This document was generated for rebranding purposes. Keep it updated as the codebase evolves.*
