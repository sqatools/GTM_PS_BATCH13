from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings


def create_vectorstore(docs):
    """Create a FAISS vector store from documents."""
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore


def get_retriever(vectorstore, k: int = 3):
    """Get a retriever from the vector store."""
    retriever = vectorstore.as_retriever(search_kwargs={"k": k})
    return retriever
