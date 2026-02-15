import streamlit as st
import requests

# -----------------------------
# Configuration
# -----------------------------
OLLAMA_URL = "http://localhost:11434/api/generate"  # Ollama local API
MODEL_NAME = "tinyllama"  # change to your installed model name

# -----------------------------
# Helper function to query Ollama
# -----------------------------
def query_ollama(prompt):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_URL, json=payload)
        if response.status_code == 200:
            return response.json().get("response", "No response from LLM.")
        else:
            return f"Error {response.status_code}: Unable to connect to LLM."
    except Exception as e:
        return f"Error: {str(e)}"

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Local LLM Chat (Ollama)", layout="wide")
st.title("💬 Local LLM Chat Interface")

# Initialize session state for conversation history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar controls
with st.sidebar:
    st.header("Controls")
    if st.button("🔄 Reset Conversation"):
        st.session_state.chat_history = []
        st.experimental_rerun()

# Main chat input
user_input = st.text_input("Enter your query:", placeholder="Ask something...")

if st.button("Send") and user_input.strip():
    with st.spinner("Generating response..."):
        response = query_ollama(user_input)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("LLM", response))

# Display conversation history
st.subheader("Conversation History")
for role, message in st.session_state.chat_history:
    if role == "You":
        st.markdown(f"**🧑 {role}:** {message}")
    else:
        st.markdown(f"**🤖 {role}:** {message}")
