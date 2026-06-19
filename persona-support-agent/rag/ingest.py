from pathlib import Path

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

documents = []

files = [
    "data/faq.txt",
    "data/refund_policy.txt",
    "data/shipping_policy.txt",
    "data/api_authentication.txt",
    "data/password_reset.txt",
    "data/account_locked.txt",
    "data/billing_issue.txt",
    "data/subscription_management.txt",
    "data/login_troubleshooting.txt",
    "data/service_outage.txt"
]

for file in files:
    text = Path(file).read_text(encoding="utf-8")

    documents.append(
        Document(
            page_content=text,
            metadata={"source": file}
        )
    )

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectordb = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="db"
)

print("Documents Indexed Successfully")