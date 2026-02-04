from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_documents(file_path: str):
    """Load documents from a text file."""
    loader = TextLoader(file_path)
    documents = loader.load()
    return documents


def split_documents(documents, chunk_size: int = 500, chunk_overlap: int = 50):
    """Split documents into chunks for embedding."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    docs = splitter.split_documents(documents)
    return docs
