#!/usr/bin/env python3
"""
Apply Open Graph and Twitter Card meta tags to all HTML tool pages.
This enables rich social media previews when links are shared.
"""

import os
import re
from pathlib import Path

# Page-specific metadata for better descriptions
PAGE_META = {
    # Cosmic Forecasts
    'cosmic-daily-forecast.html': {
        'title': 'Cosmic Daily Forecast | Quantum Merlin',
        'description': 'Your personalized daily cosmic guidance combining numerology, lunar phases, moon signs, and planetary positions.'
    },
    'cosmic-weekly-forecast.html': {
        'title': 'Cosmic Weekly Forecast | Quantum Merlin',
        'description': 'Your complete weekly cosmic preview with Chinese zodiac, lunar calendar, and numerology guidance.'
    },
    'cosmic-monthly-forecast.html': {
        'title': 'Cosmic Monthly Forecast | Quantum Merlin',
        'description': 'Your full monthly cosmic overview with lunar calendar, power days, and week-by-week energy guidance.'
    },
    'cosmic-yearly-forecast.html': {
        'title': 'Cosmic Yearly Forecast | Quantum Merlin',
        'description': 'Your complete yearly cosmic preview with Chinese zodiac compatibility, retrogrades, and monthly guidance.'
    },
    # Regular Forecasts
    'daily-forecast.html': {
        'title': 'Daily Numerology Forecast | Quantum Merlin',
        'description': 'Get your personalized daily numerology forecast based on your Personal Day Number.'
    },
    'weekly-forecast.html': {
        'title': 'Weekly Numerology Forecast | Quantum Merlin',
        'description': 'Discover your weekly energy patterns with personalized numerology insights.'
    },
    'monthly-forecast.html': {
        'title': 'Monthly Numerology Forecast | Quantum Merlin',
        'description': 'Your monthly numerology forecast revealing themes, opportunities, and guidance.'
    },
    'yearly-forecast.html': {
        'title': 'Yearly Numerology Forecast | Quantum Merlin',
        'description': 'Explore your Personal Year Number and discover what the year holds for you.'
    },
    'decade-forecast.html': {
        'title': 'Decade Forecast | Quantum Merlin',
        'description': 'See your 9-year numerology cycle and understand where you are in your life journey.'
    },
    # Numerology Calculators
    'life-path-calculator.html': {
        'title': 'Life Path Calculator | Quantum Merlin',
        'description': 'Calculate your Life Path Number and discover your core purpose and spiritual mission.'
    },
    'destiny-number-calculator.html': {
        'title': 'Destiny Number Calculator | Quantum Merlin',
        'description': 'Discover your Destiny Number and understand your life\'s true calling.'
    },
    'soul-urge-calculator.html': {
        'title': 'Soul Urge Calculator | Quantum Merlin',
        'description': 'Reveal your Soul Urge Number and uncover your deepest desires and motivations.'
    },
    'personality-number-calculator.html': {
        'title': 'Personality Number Calculator | Quantum Merlin',
        'description': 'Calculate your Personality Number to understand how others perceive you.'
    },
    'name-number-calculator.html': {
        'title': 'Name Number Calculator | Quantum Merlin',
        'description': 'Discover the numerological vibration of your name and its influence on your life.'
    },
    # Chinese Zodiac
    'chinese-zodiac-calculator.html': {
        'title': 'Chinese Zodiac Calculator | Quantum Merlin',
        'description': 'Find your Chinese zodiac animal sign based on your birth year.'
    },
    # Western Astrology
    'zodiac-calculator.html': {
        'title': 'Zodiac Sign Calculator | Quantum Merlin',
        'description': 'Discover your Western zodiac sun sign and its cosmic significance.'
    },
    'moon-phase-calculator.html': {
        'title': 'Moon Phase Calculator | Quantum Merlin',
        'description': 'Find the moon phase on any date and understand its spiritual significance.'
    },
    # Fun Tools
    'crystal-ball.html': {
        'title': 'Crystal Ball | Quantum Merlin',
        'description': 'Gaze into the mystical crystal ball and receive cosmic guidance.'
    },
    'fortune-cookie.html': {
        'title': 'Fortune Cookie | Quantum Merlin',
        'description': 'Crack open a virtual fortune cookie and discover your message from the universe.'
    },
    'daily-fortune.html': {
        'title': 'Daily Fortune | Quantum Merlin',
        'description': 'Receive your personalized daily fortune and cosmic message.'
    },
    'lucky-numbers.html': {
        'title': 'Lucky Numbers Generator | Quantum Merlin',
        'description': 'Generate your personalized lucky numbers for today.'
    },
    'yes-no-oracle.html': {
        'title': 'Yes/No Oracle | Quantum Merlin',
        'description': 'Ask the mystic oracle a yes or no question and receive cosmic guidance.'
    },
    # Personal Tools
    'age-calculator.html': {
        'title': 'Age Calculator | Quantum Merlin',
        'description': 'Calculate your exact age in years, months, days, and more.'
    },
    'birthday-countdown.html': {
        'title': 'Birthday Countdown | Quantum Merlin',
        'description': 'Count down the days until your next birthday celebration.'
    },
    'life-progress.html': {
        'title': 'Life Progress | Quantum Merlin',
        'description': 'Visualize your life progress and see how far you\'ve come on your journey.'
    },
    'birthstone-finder.html': {
        'title': 'Birthstone Finder | Quantum Merlin',
        'description': 'Discover your birthstone and its mystical properties.'
    },
    'birth-flower-finder.html': {
        'title': 'Birth Flower Finder | Quantum Merlin',
        'description': 'Find your birth month flower and understand its symbolism.'
    },
    # Personality Tests
    'aura-color-test.html': {
        'title': 'Aura Color Test | Quantum Merlin',
        'description': 'Discover your aura color and what it reveals about your energy.'
    },
    'brain-type-test.html': {
        'title': 'Brain Type Test | Quantum Merlin',
        'description': 'Discover whether you\'re left-brained or right-brained dominant.'
    },
    'color-personality-test.html': {
        'title': 'Color Personality Test | Quantum Merlin',
        'description': 'Find out what your color preferences reveal about your personality.'
    },
    'element-calculator.html': {
        'title': 'Element Calculator | Quantum Merlin',
        'description': 'Discover which classical element (Fire, Water, Air, Earth) governs your spirit.'
    },
}

# Default metadata for pages not specifically listed
DEFAULT_META = {
    'title': 'Quantum Merlin | Ancient Patterns. Modern Interfaces.',
    'description': 'Discover your cosmic destiny with numerology, astrology, and mystical calculators'
}

BASE_URL = 'https://funtools.quantummerlin.com/'
IMAGE_URL = 'https://funtools.quantummerlin.com/RetroMerlin.jpg'

def generate_og_tags(filename):
    """Generate Open Graph and Twitter Card meta tags for a file."""
    meta = PAGE_META.get(filename, DEFAULT_META)
    title = meta['title']
    description = meta['description']
    url = BASE_URL + filename
    
    tags = f'''
    <!-- Open Graph / Social Media -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="{url}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:image" content="{IMAGE_URL}">
    
    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:url" content="{url}">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{description}">
    <meta name="twitter:image" content="{IMAGE_URL}">
'''
    return tags.strip()

def has_og_tags(content):
    """Check if the file already has OG tags."""
    return 'og:title' in content or 'og:description' in content

def add_og_tags_to_file(filepath):
    """Add OG tags to an HTML file if they don't exist."""
    filename = os.path.basename(filepath)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if has_og_tags(content):
        print(f"  ⏭️  {filename} - already has OG tags")
        return False
    
    og_tags = generate_og_tags(filename)
    
    # Insert OG tags before </head>
    if '</head>' in content:
        new_content = content.replace('</head>', f'{og_tags}\n</head>')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"  ✅ {filename} - added OG tags")
        return True
    else:
        print(f"  ❌ {filename} - no </head> tag found")
        return False

def main():
    """Main function to process all HTML files."""
    script_dir = Path(__file__).parent
    
    # Get all HTML files
    html_files = list(script_dir.glob('*.html'))
    
    # Filter out files we want to skip
    skip_files = {'index.html', 'tools_index.html', 'advertise.html', 'disclaimer.html', 'forecasts.html'}
    
    print("\n🌐 Adding Open Graph & Twitter Card meta tags")
    print("=" * 50)
    
    updated = 0
    skipped = 0
    
    for filepath in sorted(html_files):
        filename = filepath.name
        
        if filename in skip_files:
            continue
            
        if add_og_tags_to_file(filepath):
            updated += 1
        else:
            skipped += 1
    
    print("=" * 50)
    print(f"✨ Complete! Updated: {updated}, Skipped: {skipped}")
    print("\nNow your pages will show rich previews when shared on social media!")

if __name__ == '__main__':
    main()
