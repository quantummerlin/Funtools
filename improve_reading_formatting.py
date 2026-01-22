"""
Improve reading formatting: sentences on new lines + color highlights
Makes readings easier to read with better visual breaks and accent colors
"""

import os
import re

# CSS for highlight class (gradient color accents)
HIGHLIGHT_CSS = """        .highlight {
            background: linear-gradient(120deg, rgba(251, 191, 36, 0.3) 0%, rgba(236, 72, 153, 0.3) 100%);
            border: 1px solid rgba(251, 191, 36, 0.5);
            padding: 2px 8px;
            border-radius: 4px;
            color: #fbbf24;
            font-weight: 600;
        }"""

def add_highlight_css(html_content, filename):
    """Add highlight CSS if not already present"""
    
    if '.highlight {' in html_content:
        return html_content, False
    
    # Find where to insert (before closing </style>)
    pattern = r'(</style>)'
    match = re.search(pattern, html_content)
    if not match:
        print(f"  ⚠ {filename} - no </style> tag found")
        return html_content, False
    
    insert_pos = match.start()
    new_content = (
        html_content[:insert_pos] +
        HIGHLIGHT_CSS + '\n' +
        html_content[insert_pos:]
    )
    
    return new_content, True


def format_reading_content(content):
    """
    Format reading content to:
    1. Put sentences on separate lines (new <p> tags)
    2. Add highlight spans to key phrases
    
    Preserves existing HTML structure
    """
    
    # Don't process if already has many <p> tags (already formatted)
    if content.count('<p>') > 10:
        return content
    
    # Don't process if it has complex HTML structure
    if '<div' in content or '<ul' in content or '<ol' in content:
        return content
    
    # Split by periods followed by space and capital letter (sentences)
    # But preserve existing <p> tags and <strong> tags
    
    # First, protect existing tags
    protected = []
    def protect_tag(match):
        protected.append(match.group(0))
        return f'<<<PROTECTED_{len(protected)-1}>>>'
    
    # Protect existing HTML tags
    content = re.sub(r'<[^>]+>', protect_tag, content)
    
    # Now split sentences
    sentences = re.split(r'\.\s+(?=[A-Z])', content)
    
    # Wrap each sentence in <p> tags
    formatted_sentences = []
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence:
            # Restore protected tags
            for i, tag in enumerate(protected):
                sentence = sentence.replace(f'<<<PROTECTED_{i}>>>', tag)
            
            # Don't wrap if already has <p> tag
            if not sentence.startswith('<p'):
                if not sentence.endswith('.') and not sentence.endswith('!') and not sentence.endswith('?'):
                    sentence += '.'
                formatted_sentences.append(f'<p>{sentence}</p>')
            else:
                formatted_sentences.append(sentence)
    
    return '\n                '.join(formatted_sentences)


def add_highlights_to_reading(html_content, filename):
    """Add highlight spans to key phrases in reading interpretations"""
    
    if '<span class="highlight">' in html_content:
        return html_content, 0
    
    changes = 0
    
    # Patterns to highlight (key phrases that appear in readings)
    highlight_patterns = [
        # Numerology terms
        (r'(<p><strong>)Your Mission:(</strong>)', r'\1Your Mission:\2<span class="highlight">'),
        (r'(<p><strong>)Your Calling:(</strong>)', r'\1Your Calling:\2<span class="highlight">'),
        (r'(<p><strong>)Your Gifts:(</strong>)', r'\1Your Gifts:\2<span class="highlight">'),
        (r'(<p><strong>)Your Path:(</strong>)', r'\1Your Path:\2<span class="highlight">'),
        (r'(<p><strong>)Your Purpose:(</strong>)', r'\1Your Purpose:\2<span class="highlight">'),
        (r'(<p><strong>)Core Traits:(</strong>)', r'\1Core Traits:\2<span class="highlight">'),
        (r'(<p><strong>)Your Core Nature:(</strong>)', r'\1Your Core Nature:\2<span class="highlight">'),
        (r'(<p><strong>)Your Life Challenges:(</strong>)', r'\1Your Life Challenges:\2<span class="highlight">'),
        (r'(<p><strong>)Your Relationship Path:(</strong>)', r'\1Your Relationship Path:\2<span class="highlight">'),
        (r'(<p><strong>)Your Life Purpose:(</strong>)', r'\1Your Life Purpose:\2<span class="highlight">'),
        (r'(<p><strong>)Finding Fulfillment:(</strong>)', r'\1Finding Fulfillment:\2<span class="highlight">'),
        (r'(<p><strong>)Guidance for Your Journey:(</strong>)', r'\1Guidance for Your Journey:\2<span class="highlight">'),
        (r'(<p><strong>)Wisdom for Your Journey:(</strong>)', r'\1Wisdom for Your Journey:\2<span class="highlight">'),
        
        # Astrology terms
        (r'(<p><strong>)Your Wound:(</strong>)', r'\1Your Wound:\2<span class="highlight">'),
        (r'(<p><strong>)Your Gift:(</strong>)', r'\1Your Gift:\2<span class="highlight">'),
        (r'(<p><strong>)The Healing:(</strong>)', r'\1The Healing:\2<span class="highlight">'),
        (r'(<p><strong>)Shadow to Watch:(</strong>)', r'\1Shadow to Watch:\2<span class="highlight">'),
        (r'(<p><strong>)Soul Desire:(</strong>)', r'\1Soul Desire:\2<span class="highlight">'),
        (r'(<p><strong>)Emotional Nature:(</strong>)', r'\1Emotional Nature:\2<span class="highlight">'),
        (r'(<p><strong>)What You Seek:(</strong>)', r'\1What You Seek:\2<span class="highlight">'),
    ]
    
    # Also wrap first phrase after opening <p> in some paragraphs
    # Find description paragraphs that start with the person's name
    def highlight_first_phrase(match):
        nonlocal changes
        changes += 1
        full_match = match.group(0)
        # Find first sentence or up to first comma/period
        first_phrase = re.match(r'[^.,!?]+', match.group(1))
        if first_phrase:
            phrase = first_phrase.group(0)
            rest = match.group(1)[len(phrase):]
            return f'<p><span class="highlight">{phrase}</span>{rest}</p>'
        return full_match
    
    # Look for paragraphs that start with someone's name and description
    name_pattern = r'<p>([A-Z][a-z]+, your [^<]+)</p>'
    html_content = re.sub(name_pattern, highlight_first_phrase, html_content)
    
    # Apply all highlight patterns
    for pattern, replacement in highlight_patterns:
        before = html_content
        html_content = re.sub(pattern, replacement, html_content)
        if html_content != before:
            changes += 1
            # Close the span after the content (before next <p> or <strong>)
            html_content = re.sub(
                r'(<span class="highlight">[^<]+)(</strong>)',
                r'\1\2</span>',
                html_content
            )
    
    if changes > 0:
        print(f"  ✓ {filename} - added {changes} color highlights")
    
    return html_content, changes


def improve_text_alignment(html_content, filename):
    """Change text-align: justify to center for reading content"""
    
    if 'text-align: justify' not in html_content:
        return html_content, False
    
    # Replace justify with center for result-content
    pattern = r'(\.result-content[^}]*text-align:\s*)justify'
    
    def replace_alignment(match):
        return match.group(1) + 'center'
    
    new_content = re.sub(pattern, replace_alignment, html_content)
    
    if new_content != html_content:
        print(f"  ✓ {filename} - changed alignment to center")
        return new_content, True
    
    return html_content, False


def process_file(filepath):
    """Process a single HTML file"""
    filename = os.path.basename(filepath)
    
    # Skip certain files
    skip_files = ['index.html', 'tools_index.html', 'disclaimer.html', 'privacy.html', 'terms.html',
                  'reading-loading.html', 'advertise.html']
    if filename in skip_files:
        return False
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Step 1: Add highlight CSS
        content, css_added = add_highlight_css(content, filename)
        
        # Step 2: Add highlight spans to key phrases
        content, highlights_added = add_highlights_to_reading(content, filename)
        
        # Step 3: Change text alignment to center
        content, alignment_changed = improve_text_alignment(content, filename)
        
        # Only write if changed
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            changes = []
            if css_added:
                changes.append('CSS')
            if highlights_added:
                changes.append(f'{highlights_added} highlights')
            if alignment_changed:
                changes.append('center-aligned')
            
            print(f"  ✓ {filename} - updated: {', '.join(changes)}")
            return True
        
        return False
        
    except Exception as e:
        print(f"  ✗ Error processing {filename}: {e}")
        return False


def main():
    print("🎨 Improving reading formatting: sentences on new lines + color highlights...")
    print()
    
    # Find all reading-related HTML files
    reading_keywords = [
        'calculator', 'reading', '-sign-', 'forecast',
        'compatibility', 'chart', 'numbers', 'oracle',
        'crystal', 'fortune'
    ]
    
    files_to_process = []
    for file in os.listdir('.'):
        if file.endswith('.html'):
            if any(keyword in file for keyword in reading_keywords):
                files_to_process.append(file)
    
    files_to_process.sort()
    
    updated_count = 0
    
    for filename in files_to_process:
        if os.path.exists(filename):
            if process_file(filename):
                updated_count += 1
    
    print()
    print(f"✅ Done! Updated {updated_count} files")
    print()
    print("What changed:")
    print("  • Text is now center-aligned (easier to read)")
    print("  • Key phrases have color highlights (better visual flow)")
    print("  • Added gradient accent colors throughout readings")
    print()
    print("The readings are now much easier to scan and absorb!")


if __name__ == '__main__':
    main()
