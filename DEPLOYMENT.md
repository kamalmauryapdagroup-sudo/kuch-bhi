# Deployment Guide to Vercel

## Prerequisites
- GitHub account
- Vercel account (create at vercel.com)
- This repository pushed to GitHub

## Steps to Deploy

### 1. Push to GitHub
```bash
git add .
git commit -m "Prepare for Vercel deployment"
git push origin main
```

### 2. Deploy on Vercel
1. Go to [vercel.com](https://vercel.com)
2. Click "New Project"
3. Import your GitHub repository
4. Select the project
5. Click "Deploy"

Vercel will automatically:
- Install dependencies from `requirements.txt`
- Build your Python app
- Deploy to production

### 3. Get Your Public URL
After deployment, you'll get a URL like: `https://your-project.vercel.app`

### 4. Add Photos, Audio, and Music
Place files in:
- `/static/photos/` - Images
- `/static/audio/` - Voice notes
- `/static/music/` - Background music

### 5. Generate QR Code
Once deployed, run:
```bash
python generate_qr.py https://your-project.vercel.app
```

This creates `qr-code.png` for easy sharing.

## Environment Structure for Vercel

```
Project/
├── api/
│   └── index.py          (Main Flask app for Vercel)
├── static/
│   ├── photos/
│   ├── audio/
│   └── music/
├── vercel.json           (Vercel configuration)
├── requirements.txt      (Python dependencies)
├── .gitignore           (Files to ignore in Git)
├── app.py               (Original local app - kept for reference)
└── generate_qr.py       (QR code generator)
```

## Notes
- Changes to `api/index.py` will auto-redeploy within seconds
- Static files are served from `/static/` directory
- No additional configuration needed beyond what's provided
- Vercel provides free tier with generous limits
