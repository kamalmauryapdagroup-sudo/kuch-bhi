MADAM JI BIRTHDAY — CHERRY BLOSSOM VERSION

WHAT'S NEW IN THIS VERSION
- Moonlit cherry blossom theme: dusk-pink sky, blossom branches framing
  the corners, and a petal shower in white/blush/pink instead of the
  old deep-space look
- Mobile-friendly: safe-area support for notched phones, tighter font
  scaling on small screens, lighter animation load on phones
- Production-ready: works both locally and when deployed (Render,
  PythonAnywhere, etc.) — no code changes needed either way
- Single-file app: the whole page lives inside app.py (via
  render_template_string), so there's no separate templates folder to
  keep in sync

HOW TO RUN LOCALLY
1. Open a terminal in this folder.
2. Install dependencies:
   pip install -r requirements.txt
3. Run:
   python app.py
4. Open:
   http://127.0.0.1:5000

HOW TO PERSONALIZE
- Photos:     drop files into static/photos/ (see the README in that folder)
- Voice note: drop a file into static/audio/ (see the README in that folder)
- Music:      drop a file into static/music/ (see the README in that folder)
- Text:       everything visible on the page lives inside app.py, in the
              INDEX_HTML variable near the top of the file. Open it in
              any text editor and search for the line you want to change.
              Quiz questions are the easiest to personalize with real
              inside jokes — search for "QUESTION 0" to find them.
- Captions:   in the scrapbook section, search for "Add a caption here"

UPDATING YOUR GITHUB REPO WITH THIS VERSION
1. Go to your repo on github.com and open the folder your files are in
   (e.g. Madam_Ji_Birthday_Python_App (1)).
2. Click "Add file" -> "Upload files".
3. Drag in app.py and requirements.txt from this zip — this will
   overwrite the old versions since the filenames match.
4. Scroll down and click "Commit changes".
5. If you're on Render, it will auto-redeploy within a minute or two.
   If you're on PythonAnywhere, go to the "Web" tab and click "Reload".

SENDING IT TO HER
Running it with "python app.py" only works on your own computer — she
can't open that link from her phone. To actually send this to her, host
it somewhere with a public URL, for example:
- Render.com (free tier, connect a GitHub repo, deploys Flask apps directly)
- PythonAnywhere (free tier, good for small Flask apps)
- Railway.app

Once you have a real public link, you can turn it into a QR code:
   pip install qrcode[pil]
   python generate_qr.py https://your-deployed-link.com
This saves qr-code.png, which you can text her directly or print.
