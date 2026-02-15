# Streamlit-Interface-For-A-Locally-Installed-LLM

# 💬 Local LLM Chat App (TinyLlama)

A local AI chat interface built with Streamlit that connects to a TinyLlama model via Ollama. Ask questions, get AI-generated responses, and maintain a conversation—all offline on your computer.

## 🚀 Features
- Local LLM execution (offline)  
- Interactive chat UI with user and AI messages  
- Conversation history for coherent conversations  
- Reset conversation button to clear history  
- Structured prompt engineering for clear responses  

## 🖼 Screenshot
<img width="1902" height="900" alt="Screenshot 2026-02-15 215908" src="https://github.com/user-attachments/assets/65bc68ab-1137-4c08-a0c8-529673ced6d6" />
<img width="1900" height="883" alt="6" src="https://github.com/user-attachments/assets/c86ef901-9535-465c-8755-b63cbeab5440" />


## 🛠 Tools & Technologies
| Tool / Library      | Purpose |
|--------------------|---------|
| Streamlit           | Build interactive web app UI |
| Ollama              | Host TinyLlama and provide local API |
| Python Requests     | Send queries from Streamlit to Ollama API |
| Python 3.10+        | Supports session state and modern Streamlit features |
| Session State       | Stores conversation history for context persistence |
| Text Prompts        | Guide TinyLlama to generate human-like responses |

## ⚙️ How It Works
1. User types a query in the text input box  
2. App formats the prompt with:  
   - Last few messages (conversation history)  
   - New user query  
   - Instructions to answer clearly and concisely  
3. Sends the prompt to TinyLlama via the Ollama local API (`http://localhost:11434/api/generate`)  
4. TinyLlama generates a response  
5. Response is displayed and stored in `st.session_state.chat_history`  
6. Reset button clears conversation to start fresh  

## 💡 Benefits of TinyLlama
- Lightweight and fast (637 MB)  
- Fully offline operation  
- Ideal for private AI assistants, research, brainstorming, and coding help  
- Supports structured prompts for better answers  

## 🖥 Getting Started


1)Install dependencies:

pip install streamlit requests

2)Make sure TinyLlama is installed in Ollama:

ollama list
You should see tinyllama:latest

3)Run the Streamlit app:

streamlit run app.py

Open the URL provided by Streamlit (usually http://localhost:8501) and start chatting!
