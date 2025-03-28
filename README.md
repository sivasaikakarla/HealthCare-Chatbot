Project Overview:
 - This is an AI Healthcare Assistant is a chatbot designed to provide quick and accurate responses to healthcare-related queries. It retrieves information from a structured knowledge base and enhances answers using a llm.


Tech Stack Used:

  - Streamlit: Used to create an interactive and user-friendly chatbot interface with minimal development effort.
  
  - FAISS: Implements fast and efficient vector search for retrieving relevant answers from the knowledge base.
  
  - SentenceTransformers: Converts user queries into embeddings, enabling semantic search for accurate responses.
  
  - Redis: Stores conversation history to maintain session context and improve user experience.
  
  - Hugging Face API: Used as a fallback mechanism for generating responses when the chatbot does not find relevant answers in the knowledge base.
 

How to Run:
  - python -m streamlit run frontend/app.py    (frontend)
  - uvicorn backend.chatbot:app --reload  (backend)


