"""
Apply Cosmic Loader to all tools that show results inline
This script adds the cosmic-loader.js and updates result display code
"""

import re
import os

# Tools that show results inline (not using reading-loading.html redirect)
INLINE_TOOLS = [
    "challenge-numbers-reading.html",
    "chiron-reading.html",
    "composite-chart-reading.html",
    "descendant-reading.html",
    "dharma-number-reading.html",
    "expression-number-reading.html",
    "hidden-passion-number.html",
    "life-mission-reading.html",
    "lilith-reading.html",
    "love-compatibility-reading.html",
    "mercury-retrograde-checker.html",
    "north-node-reading.html",
    "part-of-fortune-reading.html",
    "personal-day-number.html",
    "pinnacle-numbers-reading.html",
    "relationship-karma-reading.html",
    "relationship-life-path.html",
    "soul-contract-reading.html",
    "soul-mate-analysis.html",
    "south-node-reading.html",
    "synastry-reading.html",
    "venus-mars-compatibility.html",
    "vocation-reading.html",
    "void-of-course-moon.html"
]

def apply_cosmic_loader(filepath):
    """Add cosmic loader to a tool file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    changes_made = []
    
    # 1. Add cosmic-loader.js script if not already present
    if 'cosmic-loader.js' not in content:
        # Find auto-fill.js or tool-tracker.js and add after it
        if '<script src="auto-fill.js">' in content:
            content = content.replace(
                '<script src="auto-fill.js"></script>',
                '<script src="auto-fill.js"></script>\n    <script src="cosmic-loader.js"></script>'
            )
            changes_made.append("Added cosmic-loader.js script")
        elif '<script src="tool-tracker.js' in content:
            # Find the tool-tracker line and add after
            pattern = r'(<script src="tool-tracker\.js[^"]*"></script>)'
            match = re.search(pattern, content)
            if match:
                content = content.replace(
                    match.group(1),
                    match.group(1) + '\n    <script src="cosmic-loader.js"></script>'
                )
                changes_made.append("Added cosmic-loader.js script after tool-tracker.js")
    
    # 2. Replace inline result display with CosmicLoader.showResult()
    # Common patterns:
    # Pattern A: document.getElementById('result').innerHTML = X; document.getElementById('result').style.display = 'block';
    # Pattern B: Sometimes with toolForm or form hidden too
    
    # Look for the pattern where result is displayed
    # We need to find where innerHTML is set and display is set to block
    
    # Pattern: set innerHTML then set display to block
    # We'll wrap the display:block in CosmicLoader
    
    # Find patterns like:
    # document.getElementById('result').innerHTML = resultHTML;
    # document.getElementById('result').style.display = 'block';
    # document.getElementById('toolForm').style.display = 'none';
    
    # Replace with:
    # document.getElementById('result').innerHTML = resultHTML;
    # CosmicLoader.showResult('result', 'toolForm');
    
    # Pattern 1: result + toolForm
    pattern1 = r"(document\.getElementById\(['\"]result['\"]\)\.innerHTML\s*=\s*[^;]+;)\s*\n\s*document\.getElementById\(['\"]result['\"]\)\.style\.display\s*=\s*['\"]block['\"];\s*\n\s*document\.getElementById\(['\"]toolForm['\"]\)\.style\.display\s*=\s*['\"]none['\"];"
    
    if re.search(pattern1, content):
        content = re.sub(pattern1, r"\1\n            CosmicLoader.showResult('result', 'toolForm');", content)
        changes_made.append("Updated result display with CosmicLoader (pattern 1: result + toolForm)")
    
    # Pattern 2: result + form (generic)
    pattern2 = r"(document\.getElementById\(['\"]result['\"]\)\.innerHTML\s*=\s*[^;]+;)\s*\n\s*document\.getElementById\(['\"]result['\"]\)\.style\.display\s*=\s*['\"]block['\"];\s*\n\s*document\.getElementById\(['\"]form['\"]\)\.style\.display\s*=\s*['\"]none['\"];"
    
    if re.search(pattern2, content):
        content = re.sub(pattern2, r"\1\n            CosmicLoader.showResult('result', 'form');", content)
        changes_made.append("Updated result display with CosmicLoader (pattern 2: result + form)")
    
    # Pattern 3: Just result display with toolForm hidden (different spacing)
    pattern3 = r"(document\.getElementById\(['\"]result['\"]\)\.innerHTML\s*=\s*[^;]+;)\s*document\.getElementById\(['\"]result['\"]\)\.style\.display\s*=\s*['\"]block['\"];\s*document\.getElementById\(['\"]toolForm['\"]\)\.style\.display\s*=\s*['\"]none['\"];"
    
    if re.search(pattern3, content):
        content = re.sub(pattern3, r"\1\n            CosmicLoader.showResult('result', 'toolForm');", content)
        changes_made.append("Updated result display with CosmicLoader (pattern 3: single line)")
    
    # Pattern 4: Just result.style.display = 'block' on its own line
    if 'CosmicLoader.showResult' not in content:
        # Check if we still have the pattern
        pattern4 = r"(document\.getElementById\(['\"]result['\"]\)\.innerHTML\s*=\s*[^;]+;)\s*\n(\s*)(document\.getElementById\(['\"]result['\"]\)\.style\.display\s*=\s*['\"]block['\"];)"
        
        match = re.search(pattern4, content)
        if match:
            # Check if next line has form hidden
            pos = match.end()
            next_lines = content[pos:pos+200]
            
            form_match = re.search(r"^\s*(document\.getElementById\(['\"](\w+)['\"]\)\.style\.display\s*=\s*['\"]none['\"];)", next_lines)
            
            if form_match:
                form_id = form_match.group(2)
                # Replace both lines
                full_pattern = pattern4 + r"\s*\n\s*document\.getElementById\(['\"]" + form_id + r"['\"]\)\.style\.display\s*=\s*['\"]none['\"];"
                replacement = r"\1\n\2CosmicLoader.showResult('result', '" + form_id + "');"
                content = re.sub(full_pattern, replacement, content)
                changes_made.append(f"Updated result display with CosmicLoader (pattern 4: with {form_id})")
            else:
                # Just replace result display
                content = re.sub(pattern4, r"\1\n\2CosmicLoader.showResult('result');", content)
                changes_made.append("Updated result display with CosmicLoader (pattern 4: result only)")
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, changes_made
    return False, ["No changes needed or pattern not found"]

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    print("Applying Cosmic Loader to inline tools...\n")
    
    updated = 0
    for filename in INLINE_TOOLS:
        filepath = os.path.join(base_dir, filename)
        if os.path.exists(filepath):
            success, changes = apply_cosmic_loader(filepath)
            if success:
                print(f"✓ {filename}")
                for change in changes:
                    print(f"    - {change}")
                updated += 1
            else:
                print(f"⚠ {filename} - {changes[0]}")
        else:
            print(f"✗ {filename} - File not found")
    
    print(f"\nUpdated {updated}/{len(INLINE_TOOLS)} files")

if __name__ == "__main__":
    main()
