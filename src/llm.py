from google import genai

from src.config import (
    GEMINI_API_KEY,
    GEMINI_MODEL,
)


def load_llm():
    """
    Load Gemini LLM.
    """

    print("\n" + "=" * 60)
    print("🤖 GEMINI LLM")
    print("=" * 60)

    client = genai.Client(
        api_key=GEMINI_API_KEY
    )

    print("✅ Gemini Connected Successfully!")

    return client