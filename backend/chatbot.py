import faiss
import json
import redis
import requests
import numpy as np
from fastapi import FastAPI
from sentence_transformers import SentenceTransformer
from collections import Counter



app = FastAPI()


index = faiss.read_index("knowledge_base.index")


with open("backend/knowledge_base.json", "r") as f:
    knowledge_base = json.load(f)


model = SentenceTransformer("all-MiniLM-L6-v2")


redis_client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

question_logs = Counter()


HF_API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
HEADERS = {"Authorization": "Bearer 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"}



def enhance_answer_with_llm(user_id, question, retrieved_answer):

    last_question = redis_client.get(f"user:{user_id}:last_question")
    last_answer = redis_client.get(f"user:{user_id}:last_answer")

    context_prompt = (
        f"Previous Question: {last_question}\nPrevious Answer: {last_answer}\n\n"
        if last_question and last_answer else ""
    )

    prompt = f"{last_question}User Question: {question}\nKnowledge Base Answer: {retrieved_answer}\nCan you expand, clarify, and give answer shortly if asked.keep it consistent with the previous question"

    payload = {"inputs": prompt, "parameters": {"max_length": 200}}

    response = requests.post(HF_API_URL, headers=HEADERS, json=payload)

    print("Raw API Response:", response.text)

    if response.status_code == 200:
        json_response = response.json()
        if isinstance(json_response, list) and "generated_text" in json_response[0]:
            return json_response[0]["generated_text"]
        else:
            print("Unexpected response format:", json_response)
            return retrieved_answer
    else:
        print("Hugging Face API Error:", response.status_code, response.text)
        return retrieved_answer  



@app.get("/chat")
def chat(user_id: str, query: str):
    question_logs[query] += 1  


    query_vector = np.array([model.encode(query)], dtype="float32")


    _, idx = index.search(query_vector, 1)
    retrieved_answer = knowledge_base[idx[0][0]]["answer"]


    enhanced_answer = enhance_answer_with_llm(user_id, query, retrieved_answer)


    redis_client.rpush(f"user:{user_id}:history", f"User: {query}")
    redis_client.rpush(f"user:{user_id}:history", f"AI: {enhanced_answer}")


    chat_history = redis_client.lrange(f"user:{user_id}:history", 0, -1)

    return {
        "answer": enhanced_answer,
        "chat_history": chat_history
    }
