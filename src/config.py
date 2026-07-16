"""
Project Configuration
Multi-Document RAG Chatbot
"""

import os
from dotenv import load_dotenv

load_dotenv()

# ==========================================
# GEMINI CONFIGURATION
# ==========================================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

GEMINI_MODEL = "gemini-2.5-flash"

# ==========================================
# DATA CONFIGURATION
# ==========================================

DATA_FOLDER = "data"

# ==========================================
# TEXT SPLITTER
# ==========================================

CHUNK_SIZE = 1000

CHUNK_OVERLAP = 200

# ==========================================
# EMBEDDING MODEL
# ==========================================

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ==========================================
# VECTOR DATABASE
# ==========================================

VECTOR_DB_PATH = "vectorstore"

# ==========================================
# RETRIEVER
# ==========================================

TOP_K_RESULTS = 4

# ==========================================
# MEMORY
# ==========================================

MAX_HISTORY = 5