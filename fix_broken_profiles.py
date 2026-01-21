"""
Fix broken profile sections in tools.
Remove the incomplete profile section HTML that has "Profile:" label with no dropdown
and a non-functional "Remove Profile" button.
"""

import os
import re

# Files with the broken profile section
files_to_fix = [
    'personal-month-reading.html',
    'rising-sign-reading.html', 
    'personality-number-calculator.html',
    'name-number-calculator.html',
    'destiny-number-calculator.html',
    'karmic-debt-reading.html',
    'master-number-reading.html',
    'birthday-number-reading.html',
    'maturity-number-reading.html'
]

# The broken profile section HTML pattern to remove
# This matches the incomplete profile section with empty dropdown area
broken_section_pattern = r'''            <!-- Profile Management Section -->
            <div class="profile-section" style="background: rgba\(139, 92, 246, 0\.08\); border: 1px solid rgba\(139, 92, 246, 0\.3\); border-radius: 12px; padding: 15px 20px; margin-bottom: 25px;">
                <div style="display: flex; flex-wrap: wrap; gap: 12px; align-items: center;">
                    <div style="display: flex; align-items: center; gap: 10px; flex: 1; min-width: 200px;">
                        <label style="color: #BF5AF2; font-family: 'Cinzel', serif; white-space: nowrap; font-size: 0\.95em;">👤 Profile:</label>
                        </div>
                    <button type="button" onclick="showDeleteProfileDialog\(\)" class="profile-btn" style="background: rgba\(236, 72, 153, 0\.1\); border: 1px solid rgba\(236, 72, 153, 0\.4\); color: #ec4899; padding: 10px 16px; border-radius: 8px; cursor: pointer; font-family: 'Cinzel', serif; font-size: 0\.85em; transition: all 0\.3s;">
                        🗑️ Remove Profile
                    </button>
                </div>
                <p style="color: #9A8F7A; font-size: 0\.8em; margin-top: 10px; margin-bottom: 0;">
                    ✨ Your info auto-saves as you type\. Create profiles for friends & family!
                </p>
            </div>
'''

# Also fix the duplicate/malformed input sections that sometimes appear
malformed_patterns = [
    # Fix duplicate "As it appears on your birth certificate" text
    (r'<div class="input-group">As it appears on your birth certificate</div>\s*</div>', '</div>'),
    # Remove showDeleteProfileDialog function if it's not needed
]

fixed_count = 0
for filename in files_to_fix:
    if not os.path.exists(filename):
        print(f"⚠️  File not found: {filename}")
        continue
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Remove the broken profile section
        # Use a more flexible pattern since exact formatting may vary
        content = re.sub(
            r'<!-- Profile Management Section -->\s*<div class="profile-section"[^>]*>.*?</div>\s*</div>\s*</div>\s*(?=<form)',
            '',
            content,
            flags=re.DOTALL
        )
        
        # Also try alternate pattern with different whitespace
        if content == original:
            content = re.sub(
                r'\s*<!-- Profile Management Section -->\s*<div class="profile-section" style="[^"]*">\s*<div[^>]*>\s*<div[^>]*>\s*<label[^>]*>👤 Profile:</label>\s*</div>\s*<button[^>]*onclick="showDeleteProfileDialog\(\)"[^>]*>\s*🗑️ Remove Profile\s*</button>\s*</div>\s*<p[^>]*>.*?</p>\s*</div>\s*',
                '\n',
                content,
                flags=re.DOTALL
            )
        
        # Fix malformed input sections
        content = re.sub(r'<div class="input-group">As it appears on your birth certificate</div>\s*</div>', '</div>', content)
        
        # Remove any orphaned showDeleteProfileDialog calls (if function doesn't exist)
        # Don't remove the function itself if it exists, just clean up orphaned buttons
        
        if content != original:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Fixed: {filename}")
            fixed_count += 1
        else:
            print(f"⏭️  No changes needed: {filename}")
            
    except Exception as e:
        print(f"❌ Error processing {filename}: {e}")

print(f"\n🎉 Fixed {fixed_count} files")
