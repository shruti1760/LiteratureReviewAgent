def chunk_text(text: str, chunk_size: int = 6000) -> list[str]:
    chunks = []

    for start in range(0, len(text), chunk_size):
        chunks.append(text[start:start + chunk_size])

    return chunks