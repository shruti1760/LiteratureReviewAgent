from services.pdf_loader import extract_text_from_pdf
from services.text_chunker import chunk_text


text = extract_text_from_pdf("papers\\Impact-of-PM-and-BM-on-Success.pdf")

chunks = chunk_text(text)

print("Number of chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i + 1} ---")
    print(chunk[:300])