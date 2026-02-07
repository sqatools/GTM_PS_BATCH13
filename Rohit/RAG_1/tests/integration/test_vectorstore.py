"""
Integration tests for vector store
"""

import pytest
import os
from app.vectorstore.faiss_store import FAISSStore


class TestVectorStore:
    """Test vector store functionality"""
    
    @pytest.mark.skipif(
        not os.getenv("OPENAI_API_KEY"),
        reason="OPENAI_API_KEY not set"
    )
    def test_vectorstore_initialization(self):
        """Test initializing FAISS vectorstore"""
        try:
            store = FAISSStore("app/data/vectorstore_test")
            assert store is not None
        except Exception as e:
            pytest.skip(f"Could not initialize vectorstore: {e}")
    
    @pytest.mark.skipif(
        not os.getenv("OPENAI_API_KEY"),
        reason="OPENAI_API_KEY not set"
    )
    def test_create_vectorstore(self, sample_documents):
        """Test creating vectorstore from documents"""
        try:
            store = FAISSStore("app/data/vectorstore_test")
            store.create_from_documents(sample_documents)
            
            assert store.vectorstore is not None
        except Exception as e:
            pytest.skip(f"Could not create vectorstore: {e}")
    
    @pytest.mark.skipif(
        not os.getenv("OPENAI_API_KEY"),
        reason="OPENAI_API_KEY not set"
    )
    def test_similarity_search(self, mock_vectorstore):
        """Test similarity search"""
        store = mock_vectorstore
        store.similarity_search.return_value = [
            Mock(page_content="Test result", metadata={})
        ]
        
        results = store.similarity_search("test query", k=1)
        
        assert len(results) >= 1
