"""
Add localStorage auto-fill functionality to all HTML tools
"""

import os
import re

# localStorage JavaScript code to inject
LOCALSTORAGE_CODE = """
        // Load saved data from localStorage
        function loadSavedData() {
            const savedData = localStorage.getItem('quantumMerlinUserData');
            if (savedData) {
                const data = JSON.parse(savedData);
                
                // Map of possible field names to data keys
                const fieldMappings = {
                    'preferredName': 'preferredName',
                    'name': 'preferredName',
                    'yourName': 'preferredName',
                    'birthName': 'birthName',
                    'fullName': 'birthName',
                    'birthDate': 'birthDate',
                    'date': 'birthDate',
                    'dob': 'birthDate',
                    'birthdate': 'birthDate',
                    'birthTime': 'birthTime',
                    'time': 'birthTime',
                    'birthPlace': 'birthPlace',
                    'place': 'birthPlace',
                    'location': 'birthPlace'
                };
                
                Object.keys(fieldMappings).forEach(fieldId => {
                    const field = document.getElementById(fieldId);
                    const dataKey = fieldMappings[fieldId];
                    if (field && data[dataKey]) {
                        field.value = data[dataKey];
                    }
                });
            }
        }
        
        // Save user data to localStorage
        function saveUserData() {
            const userData = {};
            
            // Try to find and save various field types
            const fields = [
                {ids: ['preferredName', 'name', 'yourName'], key: 'preferredName'},
                {ids: ['birthName', 'fullName'], key: 'birthName'},
                {ids: ['birthDate', 'date', 'dob', 'birthdate'], key: 'birthDate'},
                {ids: ['birthTime', 'time'], key: 'birthTime'},
                {ids: ['birthPlace', 'place', 'location'], key: 'birthPlace'}
            ];
            
            fields.forEach(field => {
                for (let id of field.ids) {
                    const element = document.getElementById(id);
                    if (element && element.value) {
                        userData[field.key] = element.value;
                        break;
                    }
                }
            });
            
            if (Object.keys(userData).length > 0) {
                localStorage.setItem('quantumMerlinUserData', JSON.stringify(userData));
            }
        }
        
        // Clear saved data
        function clearSavedData() {
            if (confirm('This will clear your saved personal information. Are you sure?')) {
                localStorage.removeItem('quantumMerlinUserData');
                location.reload();
            }
        }
        
        // Load saved data when page loads
        window.addEventListener('DOMContentLoaded', function() {
            loadSavedData();
            
            // Auto-save on form submission
            const forms = document.querySelectorAll('form');
            forms.forEach(form => {
                form.addEventListener('submit', function() {
                    saveUserData();
                });
            });
            
            // Auto-save on button clicks (for tools without forms)
            const calcButtons = document.querySelectorAll('button[id*="calculate"], button[id*="btn"]');
            calcButtons.forEach(btn => {
                btn.addEventListener('click', function() {
                    setTimeout(saveUserData, 100);
                });
            });
        });
"""

CLEAR_BUTTON_HTML = """<div style="text-align: right; margin-bottom: 15px;">
                <button type="button" onclick="clearSavedData()" style="background: rgba(236, 72, 153, 0.1); border: 2px solid rgba(236, 72, 153, 0.3); color: #ec4899; padding: 8px 16px; font-size: 0.85em; border-radius: 8px; cursor: pointer; transition: all 0.3s; font-family: 'Cinzel', serif; font-weight: 600;">
                    🗑️ Clear My Data
                </button>
            </div>"""

def add_localstorage_to_file(filepath):
    """Add localStorage functionality to an HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if already has localStorage code
        if 'loadSavedData' in content or 'quantumMerlinUserData' in content:
            return False
        
        # Add clear button after opening tool-card div
        if '<div class="tool-card">' in content and '🗑️ Clear My Data' not in content:
            content = content.replace(
                '<div class="tool-card">',
                f'<div class="tool-card">\n            {CLEAR_BUTTON_HTML}'
            )
        
        # Find the last </script> tag and inject code before it
        script_pattern = r'(</script>\s*</body>)'
        if re.search(script_pattern, content):
            content = re.sub(
                script_pattern,
                f'{LOCALSTORAGE_CODE}\n    </script>\n</body>',
                content
            )
        else:
            # If no script tag, add before </body>
            content = content.replace(
                '</body>',
                f'    <script>\n{LOCALSTORAGE_CODE}\n    </script>\n</body>'
            )
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
        
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    """Process all HTML files"""
    print("🔄 Adding localStorage auto-fill to all tools...")
    print("=" * 50)
    
    updated = 0
    skipped = 0
    
    for filename in os.listdir('.'):
        if filename.endswith('.html') and filename != 'tools_index.html':
            if add_localstorage_to_file(filename):
                print(f"✅ Updated: {filename}")
                updated += 1
            else:
                print(f"⏭️  Skipped: {filename} (already has localStorage)")
                skipped += 1
    
    print("=" * 50)
    print(f"✨ Updated: {updated} files")
    print(f"⏭️  Skipped: {skipped} files")

if __name__ == "__main__":
    main()
