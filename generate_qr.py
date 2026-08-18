"""
Run this AFTER you've deployed the site somewhere (Render, PythonAnywhere,
Railway, etc.) and have a real public URL for it.

Usage:
    pip install qrcode[pil]
    python generate_qr.py https://your-deployed-link.com

This saves qr-code.png in this folder — print it, put it on a card,
or just text her the image directly.
"""
import sys
import qrcode

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_qr.py <your-deployed-url>")
        sys.exit(1)

    url = sys.argv[1]
    img = qrcode.make(url)
    img.save("qr-code.png")
    print(f"Saved qr-code.png for: {url}")
