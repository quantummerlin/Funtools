#!/usr/bin/env python3
"""
Full SEO Optimization Script for Quantum Merlin
- Adds JSON-LD structured data (WebApplication schema)
- Adds canonical URLs
- Adds keywords meta tag
- Ensures proper og:url and twitter:url
"""

import os
import re
import glob

BASE_URL = "https://quantummerlin.com/classic"

# SEO data for each page
SEO_DATA = {
    'life-path-calculator.html': {
        'title': 'Life Path Number Calculator | Free Numerology Reading',
        'description': 'Calculate your Life Path Number for free. Discover your true purpose, personality traits, and destiny with our accurate numerology calculator.',
        'keywords': 'life path number, numerology calculator, life path calculator, numerology reading, destiny number, free numerology'
    },
    'destiny-number-calculator.html': {
        'title': 'Destiny Number Calculator | Free Numerology',
        'description': 'Calculate your Destiny Number and uncover your life mission. Free numerology calculator reveals your soul purpose and spiritual path.',
        'keywords': 'destiny number, expression number, numerology calculator, life mission, soul purpose, free numerology'
    },
    'soul-urge-calculator.html': {
        'title': 'Soul Urge Number Calculator | Heart\'s Desire Number',
        'description': 'Discover your Soul Urge Number and deepest desires. Free calculator reveals your heart\'s true motivations and inner drives.',
        'keywords': 'soul urge number, heart desire number, numerology calculator, inner motivation, spiritual desires'
    },
    'zodiac-calculator.html': {
        'title': 'Zodiac Sign Calculator | What\'s My Sun Sign?',
        'description': 'Find your zodiac sign instantly with our free calculator. Discover your sun sign, element, modality, and personality traits.',
        'keywords': 'zodiac sign calculator, sun sign, astrology calculator, horoscope sign, star sign, zodiac personality'
    },
    'moon-sign-reading.html': {
        'title': 'Moon Sign Calculator & Reading | Emotional Astrology',
        'description': 'Calculate your Moon sign and get a detailed reading. Discover your emotional nature, instincts, and inner self with our free astrology tool.',
        'keywords': 'moon sign calculator, lunar sign, emotional astrology, moon reading, astrology calculator'
    },
    'rising-sign-reading.html': {
        'title': 'Rising Sign Calculator | Ascendant Sign Reading',
        'description': 'Find your Rising Sign (Ascendant) and discover how others see you. Free astrology calculator with detailed personality reading.',
        'keywords': 'rising sign calculator, ascendant sign, first impression astrology, rising sign reading'
    },
    'love-compatibility-reading.html': {
        'title': 'Love Compatibility Calculator | Numerology & Astrology',
        'description': 'Check your love compatibility with our detailed numerology analysis. Discover relationship dynamics, chemistry, and long-term potential.',
        'keywords': 'love compatibility, relationship compatibility, numerology compatibility, astrology love match'
    },
    'cosmic-daily-forecast.html': {
        'title': 'Daily Cosmic Forecast | Personalized Horoscope',
        'description': 'Get your personalized daily cosmic forecast. Combines numerology, moon phases, and planetary alignments for accurate daily guidance.',
        'keywords': 'daily horoscope, cosmic forecast, daily numerology, moon phase today, personalized horoscope'
    },
    'cosmic-weekly-forecast.html': {
        'title': 'Weekly Cosmic Forecast | 7-Day Horoscope',
        'description': 'Your personalized weekly cosmic forecast. Discover what the stars, numbers, and moon phases have in store for your week ahead.',
        'keywords': 'weekly horoscope, weekly forecast, cosmic weekly, numerology weekly, astrology forecast'
    },
    'cosmic-monthly-forecast.html': {
        'title': 'Monthly Cosmic Forecast | Personal Month Reading',
        'description': 'Get your complete monthly cosmic forecast. Numerology, lunar calendar, and astrological insights for the month ahead.',
        'keywords': 'monthly horoscope, monthly forecast, personal month, numerology monthly, lunar calendar'
    },
    'cosmic-yearly-forecast.html': {
        'title': 'Yearly Cosmic Forecast | Annual Numerology Reading',
        'description': 'Your complete yearly cosmic forecast. Personal year number, annual themes, and cosmic guidance for the entire year.',
        'keywords': 'yearly horoscope, annual forecast, personal year reading, numerology yearly, year ahead'
    },
    'chinese-zodiac-calculator.html': {
        'title': 'Chinese Zodiac Calculator | Year of Birth Animal',
        'description': 'Find your Chinese zodiac animal sign. Discover your lunar year animal, personality traits, and compatibility.',
        'keywords': 'chinese zodiac, chinese astrology, zodiac animal, lunar new year, chinese horoscope'
    },
    'moon-phase-calculator.html': {
        'title': 'Moon Phase Calculator | Today\'s Lunar Phase',
        'description': 'Calculate the current moon phase and lunar cycle. See moon illumination, phase name, and astrological significance.',
        'keywords': 'moon phase, lunar phase, moon today, full moon, new moon, moon calculator'
    },
    'mercury-retrograde-checker.html': {
        'title': 'Mercury Retrograde Checker | Is Mercury Retrograde?',
        'description': 'Check if Mercury is in retrograde right now. See current and upcoming Mercury retrograde periods and survival tips.',
        'keywords': 'mercury retrograde, is mercury retrograde, retrograde dates, mercury retrograde 2026'
    },
    'personal-year-reading.html': {
        'title': 'Personal Year Number Calculator | Numerology Forecast',
        'description': 'Calculate your Personal Year Number for accurate yearly guidance. Discover themes, opportunities, and challenges for this year.',
        'keywords': 'personal year number, numerology forecast, yearly numerology, life cycle, personal year reading'
    },
    'life-mission-reading.html': {
        'title': 'Life Mission Reading | Discover Your Purpose',
        'description': 'Uncover your true life mission through numerology and astrology. Comprehensive reading reveals your divine purpose.',
        'keywords': 'life mission, life purpose, soul purpose, dharma, destiny reading, spiritual path'
    },
    'north-node-reading.html': {
        'title': 'North Node Reading | Soul\'s Evolutionary Path',
        'description': 'Discover your North Node and understand your soul\'s evolutionary direction. Free astrology reading reveals your karmic path.',
        'keywords': 'north node, karmic astrology, soul evolution, lunar nodes, life direction'
    },
    'chiron-reading.html': {
        'title': 'Chiron Reading | The Wounded Healer',
        'description': 'Explore your Chiron placement and discover your deepest wound and greatest healing gift. Free astrology reading.',
        'keywords': 'chiron astrology, wounded healer, chiron sign, healing journey, astrology reading'
    },
    'tools_index.html': {
        'title': 'Quantum Merlin | Free Numerology & Astrology Tools',
        'description': 'Explore 60+ free numerology and astrology tools. Life path calculator, zodiac readings, cosmic forecasts, and personalized insights - no signup required.',
        'keywords': 'numerology tools, astrology calculator, free horoscope, life path number, zodiac sign, cosmic forecast, spiritual tools'
    }
}

# Default SEO for pages not in the dictionary
DEFAULT_KEYWORDS = 'numerology, astrology, horoscope, zodiac, spiritual tools, cosmic insights, free calculator'

def get_page_title(content):
    """Extract title from page."""
    match = re.search(r'<title>([^<]+)</title>', content)
    return match.group(1) if match else 'Quantum Merlin'

def add_seo_enhancements(filepath):
    """Add comprehensive SEO enhancements to a page."""
    filename = os.path.basename(filepath)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    changes = []
    
    # Skip if already has JSON-LD
    if 'application/ld+json' in content:
        return False, "already has JSON-LD"
    
    # Get SEO data for this page
    seo = SEO_DATA.get(filename, {})
    page_url = f"{BASE_URL}/{filename}"
    page_title = seo.get('title', get_page_title(content))
    page_desc = seo.get('description', '')
    page_keywords = seo.get('keywords', DEFAULT_KEYWORDS)
    
    # If no specific description, try to extract from existing meta
    if not page_desc:
        desc_match = re.search(r'<meta name="description" content="([^"]+)"', content)
        if desc_match:
            page_desc = desc_match.group(1)
        else:
            page_desc = "Free numerology and astrology tools from Quantum Merlin. Discover your cosmic path."
    
    # 1. Add canonical URL if not present
    if 'rel="canonical"' not in content:
        canonical = f'    <link rel="canonical" href="{page_url}">\n'
        content = re.sub(r'(<link rel="icon"[^>]+>)', canonical + r'\1', content, count=1)
        changes.append('canonical')
    
    # 2. Add keywords meta if not present
    if 'name="keywords"' not in content:
        keywords_tag = f'    <meta name="keywords" content="{page_keywords}">\n'
        # Insert after description
        if 'name="description"' in content:
            content = re.sub(
                r'(<meta name="description"[^>]+>)',
                r'\1\n' + keywords_tag.strip(),
                content,
                count=1
            )
            changes.append('keywords')
    
    # 3. Add JSON-LD structured data
    json_ld = f'''
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": "{page_title.split('|')[0].strip()}",
        "url": "{page_url}",
        "description": "{page_desc}",
        "applicationCategory": "LifestyleApplication",
        "operatingSystem": "Web Browser",
        "offers": {{
            "@type": "Offer",
            "price": "0",
            "priceCurrency": "USD"
        }},
        "provider": {{
            "@type": "Organization",
            "name": "Quantum Merlin",
            "url": "{BASE_URL}"
        }}
    }}
    </script>
'''
    
    # Insert JSON-LD before </head>
    content = content.replace('</head>', json_ld + '</head>')
    changes.append('JSON-LD')
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, ', '.join(changes)
    
    return False, "no changes"

def main():
    print("🔍 Full SEO Optimization")
    print("=" * 55)
    
    # Get all HTML files
    html_files = glob.glob('*.html')
    
    # Skip certain files
    skip = ['reading-loading.html', 'reading-result.html', 'test-astronomy.html', 
            'test-may3.html', 'test-moon-calc.html', 'debug-life-path.html',
            'stellium-result.html', 'modality-result.html']
    
    updated = 0
    for filepath in sorted(html_files):
        filename = os.path.basename(filepath)
        if filename in skip:
            continue
        
        success, message = add_seo_enhancements(filepath)
        if success:
            print(f"  ✅ {filename} - {message}")
            updated += 1
        else:
            print(f"  ✓  {filename} - {message}")
    
    print("=" * 55)
    print(f"✨ Complete! Updated: {updated} files")
    print("\n📝 Also created:")
    print("  • robots.txt")
    print("  • sitemap.xml")

if __name__ == '__main__':
    main()
