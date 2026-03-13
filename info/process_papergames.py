from PIL import Image

img_path = r"E:\ClaudeProjs\website\assets\clients_new\papergames.png"
out_path = r"E:\ClaudeProjs\website\assets\clients_new\papergames_bw.png"

try:
    img = Image.open(img_path).convert("RGBA")
    width, height = img.size
    pixels = img.load()
    
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            
            if a > 0:
                # Calculate perceptive luminance
                lum = int(0.299 * r + 0.587 * g + 0.114 * b)
                
                # We are placing this on a dark background.
                # Original Black text (lum ~ 0) should become White (255) to be visible.
                # Original Red bird (lum ~ 80) should become light gray (~175).
                # Original White accents (lum ~ 255) should become dark/black (0) or transparent.
                # Inverting the luminance achieves exactly this perfect dark-mode adaptation.
                inv_lum = 255 - lum
                
                # Keep original alpha to preserve smooth anti-aliased edges
                pixels[x, y] = (inv_lum, inv_lum, inv_lum, a)
                
    img.save(out_path, "PNG")
    print(f"Preserved grayscale details and inverted for dark mode! Saved to {out_path}")
except Exception as e:
    print(f"Error: {e}")
