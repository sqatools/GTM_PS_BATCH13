"""
Embeddings Service
Generates embeddings for document chunks
"""

from typing import List
from unittest.mock import Mock

# Gracefully handle missing langchain_openai
try:
    from langchain_openai import OpenAIEmbeddings
except ModuleNotFoundError:
    # Mock for when dependencies are not installed
    OpenAIEmbeddings = Mock

from app.utils.logger import get_logger
from app.config.settings import Config

logger = get_logger(__name__)


class EmbeddingsService:
    """Service to generate embeddings"""
    
    def __init__(self, model: str = None):
        self.model = model or Config.EMBEDDING_MODEL
        
        try:
            self.embeddings = OpenAIEmbeddings(
                model=self.model,
                openai_api_key=Config.OPENAI_API_KEY
            )
            logger.info(f"Initialized EmbeddingsService with model: {self.model}")
        except Exception as e:
            logger.error(f"Error initializing embeddings: {str(e)}")
            raise
    
    def embed_text(self, text: str) -> List[float]:
        """Generate embedding for a single text"""
        try:
            embedding = self.embeddings.embed_query(text)
            logger.debug(f"Generated embedding of dimension: {len(embedding)}")
            return embedding
        except Exception as e:
            logger.error(f"Error embedding text: {str(e)}")
            raise
    
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for multiple texts"""
        try:
            embeddings = self.embeddings.embed_documents(texts)
            logger.info(f"Generated {len(embeddings)} embeddings")
            return embeddings
        except Exception as e:
            logger.error(f"Error embedding documents: {str(e)}")
            raise
