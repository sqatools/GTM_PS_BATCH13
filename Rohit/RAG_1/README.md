# RAG_1 - Modular RAG Framework

A production-ready RAG (Retrieval-Augmented Generation) system with support for multiple document types including Word documents (.docx).

## 📋 Project Structure

```
RAG_1/
├── app/
│   ├── __init__.py
│   ├── config/
│   │   ├── __init__.py
│   │   ├── settings.py          # Configuration management
│   │   └── constants.py         # App constants
│   ├── data/
│   │   ├── raw_docs/            # Input documents (PDFs, Word, txt)
│   │   ├── processed/           # Processed documents
│   │   ├── vectorstore/         # FAISS vector store
│   │   └── oopsque.docx         # Sample Word document
│   ├── ingestion/
│   │   ├── __init__.py
│   │   ├── document_loader.py   # Load PDF, Word, Text
│   │   ├── text_splitter.py     # Chunk documents
│   │   └── embeddings.py        # Generate embeddings
│   ├── vectorstore/
│   │   ├── __init__.py
│   │   ├── faiss_store.py       # FAISS vector database
│   │   └── retriever.py         # Retrieve similar docs
│   ├── llm/
│   │   ├── __init__.py
│   │   ├── llm_client.py        # OpenAI API client
│   │   └── prompt_template.py   # Prompt templates
│   ├── rag/
│   │   ├── __init__.py
│   │   └── rag_pipeline.py      # Main RAG orchestration
│   └── utils/
│       ├── __init__.py
│       └── logger.py            # Logging configuration
├── tests/
│   ├── __init__.py
│   ├── conftest.py              # Pytest fixtures
│   ├── unit/
│   │   ├── test_loader.py
│   │   ├── test_splitter.py
│   │   ├── test_embeddings.py
│   │   └── test_retriever.py
│   ├── integration/
│   │   ├── test_rag_pipeline.py
│   │   └── test_vectorstore.py
│   └── llm/
│       ├── test_prompt.py
│       └── test_llm_response.py
├── logs/                        # Application logs
├── .env                        # Environment variables
├── requirements.txt            # Python dependencies
├── pytest.ini                 # Pytest configuration
└── README.md                  # This file
```

## 🚀 Feature Highlights

- **Word Document Support**: Load and process .docx files with python-docx
- **Modular Architecture**: Clean separation of concerns (ingestion, vectorstore, LLM, RAG)
- **FAISS Vector Store**: Fast semantic similarity search
- **OpenAI Integration**: ChatGPT for answer generation
- **Comprehensive Testing**: Unit, integration, and LLM tests
- **Structured Logging**: Detailed logging across all components
- **Configuration Management**: Environment-based settings

## 📦 Installation

### 1. Create Virtual Environment
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

### 2. Install Dependencies
```powershell
pip install -r requirements.txt
```

### 3. Setup Environment Variables
```powershell
# Copy .env and add your OpenAI API key
Copy .env .env.local
# Edit .env.local and add:
# OPENAI_API_KEY=sk-...
```

## 🔧 Configuration

### settings.py
- `OPENAI_API_KEY`: Your OpenAI API key
- `LLM_MODEL`: Model to use (default: gpt-3.5-turbo)
- `CHUNK_SIZE`: Document chunk size (default: 500)
- `CHUNK_OVERLAP`: Chunk overlap (default: 50)
- `RETRIEVAL_K`: Number of documents to retrieve (default: 3)

## 📚 Quick Start

### 1. Prepare Your Documents

Place your Word documents in `app/data/raw_docs/`:
```
app/data/raw_docs/
├── oopsque.docx
├── another_document.docx
└── more_docs.pdf
```

### 2. Ingest Documents

```python
from app.rag import RAGPipeline

# Initialize pipeline
pipeline = RAGPipeline()

# Ingest documents
pipeline.ingest_documents()

# This will:
# 1. Load all documents from app/data/raw_docs/
# 2. Split into chunks
# 3. Generate embeddings
# 4. Create FAISS vector store
# 5. Save vectorstore to disk
```

### 3. Query the System

```python
# Single query
result = pipeline.query("What are the key concepts discussed?")
print(f"Answer: {result['answer']}")
print(f"Sources: {[doc.metadata['filename'] for doc in result['retrieved_docs']]}")

# Batch queries
questions = [
    "What is the main topic?",
    "How does it work?",
    "What are the benefits?",
]
results = pipeline.batch_query(questions)
```

## 🧪 Testing

### Run All Tests
```powershell
pytest tests/ -v
```

### Run Specific Test Category
```powershell
# Unit tests
pytest tests/unit/ -v

# Integration tests
pytest tests/integration/ -v

# LLM tests
pytest tests/llm/ -v
```

### Run with Coverage
```powershell
pytest tests/ --cov=app --cov-report=html
```

### Run Mock Tests (No API Key Needed)
```powershell
pytest tests/unit/ -v
```

## 📊 Supported Document Types

| Format | Library | Status |
|--------|---------|--------|
| .docx | python-docx | ✅ Supported |
| .pdf | PyPDF | ✅ Supported |
| .txt | Built-in | ✅ Supported |
| .md | Built-in | ✅ Supported |

### Word Document Features
- Extracts text from paragraphs
- Extracts text from tables (preserves structure)
- Handles metadata (filename, type)

## 🔍 Component Details

### Document Loader (`ingestion/document_loader.py`)
- Automatically detects document type by extension
- Loads from `app/data/raw_docs/`
- Returns LangChain Document objects with metadata

### Text Splitter (`ingestion/text_splitter.py`)
- Uses RecursiveCharacterTextSplitter
- Configurable chunk size and overlap
- Preserves document metadata

### FAISS Store (`vectorstore/faiss_store.py`)
- In-memory vector database
- Support for save/load from disk
- Similarity search functionality

### Retriever (`vectorstore/retriever.py`)
- Semantic search in vector store
- Returns top-K similar documents
- Converts documents to context string

### LLM Client (`llm/llm_client.py`)
- OpenAI API integration
- Configurable model and temperature
- Connection testing

### Prompt Template (`llm/prompt_template.py`)
- RAG prompt with context
- Q&A prompts
- Classification prompts
- Summary prompts

### RAG Pipeline (`rag/rag_pipeline.py`)
- Orchestrates entire workflow
- `ingest_documents()`: Load and process documents
- `query(question)`: Answer a single question
- `batch_query(questions)`: Answer multiple questions
- `test_connection()`: Verify all components

## 📝 Logging

All components log to:
- **Console**: Real-time output
- **File**: `logs/rag_pipeline.log`

Log levels: DEBUG, INFO, WARNING, ERROR

## 🐛 Troubleshooting

### "OPENAI_API_KEY not set"
```powershell
# Set API key
$env:OPENAI_API_KEY = "sk-..."
```

### "No documents loaded"
- Check `app/data/raw_docs/` directory exists
- Verify documents are in supported format
- Check file permissions

### "ModuleNotFoundError: No module named 'docx'"
```powershell
pip install python-docx
```

### "FAISS not initialized"
- Run `pipeline.ingest_documents()` first
- Or load existing: `pipeline = RAGPipeline(load_existing=True)`

## 🚀 Advanced Usage

### Custom Configuration
```python
pipeline = RAGPipeline(
    data_path="custom/path/to/docs",
    vectorstore_path="custom/path/to/vectorstore",
    load_existing=True
)
```

### Custom Chunk Size
```python
config = Config()
config.CHUNK_SIZE = 1000
config.CHUNK_OVERLAP = 100
```

### Using Different LLM
```python
from app.llm import LLMClient

llm = LLMClient(model="gpt-4")
```

## 📖 Learning Resources

- [LangChain Documentation](https://python.langchain.com)
- [FAISS Documentation](https://github.com/facebookresearch/faiss)
- [OpenAI API Docs](https://platform.openai.com/docs)

## 📄 License

MIT License

## 🤝 Contributing

Contributions welcome! Please follow the code structure and add tests for new features.

---

**Ready to use RAG_1! 🚀**
