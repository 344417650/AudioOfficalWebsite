from PIL import Image

img_path = r"E:\ClaudeProjs\website\assets\clients_new\sanbao.jpg"
out_path = r"E:\ClaudeProjs\website\assets\clients_new\sunborn.png"

try:
    img = Image.open(img_path).convert("RGBA")
    width, height = img.size
    pixels = img.load()
    
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            
            # Simple threshold for white background
            if r > 220 and g > 220 and b > 220:
                # Make white pixels transparent
                pixels[x, y] = (255, 255, 255, 0)
            else:
                # To make edges smoother and avoid white jagged artifacts around the logo:
                # We can do a slight alpha blend based on brightness if we want,
                # but let's keep it simple and just preserve the exact original color for now.
                # If the user wants just white replaced by transparent, this does exactly that.
                pass
                
    img.save(out_path, "PNG")
    print(f"White background removed, original logo colors kept. Saved to {out_path}")
except Exception as e:
    print(f"Error: {e}")
