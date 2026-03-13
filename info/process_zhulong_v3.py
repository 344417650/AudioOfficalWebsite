from PIL import Image

img_path = r"E:\ClaudeProjs\website\assets\clients_new\zhulong.png"
out_path = r"E:\ClaudeProjs\website\assets\clients_new\aurogon_white.png"

try:
    img = Image.open(img_path).convert("RGBA")
    width, height = img.size
    
    out_img = Image.new("RGBA", img.size)
    pixels = img.load()
    out_pixels = out_img.load()
    
    # Pass 1: find main bounds
    min_x, max_x, min_y, max_y = width, 0, height, 0
    
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            luminance = 0.299*r + 0.587*g + 0.114*b
            
            # Is it green?
            # Green pixels will have G significantly higher than R and B
            is_green = (g > r + 20) and (g > b + 20)
            
            if a > 0 and luminance < 200 and not is_green:
                min_x = min(min_x, x)
                max_x = max(max_x, x)
                min_y = min(min_y, y)
                max_y = max(max_y, y)

    # Find the main chunk (ignore bottom tagline if exists)
    row_density = [0] * height
    for y in range(min_y, max_y + 1):
        count = 0
        for x in range(min_x, max_x + 1):
            r, g, b, a = pixels[x, y]
            luminance = 0.299*r + 0.587*g + 0.114*b
            is_green = (g > r + 20) and (g > b + 20)
            if a > 0 and luminance < 200 and not is_green:
                count += 1
        row_density[y] = count

    max_dense = max(row_density) if row_density else 0
    main_bottom = max_y
    for y in range(min_y + 1, max_y):
        if row_density[y] < max_dense * 0.05 and row_density[y-1] > max_dense * 0.1:
            main_bottom = y
            break

    # Pass 2: render and remove green
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            luminance = 0.299*r + 0.587*g + 0.114*b
            
            # Remove green glow (if green is dominant)
            # Or if it's very white bg
            is_green = (g > r + 15) and (g > b + 15)
            is_bg = r > 240 and g > 240 and b > 240
            
            if y <= main_bottom:
                if is_bg or is_green:
                    out_pixels[x, y] = (255, 255, 255, 0)
                elif a > 0:
                    if luminance < 200:
                        alpha = int(255 - (luminance / 200.0) * 155)
                    else:
                        alpha = int(100 - ((luminance - 200) / 55.0) * 100)
                    out_pixels[x, y] = (255, 255, 255, max(0, min(255, alpha * 2)))
            else:
                out_pixels[x, y] = (0, 0, 0, 0)

    # Crop tightly
    bbox = out_img.getbbox()
    if bbox:
        out_img = out_img.crop(bbox)
        
    out_img.save(out_path, "PNG")
    print(f"Removed green glow and bottom elements, saved to {out_path}")
except Exception as e:
    print(f"Error: {e}")
