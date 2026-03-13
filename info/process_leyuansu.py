from PIL import Image

img_path = r"E:\ClaudeProjs\website\assets\clients_new\leyuansu.png"
out_path = r"E:\ClaudeProjs\website\assets\clients_new\happyelements.png"

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
                
    img.save(out_path, "PNG")
    print(f"White background removed. Saved to {out_path}")
except Exception as e:
    print(f"Error: {e}")
