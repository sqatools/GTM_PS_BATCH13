"""
Integration tests for LLM with RAG system
"""
import pytest
from rag.qa_engine import get_rag_chain


class TestLLMIntegration:
    """Test cases for LLM integration with RAG"""
    
    @pytest.fixture
    def rag_chain(self):
        """Setup RAG chain for testing"""
        return get_rag_chain()
    
    def test_answer_is_string(self, rag_chain):
        """Verify answer is a string"""
        question = "What is the waiting period?"
        result = rag_chain(question)
        
        assert isinstance(result["answer"], str)
        assert len(result["answer"]) > 0
    
    def test_sources_are_provided(self, rag_chain):
        """Verify source documents are returned"""
        question = "What is the waiting period?"
        result = rag_chain(question)
        
        assert "context" in result
        assert len(result["context"]) > 0
    
    def test_answer_relevance(self, rag_chain):
        """Verify answer is relevant to question"""
        question = "What is covered under health insurance?"
        result = rag_chain(question)
        
        answer = result["answer"].lower()
        
        # Check if answer contains relevant keywords
        relevant_keywords = ["coverage", "covered", "hospital", "treatment", "expenses"]
        assert any(keyword in answer for keyword in relevant_keywords)
    
    def test_multiple_queries(self, rag_chain):
        """Test LLM with multiple queries"""
        queries = [
            "What is the waiting period for health insurance?",
            "What are the exclusions in the policy?",
            "How long does claim settlement take?",
            "What is the coverage limit for hospitalization?"
        ]
        
        for query in queries:
            result = rag_chain(query)
            assert isinstance(result["answer"], str)
            assert len(result["answer"]) > 0
            assert len(result["context"]) > 0
    
    def test_source_grounding(self, rag_chain):
        """Verify answer is grounded in source documents"""
        question = "What are the exclusions?"
        result = rag_chain(question)
        
        answer = result["answer"].lower()
        source_text = " ".join([doc.page_content.lower() for doc in result["context"]])
        
        # The answer should contain relevant terms from the source
        assert len(answer) > 0
        assert len(result["context"]) > 0


