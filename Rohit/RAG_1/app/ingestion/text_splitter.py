"""
Text Splitter
Splits documents into chunks for embedding
"""

from typing import List
from unittest.mock import Mock

# Gracefully handle missing langchain
try:
    from langchain_core.documents import Document
except ModuleNotFoundError:
    class Document(Mock):
        def __init__(self, page_content: str = "", metadata: dict = None, **kwargs):
            super().__init__()
            self.page_content = page_content
            self.metadata = metadata or {}

try:
    from langchain_text_splitters import RecursiveCharacterTextSplitter
except ModuleNotFoundError:
    # Fallback mock for when langchain_text_splitters is not installed
    class RecursiveCharacterTextSplitter:
        """Fallback text splitter implementation"""
        def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 20, separators: list = None, **kwargs):
            self.chunk_size = chunk_size
            self.chunk_overlap = chunk_overlap
            self.separators = separators or ["\n\n", "\n", " ", ""]
        
        def split_text(self, text: str) -> List[str]:
            """Simple text splitting fallback"""
            if not text:
                return []
            # Simple splitting by chunk_size
            chunks = []
            for i in range(0, len(text), self.chunk_size):
                chunks.append(text[i:i + self.chunk_size])
            return chunks
        
        def split_documents(self, documents: List[Document]) -> List[Document]:
            """Simple document splitting fallback"""
            if not documents:
                return []
            split_docs = []
            for doc in documents:
                text_chunks = self.split_text(doc.page_content)
                for chunk in text_chunks:
                    split_docs.append(Document(page_content=chunk, metadata=doc.metadata))
            return split_docs

from app.utils.logger import get_logger
from app.config.settings import Config

logger = get_logger(__name__)


class TextSplitterService:
    """Service to split documents into chunks"""
    
    def __init__(
        self,
        chunk_size: int = None,
        chunk_overlap: int = None
    ):
        self.chunk_size = chunk_size or Config.CHUNK_SIZE
        self.chunk_overlap = chunk_overlap or Config.CHUNK_OVERLAP
        
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            separators=["\n\n", "\n", " ", ""]
        )
        
        logger.info(
            f"Initialized TextSplitter: chunk_size={self.chunk_size}, "
            f"chunk_overlap={self.chunk_overlap}"
        )
    
    def split_documents(self, documents: List[Document]) -> List[Document]:
        """Split documents into chunks"""
        if not documents:
            logger.warning("No documents to split")
            return []
        
        logger.info(f"Splitting {len(documents)} documents...")
        split_docs = self.splitter.split_documents(documents)
        
        logger.info(f"Split into {len(split_docs)} chunks")
        return split_docs
    
    def split_text(self, text: str) -> List[str]:
        """Split raw text into chunks"""
        chunks = self.splitter.split_text(text)
        logger.info(f"Split text into {len(chunks)} chunks")
        return chunks
