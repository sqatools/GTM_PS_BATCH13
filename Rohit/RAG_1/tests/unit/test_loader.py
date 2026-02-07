"""
Unit tests for document loader
"""

import pytest
from app.ingestion.document_loader import DocumentLoader


class TestDocumentLoader:
    """Test document loader functionality"""
    
    def test_loader_initialization(self):
        """Test initializing document loader"""
        loader = DocumentLoader("app/data/raw_docs")
        assert loader.data_path == "app/data/raw_docs"
    
    def test_load_documents(self):
        """Test loading documents from data path"""
        loader = DocumentLoader("app/data/raw_docs")
        documents = loader.load_documents()
        
        # Should load at least the Word document
        assert len(documents) >= 1
        assert documents[0].metadata.get("source") is not None
    
    def test_load_docx(self):
        """Test loading Word document"""
        loader = DocumentLoader("app/data/raw_docs")
        
        # Look for .docx files in the data directory
        import os
        docx_files = [f for f in os.listdir("app/data/raw_docs") if f.endswith('.docx')]
        
        if docx_files:
            docx_path = os.path.join("app/data/raw_docs", docx_files[0])
            docs = loader.load_docx(docx_path)
            assert len(docs) > 0
            assert "oopsque" in docs[0].metadata.get("filename", "")
    
    def test_load_text(self):
        """Test loading text file"""
        loader = DocumentLoader()
        
        # Create a temporary text file for testing
        test_content = "This is a test document for RAG system."
        test_file = "test_doc.txt"
        
        with open(test_file, 'w') as f:
            f.write(test_content)
        
        try:
            docs = loader.load_text(test_file)
            assert len(docs) == 1
            assert test_content in docs[0].page_content
        finally:
            import os
            if os.path.exists(test_file):
                os.remove(test_file)
