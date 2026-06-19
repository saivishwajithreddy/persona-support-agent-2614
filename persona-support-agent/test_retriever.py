from rag.retriever import retrieve

docs = retrieve(
    "How long does shipping take?"
)

for doc in docs:
    print(doc.page_content)