from PIL import Image
import os

img_path = r"E:\ClaudeProjs\website\info\page_8_hires.png"
out_dir = r"E:\ClaudeProjs\website\assets\clients"
os.makedirs(out_dir, exist_ok=True)

pil_img = Image.open(img_path).convert("RGBA")
gray_pil = pil_img.convert("L")
# Enhanced mask: map 50-150 intensity to 0-255 opacity
alpha_mask = gray_pil.point(lambda p: min(255, max(0, int((p - 50) * 255 / (150 - 50)))))

# Create white logos with the alpha mask
wg = Image.new("RGBA", pil_img.size, (255, 255, 255, 255))
wg.putalpha(alpha_mask)

w, h = wg.size
# 2 rows, 4 cols
cell_w = w // 4
cell_h = h // 2

count = 1
for row in range(2):
    for col in range(4):
        # Base crop for the cell
        x1 = col * cell_w
        y1 = row * cell_h
        x2 = (col + 1) * cell_w
        y2 = (row + 1) * cell_h
        
        cell = wg.crop((x1, y1, x2, y2))
        
        # Get bounding box of the non-transparent area
        bbox = cell.getbbox()
        if bbox: # (left, upper, right, lower)
            cropped_logo = cell.crop(bbox)
            
            # Save it
            out_path = os.path.join(out_dir, f"client_{count}.png")
            cropped_logo.save(out_path)
            print(f"Saved {out_path} ({cropped_logo.size[0]}x{cropped_logo.size[1]})")
            count += 1
        else:
            print(f"Empty cell at row {row}, col {col}")
