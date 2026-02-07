"""
Tests for prompt generation
"""

import pytest
from app.llm.prompt_template import PromptTemplate


class TestPromptTemplate:
    """Test prompt template functionality"""
    
    def test_template_initialization(self):
        """Test initializing prompt template"""
        template = PromptTemplate()
        assert template is not None
    
    def test_create_rag_prompt(self, prompt_template):
        """Test creating RAG prompt"""
        context = "Python is a programming language."
        question = "What is Python?"
        
        prompt = prompt_template.create_rag_prompt(context, question)
        
        assert "Context:" in prompt
        assert "Question:" in prompt
        assert "Answer:" in prompt
        assert context in prompt
        assert question in prompt
    
    def test_create_qa_prompt_with_context(self, prompt_template):
        """Test creating Q&A prompt with context"""
        question = "What is AI?"
        context = "AI is artificial intelligence."
        
        prompt = prompt_template.create_qa_prompt(question, context)
        
        assert question in prompt
        assert context in prompt
    
    def test_create_qa_prompt_without_context(self, prompt_template):
        """Test creating Q&A prompt without context"""
        question = "What is AI?"
        
        prompt = prompt_template.create_qa_prompt(question)
        
        assert question in prompt
        assert "Question:" in prompt
        assert "Answer:" in prompt
    
    def test_create_classification_prompt(self, prompt_template):
        """Test creating classification prompt"""
        text = "Python is great for data science"
        categories = ["programming", "science", "other"]
        
        prompt = prompt_template.create_classification_prompt(text, categories)
        
        assert text in prompt
        assert "programming" in prompt
    
    def test_create_summary_prompt(self, prompt_template):
        """Test creating summary prompt"""
        text = "This is a very long document that needs to be summarized into a shorter version."
        
        prompt = prompt_template.create_summary_prompt(text)
        
        assert "Summary:" in prompt
        assert text in prompt
