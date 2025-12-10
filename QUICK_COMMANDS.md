# Quick Command Reference

## 🚀 Deploy to Render (First Time)

```bash
# 1. Create GitHub repo and push
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/MRI-Brain-Tumor-Detection.git
git push -u origin main

# 2. Go to Render Dashboard
# Visit: https://dashboard.render.com
# Click: New + → Web Service
# Connect your GitHub repo
# Click: Create Web Service

# 3. Done! App deploys automatically
```

## 🔄 Update Your Deployed App

```bash
# Make changes, then:
git add .
git commit -m "Your update message"
git push

# Render auto-deploys! ✨
```

## 🧪 Test Your Deployment

```bash
# Test health endpoint
curl https://your-app.onrender.com/health

# Test API endpoint
curl https://your-app.onrender.com/get-random-image

# Or just visit in browser:
# https://your-app.onrender.com
```

## 🏠 Run Locally

```bash
# First time setup
pip install -r requirements.txt

# Run the app
python app.py

# Access at: http://localhost:5000
```

## 📂 Check Your Files

```bash
# List all important files
ls -la

# Check models folder
ls -la models/

# Check images folder
ls -la mri-images/

# Check if git is initialized
git status
```

## 🔧 Render Dashboard Commands

### Via Dashboard:
- **View Logs**: Dashboard → Logs tab
- **Restart App**: Dashboard → Manual Deploy → Deploy latest
- **Shell Access**: Dashboard → Shell tab
- **View Metrics**: Dashboard → Metrics tab

### In Render Shell:
```bash
# Check Python version
python --version

# List files
ls -la

# Check installed packages
pip list

# View environment variables
env | grep PYTHON
```

## 🆘 Troubleshooting Commands

```bash
# Check if all files are committed
git status

# See what's in your repo
git ls-files

# View recent commits
git log --oneline -5

# Check requirements
cat requirements.txt

# Verify render config
cat render.yaml
```

## 🔐 GitHub Commands

```bash
# Clone your repo (on another machine)
git clone https://github.com/YOUR_USERNAME/MRI-Brain-Tumor-Detection.git

# Pull latest changes
git pull origin main

# Check remote URL
git remote -v

# Change remote URL if needed
git remote set-url origin NEW_URL
```

## 📊 Monitor Your App

```bash
# Keep app awake - use UptimeRobot (free):
# 1. Go to https://uptimerobot.com
# 2. Add Monitor:
#    - URL: https://your-app.onrender.com/health
#    - Interval: 5 minutes

# Or use curl in a cron job:
curl https://your-app.onrender.com/health
```

## 🐛 Debug Commands

```bash
# Test model loading locally
python -c "import tensorflow as tf; print('TensorFlow:', tf.__version__)"

# Test Flask locally
python -c "import flask; print('Flask:', flask.__version__)"

# Test all imports
python -c "import flask, tensorflow, numpy, PIL; print('All imports OK!')"

# Check file sizes (for Git)
du -sh models/*
du -sh mri-images/*/
```

## 📦 Dependency Management

```bash
# Update all packages
pip install --upgrade -r requirements.txt

# Check outdated packages
pip list --outdated

# Freeze current environment
pip freeze > requirements.txt

# Install specific version
pip install flask==3.0.0
```

## 🌐 Custom Domain (Render)

```bash
# In Render Dashboard:
# 1. Settings → Custom Domain
# 2. Add your domain
# 3. Update DNS records:

# CNAME record:
# Name: @ or www
# Value: your-app.onrender.com
```

## 🔄 Switch Between Environments

```bash
# For Render (automatic via render.yaml)
git push origin main

# For cPanel (manual)
# Upload files via FTP/File Manager
# Then in SSH:
cd public_html/mri
source virtualenv/bin/activate
pip install -r requirements.txt
# Restart in cPanel interface

# For local development
python app.py
```

## 📁 File Management

```bash
# Check what's ignored
cat .gitignore

# Force add a file if needed
git add -f filename

# Remove file from git but keep locally
git rm --cached filename

# See file sizes
ls -lh models/
ls -lh mri-images/glioma/ | wc -l  # count images
```

## 🎯 Quick Deploy Checklist

```bash
# ✅ Before deploying, verify:
git status                    # All changes committed?
git log -1                    # Latest commit looks good?
git push origin main          # Pushed to GitHub?
cat render.yaml               # Config correct?
cat requirements.txt          # Dependencies listed?
ls models/                    # Model files present?
ls mri-images/*/              # Images present?
```

## 💾 Backup Your Work

```bash
# Create a backup branch
git checkout -b backup-$(date +%Y%m%d)
git push origin backup-$(date +%Y%m%d)
git checkout main

# Download everything from GitHub
git clone https://github.com/YOUR_USERNAME/MRI-Brain-Tumor-Detection.git backup-folder
```

## 🔍 Useful URLs

```bash
# Your Render app
https://your-app-name.onrender.com

# Render Dashboard
https://dashboard.render.com

# Your GitHub repo
https://github.com/YOUR_USERNAME/MRI-Brain-Tumor-Detection

# Render Docs
https://render.com/docs
```

## 🎨 Customize Your Deployment

```bash
# Edit render.yaml to change:
# - Python version
# - Build command
# - Start command
# - Environment variables

# Then commit and push:
git add render.yaml
git commit -m "Update Render config"
git push
```

## 📱 Share Your App

```bash
# Get your URL from Render Dashboard
# Then share:

# On Twitter/X:
# "Check out my ML project: https://your-app.onrender.com 🧠🤖"

# On LinkedIn:
# "Deployed my MRI Brain Tumor Detection app using Flask, TensorFlow, and Render!"

# In README:
echo "Live Demo: https://your-app.onrender.com" >> README.md
git add README.md
git commit -m "Add live demo link"
git push
```

## 🔄 Rollback if Needed

```bash
# View recent commits
git log --oneline -10

# Rollback to previous commit
git revert HEAD
git push

# Or restore specific file
git checkout HEAD~1 -- filename
git add filename
git commit -m "Restore filename"
git push
```

## 🎓 Learning More

```bash
# Render documentation for Flask
# https://render.com/docs/deploy-flask

# Git basics
# https://git-scm.com/doc

# Flask documentation
# https://flask.palletsprojects.com/

# TensorFlow guides
# https://www.tensorflow.org/guide
```

---

## Quick Copy-Paste Commands

### First Time Deploy:
```bash
git init && git add . && git commit -m "Initial commit" && git branch -M main
# Then set remote and push (replace YOUR_USERNAME):
git remote add origin https://github.com/YOUR_USERNAME/MRI-Brain-Tumor-Detection.git
git push -u origin main
```

### Regular Updates:
```bash
git add . && git commit -m "Update" && git push
```

### Check Everything:
```bash
python app.py  # Test locally first
git status     # Check what's changed
git push       # Deploy to Render
```

---

**Pro Tip**: Bookmark this file for quick reference! 📌

