from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.config import CHUNK_SIZE, CHUNK_OVERLAP


def split_documents(documents):
    """
    Split documents into smaller chunks.
    """

    print("\n" + "=" * 60)
    print("✂️ TEXT SPLITTING")
    print("=" * 60)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    chunks = splitter.split_documents(documents)

    print(f"\n✅ Total Chunks Created : {len(chunks)}")

    print(f"📄 Chunk Size : {CHUNK_SIZE}")

    print(f"🔁 Chunk Overlap : {CHUNK_OVERLAP}")

    return chunks