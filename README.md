Project Overview
The AI Healthcare Assistant is a chatbot designed to provide quick and accurate responses to healthcare-related queries. It retrieves information from a structured knowledge base and enhances answers using a language model when necessary. The chatbot is built with efficiency, scalability, and ease of deployment in mind, ensuring users receive reliable healthcare information.

Technologies Used and Justification
This project utilizes a combination of modern technologies for optimal performance and scalability.

Python: Used as the primary programming language due to its extensive libraries for machine learning, NLP, and API development.

FastAPI: Chosen for building the backend API because of its speed, asynchronous capabilities, and easy integration with machine learning models.

Streamlit: Used to create an interactive and user-friendly chatbot interface with minimal development effort.

FAISS: Implements fast and efficient vector search for retrieving relevant answers from the knowledge base.

SentenceTransformers: Converts user queries into embeddings, enabling semantic search for accurate responses.

Redis: Stores conversation history to maintain session context and improve user experience.

Docker: Ensures smooth deployment and consistency across different environments by containerizing the application.

Hugging Face API: Used as a fallback mechanism for generating responses when the chatbot does not find relevant answers in the knowledge base.

GitHub: Provides version control and collaboration tools for managing the project efficiently.

Setup Instructions
The project can be set up and launched easily, either manually or using Docker for streamlined deployment.

Clone the repository from GitHub.

Install the required dependencies or use Docker to set up the entire system in a few commands.

Run the backend to handle queries and responses.

Launch the frontend interface for users to interact with the chatbot.

The setup ensures that the chatbot is operational within minutes.

Sample Input & Output
User Query:
"What are the symptoms of diabetes?"

Chatbot Response:
"The symptoms of diabetes include excessive thirst, frequent urination, sudden weight loss, and fatigue."

If the chatbot encounters a query beyond its knowledge base, it utilizes an external LLM to generate an informed response while maintaining the conversation context.

Fallback Mechanism for Out-of-Knowledge Queries
To ensure the chatbot can handle a wide range of queries, a fallback mechanism is implemented. If a query is not found in the knowledge base, an external LLM is used to generate a relevant response. The chatbot also maintains the conversation context, allowing for more coherent and meaningful interactions.

Features & Functionalities
A user-friendly interface inspired by WhatsApp-style chat.

Fast and accurate responses powered by FAISS and SentenceTransformers.

Context-aware responses using Redis for conversation memory.

External LLM support for answering complex or unknown queries.

