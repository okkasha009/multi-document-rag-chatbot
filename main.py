from src.config import GEMINI_MODEL

from src.embeddings import get_embedding_model
from src.vector_store import load_vector_store
from src.retriever import create_retriever
from src.llm import load_llm
from src.memory import ConversationMemory
from src.rag_pipeline import (
    search_documents,
    generate_answer,
)


def main():

    print("=" * 60)
    print("🤖 MULTI DOCUMENT RAG CHATBOT")
    print("=" * 60)

    # ======================================
    # Load Embedding Model
    # ======================================

    embedding_model = get_embedding_model()

    # ======================================
    # Load Existing Vector Database
    # ======================================

    vector_store = load_vector_store(embedding_model)

    # ======================================
    # Create Retriever
    # ======================================

    retriever = create_retriever(vector_store)

    # ======================================
    # Connect Gemini
    # ======================================

    client = load_llm()

    # ======================================
    # Conversation Memory
    # ======================================

    memory = ConversationMemory()

    print("\n" + "=" * 60)
    print("💬 CHAT STARTED")
    print("=" * 60)
    print("Type 'exit' to quit.")
    print("Type 'clear' to clear conversation memory.\n")

    while True:

        question = input("👤 You: ")

        if question.lower() in ["exit", "quit", "bye"]:
            print("\n👋 Thank you for using the chatbot!")
            break

        if question.lower() == "clear":
            memory.clear()
            print("🗑 Conversation memory cleared.\n")
            continue

        if question.strip() == "":
            print("⚠ Please enter a valid question.\n")
            continue

        # Retrieve relevant documents
        documents = search_documents(
            retriever,
            question
        )

        # Generate answer
        answer = generate_answer(
            client,
            documents,
            question,
            memory
        )

        # Save conversation
        memory.add("User", question)
        memory.add("Assistant", answer)

        print("\n🤖 AI:\n")
        print(answer)

        print("\n" + "-" * 70 + "\n")


if __name__ == "__main__":
    main()