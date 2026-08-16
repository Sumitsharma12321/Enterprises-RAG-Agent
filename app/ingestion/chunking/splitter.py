from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter
import logfire

def chunk_text(text: str, chunk_size: int = 1000, chunk_overlap: int = 150) -> List[str]:
    """
    Recursive chunker with overlap — preserves structured content (YAML blocks,
    multi-line CLI sequences) by falling back through separators (paragraph →
    line → sentence → word) instead of blindly splitting on \n\n.
    """
    with logfire.span("✂️ Text Chunking", text_length=len(text)):
        if not text.strip():
            return []

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=["\n\n", "\n", ". ", " ", ""],
            length_function=len,
        )

        chunks = splitter.split_text(text)
        valid_chunks = [c.strip() for c in chunks if c.strip()]
        logfire.info(f"✅ Generated {len(valid_chunks)} chunks")
        return valid_chunks