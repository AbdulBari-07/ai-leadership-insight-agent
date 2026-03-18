import faiss
import numpy as np

class VectorStore:
    def __init__(self, embeddings):
        self.index = faiss.IndexFlatL2(len(embeddings[0]))
        self.index.add(np.array(embeddings))

    def search(self, query_embeddings, k=4):
        distances, indices = self.index.search(np.array([query_embeddings]), k)
        return indices[0]