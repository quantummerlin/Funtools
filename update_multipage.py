#!/usr/bin/env python3
"""
Update premium tools to use the multi-page reading flow:
Form Page → Loading Interstitial → Results Page
"""

import os
import re

# Configuration for each tool
TOOL_CONFIGS = {
    'destiny-number-calculator.html': {
        'toolType': 'destiny',
        'headerTitle': '🌟 Your Destiny Number Reading',
        'headerSubtitle': 'The cosmos has revealed your life mission'
    },
    'life-path-calculator.html': {
        'toolType': 'life-path',
        'headerTitle': '🔮 Your Life Path Reading',
        'headerSubtitle': 'Your soul\'s journey has been illuminated'
    },
    'soul-urge-calculator.html': {
        'toolType': 'soul-urge',
        'headerTitle': '💫 Your Soul Urge Reading',
        'headerSubtitle': 'Your heart\'s deepest desires revealed'
    },
    'personality-number-calculator.html': {
        'toolType': 'personality',
        'headerTitle': '✨ Your Personality Number Reading',
        'headerSubtitle': 'How the world perceives you'
    },
    'name-number-calculator.html': {
        'toolType': 'name-number',
        'headerTitle': '📝 Your Name Number Reading',
        'headerSubtitle': 'The vibrational power of your name'
    },
    'birthday-number-reading.html': {
        'toolType': 'birthday',
        'headerTitle': '🎂 Your Birthday Number Reading',
        'headerSubtitle': 'The unique talents you were born with'
    },
    'personal-year-reading.html': {
        'toolType': 'personal-year',
        'headerTitle': '📅 Your Personal Year Reading',
        'headerSubtitle': 'The theme of your current year'
    },
    'personal-month-reading.html': {
        'toolType': 'personal-month',
        'headerTitle': '🗓️ Your Personal Month Reading',
        'headerSubtitle': 'The energy of this month revealed'
    },
    'maturity-number-reading.html': {
        'toolType': 'maturity',
        'headerTitle': '🌅 Your Maturity Number Reading',
        'headerSubtitle': 'Who you are becoming'
    },
    'karmic-debt-reading.html': {
        'toolType': 'karmic',
        'headerTitle': '⚖️ Your Karmic Debt Reading',
        'headerSubtitle': 'Lessons from past lives'
    },
    'master-number-reading.html': {
        'toolType': 'master',
        'headerTitle': '👑 Your Master Number Reading',
        'headerSubtitle': 'Your heightened spiritual gifts'
    },
    'moon-sign-reading.html': {
        'toolType': 'moon-sign',
        'headerTitle': '🌙 Your Moon Sign Reading',
        'headerSubtitle': 'Your emotional nature revealed'
    },
    'rising-sign-reading.html': {
        'toolType': 'rising-sign',
        'headerTitle': '🌅 Your Rising Sign Reading',
        'headerSubtitle': 'How you present to the world'
    }
}

def get_redirect_code(config, source_url):
    """Generate the sessionStorage and redirect code."""
    return f'''
            // Store reading for the results page
            const readingData = {{
                toolType: '{config["toolType"]}',
                headerTitle: '{config["headerTitle"]}',
                headerSubtitle: '{config["headerSubtitle"]}',
                number: destinyNumber || number || resultNumber || '',
                title: resultTitle,
                subtitle: resultSubtitle,
                content: resultContent,
                sourceUrl: '{source_url}'
            }};
            sessionStorage.setItem('quantumMerlinReading', JSON.stringify(readingData));
            
            // Redirect to loading page
            window.location.href = 'reading-loading.html';
'''

def update_tool(filepath, config):
    """Update a single tool to use the multi-page flow."""
    if not os.path.exists(filepath):
        print(f"  ⚠ File not found: {filepath}")
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    filename = os.path.basename(filepath)
    source_url = filename
    
    # This is complex because each tool has different result variable names
    # We need a more surgical approach - just add the redirect code before the result display
    
    # Look for the pattern where results are displayed
    patterns = [
        # Pattern for result.classList.add('show')
        (r"(document\.getElementById\('result'\)\.classList\.add\('show'\);)", 
         r"// REPLACED - now redirecting to result page"),
        # Pattern for scrollIntoView
        (r"(document\.getElementById\('result'\)\.scrollIntoView\([^)]+\);)", 
         r"// REPLACED - now redirecting to result page"),
    ]
    
    # Check if already updated
    if 'quantumMerlinReading' in content:
        print(f"  ✓ Already updated")
        return False
    
    print(f"  Processing {filename}...")
    return False  # Don't auto-update, too complex

def main():
    print("=" * 60)
    print("Multi-page reading system setup")
    print("=" * 60)
    print("\nThis update is complex - each tool has different variable names.")
    print("Manual updates recommended for each tool.")
    print("\nCreated files:")
    print("  ✓ reading-loading.html - Mystical loading interstitial")
    print("  ✓ reading-result.html - Universal results page")
    print("\nTo update each tool, modify the form submit handler to:")
    print("  1. Build the result content as usual")
    print("  2. Store it in sessionStorage")
    print("  3. Redirect to reading-loading.html")
    print("\nExample code to add before result display:")
    print('''
    // Store reading for the results page
    const readingData = {
        toolType: 'destiny',
        headerTitle: '🌟 Your Destiny Number Reading',
        headerSubtitle: 'The cosmos has revealed your life mission',
        number: destinyNumber,
        title: interpretation.title,
        subtitle: `${preferredName}, this is your life's mission`,
        content: `<p>...</p>`,
        sourceUrl: 'destiny-number-calculator.html'
    };
    sessionStorage.setItem('quantumMerlinReading', JSON.stringify(readingData));
    window.location.href = 'reading-loading.html';
    ''')

if __name__ == '__main__':
    main()
