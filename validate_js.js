const fs = require('fs');
const path = require('path');

const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));

let hasErrors = false;

files.forEach(file => {
    const html = fs.readFileSync(file, 'utf8');
    const scriptMatches = html.matchAll(/<script(?:\s[^>]*)?>([\s\S]*?)<\/script>/g);
    let blockNum = 0;
    
    for (const match of scriptMatches) {
        blockNum++;
        // Skip external script tags (with src attribute)
        if (match[0].includes(' src=')) continue;
        
        const code = match[1];
        if (code.trim() === '') continue;
        
        try {
            new Function(code);
        } catch(e) {
            console.log(`${file} script block ${blockNum}: ERROR - ${e.message}`);
            hasErrors = true;
        }
    }
});

if (!hasErrors) {
    console.log('All files validated successfully!');
}
