from rag.retriever import retrieve

def answer(question):

    docs = retrieve(question)

    return {
        "persona": "technical expert",
        "response": str(docs)
    }