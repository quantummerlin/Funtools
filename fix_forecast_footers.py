#!/usr/bin/env python3
"""
Fix remaining forecast pages that have different footer patterns.
"""

import os

# Files with simpler footer pattern  
FORECAST_FILES = [
    'cosmic-daily-forecast.html',
    'cosmic-weekly-forecast.html', 
    'cosmic-monthly-forecast.html',
    'cosmic-yearly-forecast.html',
    'daily-forecast.html',
    'weekly-forecast.html',
    'monthly-forecast.html',
    'yearly-forecast.html',
    'decade-forecast.html',
    'forecasts.html'
]

OLD_SIMPLE_FOOTER = '''    <footer class="legal-footer">
        <div class="legal-links">
            <a href="terms.html">Terms</a><span class="separator">|</span>
            <a href="privacy.html">Privacy</a><span class="separator">|</span>
            <a href="disclaimer.html">Disclaimer</a>
        </div>
        <p class="copyright">&copy; 2026 Quantum Merlin. For entertainment purposes only.</p>
    </footer>'''

NEW_FOOTER = '''    <footer class="legal-footer">
        <div class="feedback-section">
            <p class="feedback-text">🛠️ Found an issue or have a suggestion?</p>
            <a href="mailto:fixit@quantummerlin.com?subject=Quantum%20Merlin%20Feedback" class="footer-feedback-btn">📧 fixit@quantummerlin.com</a>
        </div>
        <div class="legal-links">
            <a href="terms.html">Terms</a><span class="separator">|</span>
            <a href="privacy.html">Privacy</a><span class="separator">|</span>
            <a href="disclaimer.html">Disclaimer</a>
        </div>
        <p class="copyright">&copy; 2026 Quantum Merlin. For entertainment purposes only.</p>
        <div class="coffee-section">
            <a href="#" class="coffee-btn" id="coffeeBtn">☕ Buy Us a Coffee</a>
        </div>
    </footer>'''

OLD_FOOTER_STYLE = '''.legal-footer { margin-top: 50px; padding: 30px 20px; text-align: center; border-top: 1px solid rgba(191, 90, 242, 0.2); }
        .legal-links { display: flex; justify-content: center; gap: 10px; flex-wrap: wrap; margin-bottom: 10px; }
        .legal-links a { color: #9A8F7A; text-decoration: none; font-size: 0.9rem; }
        .legal-links a:hover { color: #fbbf24; }
        .legal-links .separator { color: rgba(191, 90, 242, 0.3); }
        .copyright { color: #6B6B6B; font-size: 0.8rem; }'''

NEW_FOOTER_STYLE = '''.legal-footer { margin-top: 50px; padding: 30px 20px; text-align: center; border-top: 1px solid rgba(191, 90, 242, 0.2); }
        .feedback-section { margin-bottom: 20px; padding-bottom: 20px; border-bottom: 1px solid rgba(191, 90, 242, 0.15); }
        .feedback-text { color: #9A8F7A; font-size: 0.9rem; margin-bottom: 10px; }
        .footer-feedback-btn { display: inline-block; color: #06b6d4; text-decoration: none; font-family: 'Cinzel', serif; font-size: 0.95rem; padding: 10px 20px; border: 1px solid rgba(6, 182, 212, 0.4); border-radius: 25px; transition: all 0.3s; }
        .footer-feedback-btn:hover { background: rgba(6, 182, 212, 0.15); border-color: #06b6d4; }
        .legal-links { display: flex; justify-content: center; gap: 10px; flex-wrap: wrap; margin-bottom: 10px; }
        .legal-links a { color: #9A8F7A; text-decoration: none; font-size: 0.9rem; }
        .legal-links a:hover { color: #fbbf24; }
        .legal-links .separator { color: rgba(191, 90, 242, 0.3); }
        .copyright { color: #6B6B6B; font-size: 0.8rem; margin-bottom: 15px; }
        .coffee-section { padding-top: 15px; border-top: 1px solid rgba(191, 90, 242, 0.15); }
        .coffee-btn { display: inline-block; background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%); color: #0a0a0f; text-decoration: none; font-family: 'Cinzel', serif; font-weight: 600; font-size: 1rem; padding: 12px 25px; border-radius: 25px; transition: all 0.3s; box-shadow: 0 4px 15px rgba(251, 191, 36, 0.3); }
        .coffee-btn:hover { transform: translateY(-3px); box-shadow: 0 6px 25px rgba(251, 191, 36, 0.5); }'''

def update_file(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    
    if not os.path.exists(filepath):
        print(f"  ⚠️  {filename} - not found")
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Skip if already updated
    if 'fixit@quantummerlin.com' in content:
        print(f"  ✓  {filename} - already updated")
        return False
    
    original = content
    
    # Replace footer HTML
    content = content.replace(OLD_SIMPLE_FOOTER, NEW_FOOTER)
    
    # Replace footer styles
    content = content.replace(OLD_FOOTER_STYLE, NEW_FOOTER_STYLE)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✅ {filename}")
        return True
    else:
        print(f"  ⚠️  {filename} - pattern not matched")
        return False

def main():
    print("📧 Fixing Forecast Page Footers")
    print("=" * 45)
    
    updated = 0
    for filename in FORECAST_FILES:
        if update_file(filename):
            updated += 1
    
    print("=" * 45)
    print(f"✨ Complete! Updated: {updated} files")

if __name__ == '__main__':
    main()
