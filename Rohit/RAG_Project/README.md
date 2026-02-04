# RAG (Retrieval-Augmented Generation) Q&A System

A production-ready RAG system for testing LLM capabilities with document-grounded question answering.

## Project Structure

```
RAG_Project/
├── Data/
│   ├── insurance_policy.txt          # Sample document for RAG
│   └── __init__.py
├── rag/
│   ├── loader.py                     # Document loading utilities
│   ├── retriever.py                  # Vector store and retriever setup
│   ├── qa_engine.py                  # Main RAG chain orchestration
│   └── __init__.py
├── tests/
│   ├── test_rag_answers.py           # RAG answer validation tests
│   ├── test_qa_system.py             # QA system tests
│   ├── test_llm_integration.py       # LLM integration tests
│   └── __init__.py
├── main.py                           # Entry point for testing
├── requirements.txt                  # Project dependencies
└── README.md                         # This file
```

## Components

### 1. Document Loader (rag/loader.py)
- Loads text documents using LangChain's TextLoader
- Splits documents into manageable chunks using RecursiveCharacterTextSplitter
- Configurable chunk size and overlap for optimal retrieval

### 2. Vector Store & Retriever (rag/retriever.py)
- Creates FAISS vector store for efficient similarity search
- Uses OpenAI embeddings for semantic understanding
- Returns k-nearest relevant documents for queries

### 3. QA Engine (rag/qa_engine.py)
- Orchestrates the complete RAG pipeline
- Combines retriever with ChatOpenAI LLM
- Returns both answer and source documents for transparency

### 4. Test Suite (tests/)
- **test_rag_answers.py**: Validates RAG pipeline health
- **test_qa_system.py**: Tests QA system with policy-specific queries
- **test_llm_integration.py**: Integration tests for LLM behavior

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Environment Variables
```bash
export OPENAI_API_KEY="your_openai_api_key_here"
```

### 3. Verify Installation
```bash
python main.py
```

## Running Tests

### Run All Tests
```bash
pytest tests/ -v
```

### Run Specific Test File
```bash
pytest tests/test_qa_system.py -v
```

### Run with Coverage
```bash
pytest tests/ --cov=rag --cov-report=html
```

## Usage Example

```python
from rag.qa_engine import get_rag_chain

# Initialize RAG chain
rag_chain = get_rag_chain()

# Ask a question
question = "What is the waiting period for health insurance?"
result = rag_chain({"query": question})

# Get answer and sources
print("Answer:", result["result"])
print("Sources:", result["source_documents"])
```

## Key Features

✓ Document-grounded Q&A with source attribution
✓ Semantic search using embeddings
✓ LLM integration with OpenAI
✓ Comprehensive test coverage
✓ Configurable chunk size and retrieval parameters
✓ Production-ready error handling

## Test Coverage

- **Document Loading**: Validates document processing
- **Embedding & Retrieval**: Tests vector store functionality
- **Answer Generation**: Validates LLM output quality
- **Source Grounding**: Ensures answers are referenced from source documents
- **Integration**: End-to-end pipeline testing

## Configuration

Edit `qa_engine.py` to customize:
- Chunk size (default: 500 characters)
- Chunk overlap (default: 50 characters)
- Temperature (default: 0 for deterministic answers)
- Number of retrieved documents (k=3)

## Troubleshooting

### Import Errors
Ensure all dependencies are installed and OPENAI_API_KEY is set

### API Errors
Check OpenAI API key validity and account balance

### No Relevant Documents
Adjust chunk_size and chunk_overlap in loader.py

## Performance Notes

- First run initializes embeddings (may take 30-60 seconds)
- Subsequent queries are faster due to caching
- FAISS provides O(1) retrieval time for vector similarity

## Future Enhancements

- Multi-document support with metadata filtering
- Streaming responses for long documents
- Conversation history with context management
- Custom embedding models
- Performance monitoring and logging
