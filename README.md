# ChatWithDocs - Document Q&A Bot using Groq + LangChain (RAG Chain)

**ChatWithDocs** is a simple document question-answering chatbot that uses:
- **LangChain** for RAG (Retrieval-Augmented Generation)
- **Groq LLMs** for fast inference
- **Hugging Face embeddings**
- **Chroma** as a vector database
- **Streamlit UI** for an interactive chat interface

You can upload any `.pdf` or `.txt` file and ask natural language questions about it.

---

## 🚀 Features
- ✅ Load PDF or TXT documents  
- ✅ Chunk and embed with Hugging Face model  
- ✅ Store and retrieve context using Chroma  
- ✅ Query using Groq LLM (Llama-3.1-8B-Instant)   
- ✅ UI for an interactive chatting experience.

---

## 🧩 Prerequisites

Make sure you have:

- **Python 3.10+**
- A **Groq API key** → get it from [https://console.groq.com/keys](https://console.groq.com/keys)
- The PDF or text file you want to query (e.g., `AI.pdf`)

---

## 🛠️ Installation

1. **Clone or create your project folder:**
   ```bash
   mkdir ChatWithDocs
   cd ChatWithDocs
