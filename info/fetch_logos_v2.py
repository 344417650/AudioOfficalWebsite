import urllib.request
import urllib.parse
import re
import ssl
import os

ssl._create_default_https_context = ssl._create_unverified_context
out_dir = r"E:\ClaudeProjs\website\assets\clients_new"
os.makedirs(out_dir, exist_ok=True)

def download_url(url, name):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=10) as response:
            with open(os.path.join(out_dir, f"{name}.png"), "wb") as f:
                f.write(response.read())
        print(f"Successfully downloaded direct URL for {name}")
    except Exception as e:
        print(f"Failed direct URL for {name}: {e}")

# Exact URL from User for Perfect World
download_url("https://games.wanmei.com/images/index2205/main/logo.png", "perfectworld")

# Search Baidu Images for the rest
def get_baidu_image(query):
    # 'objURL' in Baidu Images json matches
    url = f"https://image.baidu.com/search/index?tn=baiduimage&word={urllib.parse.quote(query)}"
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/116.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
    })
    try:
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
        # Baidu uses 'thumbURL' or 'objURL'
        urls = re.findall(r'"objURL":"(.*?)"', html)
        if not urls:
            urls = re.findall(r'"thumbURL":"(.*?)"', html)
        if urls:
            # Filter out some very common invalid image hosts or just take the first
            return urls[0]
    except Exception as e:
         print(f"Search failed for {query}: {e}")
    return None

q_dict = {
    'firewick': '烛薪网络 logo png透明',
    'aurogon': '上海烛龙 logo png透明',
    'sunborn': '散爆网络 logo png',
    'xd': '心动 xd logo png透明',
    'happyelements': '乐元素 logo png透明'
}

for name, q in q_dict.items():
    print(f"Searching for {name} ({q})...")
    img_url = get_baidu_image(q)
    print(f"Found URL for {name}: {img_url}")
    if img_url:
        try:
            req = urllib.request.Request(img_url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/116.0.0.0 Safari/537.36',
                'Referer': 'https://image.baidu.com/'
            })
            with urllib.request.urlopen(req, timeout=10) as response:
                with open(os.path.join(out_dir, f"{name}.png"), "wb") as f:
                    f.write(response.read())
            print(f"Downloaded {name}.png")
        except Exception as e:
            print(f"Failed downloading {name}: {e}")
