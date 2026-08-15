from services.pdf_loader import extract_text_from_pdf


text = extract_text_from_pdf("papers\\294_Final.pdf")

print(text[:3000])