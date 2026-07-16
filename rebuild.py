from src.document_loader import load_documents
from src.text_splitter import split_documents
from src.embeddings import get_embedding_model
from src.vector_store import create_vector_store


def rebuild_vector_database():

    print("=" * 60)
    print("🔄 REBUILDING VECTOR DATABASE")
    print("=" * 60)

    # Step 1: Load Documents
    documents = load_documents()

    # Step 2: Split Documents
    chunks = split_documents(documents)

    # Step 3: Load Embedding Model
    embedding_model = get_embedding_model()

    # Step 4: Create Vector Database
    create_vector_store(
        chunks,
        embedding_model
    )

    print("\n" + "=" * 60)
    print("✅ VECTOR DATABASE REBUILT SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    rebuild_vector_database()