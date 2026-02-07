"""
Application Constants
Reusable constants across the RAG system
"""

# Document Types
SUPPORTED_DOC_TYPES = {
    ".pdf": "PDF",
    ".docx": "Word",
    ".doc": "Word",
    ".txt": "Text",
    ".md": "Markdown",
}

# Metrics Thresholds
HALLUCINATION_THRESHOLD = 0.05  # 5%
ACCURACY_THRESHOLD = 0.95  # 95%
RESPONSE_TIME_THRESHOLD = 100  # ms

# Retrieval Settings
MIN_RELEVANCE_SCORE = 0.5
MAX_RETRIEVAL_ATTEMPTS = 3

# Vector Store Settings
FAISS_METRIC = "l2"  # euclidean distance
FAISS_INDEX_TYPE = "IVFFlat"

# Logging
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# System Prompt Template
DEFAULT_SYSTEM_PROMPT = """You are an assistant for question-answering tasks. 
Use the following pieces of retrieved context to answer the question. 
If you don't know the answer, say that you don't know.
Keep answers concise and relevant to the context provided."""
