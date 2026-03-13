from PIL import Image, ImageOps

img_path = r"E:\ClaudeProjs\website\assets\clients_new\sanbao.jpg"
out_path = r"E:\ClaudeProjs\website\assets\clients_new\sunborn.png"

try:
    img = Image.open(img_path).convert("RGBA")
    
    # Create the output image
    out_img = Image.new("RGBA", img.size)
    
    # We will assume a white background for typical JPG logos.
    # We'll calculate grayscale value. If it's close to 255 (white), transparency goes up.
    # If it's dark (black or red text/logo), it becomes solid white.
    
    width, height = img.size
    pixels = img.load()
    out_pixels = out_img.load()
    
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            
            # Calculate brightness (0-255)
            # A simple perceptive luminance formula
            luminance = 0.299*r + 0.587*g + 0.114*b
            
            # We want dark pixels to be fully opaque (alpha=255)
            # and bright pixels (background) to be transparent (alpha=0)
            # Using 255 - luminance gives a nice smooth alpha mask.
            # To increase contrast for the logo elements, we can map everything < 200 luminance to nearly opaque
            
            if luminance < 200:
                # The darker it is, the more opaque. But let's just make it very opaque if it's distinctly not white.
                # Linear mapping from luminance [0, 200] -> alpha [255, 100]
                alpha = int(255 - (luminance / 200.0) * 155)
            else:
                # Map luminance [200, 255] -> alpha [100, 0]
                alpha = int(100 - ((luminance - 200) / 55.0) * 100)
                
            # To make it "pop" better on a dark site, we'll make any non-white area pure white.
            # So the color is always 255,255,255 with the calculated alpha.
            # If the original had anti-aliased edges, this preserves the smooth edge as a white glow!
            out_pixels[x, y] = (255, 255, 255, max(0, min(255, alpha * 2)))  # Multiply alpha a bit for solid logo
            
    out_img.save(out_path, "PNG")
    print(f"Fixed image saved to {out_path}")
except Exception as e:
    print(f"Error: {e}")
