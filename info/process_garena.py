from PIL import Image

def process_garena():
    img_path = r"E:\ClaudeProjs\website\assets\clients_new\garena.png"
    out_path = r"E:\ClaudeProjs\website\assets\clients_new\garena_white.png"
    
    img = Image.open(img_path).convert("RGBA")
    data = img.getdata()
    
    new_data = []
    for item in data:
        # Check if the pixel is close to white (background in some images)
        if item[0] > 240 and item[1] > 240 and item[2] > 240:
            new_data.append((255, 255, 255, 0))
        # Ignore fully transparent pixels that might already exist
        elif item[3] == 0:
            new_data.append((255, 255, 255, 0))
        # Turn everything else (the colored logo content string) into pure solid white
        else:
            new_data.append((255, 255, 255, 255))
            
    img.putdata(new_data)
    img.save(out_path, "PNG")
    print("garena logo correctly processed: background/white removed, content turned to solid white!")

if __name__ == "__main__":
    process_garena()
