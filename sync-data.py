"""
sync-data.py — Sync JSON data files to JS globals for portfolio page.
Run after editing any of the three JSON files:
    python sync-data.py
"""

import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
DOC  = os.path.join(BASE, 'assets', 'prortfolio', 'doc')

def sync(json_file, js_file, var_name):
    json_path = os.path.join(DOC, json_file)
    js_path   = os.path.join(DOC, js_file)

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    js_content = 'window.{} = {};\n'.format(
        var_name,
        json.dumps(data, ensure_ascii=False, indent=2)
    )

    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(js_content)

    print(f'  synced: {json_file} -> {js_file}')

if __name__ == '__main__':
    print('Syncing portfolio data...')
    sync('credits.json',  'credits-data.js',  'creditsData')
    sync('playlist.json', 'playlist-data.js', 'playlistData')
    sync('videos.json',   'videos-data.js',   'videosData')
    print('Done.')
