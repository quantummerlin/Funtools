"""
Add highlight color accents to reading content - Part 2
Adds <span class="highlight"> to key phrases in the actual reading text
"""

import os
import re

def add_content_highlights(html_content, filename):
    """Add highlight spans around key labeled sections in readings"""
    
    changes = 0
    
    # Pattern 1: Highlight the label in <p><strong>Label:</strong> content</p>
    # Match: <p><strong>Your Mission:</strong>
    # Replace with: <p><span class="highlight">Your Mission:</span>
    
    labels_to_highlight = [
        'Your Mission', 'Your Calling', 'Your Gifts', 'Your Path', 'Your Purpose',
        'Core Traits', 'Your Core Nature', 'Your Life Challenges', 
        'Your Relationship Path', 'Your Life Purpose', 'Finding Fulfillment',
        'Guidance for Your Journey', 'Wisdom for Your Journey',
        'Your Wound', 'Your Gift', 'The Healing', 'Shadow to Watch',
        'Soul Desire', 'Emotional Nature', 'What You Seek', 'Your Greatest Strength',
        'Communication Style', 'Career Path', 'Love and Attraction',
        'Soul Purpose', 'Life Lesson', 'Past Life Connection', 
        'Healing Path', 'Relationship Needs', 'Spiritual Gift'
    ]
    
    for label in labels_to_highlight:
        # Pattern: <p><strong>Label:</strong> text
        pattern = f'<p><strong>{re.escape(label)}:</strong>'
        replacement = f'<p><span class="highlight">{label}:</span>'
        
        before = html_content
        html_content = html_content.replace(pattern, replacement)
        if html_content != before:
            changes += 1
    
    # Pattern 2: Highlight the first occurrence of key power words in each paragraph
    # But only if they're at the start of a sentence
    
    power_words = [
        'transformation', 'purpose', 'destiny', 'mission', 'calling',
        'awakening', 'enlightenment', 'healing', 'mastery', 'wisdom',
        'leadership', 'visionary', 'pioneer', 'teacher', 'guide'
    ]
    
    for word in power_words:
        # Match word at start of sentence (after period or <p>)
        pattern = f'([\\.>]\\s+)({word})'
        replacement = f'\\1<span class="highlight">\\2</span>'
        
        before = html_content
        html_content = re.sub(pattern, replacement, html_content, count=1, flags=re.IGNORECASE)
        if html_content != before:
            changes += 1
    
    if changes > 0:
        print(f"  ✓ {filename} - added {changes} highlighted phrases")
    
    return html_content, changes


def process_file(filepath):
    """Process a single HTML file to add content highlights"""
    filename = os.path.basename(filepath)
    
    # Only process reading files
    if not any(kw in filename for kw in [
        'calculator', 'reading', '-sign-', 'forecast', 'compatibility', 
        'chart', 'numbers', 'oracle', 'crystal', 'fortune'
    ]):
        return False
    
    # Skip index and legal pages
    skip_files = ['index.html', 'tools_index.html', 'disclaimer.html', 
                  'privacy.html', 'terms.html', 'reading-loading.html', 'advertise.html']
    if filename in skip_files:
        return False
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Add content highlights
        content, changes = add_content_highlights(content, filename)
        
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
    print("✨ Adding color highlights to reading content...")
    print()
    
    files = [f for f in os.listdir('.') if f.endswith('.html')]
    files.sort()
    
    updated_count = 0
    
    for filename in files:
        if os.path.exists(filename):
            if process_file(filename):
                updated_count += 1
    
    print()
    print(f"✅ Done! Added highlights to {updated_count} files")
    print()
    print("Readings now have beautiful color accents on key phrases!")


if __name__ == '__main__':
    main()
