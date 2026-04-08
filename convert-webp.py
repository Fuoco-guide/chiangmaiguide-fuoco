#!/usr/bin/env python3
"""
Usage: python3 convert-webp.py listing-9-talung-*.png
Converts PNGs to WebP at max 1200px width, quality 85, deletes originals.
"""
import sys, os, glob
from PIL import Image

patterns = sys.argv[1:]
files = []
for p in patterns:
    files += glob.glob(p)
files = sorted(set(files))

if not files:
    print("No files matched.")
    sys.exit(1)

for f in files:
    with Image.open(f) as img:
        if img.width > 1200:
            ratio = 1200 / img.width
            img = img.resize((1200, int(img.height * ratio)), Image.LANCZOS)
        out = f.replace(".png", ".webp")
        img.save(out, "WEBP", quality=85)
        size_in = os.path.getsize(f) // 1024
        size_out = os.path.getsize(out) // 1024
        print(f"  {f} ({size_in}KB) -> {out} ({size_out}KB)")
    os.remove(f)

print(f"Done. {len(files)} files converted.")
