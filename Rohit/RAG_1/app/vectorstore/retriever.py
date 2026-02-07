"""
Retriever Service
Retrieves relevant documents for a query
"""

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

from app.vectorstore.faiss_store import FAISSStore
from app.utils.logger import get_logger
from app.config.settings import Config

logger = get_logger(__name__)


class RetrieverService:
    """Service to retrieve relevant documents"""
    
    def __init__(self, vectorstore: FAISSStore = None):
        self.vectorstore = vectorstore or FAISSStore()
        logger.info("Initialized RetrieverService")
    
    def retrieve(self, query: str, k: int = None) -> List[Document]:
        """Retrieve relevant documents for a query"""
        k = k or Config.RETRIEVAL_K
        
        try:
            logger.info(f"Retrieving top {k} documents for query: {query[:100]}...")
            documents = self.vectorstore.similarity_search(query, k=k)
            
            logger.info(f"Retrieved {len(documents)} documents")
            for i, doc in enumerate(documents, 1):
                logger.debug(f"  {i}. {doc.metadata.get('filename', 'unknown')}")
            
            return documents
        except Exception as e:
            logger.error(f"Error retrieving documents: {str(e)}")
            raise
    
    def retrieve_with_scores(
        self,
        query: str,
        k: int = None
    ) -> List[tuple]:
        """Retrieve documents with similarity scores"""
        k = k or Config.RETRIEVAL_K
        
        try:
            logger.info(f"Retrieving documents with scores for query: {query[:100]}...")
            results = self.vectorstore.get_vectorstore().similarity_search_with_scores(query, k=k)
            
            logger.info(f"Retrieved {len(results)} documents with scores")
            return results
        except Exception as e:
            logger.error(f"Error retrieving documents with scores: {str(e)}")
            raise
    
    def get_context_string(self, documents: List[Document]) -> str:
        """Convert retrieved documents to context string"""
        context_parts = []
        for doc in documents:
            context_parts.append(doc.page_content)
        
        context_string = "\n\n---\n\n".join(context_parts)
        logger.debug(f"Generated context string of length: {len(context_string)}")
        return context_string
