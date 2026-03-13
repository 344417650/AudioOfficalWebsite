from PIL import Image, ImageOps

img_path = r"E:\ClaudeProjs\website\assets\clients_new\sanbao.jpg"
out_path = r"E:\ClaudeProjs\website\assets\clients_new\sunborn.png"

try:
    img = Image.open(img_path).convert("RGBA")
    
    # Let's see if the background is white or black.
    # We will convert it to Grayscale.
    gray = img.convert("L")
    
    # Get extrema to figure out if it's black-on-white or white-on-black
    min_val, max_val = gray.getextrema()
    print(f"Min: {min_val}, Max: {max_val}")
    
    # We want a white logo on transparent bg.
    # The alpha channel should be the inverted grayscale (if bg is white).
    # If bg is white, black pixels should be fully opaque (255), white pixels transparent (0).
    alpha = ImageOps.invert(gray)
    
    # Create a solid white RGBA image
    white_img = Image.new("RGBA", img.size, (255, 255, 255, 255))
    
    # Put the extracted alpha 
    white_img.putalpha(alpha)
    
    white_img.save(out_path, "PNG")
    print("Re-processed with smooth alpha mask!")
except Exception as e:
    print(f"Error: {e}")
