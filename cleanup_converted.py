#!/usr/bin/env python3
"""
Clean up unreachable code after redirect in converted reading files.
Removes CosmicLoader.showResult and tool-card hiding that won't execute.
"""

import os
import re

FILES = [
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

def cleanup_file(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    
    if not os.path.exists(filepath):
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Pattern to remove unreachable code after redirect
    # After: window.location.href = 'reading-loading.html?data=' + encodedData;\n            }
    # Remove: CosmicLoader.showResult(...);
    #         document.querySelector('.tool-card').style.display = 'none';
    #         if (window.ToolTracker...) { ... }
    
    # Remove CosmicLoader.showResult line
    content = re.sub(
        r"\n\s*CosmicLoader\.showResult\([^)]*\);",
        "",
        content
    )
    
    # Remove tool-card hiding
    content = re.sub(
        r"\n\s*document\.querySelector\(['\"]\.tool-card['\"]\)\.style\.display\s*=\s*['\"]none['\"];",
        "",
        content
    )
    
    # Remove ToolTracker.renderGoDeeper calls (that are now unreachable)
    # These are now handled by reading-result.html
    content = re.sub(
        r"\n\s*// Render Go Deeper suggestions\n\s*if \(window\.ToolTracker.*?ToolTracker\.renderGoDeeper.*?\n\s*\}",
        "",
        content,
        flags=re.DOTALL
    )
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✅ {filename} - cleaned up")
        return True
    else:
        print(f"  ✓  {filename} - already clean")
        return False

def main():
    print("🧹 Cleaning Up Unreachable Code")
    print("=" * 45)
    
    cleaned = 0
    for filename in FILES:
        if cleanup_file(filename):
            cleaned += 1
    
    print("=" * 45)
    print(f"✨ Complete! Cleaned: {cleaned} files")

if __name__ == '__main__':
    main()
