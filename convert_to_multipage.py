#!/usr/bin/env python3
"""
Convert inline reading results to multi-page flow.
This script converts readings that show results inline (innerHTML) 
to use the reading-loading.html → reading-result.html flow.
"""

import os
import re

# Readings that currently use inline results and need to be converted
INLINE_READINGS = [
    'vocation-reading.html',
    'synastry-reading.html', 
    'south-node-reading.html',
    'soul-contract-reading.html',
    'relationship-karma-reading.html',
    'pinnacle-numbers-reading.html',
    'part-of-fortune-reading.html',
    'north-node-reading.html',
    'lilith-reading.html',
    'life-mission-reading.html',
    'expression-number-reading.html',
    'dharma-number-reading.html',
    'descendant-reading.html',
    'composite-chart-reading.html',
    'chiron-reading.html',
    'challenge-numbers-reading.html'
]

# Tool type mappings for readingData
TOOL_MAPPINGS = {
    'vocation-reading.html': {
        'toolType': 'vocation',
        'headerTitle': 'Your Vocation Reading',
        'headerSubtitle': 'Your true calling revealed'
    },
    'synastry-reading.html': {
        'toolType': 'synastry',
        'headerTitle': 'Synastry Reading',
        'headerSubtitle': 'Planetary connections between souls'
    },
    'south-node-reading.html': {
        'toolType': 'south-node',
        'headerTitle': 'South Node Reading',
        'headerSubtitle': 'Your past life gifts and karmic origins'
    },
    'soul-contract-reading.html': {
        'toolType': 'soul-contract',
        'headerTitle': 'Soul Contract Reading',
        'headerSubtitle': 'The sacred agreements of your soul'
    },
    'relationship-karma-reading.html': {
        'toolType': 'relationship-karma',
        'headerTitle': 'Relationship Karma Reading',
        'headerSubtitle': 'Past life connections revealed'
    },
    'pinnacle-numbers-reading.html': {
        'toolType': 'pinnacle',
        'headerTitle': 'Pinnacle Numbers Reading',
        'headerSubtitle': 'The four phases of your life journey'
    },
    'part-of-fortune-reading.html': {
        'toolType': 'part-of-fortune',
        'headerTitle': 'Part of Fortune Reading',
        'headerSubtitle': 'Your path to prosperity and joy'
    },
    'north-node-reading.html': {
        'toolType': 'north-node',
        'headerTitle': 'North Node Reading',
        'headerSubtitle': 'Your soul\'s evolutionary path'
    },
    'lilith-reading.html': {
        'toolType': 'lilith',
        'headerTitle': 'Lilith Reading',
        'headerSubtitle': 'Your shadow power and raw authenticity'
    },
    'life-mission-reading.html': {
        'toolType': 'life-mission',
        'headerTitle': 'Life Mission Reading',
        'headerSubtitle': 'Your divine purpose revealed'
    },
    'expression-number-reading.html': {
        'toolType': 'expression',
        'headerTitle': 'Expression Number Reading',
        'headerSubtitle': 'Your natural talents and abilities'
    },
    'dharma-number-reading.html': {
        'toolType': 'dharma',
        'headerTitle': 'Dharma Number Reading',
        'headerSubtitle': 'Your sacred path and purpose'
    },
    'descendant-reading.html': {
        'toolType': 'descendant',
        'headerTitle': 'Descendant Reading',
        'headerSubtitle': 'Your relationship destiny'
    },
    'composite-chart-reading.html': {
        'toolType': 'composite',
        'headerTitle': 'Composite Chart Reading',
        'headerSubtitle': 'The unique entity of your union'
    },
    'chiron-reading.html': {
        'toolType': 'chiron',
        'headerTitle': 'Chiron Reading',
        'headerSubtitle': 'Your deepest wound becomes your greatest gift'
    },
    'challenge-numbers-reading.html': {
        'toolType': 'challenge',
        'headerTitle': 'Challenge Numbers Reading',
        'headerSubtitle': 'Obstacles you\'re here to master'
    }
}

def convert_reading(filename):
    """Convert a single reading file to multi-page flow."""
    filepath = os.path.join(os.path.dirname(__file__), filename)
    
    if not os.path.exists(filepath):
        print(f"  ⚠️  {filename} - file not found")
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    mapping = TOOL_MAPPINGS.get(filename, {})
    
    # Find and replace the innerHTML assignment pattern
    # Pattern: document.getElementById('result').innerHTML = resultHTML;
    # Replace with the multi-page redirect flow
    
    # First, check if already converted
    if 'reading-loading.html' in content:
        print(f"  ✓  {filename} - already converted")
        return False
    
    # Find the showResult or generateReading function that sets innerHTML
    # Look for: document.getElementById('result').innerHTML = resultHTML;
    inline_pattern = r"document\.getElementById\('result'\)\.innerHTML\s*=\s*(\w+);"
    
    match = re.search(inline_pattern, content)
    if not match:
        print(f"  ⚠️  {filename} - pattern not found")
        return False
    
    result_var = match.group(1)  # e.g., 'resultHTML'
    
    # Build the replacement code
    tool_type = mapping.get('toolType', filename.replace('.html', '').replace('-reading', ''))
    header_title = mapping.get('headerTitle', 'Your Reading')
    header_subtitle = mapping.get('headerSubtitle', 'Cosmic insights revealed')
    source_url = filename
    
    replacement = f'''// Store reading for the multi-page results flow
            const readingData = {{
                toolType: '{tool_type}',
                headerTitle: '{header_title}',
                headerSubtitle: '{header_subtitle}',
                content: {result_var},
                sourceUrl: '{source_url}'
            }};
            // Try sessionStorage first, fallback to URL params for private browsing
            try {{
                sessionStorage.setItem('quantumMerlinReading', JSON.stringify(readingData));
                window.location.href = 'reading-loading.html';
            }} catch (e) {{
                // Private browsing mode - pass data via URL
                const encodedData = encodeURIComponent(JSON.stringify(readingData));
                window.location.href = 'reading-loading.html?data=' + encodedData;
            }}'''
    
    # Replace the innerHTML assignment
    content = re.sub(inline_pattern, replacement, content)
    
    # Also remove/hide the result div since we're redirecting
    # (We'll leave it for now in case it's needed for loading states)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✅ {filename} - converted to multi-page flow")
        return True
    else:
        print(f"  ⚠️  {filename} - no changes made")
        return False

def main():
    print("🔄 Converting Inline Readings to Multi-Page Flow")
    print("=" * 55)
    
    converted = 0
    for filename in INLINE_READINGS:
        if convert_reading(filename):
            converted += 1
    
    print("=" * 55)
    print(f"✨ Complete! Converted: {converted} files")
    
    if converted > 0:
        print("\n📝 Note: Commit and deploy to apply changes")

if __name__ == '__main__':
    main()
