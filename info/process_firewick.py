import urllib.request
from PIL import Image
import os

url = "https://i0.hdslb.com/bfs/archive/95cbfe74ef1929a1f944fcbc018a5c33f917c8db.jpg"
temp_img = r"E:\ClaudeProjs\website\assets\clients_new\firewick.jpg"
out_img = r"E:\ClaudeProjs\website\assets\clients_new\firewick.png"

try:
    # 1. Download
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        with open(temp_img, 'wb') as f:
            f.write(response.read())
    print("Downloaded successfully.")

    # 2. Process
    img = Image.open(temp_img).convert("RGBA")
    width, height = img.size
    pixels = img.load()
    
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            # Threshold for white background
            if r > 220 and g > 220 and b > 220:
                pixels[x, y] = (255, 255, 255, 0)
                
    img.save(out_img, "PNG")
    print(f"Processed and saved to {out_img}")
except Exception as e:
    print(f"Error: {e}")
