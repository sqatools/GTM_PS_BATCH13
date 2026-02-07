# RAG_1 Quick Start and Commands

## Quick Start (Windows PowerShell)

### 1. Setup
```powershell
# Navigate to project
cd C:\AutomationLearning\Testrepository\GTM_PS_BATCH13\Rohit\RAG_1

# Create virtual environment
python -m venv venv
venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Set OpenAI API key
$env:OPENAI_API_KEY = "sk-your-api-key-here"
```

### 2. Verify Setup
```powershell
# Run mock tests (no API key needed initially)
pytest tests/unit/ -v

# Check if API key is set
echo $env:OPENAI_API_KEY
```

### 3. Run Main Demo
```powershell
python main.py
```

### 4. Run All Tests  
```powershell
pytest tests/ -v

# With coverage
pytest tests/ --cov=app --cov-report=html
```

### 5. Run Specific Tests
```powershell
# Unit tests only
pytest tests/unit/ -v

# Integration tests
pytest tests/integration/ -v

# LLM tests
pytest tests/llm/ -v

# Single test
pytest tests/unit/test_loader.py -v
```

## Common Commands

### Environment
```powershell
# Set API key
$env:OPENAI_API_KEY = "sk-..."

# Unset (if needed)
Remove-Item env:OPENAI_API_KEY

# Activate venv
venv\Scripts\Activate.ps1

# Deactivate venv
deactivate
```

### Testing
```powershell
# All tests verbose
pytest tests/ -v

# Tests with output
pytest tests/ -v -s

# Stop on first failure
pytest tests/ -x

# Show only failed
pytest tests/ -f

# Generate report
pytest tests/ --html=report.html
```

### Code Quality
```powershell
# Format code
black app/ tests/

# Lint
flake8 app/ tests/

# Static analysis
pylint app/
```

### Logs
```powershell
# View logs
Get-Content logs/rag_pipeline.log

# Clear logs
Clear-Content logs/rag_pipeline.log

# Follow logs
Get-Content logs/rag_pipeline.log -Wait
```

## Troubleshooting

### API Key Issues
```powershell
# Verify API key is set
echo $env:OPENAI_API_KEY

# Set new API key
$env:OPENAI_API_KEY = "sk-new-key"

# Check .env file
Get-Content .env
```

### Module Issues
```powershell
# Reinstall dependencies
pip install --upgrade -r requirements.txt

# Check installed packages
pip list | grep langchain
```

### Test Issues
```powershell
# Clear pytest cache
Remove-Item -r .pytest_cache

# Rebuild venv
deactivate
Remove-Item -r venv
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Useful Python Commands

### Interactive Testing
```python
# In Python REPL
from app.rag import RAGPipeline

# Initialize
pipeline = RAGPipeline(load_existing=True)

# Query
result = pipeline.query("What is RAG?")
print(result['answer'])
```

### Jupyter Notebook
```powershell
# Start Jupyter
jupyter notebook

# Create new notebook and run:
# from app.rag import RAGPipeline
# pipeline = RAGPipeline(load_existing=True)
# result = pipeline.query("Your question here")
```

## File Locations
- Documents: `app/data/raw_docs/`
- Vector Store: `app/data/vectorstore/`
- Logs: `logs/rag_pipeline.log`
- Tests: `tests/`
- Config: `.env`

---

**Ready to go! Start with: `python main.py`** 🚀
