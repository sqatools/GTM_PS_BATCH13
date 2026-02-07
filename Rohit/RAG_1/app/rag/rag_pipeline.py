"""
RAG Pipeline
Main orchestration of document retrieval and generation
"""

from typing import List, Dict, Optional
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

from app.ingestion.document_loader import DocumentLoader
from app.ingestion.text_splitter import TextSplitterService
from app.ingestion.embeddings import EmbeddingsService
from app.vectorstore.faiss_store import FAISSStore
from app.vectorstore.retriever import RetrieverService
from app.llm.llm_client import LLMClient
from app.llm.prompt_template import PromptTemplate
from app.utils.logger import get_logger
from app.config.settings import Config

logger = get_logger(__name__)


class RAGPipeline:
    """Complete RAG pipeline"""
    
    def __init__(
        self,
        data_path: str = None,
        vectorstore_path: str = None,
        load_existing: bool = False
    ):
        self.data_path = data_path or Config.DATA_RAW_PATH
        self.vectorstore_path = vectorstore_path or Config.VECTORSTORE_PATH
        
        # Initialize components
        self.document_loader = DocumentLoader(self.data_path)
        self.text_splitter = TextSplitterService()
        self.embeddings_service = EmbeddingsService()
        self.vectorstore = FAISSStore(self.vectorstore_path)
        self.retriever = RetrieverService(self.vectorstore)
        self.llm = LLMClient()
        self.prompt_template = PromptTemplate()
        
        # Try to load existing vectorstore
        if load_existing:
            try:
                self.vectorstore.load_local()
                logger.info("Loaded existing vectorstore")
            except Exception as e:
                logger.warning(f"Could not load existing vectorstore: {str(e)}")
        
        logger.info("Initialized RAGPipeline")
    
    def ingest_documents(self) -> None:
        """Load, split, and store documents"""
        try:
            logger.info("Starting document ingestion...")
            
            # 1. Load documents
            logger.info("Step 1: Loading documents...")
            documents = self.document_loader.load_documents()
            if not documents:
                logger.error("No documents loaded")
                raise ValueError("No documents found in data path")
            
            logger.info(f"Loaded {len(documents)} documents")
            
            # 2. Split documents
            logger.info("Step 2: Splitting documents...")
            split_docs = self.text_splitter.split_documents(documents)
            logger.info(f"Split into {len(split_docs)} chunks")
            
            # 3. Create vectorstore
            logger.info("Step 3: Creating vectorstore...")
            self.vectorstore.create_from_documents(split_docs)
            
            # 4. Save vectorstore
            logger.info("Step 4: Saving vectorstore...")
            self.vectorstore.save_local()
            
            logger.info("Document ingestion completed successfully")
        
        except Exception as e:
            logger.error(f"Error during document ingestion: {str(e)}")
            raise
    
    def query(
        self,
        question: str,
        k: int = None
    ) -> Dict[str, any]:
        """Query the RAG system"""
        try:
            k = k or Config.RETRIEVAL_K
            logger.info(f"Processing query: {question[:100]}...")
            
            # 1. Retrieve relevant documents
            logger.debug("Retrieving relevant documents...")
            retrieved_docs = self.retriever.retrieve(question, k=k)
            
            # 2. Create context from retrieved documents
            logger.debug("Creating context from retrieved documents...")
            context = self.retriever.get_context_string(retrieved_docs)
            
            # 3. Create prompt
            logger.debug("Creating prompt...")
            prompt = self.prompt_template.create_rag_prompt(context, question)
            
            # 4. Generate answer
            logger.debug("Generating answer using LLM...")
            answer = self.llm.generate_answer(prompt)
            
            logger.info(f"Generated answer of length: {len(answer)}")
            
            # 5. Return result
            result = {
                "question": question,
                "answer": answer,
                "retrieved_docs": retrieved_docs,
                "context": context,
                "num_docs_retrieved": len(retrieved_docs)
            }
            
            return result
        
        except Exception as e:
            logger.error(f"Error processing query: {str(e)}")
            raise
    
    def batch_query(
        self,
        questions: List[str],
        k: int = None
    ) -> List[Dict]:
        """Process multiple queries"""
        try:
            logger.info(f"Processing batch of {len(questions)} queries...")
            results = []
            
            for i, question in enumerate(questions, 1):
                logger.info(f"Processing query {i}/{len(questions)}")
                result = self.query(question, k=k)
                results.append(result)
            
            logger.info(f"Batch processing completed: {len(results)} results")
            return results
        
        except Exception as e:
            logger.error(f"Error processing batch queries: {str(e)}")
            raise
    
    def test_connection(self) -> bool:
        """Test all components"""
        try:
            logger.info("Testing RAG pipeline components...")
            
            # Test LLM
            logger.info("Testing LLM connection...")
            llm_ok = self.llm.test_connection()
            
            # Test vectorstore
            logger.info("Testing vectorstore...")
            vectorstore_ok = self.vectorstore.vectorstore is not None
            
            if llm_ok and vectorstore_ok:
                logger.info("All components working correctly")
                return True
            else:
                logger.warning("Some components not working")
                return False
        
        except Exception as e:
            logger.error(f"Error testing components: {str(e)}")
            return False
