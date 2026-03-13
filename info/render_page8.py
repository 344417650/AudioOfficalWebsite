import fitz

pdf_path = r"E:\ClaudeProjs\website\info\Luminium Studio introduce.pdf"
doc = fitz.open(pdf_path)

if len(doc) >= 8:
    page = doc[7]  # 0-indexed, so page 8 is index 7
    # Save as image
    pix = page.get_pixmap(dpi=150)
    pix.save(r"E:\ClaudeProjs\website\info\page_8.png")
    
    # Extract text to easily get client names
    text = page.get_text()
    print("--- PAGE 8 TEXT ---")
    print(text.encode('utf-8', errors='replace').decode('utf-8'))
else:
    print("PDF has fewer than 8 pages")
