import sys
import os

try:
    import pypdf
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pypdf"])
    import pypdf

pdf_path = r"E:\ClaudeProjs\website\info\Luminium Studio introduce.pdf"
try:
    with open(pdf_path, 'rb') as file:
        reader = pypdf.PdfReader(file)
        text_page_3 = reader.pages[2].extract_text() if len(reader.pages) > 2 else ""
        text_page_4 = reader.pages[3].extract_text() if len(reader.pages) > 3 else ""
        
        print("--- PAGE 3 ---")
        print(text_page_3.encode('utf-8', errors='replace').decode('utf-8'))
        print("--- PAGE 4 ---")
        print(text_page_4.encode('utf-8', errors='replace').decode('utf-8'))
except Exception as e:
    print(f"Error: {e}")
