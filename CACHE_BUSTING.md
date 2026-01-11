# 🔄 Cache Busting System

This repository uses an automated cache busting system to ensure users always get the latest version of the tools.

## How It Works

### 1. **Meta Tags** (Immediate Effect)
Every HTML file includes cache control meta tags:
```html
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
<meta http-equiv="Pragma" content="no-cache">
<meta http-equiv="Expires" content="0">
<meta name="version" content="TIMESTAMP">
```

### 2. **Version Query Strings**
External resources include version parameters:
- `astronomy.browser.min.js?v=TIMESTAMP`
- `fonts.googleapis.com/css2?...&v=TIMESTAMP`

### 3. **Service Worker** (Progressive Enhancement)
- Registers at `/sw.js`
- Uses "network first" strategy for HTML files
- Auto-detects updates and prompts users to reload
- Checks for updates every 5 minutes
- Cleans up old caches automatically

### 4. **GitHub Actions** (Automation)
On every push to main branch:
- Automatically runs `apply_cache_busting.py`
- Updates all version timestamps
- Commits changes with `[skip ci]` to prevent loops

### 5. **HTTP Headers** (`_headers` file)
Cloudflare/GitHub Pages will respect:
- HTML files: `no-cache, must-revalidate`
- Static assets: `max-age=31536000` (1 year, since versioned)

## Manual Cache Busting

To manually update all cache versions:

```bash
python apply_cache_busting.py
git add .
git commit -m "🔄 Manual cache bust"
git push
```

## What Gets Updated

- ✅ All `.html` files
- ✅ Service worker (`sw.js`)
- ✅ External library references
- ✅ Google Fonts (optional)

## User Experience

When you push updates:

1. **Immediate**: HTML meta tags prevent browser caching
2. **~30 seconds**: GitHub Pages deployment completes
3. **~2 minutes**: Cloudflare CDN cache refreshes
4. **5 minutes**: Service worker checks for updates
5. **User sees prompt**: "New version available! Reload?"

## Benefits

- 🚀 **Instant Updates**: Users get changes within minutes
- 💾 **Smart Caching**: Static assets still cached for performance
- 🔄 **Auto-Refresh**: Service worker prompts users to reload
- 🤖 **Automated**: GitHub Actions handles everything
- 📊 **Version Tracking**: Every deployment has unique timestamp

## Files

- `apply_cache_busting.py` - Main cache busting script
- `sw.js` - Service worker for cache management
- `_headers` - HTTP cache control headers
- `.github/workflows/cache-bust.yml` - Auto-run on push

## Testing

To test cache busting locally:

```bash
# Run the script
python apply_cache_busting.py

# Start local server
python -m http.server 8000

# Open browser
# http://localhost:8000/tools_index.html

# Check console for service worker registration
# Try updating a file and reloading
```

## Troubleshooting

**Users not getting updates?**
1. Check version meta tag in page source
2. Hard refresh: `Ctrl+Shift+R` (Windows) or `Cmd+Shift+R` (Mac)
3. Clear browser cache completely
4. Check service worker in DevTools > Application > Service Workers

**Service worker not updating?**
1. Unregister old workers in DevTools
2. Check `/sw.js` is accessible
3. Ensure HTTPS (service workers require secure connection)

## Version Format

`YYYYMMDDHHMMSS` - e.g., `20260111121858`
- Easy to read and sort
- Unique per deployment
- Human-readable timestamp
