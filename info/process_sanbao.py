from PIL import Image

# Open the image
img_path = r"E:\ClaudeProjs\website\assets\clients_new\sanbao.jpg"
out_path = r"E:\ClaudeProjs\website\assets\clients_new\sunborn.png"

try:
    img = Image.open(img_path).convert("RGBA")
    data = img.getdata()
    
    # Assuming it's a black/gray logo on white background.
    # We want to make the background transparent and keep the logo white.
    new_data = []
    for item in data:
        # If it's bright (white background), make it transparent
        # If it's dark (the logo), make it white and opaque
        avg = (item[0] + item[1] + item[2]) / 3
        if avg > 200:
            # Transparent background
            new_data.append((255, 255, 255, 0))
        else:
            # White logo
            new_data.append((255, 255, 255, 255))
    
    img.putdata(new_data)
    img.save(out_path, "PNG")
    print(f"Successfully processed and saved to {out_path}")
except Exception as e:
    print(f"Error processing image: {e}")
