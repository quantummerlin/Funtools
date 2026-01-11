"""
Quick Deploy Script - Run this before every git push to ensure cache busting
"""

import subprocess
import sys

print("🚀 QUANTUM MERLIN - QUICK DEPLOY")
print("=" * 50)

# Step 1: Apply cache busting
print("\n📦 Step 1: Applying cache busting...")
result = subprocess.run([sys.executable, "apply_cache_busting.py"], capture_output=True, text=True)
print(result.stdout)
if result.returncode != 0:
    print("❌ Error:", result.stderr)
    sys.exit(1)

# Step 2: Git add all
print("\n📝 Step 2: Staging changes...")
subprocess.run(["git", "add", "."], check=True)
print("✅ All files staged")

# Step 3: Git commit
print("\n💾 Step 3: Committing changes...")
commit_msg = input("Enter commit message (or press Enter for default): ").strip()
if not commit_msg:
    commit_msg = "🔄 Update with cache busting"

result = subprocess.run(["git", "commit", "-m", commit_msg], capture_output=True, text=True)
if "nothing to commit" in result.stdout:
    print("⚠️  No changes to commit")
else:
    print("✅ Changes committed")
    print(result.stdout)

# Step 4: Git push
print("\n🚀 Step 4: Pushing to GitHub...")
confirm = input("Push to GitHub? (y/n): ").strip().lower()
if confirm == 'y':
    subprocess.run(["git", "push"], check=True)
    print("✅ Pushed to GitHub!")
    print("\n🎉 Deployment complete!")
    print("Your changes will be live in ~2 minutes")
else:
    print("⏸️  Push cancelled. Run 'git push' manually when ready.")
