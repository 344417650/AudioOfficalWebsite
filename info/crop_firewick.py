from PIL import Image

img_path = r"E:\ClaudeProjs\website\assets\clients_new\firewick.png"

try:
    img = Image.open(img_path).convert("RGBA")
    
    # getbbox() finds the bounding box of non-zero alpha in the image
    # For RGBA images, it looks at the alpha channel.
    bbox = img.getbbox()
    
    if bbox:
        cropped_img = img.crop(bbox)
        cropped_img.save(img_path, "PNG")
        print(f"Successfully cropped empty transparent borders. New size: {cropped_img.size}")
    else:
        print("Image consists of entirely transparent pixels.")
        
except Exception as e:
    print(f"Error: {e}")
