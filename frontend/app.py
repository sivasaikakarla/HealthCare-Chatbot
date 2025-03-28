import requests
import streamlit as st


st.set_page_config(page_title="AI Healthcare Assistant", layout="centered")

st.markdown(
    """
    <style>
    .chat-container {
        max-width: 700px;
        margin: auto;
        display: flex;
        flex-direction: column;
    }
    .chat-bubble {
        padding: 10px 15px;
        border-radius: 10px;
        margin-bottom: 10px;
        max-width: 70%;
        word-wrap: break-word;
        color: black;
    }
    .user-bubble {
        background-color: #dcf8c6;
        align-self: flex-end;
        text-align: right;
        color: black;
    }
    .ai-bubble {
        background-color: #e5e5ea;
        align-self: flex-start;
        color: black;
    }
    .chatbox {
        color: black;
        position: fixed;
        bottom: 10px;
        width: 100%;
        max-width: 700px;
        left: 50%;
        transform: translateX(-50%);
        display: flex;
        gap: 10px;
        padding: 10px;
        background: white;
    }
    .chatbox input {
        flex: 1;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 20px;
        outline: none;
    }
    .chatbox button {
        padding: 10px 15px;
        border: none;
        background-color: #25d366;
        color: white;
        font-weight: bold;
        border-radius: 20px;
        cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("🤖 AI Healthcare Assistant")

st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for message in st.session_state.chat_history:
    if message.startswith("You:"):
        st.markdown(f'<div class="chat-bubble user-bubble">{message}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-bubble ai-bubble">{message}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


query = st.text_input("Type your question...", key="chat_input", label_visibility="collapsed")


if st.button("Send"):
    if query:
        user_id = "user123"
        response = requests.get(f"http://127.0.0.1:8000/chat?user_id={user_id}&query={query}")
        data = response.json()

        st.session_state.chat_history.append(f"You: {query}")
        st.session_state.chat_history.append(f"AI: {data['answer']}")

        st.rerun()


if st.button("Clear Chat"):
    st.session_state.chat_history = []
    st.rerun()
