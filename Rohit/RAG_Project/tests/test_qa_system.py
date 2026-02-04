"""
QA System tests for RAG pipeline
"""
import pytest
from rag.qa_engine import get_rag_chain


class TestQASystem:
    """Test cases for QA System"""
    
    @pytest.fixture
    def rag_chain(self):
        """Setup RAG chain"""
        return get_rag_chain()
    
    def test_waiting_period_query(self, rag_chain):
        """Test query about waiting period"""
        question = "What is the waiting period for health insurance?"
        result = rag_chain(question)
        
        answer = result["answer"].lower()
        
        # Assertions
        assert "waiting period" in answer or "30 days" in answer
        assert len(result["context"]) > 0
    
    def test_coverage_query(self, rag_chain):
        """Test query about coverage"""
        question = "What medical services are covered?"
        result = rag_chain(question)
        
        answer = result["answer"].lower()
        sources = result["context"]
        
        assert len(answer) > 0
        assert len(sources) > 0
    
    def test_claim_settlement_query(self, rag_chain):
        """Test query about claim settlement"""
        question = "How long does claim settlement take?"
        result = rag_chain(question)
        
        answer = result["answer"].lower()
        
        assert len(answer) > 0
        assert len(result["context"]) > 0
    
    def test_exclusions_query(self, rag_chain):
        """Test query about policy exclusions"""
        question = "What procedures are excluded from coverage?"
        result = rag_chain(question)
        
        answer = result["answer"].lower()
        
        assert len(answer) > 0
        assert len(result["context"]) > 0
    
    def test_premium_query(self, rag_chain):
        """Test query about premiums"""
        question = "How are premiums paid?"
        result = rag_chain(question)
        
        answer = result["answer"].lower()
        
        assert len(answer) > 0
        assert len(result["context"]) > 0



# C:/AutomationLearning/Testrepository/GTM_PS_BATCH13/.venv/Scripts/python.exe -m pytest tests/test_mock_qa.py -v