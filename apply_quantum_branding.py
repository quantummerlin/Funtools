#!/usr/bin/env python3
"""Apply Quantum Merlin branding to HTML files"""

import os
import re

WORK_DIR = r"C:\Users\WIPED\funtools"

# Files that still need updates (excluding already completed ones)
FILES_TO_UPDATE = [
    "age-calculator.html",
    "aura-color-test.html",
    "birthday-countdown.html",
    "brain-type-test.html",
    "coin-flip.html",
    "color-generator.html",
    "color-personality-test.html",
    "crystal-ball.html",
    "daily-fortune.html",
    "decision-wheel.html",
    "dice-roller.html",
    "fortune-cookie.html",
    "life-progress.html",
    "lucky-numbers.html",
    "password-generator.html",
    "random-fact.html",
    "random-name-picker.html",
    "time-until.html",
    "yes-no-oracle.html",
    # Also finish these partially completed files
    "chinese-zodiac-calculator.html",
    "moon-phase-calculator.html",
    "element-calculator.html",
    "birthstone-finder.html",
    "birth-flower-finder.html"
]

# Title suffix mapping (for meta tags)
TITLE_MAPPING = {
    "age-calculator.html": ("Age Calculator | Free Online Tool", "Age Calculator | Quantum Merlin"),
    "aura-color-test.html": ("Aura Color Test | Free Online Tool", "Aura Color Test | Quantum Merlin"),
    "birthday-countdown.html": ("Birthday Countdown | Free Online Tool", "Birthday Countdown | Quantum Merlin"),
    "brain-type-test.html": ("Brain Type Test | Free Online Tool", "Brain Type Test | Quantum Merlin"),
    "coin-flip.html": ("Coin Flip | Free Online Tool", "Coin Flip | Quantum Merlin"),
    "color-generator.html": ("Color Generator | Free Online Tool", "Color Generator | Quantum Merlin"),
    "color-personality-test.html": ("Color Personality Test | Free Online Tool", "Color Personality Test | Quantum Merlin"),
    "crystal-ball.html": ("Crystal Ball | Free Online Tool", "Crystal Ball | Quantum Merlin"),
    "daily-fortune.html": ("Daily Fortune | Free Online Tool", "Daily Fortune | Quantum Merlin"),
    "decision-wheel.html": ("Decision Wheel | Free Online Tool", "Decision Wheel | Quantum Merlin"),
    "dice-roller.html": ("Dice Roller | Free Online Tool", "Dice Roller | Quantum Merlin"),
    "fortune-cookie.html": ("Fortune Cookie | Free Online Tool", "Fortune Cookie | Quantum Merlin"),
    "life-progress.html": ("Life Progress | Free Online Tool", "Life Progress | Quantum Merlin"),
    "lucky-numbers.html": ("Lucky Numbers | Free Online Tool", "Lucky Numbers | Quantum Merlin"),
    "password-generator.html": ("Password Generator | Free Online Tool", "Password Generator | Quantum Merlin"),
    "random-fact.html": ("Random Fact | Free Online Tool", "Random Fact | Quantum Merlin"),
    "random-name-picker.html": ("Random Name Picker | Free Online Tool", "Random Name Picker | Quantum Merlin"),
    "time-until.html": ("Time Until | Free Online Tool", "Time Until | Quantum Merlin"),
    "yes-no-oracle.html": ("Yes/No Oracle | Free Online Tool", "Yes/No Oracle | Quantum Merlin"),
}

GOOGLE_FONTS_LINK = '''    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@400;700;900&family=Cinzel:wght@400;500;600;700;800;900&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400;1,500;1,600;1,700&display=swap" rel="stylesheet">'''

def add_fonts_if_missing(content):
    """Add Google Fonts link if not already present"""
    if "fonts.googleapis.com" not in content:
        # Find the closing </head> tag and insert before it
        content = content.replace('    <style>', f'{GOOGLE_FONTS_LINK}\n    <style>')
    return content

def update_title(content, filename):
    """Update page title"""
    if filename in TITLE_MAPPING:
        old_title, new_title = TITLE_MAPPING[filename]
        content = content.replace(f'<title>{old_title}</title>', f'<title>{new_title}</title>')
    return content

def update_back_button(content):
    """Update back button text"""
    content = content.replace('← Back to All Tools', '← Quantum Merlin Hub')
    return content

def apply_branding(filename):
    """Apply all branding updates to a file"""
    filepath = os.path.join(WORK_DIR, filename)
    
    if not os.path.exists(filepath):
        print(f"❌ File not found: {filename}")
        return False
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Apply updates
        content = add_fonts_if_missing(content)
        content = update_title(content, filename)
        content = update_back_button(content)
        
        # Write back
        with open(filepath, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        
        print(f"✅ Updated: {filename}")
        return True
    
    except Exception as e:
        print(f"❌ Error updating {filename}: {e}")
        return False

def main():
    """Main function"""
    print("Starting Quantum Merlin branding application...\n")
    
    success_count = 0
    fail_count = 0
    
    for filename in FILES_TO_UPDATE:
        if apply_branding(filename):
            success_count += 1
        else:
            fail_count += 1
    
    print(f"\n{'='*50}")
    print(f"Summary:")
    print(f"✅ Successfully updated: {success_count} files")
    print(f"❌ Failed: {fail_count} files")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()
