from langchain_community.embeddings import HuggingFaceEmbeddings


def get_embedding_model():
    """
    Load HuggingFace embedding model.
    """

    print("\n" + "=" * 60)
    print("🧠 EMBEDDING MODEL")
    print("=" * 60)

    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("✅ HuggingFace Embedding Model Loaded Successfully!")

    return embedding