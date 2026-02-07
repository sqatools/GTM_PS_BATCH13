"""
LLM Client
OpenAI API client for generating answers
"""

from typing import Optional
from unittest.mock import Mock

# Gracefully handle missing langchain imports
try:
    from langchain_openai import ChatOpenAI
except ModuleNotFoundError:
    ChatOpenAI = Mock

try:
    from langchain_core.messages import BaseMessage
except ModuleNotFoundError:
    BaseMessage = Mock

from app.utils.logger import get_logger
from app.config.settings import Config
from app.config.constants import DEFAULT_SYSTEM_PROMPT

logger = get_logger(__name__)


class LLMClient:
    """OpenAI LLM client wrapper"""
    
    def __init__(
        self,
        model: str = None,
        temperature: float = None,
        api_key: str = None
    ):
        self.model = model or Config.LLM_MODEL
        self.temperature = temperature if temperature is not None else Config.LLM_TEMPERATURE
        self.api_key = api_key or Config.OPENAI_API_KEY
        
        try:
            self.llm = ChatOpenAI(
                model=self.model,
                temperature=self.temperature,
                openai_api_key=self.api_key
            )
            logger.info(
                f"Initialized LLMClient: model={self.model}, "
                f"temperature={self.temperature}"
            )
        except Exception as e:
            logger.error(f"Error initializing LLMClient: {str(e)}")
            raise
    
    def generate_answer(
        self,
        prompt: str,
        max_tokens: Optional[int] = None
    ) -> str:
        """Generate answer using LLM"""
        try:
            logger.debug(f"Generating answer for prompt of length: {len(prompt)}")
            
            response = self.llm.invoke(prompt)
            
            answer = response.content if hasattr(response, 'content') else str(response)
            logger.debug(f"Generated answer of length: {len(answer)}")
            
            return answer
        except Exception as e:
            logger.error(f"Error generating answer: {str(e)}")
            raise
    
    def generate_with_messages(self, messages: list) -> str:
        """Generate answer from structured messages"""
        try:
            logger.debug(f"Generating answer from {len(messages)} messages")
            response = self.llm.invoke(messages)
            answer = response.content if hasattr(response, 'content') else str(response)
            return answer
        except Exception as e:
            logger.error(f"Error generating answer from messages: {str(e)}")
            raise
    
    def test_connection(self) -> bool:
        """Test LLM connection"""
        try:
            logger.info("Testing LLM connection...")
            response = self.llm.invoke("Hello, are you working?")
            logger.info("LLM connection successful")
            return True
        except Exception as e:
            logger.error(f"LLM connection test failed: {str(e)}")
            return False
