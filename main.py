import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from sentence_transformers import SentenceTransformer
from langchain_core.runnables import RunnablePassthrough

from langchain_groq import ChatGroq


load_dotenv()

file_path = "AI.pdf"  # or .txt

# Load
if file_path.endswith(".pdf"):
    loader = PyPDFLoader(file_path)
else:
    loader = TextLoader(file_path)

docs = loader.load()

# Split into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_documents(docs)

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="chroma_db"
)
retriever = vectorstore.as_retriever()
llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.1-8b-instant"  
)
# Prompt template for structured reasoning
template = """
You are an intelligent assistant for answering questions from documents.
Use the provided context to answer the question clearly.
If the answer is not in the context, say "I'm not sure based on the document."

Context:
{context}

Question:
{question}
"""

prompt = ChatPromptTemplate.from_template(template)

# Define RAG chain explicitly
rag_chain = (
    {
        "context": retriever | (lambda docs: "\n\n".join([d.page_content for d in docs])),
        "question": RunnablePassthrough(),
    }
    | prompt
    | llm
)
if __name__ == "__main__":
   while True:
     query = input("\nAsk about the document (or type 'exit'): ")
     if query.lower() == "exit":
        break
     response = rag_chain.invoke(query)
     print("\n🤖 Answer:", response)
