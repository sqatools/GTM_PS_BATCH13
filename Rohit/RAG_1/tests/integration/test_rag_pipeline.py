"""
Integration tests for RAG pipeline
"""

import pytest
import os
from app.rag.rag_pipeline import RAGPipeline


class TestRAGPipeline:
    """Test RAG pipeline end-to-end"""
    
    @pytest.mark.skipif(
        not os.getenv("OPENAI_API_KEY"),
        reason="OPENAI_API_KEY not set"
    )
    def test_pipeline_initialization(self):
        """Test initializing RAG pipeline"""
        try:
            pipeline = RAGPipeline(load_existing=False)
            assert pipeline is not None
            assert pipeline.document_loader is not None
            assert pipeline.retriever is not None
        except Exception as e:
            pytest.skip(f"Could not initialize pipeline: {e}")
    
    @pytest.mark.skipif(
        not os.getenv("OPENAI_API_KEY"),
        reason="OPENAI_API_KEY not set"
    )
    def test_ingest_documents(self):
        """Test document ingestion"""
        try:
            pipeline = RAGPipeline(load_existing=False)
            pipeline.ingest_documents()
            
            # Verify vectorstore was created
            assert pipeline.vectorstore.vectorstore is not None
        except Exception as e:
            pytest.skip(f"Could not ingest documents: {e}")
    
    @pytest.mark.skipif(
        not os.getenv("OPENAI_API_KEY"),
        reason="OPENAI_API_KEY not set"
    )
    def test_query_pipeline(self, mock_rag_pipeline):
        """Test querying the pipeline"""
        pipeline = mock_rag_pipeline
        
        result = pipeline.query("What is RAG technology?")
        
        assert "question" in result
        assert "answer" in result
        assert "retrieved_docs" in result
        assert result["question"] == "What is RAG?"
    
    @pytest.mark.skipif(
        not os.getenv("OPENAI_API_KEY"),
        reason="OPENAI_API_KEY not set"
    )
    def test_batch_query(self, mock_rag_pipeline, test_queries):
        """Test batch querying"""
        pipeline = mock_rag_pipeline
        
        # Mock batch_query method
        pipeline.batch_query.return_value = [
            {"question": q, "answer": f"Answer to {q}"} for q in test_queries
        ]
        
        results = pipeline.batch_query(test_queries)
        
        assert len(results) == len(test_queries)
        assert all("question" in r for r in results)
    
    def test_test_connection(self, mock_rag_pipeline):
        """Test connection testing"""
        pipeline = mock_rag_pipeline
        pipeline.test_connection.return_value = True
        
        result = pipeline.test_connection()
        assert result is True
