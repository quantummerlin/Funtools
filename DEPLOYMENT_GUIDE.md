# 🚀 QUANTUM MERLIN - DEPLOYMENT GUIDE

## Quick Deploy (Recommended)

Just run this command before every push:

### Windows PowerShell:
```powershell
.\deploy.ps1
```

### Python (Any OS):
```bash
python deploy.py
```

This will automatically:
1. ✅ Apply cache busting to all files
2. ✅ Stage all changes
3. ✅ Prompt for commit message
4. ✅ Push to GitHub

---

## What the Cache Busting System Does

### 🎯 The Problem
When you update your tools, users might see old cached versions for hours or days.

### ✨ The Solution
Multi-layered cache busting ensures users get updates within **2-5 minutes**:

1. **Meta Tags** - Tells browsers "don't cache HTML"
2. **Version Query Strings** - External libraries get `?v=TIMESTAMP`
3. **Service Worker** - Automatically detects updates and prompts reload
4. **HTTP Headers** - Server-level cache control

---

## Deployment Timeline

| Time | What Happens |
|------|--------------|
| 0:00 | You run `deploy.ps1` or `git push` |
| 0:05 | Code reaches GitHub |
| 0:30 | GitHub Pages builds site |
| 1:00 | Cloudflare CDN starts updating |
| 2:00 | Most users can see changes |
| 5:00 | Service worker prompts all active users |

---

## Files in This System

### Core Scripts
- `apply_cache_busting.py` - Updates all version timestamps
- `deploy.ps1` - PowerShell deployment script
- `deploy.py` - Python deployment script

### Generated Files
- `sw.js` - Service worker for cache management
- `_headers` - HTTP cache control headers
- `CACHE_BUSTING.md` - Technical documentation

### What Gets Updated
Every time you deploy, these get new version numbers:
- ✅ All 42 HTML files
- ✅ External library links (astronomy-engine)
- ✅ Service worker version
- ✅ Meta tags in `<head>`

---

## Usage Instructions

### Option 1: Quick Deploy Script (Easiest)
```powershell
# Windows
.\deploy.ps1

# Or Python
python deploy.py
```

### Option 2: Manual Steps
```bash
# 1. Apply cache busting
python apply_cache_busting.py

# 2. Commit and push
git add .
git commit -m "Your update message"
git push
```

### Option 3: Just Push (Cache busting from previous run)
```bash
# If you already ran cache busting recently
git add .
git commit -m "Your update message"  
git push
```

---

## How Users Experience Updates

### First Visit
1. User loads page
2. Service worker installs
3. Page loads normally

### When You Push Update
1. User is browsing your site
2. Service worker detects new version (within 5 min)
3. User sees prompt: **"🔄 New version available! Reload to get the latest updates?"**
4. User clicks OK → instant refresh with new version
5. User clicks Cancel → can continue using old version

### Hard Refresh Always Works
Users can force-refresh anytime:
- **Windows**: `Ctrl + Shift + R` or `Ctrl + F5`
- **Mac**: `Cmd + Shift + R`

---

## Verification

### Check If Cache Busting Is Active
1. Open any tool page
2. View page source (`Ctrl+U`)
3. Look for these in `<head>`:
```html
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
<meta name="version" content="20260111121858">
```

### Check Service Worker
1. Open tools_index.html
2. Open DevTools (`F12`)
3. Go to Console
4. Look for: `✅ Service Worker registered`

### Check Version Number
The version format is: `YYYYMMDDHHMMSS`
- Example: `20260111121858`
- Means: January 11, 2026 at 12:18:58

---

## Troubleshooting

### "Users still seeing old version"
1. Check version in page source
2. Wait 2-5 minutes after push
3. Try hard refresh (`Ctrl+Shift+R`)
4. Clear browser cache completely

### "Service worker not working"
1. Requires HTTPS (works on GitHub Pages ✅)
2. Check browser console for errors
3. Unregister old workers in DevTools
4. Service workers don't work on `localhost` without special setup

### "Deploy script not running"
```powershell
# PowerShell execution policy may block scripts
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then try again
.\deploy.ps1
```

---

## Best Practices

### When to Deploy

✅ **Run cache busting before EVERY push**
- Even small HTML changes
- Even typo fixes
- Ensures users always get latest

❌ **Don't skip cache busting**
- Users might see old content
- Mixing old/new versions causes bugs

### Commit Messages

Good examples:
- `🔄 Update Moon Sign calculator readings`
- `🐛 Fix profile save issue`
- `✨ Add Venus Sign tool`
- `🎨 Improve mobile layout`

### Testing Before Deploy

1. Test locally first: `python -m http.server 8000`
2. Check console for errors
3. Test profile save/load
4. Test calculator functions
5. Then run `deploy.ps1`

---

## Privacy & Performance

### All Data Stays Local ✅
- Profile data: `localStorage` only
- Birth info: `localStorage` only
- No server storage
- No analytics (unless you add them)

### Performance Impact
- **HTML**: No caching = slightly slower initial load
- **Assets**: Full caching = fast subsequent loads
- **Service Worker**: Offline capability + instant updates
- **Net Effect**: Optimal balance of fresh content + speed

---

## Advanced: Manual Cache Bust Individual File

If you only changed one file:

```bash
# Edit the version in that file
# Find: <meta name="version" content="...">
# Change to new timestamp: 20260111HHMMSS

# Or just run the script - it's fast
python apply_cache_busting.py
```

---

## Questions?

### How do I know it's working?
Check the version number in page source after each deployment. It should match your latest deploy time.

### Can I disable it?
Not recommended, but you can skip running `apply_cache_busting.py`. Users will get updates eventually (hours to days).

### Does this cost anything?
No! All cache busting is free:
- GitHub Pages: Free
- Cloudflare: Free tier
- Service workers: Built into browsers
- No external services needed

---

## Summary

**Before every push, just run:**
```powershell
.\deploy.ps1
```

**That's it!** Your users will get updates within 2-5 minutes. ✨
