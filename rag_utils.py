from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def embed_pdf_to_faiss(pdf_path: str, index_path: str):
    loader = PyMuPDFLoader(pdf_path)
    pages = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_documents(pages)
    vectorstore = FAISS.from_documents(docs, embedding_model)
    vectorstore.save_local(index_path)

def load_vectorstore(index_path: str):
    return FAISS.load_local(index_path, embedding_model, allow_dangerous_deserialization=True)

def query_stg(query: str, index_path: str):
    db = load_vectorstore(index_path)
    results = db.similarity_search(query, k=3)
    return "\n".join([doc.page_content for doc in results])