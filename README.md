# 🤖 Multi-Document RAG Chatbot

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-Latest-success)
![Gemini](https://img.shields.io/badge/LLM-Gemini%202.5%20Flash-orange)
![ChromaDB](https://img.shields.io/badge/Vector%20Database-ChromaDB-red)
![HuggingFace](https://img.shields.io/badge/Embeddings-HuggingFace-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

</p>

A **production-inspired Retrieval-Augmented Generation (RAG) chatbot** that enables users to interact with PDF documents using natural language. The application combines **Google Gemini 2.5 Flash**, **LangChain**, **HuggingFace Sentence Transformers**, and **ChromaDB** to retrieve relevant document context and generate accurate, grounded responses.

This project was built as a **personal AI engineering project** to explore modern LLM application development, semantic search, vector databases, and Retrieval-Augmented Generation (RAG) pipelines.

---

# ✨ Features

- 📄 Load and process PDF documents
- ✂️ Intelligent document chunking
- 🧠 HuggingFace Sentence Transformer embeddings
- 🗄️ ChromaDB vector database
- 🔍 Semantic similarity search
- 🤖 Google Gemini 2.5 Flash integration
- 💬 Interactive command-line chatbot
- 🧠 Conversation memory
- 📚 Source page references
- ⚡ Fast vector database loading
- 🔄 Separate rebuild script for indexing new documents
- 📝 Professional logging system
- 🏗️ Modular and scalable project architecture

---

# 🏛️ System Architecture

```text
                        User
                          │
                          ▼
                   Chat Interface
                     (main.py)
                          │
                          ▼
               Conversation Memory
                          │
                          ▼
                   Semantic Retriever
                          │
                          ▼
                     ChromaDB
                          ▲
                          │
              HuggingFace Embeddings
                          ▲
                          │
                 Text Splitter
                          ▲
                          │
                 Document Loader
                          ▲
                          │
                    PDF Documents
                          │
                          ▼
                 Gemini 2.5 Flash
                          │
                          ▼
                    AI Response
```

---

# 📂 Project Structure

```text
MULTI-DOCUMENT-RAG-CHATBOT
│
├── data/
│   └── documents/
│       └── attention-is-all-you-need.pdf
│
├── logs/
│   └── app.log
│
├── screenshots/
│
├── src/
│   ├── chatbot.py
│   ├── config.py
│   ├── document_loader.py
│   ├── embeddings.py
│   ├── llm.py
│   ├── logger.py
│   ├── memory.py
│   ├── prompts.py
│   ├── rag_pipeline.py
│   ├── retriever.py
│   ├── text_splitter.py
│   ├── utils.py
│   └── vector_store.py
│
├── vectorstore/
├── .env.example
├── .gitignore
├── main.py
├── rebuild.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| LLM | Google Gemini 2.5 Flash |
| Framework | LangChain |
| Embedding Model | HuggingFace Sentence Transformers |
| Vector Database | ChromaDB |
| Document Processing | PyPDF |
| Environment | Python Dotenv |
| Logging | Python Logging Module |

---

# 🚀 Getting Started

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/okkasha009/multi-document-rag-chatbot.git

cd multi-document-rag-chatbot
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Configure Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

You can obtain a free Gemini API key from **Google AI Studio**.

---

## 4️⃣ Add Documents

Place your PDF files inside:

```text
data/documents/
```

---

## 5️⃣ Build the Vector Database

Run the rebuild script whenever new documents are added.

```bash
python rebuild.py
```

---

## 6️⃣ Start the Chatbot

```bash
python main.py
```

---

# 💬 Example

```text
You:
What is Self-Attention?

AI:
Self-attention is a mechanism that enables each token in a sequence to attend to every other token, allowing the model to capture contextual relationships efficiently.

📚 Sources

• Page 3
• Page 5
```

---

# 🔄 Workflow

```text
PDF Documents
      │
      ▼
Document Loader
      │
      ▼
Text Splitter
      │
      ▼
Embedding Generation
      │
      ▼
ChromaDB Vector Store
      │
      ▼
Semantic Retrieval
      │
      ▼
Gemini 2.5 Flash
      │
      ▼
AI Response
```

---

# 📸 Screenshots

### Chat Interface

> Add screenshot here

<img width="827" height="522" alt="image" src="https://github.com/user-attachments/assets/88f93565-6231-496a-8096-e321d4edd39a" />



### Semantic Search

> Add screenshot here

<img width="789" height="474" alt="image" src="https://github.com/user-attachments/assets/8c279ec3-1244-4baf-bc5a-22ea26c47cca" />


### Vector Database Creation

> Add screenshot here

<img width="814" height="425" alt="image" src="https://github.com/user-attachments/assets/15d31e38-983b-46fe-8a57-5ee9f30384f9" />


### Conversation Memory

> Add screenshot here

<img width="914" height="504" alt="image" src="https://github.com/user-attachments/assets/d946ba68-392b-4a67-9b88-26ff606173c8" />


# 📌 Future Improvements

- Streamlit Web Interface
- Multi-document upload support
- Hybrid Search (BM25 + Dense Retrieval)
- FAISS support
- REST API with FastAPI
- Docker deployment
- User authentication
- Conversation export
- Citation highlighting inside answers
- Multi-user chat sessions

---

# 📝 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

## Okkasha Muhammad

Computer Science Graduate

Passionate about Artificial Intelligence, Machine Learning, Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), NLP, and Python-based AI application development.

### Connect with Me

- GitHub: https://github.com/okkasha009
- LinkedIn: https://www.linkedin.com/in/okkasha-m-53a645370

---

## ⭐ If you found this project helpful, consider giving it a star on GitHub!
