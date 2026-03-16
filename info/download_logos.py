import urllib.request
import os

logos = {
    'firewick': 'https://upload.wikimedia.org/wikipedia/zh/0/07/Firewick_Network_logo.svg',
    'hypergryph': 'https://web-ipv6.hycdn.cn/hypergryph/official/assets/img/logo.a085fd.svg',
    'bluepoch': 'https://www.bluepoch.com/_nuxt/img/logo.46bc285.svg',
    'papergames': 'https://assets.papegames.com/nikkiweb/paper/paper-home-cn/_next/static/media/common_logo.ff5f0255.png',
    'perfectworld': 'https://upload.wikimedia.org/wikipedia/commons/f/f0/Perfect_World_Co._logo.svg',
    'aurogon': 'http://www.aurogon.com/images/index_logo.png',
    'sunborn': 'https://upload.wikimedia.org/wikipedia/zh/e/e0/Sunborn_Network_Technology_logo.svg',
    'xd': 'https://website.xdcdn.net/www/logo/tips_cn@2x.png',
    'happyelements': 'https://upload.wikimedia.org/wikipedia/zh/1/1a/Happy_Elements_logo.png'
}

out_dir = r'E:\ClaudeProjs\website\assets\clients_new'
os.makedirs(out_dir, exist_ok=True)

for name, url in logos.items():
    # Identify extension from URL
    ext = url.split('.')[-1].split('?')[0]
    filename = f"{name}.{ext}" if ext in ['png', 'svg', 'jpg', 'jpeg'] else f"{name}.png"
    out_path = os.path.join(out_dir, filename)
    try:
        # Use User-Agent to avoid blocks
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            with open(out_path, 'wb') as out_file:
                out_file.write(response.read())
        print(f'Successfully downloaded: {filename}')
    except Exception as e:
        print(f'Failed to download {name}: {e}')
