"""
Unit tests for retriever
"""

import pytest
from unittest.mock import Mock
from app.vectorstore.retriever import RetrieverService


class TestRetriever:
    """Test retriever functionality"""
    
    def test_retriever_initialization(self, mock_vectorstore):
        """Test initializing retriever"""
        retriever = RetrieverService(mock_vectorstore)
        assert retriever.vectorstore is not None
    
    def test_retrieve_documents(self, mock_vectorstore):
        """Test retrieving documents"""
        vectorstore = mock_vectorstore
        vectorstore.similarity_search.return_value = [
            Mock(page_content="Doc 1", metadata={"filename": "test.txt"}),
            Mock(page_content="Doc 2", metadata={"filename": "test.txt"}),
        ]
        
        retriever = RetrieverService(vectorstore)
        results = retriever.retrieve("test query", k=2)
        
        assert len(results) == 2
        assert results[0].page_content == "Doc 1"
    
    def test_get_context_string(self, mock_retriever_service):
        """Test converting documents to context"""
        docs = [
            Mock(page_content="First document content"),
            Mock(page_content="Second document content"),
        ]
        
        retriever = mock_retriever_service
        context = retriever.get_context_string(docs)
        
        assert "First" in context
        assert "Second" in context
        assert "---" in context
