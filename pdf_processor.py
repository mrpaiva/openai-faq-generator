from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

def process_pdfs(source_directory):
    pdf_files = [os.path.join(source_directory, f) for f in os.listdir(source_directory) if f.endswith(".pdf")]
    loader = PyPDFLoader(pdf_files[0])
    documents = loader.load_and_split()

    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    vectorstore = FAISS.from_documents(documents, embeddings)

    retriever = vectorstore.as_retriever()

    return retriever
