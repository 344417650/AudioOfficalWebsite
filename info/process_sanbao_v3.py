from PIL import Image, ImageOps

img_path = r"E:\ClaudeProjs\website\assets\clients_new\sanbao.jpg"
out_path = r"E:\ClaudeProjs\website\assets\clients_new\sunborn.png"

try:
    img = Image.open(img_path).convert("L")  # Grayscale
    
    # Check top-left corner pixel to determine background color
    bg_color = img.getpixel((0, 0))
    print(f"Background color (top-left): {bg_color}")
    
    # If bg is dark (close to 0), the logo is bright.
    # Alpha should be exactly the brightness of the pixels.
    if bg_color < 128:
        # dark background, bright logo
        alpha = img
    else:
        # bright background, dark logo
        alpha = ImageOps.invert(img)
    
    # Optional: Enhance contrast of the alpha mask so the logo is fully opaque
    # We can map the pixels to stretch contrast
    # Let's say we threshold slightly to remove compression artifacts in the background
    alpha = alpha.point(lambda p: 0 if p < 30 else (255 if p > 200 else int((p-30)*255/(200-30))))

    white_img = Image.new("RGBA", img.size, (255, 255, 255, 255))
    white_img.putalpha(alpha)
    
    white_img.save(out_path, "PNG")
    print("Re-processed with correct dynamic bg checking!")
except Exception as e:
    print(f"Error: {e}")
