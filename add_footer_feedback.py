#!/usr/bin/env python3
"""
Add feedback email and Buy Me a Coffee button to all page footers.
"""

import os
import re
import glob

def update_footer(filepath):
    """Update the legal footer to include feedback and coffee sections."""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    filename = os.path.basename(filepath)
    
    # Skip if already has the new footer
    if 'fixit@quantummerlin.com' in content:
        print(f"  ✓  {filename} - already updated")
        return False
    
    # Skip if no legal footer
    if '<footer class="legal-footer">' not in content:
        print(f"  ⚠️  {filename} - no legal footer found")
        return False
    
    # Old footer pattern
    old_footer = '''    <!-- Legal Footer -->
    <footer class="legal-footer">
        <div class="legal-links">
            <a href="terms.html">Terms of Service</a>
            <span class="separator">|</span>
            <a href="privacy.html">Privacy Policy</a>
            <span class="separator">|</span>
            <a href="disclaimer.html">Disclaimer</a>
        </div>
        <p class="copyright">&copy; 2026 Quantum Merlin. For entertainment purposes only.</p>
    </footer>
    <style>
        .legal-footer {
            margin-top: 50px;
            padding: 30px 20px;
            text-align: center;
            border-top: 1px solid rgba(191, 90, 242, 0.2);
            background: rgba(10, 10, 15, 0.8);
        }
        .legal-links {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 15px;
            flex-wrap: wrap;
            margin-bottom: 15px;
        }
        .legal-links a {
            color: #9A8F7A;
            text-decoration: none;
            font-family: 'Cinzel', serif;
            font-size: 0.9rem;
            transition: color 0.3s;
        }
        .legal-links a:hover {
            color: #fbbf24;
        }
        .legal-links .separator {
            color: rgba(191, 90, 242, 0.4);
        }
        .copyright {
            color: #6B6B6B;
            font-size: 0.85rem;
            font-style: italic;
        }
    </style>'''
    
    # New footer with feedback and coffee
    new_footer = '''    <!-- Legal Footer -->
    <footer class="legal-footer">
        <div class="feedback-section">
            <p class="feedback-text">🛠️ Found an issue or have a suggestion?</p>
            <a href="mailto:fixit@quantummerlin.com?subject=Quantum%20Merlin%20Feedback" class="footer-feedback-btn">📧 fixit@quantummerlin.com</a>
        </div>
        <div class="legal-links">
            <a href="terms.html">Terms of Service</a>
            <span class="separator">|</span>
            <a href="privacy.html">Privacy Policy</a>
            <span class="separator">|</span>
            <a href="disclaimer.html">Disclaimer</a>
        </div>
        <p class="copyright">&copy; 2026 Quantum Merlin. For entertainment purposes only.</p>
        <div class="coffee-section">
            <a href="#" class="coffee-btn" id="coffeeBtn">☕ Buy Us a Coffee</a>
        </div>
    </footer>
    <style>
        .legal-footer {
            margin-top: 50px;
            padding: 30px 20px;
            text-align: center;
            border-top: 1px solid rgba(191, 90, 242, 0.2);
            background: rgba(10, 10, 15, 0.8);
        }
        .feedback-section {
            margin-bottom: 20px;
            padding-bottom: 20px;
            border-bottom: 1px solid rgba(191, 90, 242, 0.15);
        }
        .feedback-text {
            color: #9A8F7A;
            font-size: 0.9rem;
            margin-bottom: 10px;
        }
        .footer-feedback-btn {
            display: inline-block;
            color: #06b6d4;
            text-decoration: none;
            font-family: 'Cinzel', serif;
            font-size: 0.95rem;
            padding: 10px 20px;
            border: 1px solid rgba(6, 182, 212, 0.4);
            border-radius: 25px;
            transition: all 0.3s;
        }
        .footer-feedback-btn:hover {
            background: rgba(6, 182, 212, 0.15);
            border-color: #06b6d4;
            transform: translateY(-2px);
        }
        .legal-links {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 15px;
            flex-wrap: wrap;
            margin-bottom: 15px;
        }
        .legal-links a {
            color: #9A8F7A;
            text-decoration: none;
            font-family: 'Cinzel', serif;
            font-size: 0.9rem;
            transition: color 0.3s;
        }
        .legal-links a:hover {
            color: #fbbf24;
        }
        .legal-links .separator {
            color: rgba(191, 90, 242, 0.4);
        }
        .copyright {
            color: #6B6B6B;
            font-size: 0.85rem;
            font-style: italic;
            margin-bottom: 20px;
        }
        .coffee-section {
            padding-top: 15px;
            border-top: 1px solid rgba(191, 90, 242, 0.15);
        }
        .coffee-btn {
            display: inline-block;
            background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%);
            color: #0a0a0f;
            text-decoration: none;
            font-family: 'Cinzel', serif;
            font-weight: 600;
            font-size: 1rem;
            padding: 12px 25px;
            border-radius: 25px;
            transition: all 0.3s;
            box-shadow: 0 4px 15px rgba(251, 191, 36, 0.3);
        }
        .coffee-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 25px rgba(251, 191, 36, 0.5);
        }
    </style>'''
    
    if old_footer in content:
        content = content.replace(old_footer, new_footer)
    else:
        # Try with slight variations (different spacing)
        # Use regex to be more flexible
        pattern = r'<!-- Legal Footer -->.*?\.copyright\s*\{[^}]+\}\s*</style>'
        
        if re.search(pattern, content, re.DOTALL):
            content = re.sub(pattern, new_footer.replace('    <!-- Legal Footer -->', '<!-- Legal Footer -->').strip(), content, flags=re.DOTALL)
        else:
            print(f"  ⚠️  {filename} - couldn't match footer pattern")
            return False
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✅ {filename}")
        return True
    else:
        print(f"  ⚠️  {filename} - no changes made")
        return False

def main():
    print("📧 Adding Feedback & Coffee to All Footers")
    print("=" * 50)
    
    # Get all HTML files
    html_files = glob.glob('*.html')
    
    # Skip certain files
    skip = ['tools_index.html', 'reading-loading.html', 'index.html']
    
    updated = 0
    for filepath in sorted(html_files):
        if filepath in skip:
            continue
        if update_footer(filepath):
            updated += 1
    
    print("=" * 50)
    print(f"✨ Complete! Updated: {updated} files")

if __name__ == '__main__':
    main()
