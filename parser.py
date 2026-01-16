def read_file(path):
    if path.endswith(".pdf"):
        from pdfminer.high_level import extract_text
        return extract_text(path)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
