#!/usr/bin/env python3
"""
Add tool-tracker.js to all tools that are missing it.
This enables auto-tracking of tool usage so the NEW badge disappears after use.
"""

import os
import re

# All tools that should have tool-tracker.js
TOOLS = [
    # Numerology
    'life-path-calculator.html',
    'destiny-number-calculator.html',
    'soul-urge-calculator.html',
    'personality-number-calculator.html',
    'name-number-calculator.html',
    'birthday-number-reading.html',
    'karmic-debt-reading.html',
    'master-number-reading.html',
    'maturity-number-reading.html',
    'personal-year-reading.html',
    'personal-month-reading.html',
    'personal-day-number.html',
    'expression-number-reading.html',
    'hidden-passion-number.html',
    'pinnacle-numbers-reading.html',
    'challenge-numbers-reading.html',
    
    # Compatibility
    'love-compatibility-reading.html',
    'venus-mars-compatibility.html',
    'soul-mate-analysis.html',
    'relationship-life-path.html',
    'synastry-reading.html',
    'composite-chart-reading.html',
    'relationship-karma-reading.html',
    
    # Life Purpose
    'north-node-reading.html',
    'south-node-reading.html',
    'life-mission-reading.html',
    'dharma-number-reading.html',
    'vocation-reading.html',
    'soul-contract-reading.html',
    
    # Astrology
    'rising-sign-reading.html',
    'moon-sign-reading.html',
    'mercury-sign-reading.html',
    'venus-sign-reading.html',
    'mars-sign-reading.html',
    'jupiter-sign-reading.html',
    'saturn-sign-reading.html',
    'uranus-sign-reading.html',
    'neptune-sign-reading.html',
    'pluto-sign-reading.html',
    'chiron-reading.html',
    'lilith-reading.html',
    'midheaven-reading.html',
    'descendant-reading.html',
    'part-of-fortune-reading.html',
    'stellium-reading.html',
    'modality-reading.html',
    'moon-phase-calculator.html',
    'void-of-course-moon.html',
    'mercury-retrograde-checker.html',
    'chinese-zodiac-reading.html',
    
    # Forecasts
    'cosmic-daily-forecast.html',
    'cosmic-weekly-forecast.html',
    'cosmic-monthly-forecast.html',
    'cosmic-yearly-forecast.html',
    'decade-forecast.html',
    
    # Life Cycles
    'age-calculator.html',
    'birthday-countdown.html',
    'life-progress.html',
]

def add_tool_tracker(filepath):
    """Add tool-tracker.js script tag if missing."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Error reading {filepath}: {e}")
        return False
    
    # Check if already has tool-tracker.js
    if 'tool-tracker.js' in content:
        return 'already'
    
    # Try to find cosmic-loader.js and add after it
    if '<script src="cosmic-loader.js"></script>' in content:
        content = content.replace(
            '<script src="cosmic-loader.js"></script>',
            '<script src="cosmic-loader.js"></script>\n    <script src="tool-tracker.js?v=20260121"></script>'
        )
    # Try auto-fill.js
    elif '<script src="auto-fill.js"></script>' in content:
        content = content.replace(
            '<script src="auto-fill.js"></script>',
            '<script src="auto-fill.js"></script>\n    <script src="tool-tracker.js?v=20260121"></script>'
        )
    # Try after </title>
    elif '</title>' in content:
        # Find first script tag or style tag after title
        title_end = content.find('</title>')
        rest = content[title_end:]
        
        # Find where to insert (before first <style> or <script>)
        script_match = re.search(r'(\n\s*)<script', rest)
        style_match = re.search(r'(\n\s*)<style', rest)
        
        if script_match:
            insert_pos = title_end + script_match.start()
            indent = script_match.group(1)
            content = content[:insert_pos] + f'{indent}<script src="tool-tracker.js?v=20260121"></script>' + content[insert_pos:]
        elif style_match:
            insert_pos = title_end + style_match.start()
            indent = style_match.group(1)
            content = content[:insert_pos] + f'{indent}<script src="tool-tracker.js?v=20260121"></script>' + content[insert_pos:]
        else:
            print(f"⚠️  Could not find insertion point in {filepath}")
            return False
    else:
        print(f"⚠️  No suitable insertion point in {filepath}")
        return False
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"❌ Error writing {filepath}: {e}")
        return False


def main():
    print("🔧 Adding tool-tracker.js to all tools...")
    print("=" * 50)
    
    added = 0
    skipped = 0
    failed = 0
    
    for tool in TOOLS:
        if not os.path.exists(tool):
            print(f"⚠️  File not found: {tool}")
            failed += 1
            continue
        
        result = add_tool_tracker(tool)
        if result == 'already':
            print(f"✓ Already has tool-tracker.js: {tool}")
            skipped += 1
        elif result:
            print(f"✅ Added tool-tracker.js to: {tool}")
            added += 1
        else:
            failed += 1
    
    print("=" * 50)
    print(f"\n🎉 Complete!")
    print(f"   ✅ Added: {added}")
    print(f"   ✓ Already had it: {skipped}")
    print(f"   ❌ Failed: {failed}")


if __name__ == '__main__':
    main()
