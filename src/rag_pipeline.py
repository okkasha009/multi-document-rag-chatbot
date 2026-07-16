from src.config import GEMINI_MODEL


def search_documents(retriever, query):
    """
    Retrieve relevant document chunks.
    """

    print("\n" + "=" * 60)
    print("🔎 SEMANTIC SEARCH")
    print("=" * 60)

    documents = retriever.invoke(query)

    print(f"📚 Retrieved Chunks : {len(documents)}")

    return documents


def generate_answer(client, documents, question, memory):
    """
    Generate an answer using Gemini with conversation memory.
    """

    print("\n" + "=" * 60)
    print("🤖 GENERATING ANSWER")
    print("=" * 60)

    context = ""

    source_pages = []

    for doc in documents:

        context += doc.page_content + "\n\n"

        page = doc.metadata.get("page")

        if page is not None:
            source_pages.append(page + 1)

    conversation = memory.get_context()

    prompt = f"""
You are an expert AI Research Assistant.

Your job is to answer questions ONLY from the provided document context.

Rules:
1. Never make up information.
2. If the answer is not available in the document, reply:
   "I couldn't find this information in the uploaded document."
3. Answer in professional, easy-to-understand English.
4. Use bullet points whenever appropriate.
5. If possible, give short examples.
6. If the user asks a follow-up question, use the previous conversation.
7. Keep answers concise but complete.

==========================
Previous Conversation
==========================

{conversation}

==========================
Retrieved Context
==========================

{context}

==========================
User Question
==========================

{question}

==========================
Answer
==========================
"""

    try:
     response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt
    )

     return response.text, sorted(set(source_pages))

    except Exception as e:

     return (
        f"An error occurred while generating the answer:\n{e}",
        []
    )