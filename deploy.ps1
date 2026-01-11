# Quantum Merlin Quick Deploy Script
# Run this before pushing to ensure cache busting is applied

Write-Host "🚀 QUANTUM MERLIN - QUICK DEPLOY" -ForegroundColor Cyan
Write-Host ("=" * 50) -ForegroundColor Cyan

# Step 1: Apply cache busting
Write-Host "`n📦 Step 1: Applying cache busting..." -ForegroundColor Yellow
python apply_cache_busting.py
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Error applying cache busting" -ForegroundColor Red
    exit 1
}

# Step 2: Git add all
Write-Host "`n📝 Step 2: Staging changes..." -ForegroundColor Yellow
git add .
Write-Host "✅ All files staged" -ForegroundColor Green

# Step 3: Git commit
Write-Host "`n💾 Step 3: Committing changes..." -ForegroundColor Yellow
$commitMsg = Read-Host "Enter commit message (or press Enter for default)"
if ([string]::IsNullOrWhiteSpace($commitMsg)) {
    $commitMsg = "🔄 Update with cache busting"
}

git commit -m $commitMsg
if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Changes committed" -ForegroundColor Green
} else {
    Write-Host "⚠️  No changes to commit or commit failed" -ForegroundColor Yellow
}

# Step 4: Git push
Write-Host "`n🚀 Step 4: Pushing to GitHub..." -ForegroundColor Yellow
$confirm = Read-Host "Push to GitHub? (y/n)"
if ($confirm -eq 'y') {
    git push
    if ($LASTEXITCODE -eq 0) {
        Write-Host "`n✅ Pushed to GitHub!" -ForegroundColor Green
        Write-Host "🎉 Deployment complete!" -ForegroundColor Cyan
        Write-Host "Your changes will be live in ~2 minutes" -ForegroundColor Cyan
    } else {
        Write-Host "❌ Push failed" -ForegroundColor Red
    }
} else {
    Write-Host "⏸️  Push cancelled. Run 'git push' manually when ready." -ForegroundColor Yellow
}
