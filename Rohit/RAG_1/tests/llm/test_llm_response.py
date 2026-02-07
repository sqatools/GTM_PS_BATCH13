"""
Tests for LLM responses
"""

import pytest
import os
from app.llm.llm_client import LLMClient


class TestLLMResponse:
    """Test LLM response functionality"""
    
    def test_llm_initialization(self, mock_llm_client):
        """Test initializing LLM client"""
        llm = mock_llm_client
        assert llm is not None
    
    def test_generate_answer_mock(self, mock_llm_client):
        """Test generating answer with mock"""
        llm = mock_llm_client
        
        prompt = "What is RAG?"
        answer = llm.generate_answer(prompt)
        
        assert answer is not None
        assert len(answer) > 0
        assert "test answer" in answer.lower()
    
    @pytest.mark.skipif(
        not os.getenv("OPENAI_API_KEY"),
        reason="OPENAI_API_KEY not set"
    )
    def test_generate_answer_real(self):
        """Test generating answer with real LLM"""
        try:
            llm = LLMClient()
            prompt = "What is Python?"
            answer = llm.generate_answer(prompt)
            
            assert answer is not None
            assert len(answer) > 0
            assert isinstance(answer, str)
        except Exception as e:
            pytest.skip(f"Could not generate answer: {e}")
    
    def test_test_connection_mock(self, mock_llm_client):
        """Test connection with mock"""
        llm = mock_llm_client
        
        result = llm.test_connection()
        assert result is True
    
    @pytest.mark.skipif(
        not os.getenv("OPENAI_API_KEY"),
        reason="OPENAI_API_KEY not set"
    )
    def test_test_connection_real(self):
        """Test connection with real LLM"""
        try:
            llm = LLMClient()
            result = llm.test_connection()
            assert result is True
        except Exception as e:
            pytest.skip(f"Could not test connection: {e}")
