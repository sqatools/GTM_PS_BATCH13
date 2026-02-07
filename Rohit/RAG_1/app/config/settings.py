"""
Application Configuration
Centralized settings for RAG system
"""

import os

# Gracefully handle missing python-dotenv
try:
    from dotenv import load_dotenv
    load_dotenv()
except ModuleNotFoundError:
    # If python-dotenv not installed, just read from environment
    pass


class Config:
    """Base configuration"""
    # API Keys
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    
    # Model Settings
    LLM_MODEL = os.getenv("LLM_MODEL", "gpt-3.5-turbo")
    LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", 0))
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")
    
    # Document Processing
    CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 500))
    CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 50))
    
    # Vector Store
    VECTORSTORE_TYPE = os.getenv("VECTORSTORE_TYPE", "faiss")
    VECTORSTORE_PATH = os.getenv("VECTORSTORE_PATH", "app/data/vectorstore")
    
    # Retrieval
    RETRIEVAL_K = int(os.getenv("RETRIEVAL_K", 3))
    
    # Paths
    DATA_RAW_PATH = "app/data/raw_docs"
    DATA_PROCESSED_PATH = "app/data/processed"
    LOGS_PATH = "logs"
    
    # Debug
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    LLM_TEMPERATURE = 0.3


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    LLM_TEMPERATURE = 0


def get_config():
    """Get current configuration based on environment"""
    env = os.getenv("ENVIRONMENT", "development").lower()
    if env == "production":
        return ProductionConfig
    return DevelopmentConfig
