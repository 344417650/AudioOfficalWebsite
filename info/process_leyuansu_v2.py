from PIL import Image

img_path = r"E:\ClaudeProjs\website\assets\clients_new\leyuansu.png"
out_path = r"E:\ClaudeProjs\website\assets\clients_new\happyelements.png"

try:
    img = Image.open(img_path).convert("RGBA")
    
    out_img = Image.new("RGBA", img.size)
    
    width, height = img.size
    pixels = img.load()
    out_pixels = out_img.load()
    
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            
            # Simple perceptive luminance formula
            luminance = 0.299*r + 0.587*g + 0.114*b
            
            # Since the background is pure white (R=255, G=255, B=255)
            # and the text is dark (gray/black), we can create an alpha mask
            # where dark parts are opaque white.
            
            if luminance < 200:
                # The darker it is, the more opaque.
                alpha = int(255 - (luminance / 200.0) * 155)
            else:
                # Map luminance [200, 255] -> alpha [100, 0]
                alpha = int(100 - ((luminance - 200) / 55.0) * 100)
                
            # Make dark spots pure white with calculated opacity
            out_pixels[x, y] = (255, 255, 255, max(0, min(255, alpha * 2)))

    # Crop to fit the logo tightly (remove huge empty borders if any)
    bbox = out_img.getbbox()
    if bbox:
        out_img = out_img.crop(bbox)
        
    out_img.save(out_path, "PNG")
    print(f"White background removed, black text turned to white! Saved to {out_path}")
except Exception as e:
    print(f"Error: {e}")
