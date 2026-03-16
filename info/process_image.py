from PIL import Image, ImageEnhance, ImageOps
import os

img_path = r"E:\ClaudeProjs\website\info\page_8_hires.png"
out_dir = r"E:\ClaudeProjs\website\assets\clients"
os.makedirs(out_dir, exist_ok=True)

img = Image.open(img_path).convert("RGBA")
# Background is dark grey. We want to extract the bright pixels.
# Let's get the luminance.
gray = img.convert("L")
# Convert everything brighter than 80 to white, darker to black (or transparent)
# We can use point transform.
bw = gray.point(lambda x: 255 if x > 100 else 0, '1')

# Save the full processed image just to debug
bw.save(r"E:\ClaudeProjs\website\info\debug_bw.png")
