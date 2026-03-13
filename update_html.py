import re

with open(r'e:\ClaudeProjs\website\portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

def replace_item(match):
    num = match.group(1)
    name = match.group(2)
    dur = match.group(3)
    return f'<div class="track-number">{num}</div><div class="track-name-wrapper"><div class="track-name">{name}</div></div><div class="track-duration">{dur}</div>'

pattern = r'<div class="track-number">(.*?)</div><div class="track-name">(.*?)</div><div class="track-bpm-tag">.*?</div><div class="track-duration">(.*?)</div>'

new_html = re.sub(pattern, replace_item, html)

with open(r'e:\ClaudeProjs\website\portfolio.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
