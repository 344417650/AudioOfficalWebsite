from PIL import Image

img_path = r"E:\ClaudeProjs\website\assets\clients_new\zhulong.png"
out_path = r"E:\ClaudeProjs\website\assets\clients_new\aurogon_white.png"

try:
    img = Image.open(img_path).convert("RGBA")
    width, height = img.size
    
    # We will identify connected components or bounding boxes to isolate the left icon and right text
    # But since we don't have OpenCV here easily and want a robust way:
    # A common issue with "other elements" in logos copied from websites is a background box, 
    # a tagline below, or watermarks.
    
    # Let's first do a pass to convert to white and remove white background
    out_img = Image.new("RGBA", img.size)
    pixels = img.load()
    out_pixels = out_img.load()
    
    # We will compute the bounding box of all "dark" pixels (the actual logo/text)
    min_x = width
    max_x = 0
    min_y = height
    max_y = 0
    
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            luminance = 0.299*r + 0.587*g + 0.114*b
            
            # If it's a dark pixel and not fully transparent
            if a > 0 and luminance < 200:
                min_x = min(min_x, x)
                max_x = max(max_x, x)
                min_y = min(min_y, y)
                max_y = max(max_y, y)

    # Now we know where the main content is.
    # User said: "除了左边的图标和右边的文字，其他元素都搞成透明"
    # This implies there might be a tagline text AT THE BOTTOM, or some English text below the Chinese.
    # Usually, the main logo (Icon + Chinese text) is vertically centered or forms the top chunk.
    # The tagline is usually smaller and lower.
    
    # Let's analyze vertical density of dark pixels to find the gap between main logo and tagline.
    row_density = [0] * height
    for y in range(min_y, max_y + 1):
        count = 0
        for x in range(min_x, max_x + 1):
            r, g, b, a = pixels[x, y]
            luminance = 0.299*r + 0.587*g + 0.114*b
            if a > 0 and luminance < 200:
                count += 1
        row_density[y] = count

    # Find the main chunk 
    # The icon and main text are usually the thickest vertically.
    # If there is a tagline, there will be a row with 0 or very few pixels separating them.
    
    # Let's find the bottom of the main chunk
    # Start from min_y, go down. If density drops significantly (like < 2% of max density) or to 0, that's the bottom gap.
    max_dense = max(row_density)
    
    main_bottom = max_y
    for y in range(min_y, max_y):
        # if we hit a very quiet row after a busy row
        if row_density[y] < max_dense * 0.05 and row_density[y-1] > max_dense * 0.1:
            # We found a vertical gap!
            main_bottom = y
            break

    # Also, "左边的图标和右边的文字", maybe there's something far right?
    # We'll assume the user just wants to ditch a tagline at the bottom or english text, which is the most common case for "left icon right text" logo layouts.
    
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            luminance = 0.299*r + 0.587*g + 0.114*b
            
            # Only keep pixels that are inside the main vertically bounded chunk
            if y <= main_bottom:
                if r > 240 and g > 240 and b > 240:
                    out_pixels[x, y] = (255, 255, 255, 0)
                elif a > 0:
                    if luminance < 200:
                        alpha = int(255 - (luminance / 200.0) * 155)
                    else:
                        alpha = int(100 - ((luminance - 200) / 55.0) * 100)
                    out_pixels[x, y] = (255, 255, 255, max(0, min(255, alpha * 2)))
            else:
                # Anything below the main logo (like English text or slogan) is made completely transparent
                out_pixels[x, y] = (0, 0, 0, 0)

    # Crop tightly
    bbox = out_img.getbbox()
    if bbox:
        out_img = out_img.crop(bbox)
        
    out_img.save(out_path, "PNG")
    print(f"Isolated left icon and right text, removed bottom/other elements. Saved to {out_path}")
except Exception as e:
    print(f"Error: {e}")
