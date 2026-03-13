import wave
import os
import json

MUSIC_DIR = os.path.join(os.path.dirname(__file__), '..', 'music')
OUT_FILE = os.path.join(os.path.dirname(__file__), 'playlist.json')

# Preserve the original ordering from portfolio.html
ORDERED_FILES = [
    "PJ42_+10event_BG_Casual_pre.wav",
    "PJ42_+10event_BG_Deduction_pre.wav",
    "PJ42_+7event_Boss_pre.wav",
    "PJ42_+7event_Story_pre.wav",
    "PJ42_+7event_Story_pre_offvox.wav",
    "PJ42_+7event_Story_pre_ver2.wav",
    "PJ42_+7event_Story_pre_ver2_voxonly.wav",
    "PJ42_+7event_Story_pre_voxonly.wav",
    "PJ42_+8event_Theme_full_pre.wav",
    "PJ42_+9event_BG_pre.wav",
    "PJ42_+9event_Battle_pre.wav",
    "PJ42_+9event_Story_pre.wav",
    "PJ42_+9event_lobby_pre.wav",
]

def get_wav_duration(filepath):
    with wave.open(filepath, 'r') as f:
        frames = f.getnframes()
        rate = f.getframerate()
        return round(frames / rate, 2)

def format_duration(seconds):
    m = int(seconds) // 60
    s = int(seconds) % 60
    return f"{m}:{s:02d}"

tracks = []
for i, filename in enumerate(ORDERED_FILES, 1):
    filepath = os.path.join(MUSIC_DIR, filename)
    if not os.path.exists(filepath):
        print(f"[WARN] Not found: {filename}")
        continue

    duration_sec = get_wav_duration(filepath)
    title = os.path.splitext(filename)[0].replace('_', ' ')

    tracks.append({
        "index": i,
        "title": title,
        "src": f"assets/prortfolio/music/{filename}",
        "duration_sec": duration_sec,
        "duration": format_duration(duration_sec)
    })
    print(f"  {i:02d}. {title}  [{format_duration(duration_sec)}]  ({duration_sec}s)")

playlist = {"tracks": tracks}
with open(OUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(playlist, f, ensure_ascii=False, indent=2)

print(f"\nSaved {len(tracks)} tracks → {OUT_FILE}")
