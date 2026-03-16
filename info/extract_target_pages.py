import fitz
import sys

def extract_pages(pdf_path, pages_to_extract):
    doc = fitz.open(pdf_path)
    for p in pages_to_extract:
        # PyMuPDF is 0-indexed, but usually people mean 1-indexed. Let's print out what we're extracting
        # Let's extract both 9,10,11 and 10,11,12 just to be safe if user meant 1-indexed or 0-indexed.
        print(f"--- PAGE {p+1} ---")
        page = doc.load_page(p)
        print(page.get_text())
        print("\n\n")

if __name__ == '__main__':
    # 0-indexed for 10, 11, 12 is 9, 10, 11.
    extract_pages(r"e:\ClaudeProjs\website\info\Luminium Studio introduce.pdf", [9, 10, 11])
