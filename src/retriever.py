from src.config import TOP_K_RESULTS


def create_retriever(vector_store):
    """
    Create a retriever from the Chroma vector database.
    """

    print("\n" + "=" * 60)
    print("🔍 RETRIEVER")
    print("=" * 60)

    retriever = vector_store.as_retriever(
        search_kwargs={
            "k": TOP_K_RESULTS
        }
    )

    print("✅ Retriever Created Successfully!")
    print(f"📚 Top Results : {TOP_K_RESULTS}")

    return retriever