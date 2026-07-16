import os

from langchain_community.document_loaders import PyPDFLoader

from src.config import DATA_FOLDER


def load_documents():
    """
    Load all PDF documents from the data folder.
    """

    print("\n" + "=" * 60)
    print("📄 DOCUMENT LOADER")
    print("=" * 60)

    documents = []

    pdf_files = [
        file
        for file in os.listdir(DATA_FOLDER)
        if file.endswith(".pdf")
    ]

    if len(pdf_files) == 0:
        print("❌ No PDF files found.")
        return []

    for pdf in pdf_files:

        pdf_path = os.path.join(DATA_FOLDER, pdf)

        print(f"📖 Loading: {pdf}")

        loader = PyPDFLoader(pdf_path)

        docs = loader.load()

        documents.extend(docs)

    print("\n✅ Document Loading Completed!")

    print(f"📚 Total Pages Loaded : {len(documents)}")

    return documents