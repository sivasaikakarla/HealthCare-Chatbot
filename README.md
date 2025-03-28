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

Prompt Engineering Approach:
  - Rephrasing & Clarification: LLM refines retrieved responses for better understanding.
  - Short & Relevant Responses: Ensures concise answers when needed.

Limitations & Future Improvements:
  - Relying on API
  - Limited knowledge base

Future Enhancements:
  - Using pinecone for larger knowledge base
  - Realtime Deployment

Sample Input & Output:
  - User Query:
     "What are the symptoms of diabetes?"

  - Chatbot Response:
    "The symptoms of diabetes include excessive thirst, frequent urination, sudden weight loss, and fatigue."

Demo:
ScreenShot - (https://drive.google.com/file/d/1ssiR-74A6DqN6VpTNRvemMEaoDDQDKmL/view?usp=drive_link)
  

