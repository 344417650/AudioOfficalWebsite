from PIL import Image

img_path = r"E:\ClaudeProjs\website\assets\clients_new\firewick.jpg"
out_path = r"E:\ClaudeProjs\website\assets\clients_new\firewick.png"

try:
    img = Image.open(img_path).convert("RGBA")
    width, height = img.size
    pixels = img.load()
    
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            
            # Remove white background
            if r > 220 and g > 220 and b > 220:
                pixels[x, y] = (255, 255, 255, 0)
                
            # Remove black foreground (as requested by user "把原来的logo的黑色全变成透明啊")
            elif r < 50 and g < 50 and b < 50:
                pixels[x, y] = (0, 0, 0, 0)
                
    img.save(out_path, "PNG")
    print(f"White background and black pixels both made transparent. Saved to {out_path}")
except Exception as e:
    print(f"Error: {e}")
