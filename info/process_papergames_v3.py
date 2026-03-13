from PIL import Image

img_path = r"E:\ClaudeProjs\website\assets\clients_new\papergames.png"
out_path = r"E:\ClaudeProjs\website\assets\clients_new\papergames_transparent.png"
out_path2 = r"E:\ClaudeProjs\website\assets\clients_new\papergames_white.png"

try:
    # 1. Open the original unmodified logo
    # Assuming from the URL we downloaded in process_papergames_v2.py it's still at papergames.png
    img = Image.open(img_path).convert("RGBA")
    width, height = img.size
    pixels = img.load()
    
    # 2. Create a new image to store the result
    out_img = Image.new("RGBA", (width, height))
    out_pixels = out_img.load()
    
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            
            # If the pixel is mostly white (e.g. background or white parts of the logo)
            if r > 200 and g > 200 and b > 200:
                # Make it transparent
                out_pixels[x, y] = (255, 255, 255, 0)
            elif a > 0:
                # If it has any color (red crane, black text) and is not transparent
                # Make it pure white and keep its original alpha
                out_pixels[x, y] = (255, 255, 255, a)
                
    out_img.save(out_path2, "PNG")
    print(f"White background removed, all colored elements turned to white! Saved to {out_path2}")
except Exception as e:
    print(f"Error: {e}")
