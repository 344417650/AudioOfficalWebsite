import fitz
from PIL import Image, ImageEnhance, ImageOps

pdf_path = r"E:\ClaudeProjs\website\info\Luminium Studio introduce.pdf"
doc = fitz.open(pdf_path)
page = doc[7]

# Render at 600 DPI for high resolution
print("Rendering at 600 DPI...")
mat = fitz.Matrix(4, 4) # 4x default 72 dpi = 288 dpi, wait, zooming
# Let's use dpi parameter
pix = page.get_pixmap(dpi=600)
temp_path = r"E:\ClaudeProjs\website\info\page_8_hires.png"
pix.save(temp_path)

# Open with Pillow to find and crop logos
img = Image.open(temp_path)
width, height = img.size
print(f"Image size: {width}x{height}")
