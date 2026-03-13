from PIL import Image

def process_wangyi():
    img_path = r"E:\ClaudeProjs\website\assets\clients_new\wangyi.png"
    out_path = r"E:\ClaudeProjs\website\assets\clients_new\wangyi_white.png"
    
    img = Image.open(img_path).convert("RGBA")
    data = img.getdata()
    
    new_data = []
    for item in data:
        # Check if the pixel is close to white (background)
        # R, G, B are all high values
        if item[0] > 240 and item[1] > 240 and item[2] > 240:
            # Turn white background pixels into completely transparent
            new_data.append((255, 255, 255, 0))
        # Ignore fully transparent pixels that might already exist
        elif item[3] == 0:
            new_data.append((255, 255, 255, 0))
        # Turn everything else (the colored logo content) into pure white
        else:
            new_data.append((255, 255, 255, 255))
            
    img.putdata(new_data)
    img.save(out_path, "PNG")
    print("wangyi logo correctly processed: background removed, content turned to solid white!")

if __name__ == "__main__":
    process_wangyi()
