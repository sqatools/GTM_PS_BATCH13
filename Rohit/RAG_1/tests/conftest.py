"""
Pytest Configuration and Fixtures
Shared fixtures for all tests
"""

import pytest
import os
import sys
from unittest.mock import Mock, MagicMock

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Graceful fallback for missing langchain_core
try:
    from langchain_core.documents import Document
except (ModuleNotFoundError, ImportError):
    # Fallback Document class when langchain_core is not installed or not compatible
    class Document:
        def __init__(self, page_content: str = "", metadata: dict = None):
            self.page_content = page_content
            self.metadata = metadata or {}

# Try importing app modules, skip if dependencies missing
try:
    from app.ingestion import DocumentLoader, TextSplitterService, EmbeddingsService
    from app.vectorstore import FAISSStore, RetrieverService
    from app.llm import LLMClient, PromptTemplate
    from app.rag import RAGPipeline
    DEPS_AVAILABLE = True
except ImportError:
    DEPS_AVAILABLE = False
    # Create mock versions
    DocumentLoader = Mock
    TextSplitterService = Mock
    EmbeddingsService = Mock
    FAISSStore = Mock
    RetrieverService = Mock
    LLMClient = Mock
    PromptTemplate = Mock
    RAGPipeline = Mock


# Skipif marker for tests requiring dependencies
requires_deps = pytest.mark.skipif(
    not DEPS_AVAILABLE,
    reason="langchain and dependencies not installed. Run: pip install -r requirements.txt"
)


# ============================================================
# DOCUMENT FIXTURES
# ============================================================

@pytest.fixture
def sample_documents():
    """Sample documents for testing"""
    return [
        Document(
            page_content="Python is a programming language used for web development, data science, and automation. It is known for its simplicity and readability, making it excellent for beginners and experts alike.",
            metadata={"source": "test.txt", "type": "txt"}
        ),
        Document(
            page_content="Machine learning is a subset of artificial intelligence that enables systems to learn from data without being explicitly programmed. It uses algorithms and statistical models to analyze patterns.",
            metadata={"source": "test.txt", "type": "txt"}
        ),
        Document(
            page_content="RAG systems combine retrieval and generation for accurate question answering. They retrieve relevant documents and use them as context to generate informed responses. This approach improves accuracy.",
            metadata={"source": "test.txt", "type": "txt"}
        ),
    ]


@pytest.fixture
def mock_document_loader():
    """Mock document loader"""
    loader = Mock(spec=DocumentLoader)
    loader.load_documents.return_value = [
        Document(page_content="Test document 1", metadata={"source": "test.txt"}),
        Document(page_content="Test document 2", metadata={"source": "test.txt"}),
    ]
    return loader


# ============================================================
# EMBEDDINGS FIXTURES
# ============================================================

@pytest.fixture
def mock_embeddings_service():
    """Mock embeddings service for testing without API key"""
    embeddings = MagicMock()
    embeddings.model = "text-embedding-3-small"
    embeddings.embed_text.return_value = [0.1, 0.2, 0.3, 0.4, 0.5] * 256  # 1280-dim embedding
    embeddings.embed_documents.return_value = [
        [0.1, 0.2, 0.3] * 427,  # Mock embeddings
        [0.2, 0.3, 0.4] * 427,
        [0.3, 0.4, 0.5] * 427,
    ]
    return embeddings


# ============================================================
# TEXT SPLITTER FIXTURES
# ============================================================

@pytest.fixture
def text_splitter_service():
    """Text splitter service instance"""
    return TextSplitterService(chunk_size=100, chunk_overlap=10)


@pytest.fixture
def split_documents(text_splitter_service, sample_documents):
    """Split sample documents"""
    return text_splitter_service.split_documents(sample_documents)


# ============================================================
# LLM FIXTURES
# ============================================================

@pytest.fixture
def mock_llm_client():
    """Mock LLM client"""
    llm = Mock(spec=LLMClient)
    llm.generate_answer.return_value = "This is a test answer based on the provided context."
    llm.test_connection.return_value = True
    return llm


@pytest.fixture
def llm_client():
    """Real LLM client instance (uses API key from .env)"""
    # Skip if API key not available
    if not os.getenv("OPENAI_API_KEY"):
        pytest.skip("OPENAI_API_KEY not set")
    
    try:
        return LLMClient()
    except Exception:
        pytest.skip("Could not initialize LLM client")


# ============================================================
# RETRIEVER FIXTURES
# ============================================================

@pytest.fixture
def mock_retriever_service():
    """Mock retriever service"""
    def mock_get_context_string(documents):
        """Mock implementation that joins document content"""
        context_parts = []
        for doc in documents:
            context_parts.append(doc.page_content)
        return "\n\n---\n\n".join(context_parts)
    
    retriever = MagicMock()
    retriever.retrieve.return_value = [
        Document(page_content="Relevant document 1", metadata={"source": "test.txt"}),
        Document(page_content="Relevant document 2", metadata={"source": "test.txt"}),
    ]
    retriever.get_context_string.side_effect = mock_get_context_string
    return retriever


# ============================================================
# VECTORSTORE FIXTURES
# ============================================================

@pytest.fixture
def mock_vectorstore():
    """Mock FAISS vectorstore"""
    vs = MagicMock()
    vs.vectorstore = MagicMock()
    vs.similarity_search.return_value = [
        Document(page_content="Result 1", metadata={"source": "test.txt"}),
    ]
    return vs


# ============================================================
# PROMPT TEMPLATE FIXTURES
# ============================================================

@pytest.fixture
def prompt_template():
    """Prompt template instance"""
    return PromptTemplate()


# ============================================================
# PIPELINE FIXTURES
# ============================================================

@pytest.fixture
def mock_rag_pipeline(mock_document_loader, mock_llm_client, mock_retriever_service):
    """Mock RAG pipeline"""
    with pytest.MonkeyPatch.context() as mp:
        pipeline = Mock(spec=RAGPipeline)
        pipeline.query.return_value = {
            "question": "What is RAG?",
            "answer": "RAG combines retrieval and generation.",
            "retrieved_docs": [Document(page_content="RAG info", metadata={})],
            "num_docs_retrieved": 1
        }
        pipeline.ingest_documents.return_value = None
        pipeline.test_connection.return_value = True
        return pipeline


@pytest.fixture
def rag_pipeline():
    """Real RAG pipeline instance (requires OPENAI_API_KEY and data)"""
    if not os.getenv("OPENAI_API_KEY"):
        pytest.skip("OPENAI_API_KEY not set")
    
    try:
        pipeline = RAGPipeline(load_existing=True)
        return pipeline
    except Exception:
        pytest.skip("Could not initialize RAG pipeline")


# ============================================================
# CONFIGURATION FIXTURES
# ============================================================

@pytest.fixture
def test_queries():
    """Test queries for batch processing"""
    return [
        "What is Python used for?",
        "How does machine learning work?",
        "What is RAG technology?",
    ]


@pytest.fixture
def test_config():
    """Test configuration"""
    return {
        "chunk_size": 100,
        "chunk_overlap": 10,
        "retrieval_k": 2,
        "temperature": 0.0,
    }


# ============================================================
# CLEANUP FIXTURES
# ============================================================

@pytest.fixture(autouse=True)
def cleanup():
    """Cleanup after each test"""
    yield
    # Cleanup code here if needed
