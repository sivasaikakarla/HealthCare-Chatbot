import faiss
import json
import numpy as np
from sentence_transformers import SentenceTransformer


with open("backend/knowledge_base.json", "r") as f:
    knowledge_base = json.load(f)

model = SentenceTransformer("all-MiniLM-L6-v2")

vectors = np.array([model.encode(item["question"]) for item in knowledge_base], dtype="float32")

dimension = vectors.shape[1]  
print(f"FAISS Index Dimension: {dimension}")

index = faiss.IndexFlatL2(dimension)
index.add(vectors)

faiss.write_index(index, "knowledge_base.index")
print("✅ FAISS index created and saved!")
