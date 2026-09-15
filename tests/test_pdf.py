from services.pdf_loader import extract_text_from_pdf


text = extract_text_from_pdf("papers\Impact-of-PM-and-BM-on-Success.pdf")

print(text[:3000])