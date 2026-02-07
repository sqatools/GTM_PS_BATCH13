"""
FAISS Vector Store
In-memory vector store for semantic search
"""

import os
from typing import List
from unittest.mock import Mock

# Gracefully handle missing langchain imports
try:
    from langchain_core.documents import Document
except ModuleNotFoundError:
    class Document(Mock):
        def __init__(self, page_content: str = "", metadata: dict = None, **kwargs):
            super().__init__()
            self.page_content = page_content
            self.metadata = metadata or {}

try:
    from langchain_community.vectorstores import FAISS
except ModuleNotFoundError:
    FAISS = Mock

try:
    from langchain_openai import OpenAIEmbeddings
except ModuleNotFoundError:
    OpenAIEmbeddings = Mock

from app.utils.logger import get_logger
from app.config.settings import Config

logger = get_logger(__name__)


class FAISSStore:
    """FAISS vector store wrapper"""
    
    def __init__(self, persist_path: str = None):
        self.persist_path = persist_path or Config.VECTORSTORE_PATH
        self.vectorstore = None
        self.embeddings = OpenAIEmbeddings(
            model=Config.EMBEDDING_MODEL,
            openai_api_key=Config.OPENAI_API_KEY
        )
        logger.info(f"Initialized FAISSStore with path: {self.persist_path}")
    
    def create_from_documents(self, documents: List[Document]) -> None:
        """Create vector store from documents"""
        if not documents:
            logger.error("Cannot create vectorstore from empty documents list")
            raise ValueError("Documents list is empty")
        
        try:
            logger.info(f"Creating FAISS vectorstore from {len(documents)} documents...")
            self.vectorstore = FAISS.from_documents(documents, self.embeddings)
            logger.info("FAISS vectorstore created successfully")
        except Exception as e:
            logger.error(f"Error creating vectorstore: {str(e)}")
            raise
    
    def add_documents(self, documents: List[Document]) -> None:
        """Add documents to existing vectorstore"""
        if not self.vectorstore:
            logger.error("Vectorstore not initialized. Call create_from_documents first.")
            raise ValueError("Vectorstore not initialized")
        
        try:
            logger.info(f"Adding {len(documents)} documents to vectorstore...")
            self.vectorstore.add_documents(documents)
            logger.info("Documents added successfully")
        except Exception as e:
            logger.error(f"Error adding documents: {str(e)}")
            raise
    
    def save_local(self) -> None:
        """Save vectorstore to disk"""
        if not self.vectorstore:
            logger.error("Vectorstore not initialized. Cannot save.")
            raise ValueError("Vectorstore not initialized")
        
        try:
            os.makedirs(self.persist_path, exist_ok=True)
            self.vectorstore.save_local(self.persist_path)
            logger.info(f"Vectorstore saved to {self.persist_path}")
        except Exception as e:
            logger.error(f"Error saving vectorstore: {str(e)}")
            raise
    
    def load_local(self) -> None:
        """Load vectorstore from disk"""
        if not os.path.exists(self.persist_path):
            logger.error(f"Vectorstore path not found: {self.persist_path}")
            raise FileNotFoundError(f"Vectorstore path not found: {self.persist_path}")
        
        try:
            logger.info(f"Loading vectorstore from {self.persist_path}...")
            self.vectorstore = FAISS.load_local(
                self.persist_path,
                self.embeddings,
                allow_dangerous_deserialization=True
            )
            logger.info("Vectorstore loaded successfully")
        except Exception as e:
            logger.error(f"Error loading vectorstore: {str(e)}")
            raise
    
    def get_vectorstore(self) -> FAISS:
        """Get underlying FAISS vectorstore"""
        if not self.vectorstore:
            logger.error("Vectorstore not initialized")
            raise ValueError("Vectorstore not initialized")
        return self.vectorstore
    
    def similarity_search(
        self,
        query: str,
        k: int = None
    ) -> List[Document]:
        """Search for similar documents"""
        if not self.vectorstore:
            logger.error("Vectorstore not initialized")
            raise ValueError("Vectorstore not initialized")
        
        k = k or Config.RETRIEVAL_K
        
        try:
            logger.debug(f"Similarity search for query with k={k}")
            results = self.vectorstore.similarity_search(query, k=k)
            logger.debug(f"Found {len(results)} similar documents")
            return results
        except Exception as e:
            logger.error(f"Error in similarity search: {str(e)}")
            raise
