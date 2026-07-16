import os
import shutil

from langchain_chroma import Chroma

from src.config import VECTOR_DB_PATH


def create_vector_store(chunks, embedding_model):
    """
    Create a new Chroma vector database.
    """

    print("\n" + "=" * 60)
    print("🗂 CHROMA VECTOR DATABASE")
    print("=" * 60)

    # Delete old database if it exists
    if os.path.exists(VECTOR_DB_PATH):
        print("🗑 Removing old vector database...")
        shutil.rmtree(VECTOR_DB_PATH)

    # Create new database
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=VECTOR_DB_PATH,
    )

    print("✅ Vector Database Created Successfully!")
    print(f"📚 Total Chunks Stored : {len(chunks)}")

    return vector_store


def load_vector_store(embedding_model):
    """
    Load an existing Chroma vector database.
    """

    print("\n" + "=" * 60)
    print("📂 LOADING VECTOR DATABASE")
    print("=" * 60)

    vector_store = Chroma(
        persist_directory=VECTOR_DB_PATH,
        embedding_function=embedding_model,
    )

    print("✅ Existing Vector Database Loaded!")

    return vector_store