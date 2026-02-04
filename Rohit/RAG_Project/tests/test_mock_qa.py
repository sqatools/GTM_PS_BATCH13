"""
Mock tests for RAG system (no API key required)
"""
import pytest
from unittest.mock import Mock, MagicMock, patch


@pytest.fixture
def mock_rag_chain():
    """Create a mock RAG chain"""
    def mock_chain(question):
        # Simulate RAG responses
        responses = {
            "waiting period": {
                "answer": "The waiting period for health insurance is 30 days from the date of policy issuance.",
                "context": [Mock(page_content="Standard waiting period: 30 days from the date of policy issuance")]
            },
            "exclusions": {
                "answer": "The policy excludes cosmetic procedures, experimental treatments, sports injuries, and self-inflicted injuries.",
                "context": [Mock(page_content="Cosmetic procedures, Experimental treatments, Sports injuries")]
            },
            "claim settlement": {
                "answer": "Claims are processed within 15 working days maximum.",
                "context": [Mock(page_content="Maximum claim processing time: 15 working days")]
            },
            "covered": {
                "answer": "Coverage includes hospitalization up to $100,000, out-patient treatment up to $10,000, dental up to $5,000.",
                "context": [Mock(page_content="Hospitalization expenses up to $100,000 per year")]
            },
            "coverage": {
                "answer": "Coverage includes hospitalization up to $100,000, out-patient treatment up to $10,000, dental up to $5,000.",
                "context": [Mock(page_content="Hospitalization expenses up to $100,000 per year")]
            },
            "premiums": {
                "answer": "Payment frequency options include monthly, quarterly, semi-annual, or annual payments.",
                "context": [Mock(page_content="Payment frequency options: Monthly, Quarterly, Semi-annual, Annual")]
            }
        }
        
        # Match question to response
        for key, response in responses.items():
            if key in question.lower():
                return response
        
        return {
            "answer": "Information not found in the knowledge base.",
            "context": []
        }
    
    return mock_chain


class TestMockQASystem:
    """Test cases with mock data (no API key needed)"""
    
    def test_waiting_period_query(self, mock_rag_chain):
        """Test query about waiting period"""
        result = mock_rag_chain("What is the waiting period for health insurance?")
        
        assert "30 days" in result["answer"]
        assert len(result["context"]) > 0
    
    def test_exclusions_query(self, mock_rag_chain):
        """Test query about exclusions"""
        result = mock_rag_chain("What are the exclusions in the policy?")
        
        assert "cosmetic" in result["answer"].lower()
        assert len(result["context"]) > 0
    
    def test_claim_settlement_query(self, mock_rag_chain):
        """Test query about claim settlement"""
        result = mock_rag_chain("How long does claim settlement take?")
        
        assert "15 working days" in result["answer"]
        assert len(result["context"]) > 0
    
    def test_coverage_query(self, mock_rag_chain):
        """Test query about coverage"""
        result = mock_rag_chain("What is covered under health insurance?")
        
        assert "$100,000" in result["answer"]
        assert len(result["context"]) > 0
    
    def test_premium_query(self, mock_rag_chain):
        """Test query about premiums"""
        result = mock_rag_chain("How are premiums paid?")
        
        assert "monthly" in result["answer"].lower()
        assert len(result["context"]) > 0
    
    def test_answer_is_string(self, mock_rag_chain):
        """Verify answer is a string"""
        result = mock_rag_chain("What is the waiting period?")
        
        assert isinstance(result["answer"], str)
        assert len(result["answer"]) > 0
    
    def test_sources_provided(self, mock_rag_chain):
        """Verify sources are provided"""
        result = mock_rag_chain("What is the waiting period?")
        
        assert "context" in result
        assert len(result["context"]) > 0
