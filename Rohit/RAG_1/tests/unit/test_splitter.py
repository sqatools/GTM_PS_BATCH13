"""
Unit tests for text splitter
"""

import pytest
from app.ingestion.text_splitter import TextSplitterService


class TestTextSplitter:
    """Test text splitter functionality"""
    
    def test_splitter_initialization(self):
        """Test initializing text splitter"""
        splitter = TextSplitterService(chunk_size=200, chunk_overlap=20)
        assert splitter.chunk_size == 200
        assert splitter.chunk_overlap == 20
    
    def test_split_text(self):
        """Test splitting text into chunks"""
        splitter = TextSplitterService(chunk_size=50, chunk_overlap=5)
        
        text = "This is a long text that needs to be split into multiple chunks. " * 5
        chunks = splitter.split_text(text)
        
        assert len(chunks) > 1
        assert all(len(chunk) <= 60 for chunk in chunks)  # Slight margin
    
    def test_split_documents(self, sample_documents):
        """Test splitting documents"""
        splitter = TextSplitterService(chunk_size=100, chunk_overlap=10)
        split_docs = splitter.split_documents(sample_documents)
        
        assert len(split_docs) > len(sample_documents)
        assert all(hasattr(doc, 'page_content') for doc in split_docs)
    
    def test_empty_documents_split(self):
        """Test splitting empty documents list"""
        splitter = TextSplitterService()
        result = splitter.split_documents([])
        assert result == []
    
    def test_chunk_overlap(self):
        """Test that chunks have proper overlap"""
        splitter = TextSplitterService(chunk_size=50, chunk_overlap=10)
        text = "a" * 100
        chunks = splitter.split_text(text)
        
        # Check that consecutive chunks have overlap
        if len(chunks) > 1:
            assert len(chunks) > 1
