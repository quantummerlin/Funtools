"""
Check for JavaScript errors in all tool HTML files
"""

import os
import re

files_to_check = [
    'birthday-number-reading.html',
    'destiny-number-calculator.html',
    'karmic-debt-reading.html',
    'life-path-calculator.html',
    'master-number-reading.html',
    'maturity-number-reading.html',
    'name-number-calculator.html',
    'personal-month-reading.html',
    'personal-year-reading.html',
    'personality-number-calculator.html',
    'soul-urge-calculator.html',
    'moon-sign-reading.html',
    'rising-sign-reading.html'
]

print("🔍 Checking for JavaScript issues...\n")

for filename in files_to_check:
    if not os.path.exists(filename):
        continue
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    issues = []
    
    # Check for escaped quotes that break JS
    if re.search(r"getElementById\(\\'", content):
        issues.append("Escaped quotes in getElementById")
    
    # Check for unclosed braces by counting
    open_braces = content.count('{')
    close_braces = content.count('}')
    if open_braces != close_braces:
        issues.append(f"Mismatched braces: {open_braces} open, {close_braces} close")
    
    # Check for form with onsubmit OR addEventListener
    has_form_handler = 'onsubmit=' in content or "addEventListener('submit'" in content or 'addEventListener("submit"' in content
    if not has_form_handler:
        issues.append("No form submit handler found")
    
    # Check for missing closing script tag
    script_opens = content.count('<script>')
    script_closes = content.count('</script>')
    if script_opens != script_closes:
        issues.append(f"Mismatched script tags: {script_opens} open, {script_closes} close")
    
    # Check for double Version comments (cache buster issue)
    version_count = content.count('// Version:')
    if version_count > 1:
        issues.append(f"Multiple version comments ({version_count}) - may clutter code")
    
    if issues:
        print(f"⚠️  {filename}:")
        for issue in issues:
            print(f"    - {issue}")
    else:
        print(f"✅ {filename}: OK")

print("\n🔍 Done checking files")
