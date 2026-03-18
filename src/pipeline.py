from src.ingest import load_documents, chunk_text
from src.embed import get_embeddings, model
from src.retrieve import VectorStore
from src.generate import generate_answer

def run_pipeline(query):
    docs = load_documents("data/sample_docs")

    chunks = []
    sources = []

    for doc in docs:
        for chunk in chunk_text(doc["text"]):
            chunks.append(chunk)
        sources.append(doc["source"])
    
    embeddings = get_embeddings(chunks)
    store = VectorStore(embeddings)
    query_embedding = model.encode([query])[0]
    indices = store.search(query_embedding)

    retrieved_chunks = [chunks[i] for i in indices]
    context = "\n\n".join(retrieved_chunks)

    answer = generate_answer(context, query)

    return answer