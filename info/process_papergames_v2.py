import urllib.request
from PIL import Image

url = "https://assets.papegames.com/nikkiweb/paper/paper-home-cn/_next/static/media/common_logo.ff5f0255.png"
img_path = r"E:\ClaudeProjs\website\assets\clients_new\papergames.png"
out_path = r"E:\ClaudeProjs\website\assets\clients_new\papergames_transparent.png"

try:
    # 1. Download original again to be safe
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        with open(img_path, 'wb') as f:
            f.write(response.read())

    # 2. Process: ONLY remove white background (r,g,b > 240)
    img = Image.open(img_path).convert("RGBA")
    width, height = img.size
    pixels = img.load()
    
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            
            # Make purely/mostly white pixels transparent
            if r > 240 and g > 240 and b > 240 and a > 0:
                pixels[x, y] = (255, 255, 255, 0)
                
    img.save(out_path, "PNG")
    print(f"Only white background removed! Original colors kept intact. Saved to {out_path}")
except Exception as e:
    print(f"Error: {e}")
