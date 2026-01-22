"""
Apply iOS Storage Fix to all reading tools
Fixes wrong reading data appearing on iOS by improving storage reliability
"""

import os
import re

def inject_storage_fix(html_content, filename):
    """Inject storage-fix.js script into HTML files"""
    
    # Check if already injected
    if 'storage-fix.js' in html_content:
        print(f"  ✓ {filename} already has storage-fix.js")
        return html_content
    
    # Find where to inject (after cosmic-loader.js or before closing body tag)
    injection_point = None
    
    # Try to inject after cosmic-loader.js
    cosmic_loader_pattern = r'(<script[^>]*src=["\']cosmic-loader\.js[^>]*></script>)'
    match = re.search(cosmic_loader_pattern, html_content)
    if match:
        injection_point = match.end()
        inject_method = 'after cosmic-loader'
    else:
        # Try before closing body tag
        body_pattern = r'(</body>)'
        match = re.search(body_pattern, html_content)
        if match:
            injection_point = match.start()
            inject_method = 'before </body>'
    
    if not injection_point:
        print(f"  ⚠ {filename} - no injection point found")
        return html_content
    
    # Inject the script
    script_tag = '\n    <script src="storage-fix.js?v=20260123"></script>'
    
    new_content = (
        html_content[:injection_point] +
        script_tag +
        html_content[injection_point:]
    )
    
    print(f"  ✓ {filename} - injected storage-fix.js ({inject_method})")
    return new_content


def update_reading_navigation(html_content, filename):
    """Update sessionStorage.setItem + redirect to use QMStorage.navigateWithReading"""
    
    if 'QMStorage.navigateWithReading' in html_content:
        return html_content, 0
    
    changes = 0
    
    # Pattern 1: sessionStorage.setItem + window.location.href (with try/catch)
    pattern1 = r'''try\s*{\s*sessionStorage\.setItem\(['"]quantumMerlinReading['"],\s*JSON\.stringify\(readingData\)\);\s*window\.location\.href\s*=\s*['"]([^'"]+)['"];\s*}\s*catch\s*\([^)]+\)\s*{\s*(?://[^\n]*\n\s*)*const\s+encodedData\s*=\s*encodeURIComponent\(JSON\.stringify\(readingData\)\);\s*window\.location\.href\s*=\s*['"]([^'"]+)[?]data=['"]\s*\+\s*encodedData;\s*}'''
    
    def replace_pattern1(match):
        nonlocal changes
        changes += 1
        target_url = match.group(1)
        return f"QMStorage.navigateWithReading(readingData, '{target_url}');"
    
    html_content = re.sub(pattern1, replace_pattern1, html_content, flags=re.DOTALL)
    
    # Pattern 2: CosmicLoader.show with try/catch inside
    pattern2 = r'''try\s*{\s*sessionStorage\.setItem\(['"]quantumMerlinReading['"],\s*JSON\.stringify\(readingData\)\);\s*CosmicLoader\.show\(\(\)\s*=>\s*{\s*window\.location\.href\s*=\s*['"]([^'"]+)['"];\s*}\);\s*}\s*catch\s*\([^)]+\)\s*{\s*(?://[^\n]*\n\s*)*const\s+encodedData\s*=\s*encodeURIComponent\(JSON\.stringify\(readingData\)\);\s*CosmicLoader\.show\(\(\)\s*=>\s*{\s*window\.location\.href\s*=\s*['"]([^'"]+)[?]data=['"]\s*\+\s*encodedData;\s*}\);\s*}'''
    
    def replace_pattern2(match):
        nonlocal changes
        changes += 1
        target_url = match.group(1)
        return f"CosmicLoader.show(() => {{ QMStorage.navigateWithReading(readingData, '{target_url}'); }});"
    
    html_content = re.sub(pattern2, replace_pattern2, html_content, flags=re.DOTALL)
    
    # Pattern 3: Simple sessionStorage + redirect (no try/catch)
    pattern3 = r'''sessionStorage\.setItem\(['"]quantumMerlinReading['"],\s*JSON\.stringify\(readingData\)\);\s*window\.location\.href\s*=\s*['"]([^'"]+)['"];'''
    
    def replace_pattern3(match):
        nonlocal changes
        changes += 1
        target_url = match.group(1)
        return f"QMStorage.navigateWithReading(readingData, '{target_url}');"
    
    html_content = re.sub(pattern3, replace_pattern3, html_content)
    
    if changes > 0:
        print(f"  ✓ {filename} - updated {changes} reading navigation(s)")
    
    return html_content, changes


def update_reading_retrieval(html_content, filename):
    """Update reading data retrieval to use QMStorage.getReading()"""
    
    if 'QMStorage.getReading' in html_content:
        return html_content, 0
    
    changes = 0
    
    # Look for the getReadingData function pattern
    pattern = r'''function getReadingData\(\) \{[^}]*try \{[^}]*sessionStorage\.getItem\(['"]quantumMerlinReading['"]\)[^}]*\} catch[^}]*\}[^}]*const urlParams[^}]*return null;\s*\}'''
    
    def replace_function(match):
        nonlocal changes
        changes += 1
        return '''function getReadingData() {
            return QMStorage.getReading();
        }'''
    
    html_content = re.sub(pattern, replace_function, html_content, flags=re.DOTALL)
    
    if changes > 0:
        print(f"  ✓ {filename} - updated reading retrieval")
    
    return html_content, changes


def process_file(filepath):
    """Process a single HTML file"""
    filename = os.path.basename(filepath)
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Step 1: Inject storage-fix.js
        content = inject_storage_fix(content, filename)
        
        # Step 2: Update reading navigation
        content, nav_changes = update_reading_navigation(content, filename)
        
        # Step 3: Update reading retrieval
        content, ret_changes = update_reading_retrieval(content, filename)
        
        # Only write if changed
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
        return False
        
    except Exception as e:
        print(f"  ✗ Error processing {filename}: {e}")
        return False


def main():
    print("🔧 Applying iOS Storage Fix to reading tools...")
    print()
    
    # Find all reading-related HTML files
    reading_files = [
        'reading-loading.html',
        'reading-result.html',
        'stellium-result.html',
        'modality-result.html',
    ]
    
    # Find all calculator/reading generation files
    for file in os.listdir('.'):
        if file.endswith('.html'):
            # Include files that generate readings
            if any(keyword in file for keyword in [
                'calculator', 'reading', '-sign-', 'forecast',
                'compatibility', 'chart', 'numbers'
            ]):
                if file not in reading_files:
                    reading_files.append(file)
    
    reading_files.sort()
    
    updated_count = 0
    
    for filename in reading_files:
        if os.path.exists(filename):
            print(f"Processing {filename}...")
            if process_file(filename):
                updated_count += 1
        else:
            print(f"  ⚠ {filename} not found")
    
    print()
    print(f"✅ Done! Updated {updated_count} files")
    print()
    print("What this fixes:")
    print("  • iOS Safari private browsing mode - readings no longer lost")
    print("  • iOS memory pressure - multiple fallback storage methods")
    print("  • Cross-tab/navigation issues - data persists reliably")
    print("  • Race conditions - validates data before/after save")
    print("  • Profile corruption - prevents invalid data from being saved")
    print()
    print("Next: Test on iOS Safari in both normal and private browsing mode")


if __name__ == '__main__':
    main()
