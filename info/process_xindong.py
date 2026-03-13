from PIL import Image

img_path = r"E:\ClaudeProjs\website\assets\clients_new\xindong.png"
out_path = r"E:\ClaudeProjs\website\assets\clients_new\xd_white.png"

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
            
            # If the pixel is mostly white (background)
            if r > 240 and g > 240 and b > 240:
                # Make it transparent
                out_pixels[x, y] = (255, 255, 255, 0)
            elif a > 0:
                # If it has any color / is dark, let's map it to an opaque or semi-opaque white pixel
                if luminance < 200:
                    alpha = int(255 - (luminance / 200.0) * 155)
                else:
                    alpha = int(100 - ((luminance - 200) / 55.0) * 100)
                    
                # The darker it was, the more intensely white it becomes, keeping edges anti-aliased
                final_alpha = max(0, min(255, alpha * 2))
                out_pixels[x, y] = (255, 255, 255, final_alpha)

    # Crop huge empty borders
    bbox = out_img.getbbox()
    if bbox:
        out_img = out_img.crop(bbox)
        
    out_img.save(out_path, "PNG")
    print(f"White background removed, colored text/logo turned to white! Saved to {out_path}")
except Exception as e:
    print(f"Error: {e}")
