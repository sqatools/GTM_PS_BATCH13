import pytest
from unittest.mock import Mock, patch, MagicMock
import os

# Set a dummy API key to prevent OpenAI errors during import
os.environ["OPENAI_API_KEY"] = "sk-test-dummy-key-for-testing"


class MockDocument:
    """Mock document for testing"""
    def __init__(self, content="Sample telecom KB content"):
        self.page_content = content
        self.metadata = {}


class MockEmbeddings:
    """Mock embeddings that returns dummy vectors"""
    def embed_documents(self, texts):
        return [[0.1] * 1536 for _ in texts]
    
    def embed_query(self, text):
        return [0.1] * 1536


class MockVectorStore:
    """Mock vector store for testing"""
    def __init__(self, docs):
        self.docs = docs
    
    def as_retriever(self, search_kwargs=None):
        return self
    
    def get_relevant_documents(self, query):
        return self.docs if self.docs else [MockDocument("Network outage detected. Escalate to L2 team.")]


class MockChatOpenAI:
    """Mock ChatOpenAI for testing"""
    def __init__(self, temperature=0):
        self.temperature = temperature
    
    def predict(self, prompt):
        return "The Internet issue appears to be a network outage. Escalate to L2 support team for immediate resolution."


class MockTextLoader:
    """Mock TextLoader for testing"""
    def __init__(self, file_path):
        self.file_path = file_path
    
    def load(self):
        return [MockDocument("Internet Down: Restart router or modem")]


@pytest.fixture(autouse=True)
def mock_openai_dependencies(monkeypatch):
    """Automatically mock OpenAI dependencies for all tests"""
    
    # Mock langchain_openai.OpenAIEmbeddings
    monkeypatch.setattr(
        "rag.embeddings.OpenAIEmbeddings",
        MockEmbeddings
    )
    
    # Mock langchain_openai.ChatOpenAI
    monkeypatch.setattr(
        "rag.generator.ChatOpenAI",
        MockChatOpenAI
    )
    
    # Mock TextLoader
    monkeypatch.setattr(
        "rag.loader.TextLoader",
        MockTextLoader
    )
    
    # Mock FAISS.from_documents to return MockVectorStore
    def mock_faiss_from_documents(docs, embeddings):
        return MockVectorStore(docs)
    
    monkeypatch.setattr(
        "rag.vector_store.FAISS.from_documents",
        mock_faiss_from_documents
    )
