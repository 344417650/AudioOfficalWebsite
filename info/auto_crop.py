from PIL import Image, ImageOps
import cv2
import numpy as np
import os

img_path = r"E:\ClaudeProjs\website\info\page_8_hires.png"
out_dir = r"E:\ClaudeProjs\website\assets\clients"
os.makedirs(out_dir, exist_ok=True)

# Load image using OpenCV
img = cv2.imread(img_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# The background is dark, logos are bright.
# Threshold to get a binary mask of the logos
_, thresh = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY)

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filter out small noise and huge boxes (like the whole page if any)
bboxes = []
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    if w > 200 and h > 100 and w < 3000 and h < 2000:
        bboxes.append((x, y, w, h))

# Consolidate nearby bounding boxes since a logo might have multiple parts
# A simple way to group is to dilate the thresholded image before finding contours
kernel = np.ones((100, 100), np.uint8) # large kernel to connect parts of same logo
dilated = cv2.dilate(thresh, kernel, iterations=1)
contours_merged, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print(f"Found {len(contours_merged)} main logo regions.")

# Extract the regions from the original image and make them transparent
pil_img = Image.open(img_path).convert("RGBA")
# Convert to luminesence for alpha channel
gray_pil = pil_img.convert("L")
alpha_mask = gray_pil.point(lambda p: min(255, max(0, int((p - 50) * 255 / (150 - 50))))) # enhance contrast for alpha

# Make the color white where alpha is present
white_img = Image.new("RGBA", pil_img.size, (255, 255, 255, 255))
white_img.putalpha(alpha_mask)

count = 1
# Sort contours by y first (rows), then x (cols)
bboxes = [cv2.boundingRect(c) for c in contours_merged]
# Remove small artifacts
bboxes = [b for b in bboxes if b[2] > 200 and b[3] > 100]

bboxes.sort(key=lambda b: (b[1]//500, b[0])) # Group by Y then X

for i, (x, y, w, h) in enumerate(bboxes):
    # Expand slightly
    pad = 50
    x1, y1 = max(0, x-pad), max(0, y-pad)
    x2, y2 = min(pil_img.width, x+w+pad), min(pil_img.height, y+h+pad)
    
    logo = white_img.crop((x1, y1, x2, y2))
    
    # Check if there's enough visible content
    extrema = logo.getextrema()
    if extrema[3][1] > 0: # Max alpha is > 0
        crop_path = os.path.join(out_dir, f"client_logo_{count}.png")
        logo.save(crop_path)
        print(f"Saved {crop_path} ({x2-x1}x{y2-y1})")
        count += 1
