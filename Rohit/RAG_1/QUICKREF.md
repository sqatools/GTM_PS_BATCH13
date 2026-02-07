# RAG_1 Quick Reference Card

## 📍 Directory Structure

```
RAG_1/
├── app/
│   ├── config/          Configuration (settings, constants)
│   ├── ingestion/       Document loading & processing
│   ├── vectorstore/     FAISS vector database
│   ├── llm/             LLM client & prompts
│   ├── rag/             Main RAG pipeline
│   ├── utils/           Logging utilities
│   └── data/            Input data (Word docs, PDFs, etc.)
├── tests/               Test suite (26+ tests)
├── logs/                Log files (auto-created)
├── venv/                Virtual environment (auto-created)
├── .env                 API keys (CREATE THIS)
├── requirements.txt     Dependencies (INSTALL THESE)
└── main.py             Example usage script
```

---

## ⚡ Essential Commands

### Setup (One-Time)
```bash
cd C:\AutomationLearning\Testrepository\GTM_PS_BATCH13\Rohit\RAG_1
python -m venv venv
venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Activate Environment (Every Session)
```bash
venv\Scripts\Activate.ps1
```

### Verify Installation
```bash
python check_dependencies.py
```

### Run Tests
```bash
pytest tests/unit/ -v                    # Quick test
pytest tests/ -v                         # Full suite
pytest tests/ --cov=app --cov-report=html  # With coverage
```

### Run Example
```bash
python main.py
```

### Deactivate Environment (When Done)
```bash
deactivate
```

---

## 🔑 Key Files

| File | Purpose | Edit? |
|------|---------|-------|
| `.env` | API keys | ✅ YES (CREATE) |
| `requirements.txt` | Dependencies | ❌ Usually no |
| `main.py` | Example usage | ✅ YES (customize) |
| `app/config/settings.py` | Configuration | ✅ YES (if needed) |
| `tests/conftest.py` | Pytest config | ⚠️ Only if needed |
| `README.md` | Project info | ❌ Reference only |
| `INSTALL.md` | Setup guide | ❌ Reference only |
| `TROUBLESHOOTING.md` | Help guide | ❌ Reference only |

---

## 🛠️ Initial Setup Checklist

- [ ] Navigate to RAG_1 directory
- [ ] Create virtual environment: `python -m venv venv`
- [ ] Activate venv: `venv\Scripts\Activate.ps1`
- [ ] Upgrade pip: `python -m pip install --upgrade pip`
- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Verify: `python check_dependencies.py` (all should show ✓)
- [ ] Create `.env` from template and add OPENAI_API_KEY
- [ ] Run tests: `pytest tests/unit/ -v`

---

## 🚀 Quick Start (All Steps)

```powershell
# Setup
cd C:\AutomationLearning\Testrepository\GTM_PS_BATCH13\Rohit\RAG_1
python -m venv venv
venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt

# Verify
python check_dependencies.py

# Configure
cp .env.template .env
# Edit .env and add your OPENAI_API_KEY

# Test
pytest tests/unit/ -v

# Use
python main.py
```

---

## 📋 Common Tasks

| Task | Command |
|------|---------|
| Activate environment | `venv\Scripts\Activate.ps1` |
| Install packages | `pip install -r requirements.txt` |
| Upgrade packages | `pip install --upgrade -r requirements.txt` |
| Check packages | `python check_dependencies.py` |
| List installed | `pip list` |
| Run all tests | `pytest tests/ -v` |
| Run unit tests only | `pytest tests/unit/ -v` |
| Run with coverage | `pytest --cov=app tests/` |
| Run specific test | `pytest tests/unit/test_loader.py::test_load_text_files -v` |
| Save coverage report | `pytest --cov=app --cov-report=html tests/` |
| View coverage | `htmlcov/index.html` (open in browser) |
| Run example | `python main.py` |
| View full logs | `Get-Content logs/rag_pipeline.log -Tail 50` |
| Watch logs live | `Get-Content logs/rag_pipeline.log -Tail 50 -Wait` |

---

## 🔑 Main API

### Load Documents
```python
from app.rag import RAGPipeline

pipeline = RAGPipeline()
pipeline.ingest_documents("path/to/document.docx")
```

### Query
```python
result = pipeline.query("What is Python?")
print(f"Answer: {result['answer']}")
print(f"Sources: {result['retrieved_docs']}")
```

### Batch Query
```python
questions = ["Q1", "Q2", "Q3"]
results = pipeline.batch_query(questions)
```

### Test Connection
```python
if pipeline.test_connection():
    print("✓ All systems ready")
else:
    print("✗ Connection failed")
```

---

## 🐛 Quick Fixes

| Issue | Fix |
|-------|-----|
| "ModuleNotFoundError: langchain" | `pip install -r requirements.txt` |
| "No module named 'app'" | Make sure you're in RAG_1 directory: `cd C:\...\RAG_1` |
| "Command not found: pytest" | Activate venv: `venv\Scripts\Activate.ps1` |
| "OPENAI_API_KEY not found" | Create `.env` file and add your key |
| Tests keep skipping | Run: `python check_dependencies.py` to see what's missing |
| Slow performance | Reduce dataset size or check RAM usage |
| Permission denied | Run PowerShell as Administrator |

---

## ✅ Success Indicators

- ✅ `python check_dependencies.py` shows all packages with ✓
- ✅ `pytest tests/unit/ -v` runs without errors
- ✅ `python main.py` completes successfully
- ✅ Logs show messages in `logs/rag_pipeline.log`
- ✅ Can query pipeline and get answers
- ✅ Word documents are ingested correctly

---

## 📞 Help Resources

| Resource | Location |
|----------|----------|
| Full setup guide | [INSTALL.md](INSTALL.md) |
| Troubleshooting | [TROUBLESHOOTING.md](TROUBLESHOOTING.md) |
| Project overview | [README.md](README.md) |
| All commands | [COMMANDS.md](COMMANDS.md) |
| Status & features | [STATUS.md](STATUS.md) |
| This guide | [QUICKREF.md](QUICKREF.md) |

---

## 🎯 Workflow

**Day 1: Setup**
1. Run setup commands from "Quick Start" section
2. Verify with `python check_dependencies.py`
3. Run `pytest tests/unit/ -v` to confirm

**Day 2: Test**
1. Activate venv: `venv\Scripts\Activate.ps1`
2. Run tests: `pytest tests/ -v`
3. Check logs: `logs/rag_pipeline.log`

**Day 3: Use**
1. Activate venv: `venv\Scripts\Activate.ps1`
2. Run example: `python main.py`
3. Or import and use in your code: `from app.rag import RAGPipeline`

---

## 💾 File Backup & Reset

### Backup Current Setup
```powershell
# Exclude venv, logs, cache
Get-ChildItem -Include venv, logs, __pycache__, .pytest_cache, htmlcov -Recurse | Remove-Item -Recurse

# Archive the rest
Compress-Archive -Path . -DestinationPath backup.zip
```

### Reset to Clean State
```powershell
# Remove everything except source code
Remove-Item -Recurse venv, logs, __pycache__, .pytest_cache, htmlcov, app/data/vectorstore

# Reinstall
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

## 📊 Project Info

- **Language**: Python 3.8+
- **Vector DB**: FAISS
- **LLM**: OpenAI (ChatGPT)
- **Docs**: Word, PDF, Text
- **Testing**: pytest (26+ tests)
- **Framework**: Modular (4-layer architecture)
- **Status**: Production-ready

---

**Bookmark this file for quick reference!**
