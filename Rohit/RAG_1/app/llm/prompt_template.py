"""
Prompt Template
Manages prompts for RAG system
"""

from typing import Optional
from app.utils.logger import get_logger
from app.config.constants import DEFAULT_SYSTEM_PROMPT

logger = get_logger(__name__)


class PromptTemplate:
    """Template for creating prompts"""
    
    def __init__(self, system_prompt: str = None):
        self.system_prompt = system_prompt or DEFAULT_SYSTEM_PROMPT
        logger.info("Initialized PromptTemplate")
    
    def create_rag_prompt(
        self,
        context: str,
        question: str
    ) -> str:
        """Create RAG prompt from context and question"""
        prompt = f"""{self.system_prompt}

Context:
{context}

Question:
{question}

Answer:"""
        
        logger.debug(f"Created RAG prompt of length: {len(prompt)}")
        return prompt
    
    def create_qa_prompt(
        self,
        question: str,
        context: Optional[str] = None
    ) -> str:
        """Create Q&A prompt"""
        if context:
            prompt = f"""Answer the following question based on the context provided.

Context:
{context}

Question:
{question}

Answer:"""
        else:
            prompt = f"""Answer the following question:

Question:
{question}

Answer:"""
        
        logger.debug(f"Created Q&A prompt of length: {len(prompt)}")
        return prompt
    
    def create_classification_prompt(
        self,
        text: str,
        categories: list
    ) -> str:
        """Create classification prompt"""
        categories_str = ", ".join(categories)
        
        prompt = f"""Classify the following text into one of these categories: {categories_str}

Text:
{text}

Classification:"""
        
        logger.debug(f"Created classification prompt of length: {len(prompt)}")
        return prompt
    
    def create_summary_prompt(self, text: str) -> str:
        """Create summarization prompt"""
        prompt = f"""Provide a concise summary of the following text:

Text:
{text}

Summary:"""
        
        logger.debug(f"Created summary prompt of length: {len(prompt)}")
        return prompt
