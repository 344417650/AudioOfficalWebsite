import fitz

pdf_path = r"E:\ClaudeProjs\website\info\Luminium Studio introduce.pdf"
doc = fitz.open(pdf_path)

if len(doc) > 2:
    page3 = doc[2]
    pix = page3.get_pixmap(dpi=150)
    pix.save(r"E:\ClaudeProjs\website\info\page_3.png")

if len(doc) > 3:
    page4 = doc[3]
    pix = page4.get_pixmap(dpi=150)
    pix.save(r"E:\ClaudeProjs\website\info\page_4.png")
