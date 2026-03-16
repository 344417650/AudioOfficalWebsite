from PIL import Image

def process_0c():
    img_path = r"E:\ClaudeProjs\website\assets\clients_new\0c.png"
    out_path = r"E:\ClaudeProjs\website\assets\clients_new\0c_white.png"
    
    img = Image.open(img_path).convert("RGBA")
    data = img.getdata()
    
    new_data = []
    for item in data:
        # 如果像素是不透明的（Alpha > 0），强制变成全白并保留原有透明度
        if item[3] > 10:
            new_data.append((255, 255, 255, item[3]))
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    img.save(out_path, "PNG")
    print("0c logo processed to white transparent PNG!")

if __name__ == "__main__":
    process_0c()
