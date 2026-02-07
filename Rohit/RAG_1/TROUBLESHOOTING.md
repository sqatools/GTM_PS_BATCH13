# RAG_1 Troubleshooting Guide

## Common Issues & Solutions

---

## 1. ❌ ModuleNotFoundError: No module named 'langchain_core'

### Cause
Dependencies not installed yet

### ✅ Solution
```powershell
# Make sure you're in RAG_1 directory
cd C:\AutomationLearning\Testrepository\GTM_PS_BATCH13\Rohit\RAG_1

# Activate virtual environment
venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

### How to Verify
```powershell
python -c "import langchain_core; print('✓ langchain_core installed')"
python check_dependencies.py
```

---

## 2. ❌ ModuleNotFoundError: No module named 'app'

### Cause
PowerShell session is not in RAG_1 directory

### ✅ Solution
```powershell
# Check current directory
pwd

# Should show: C:\...\RAG_1
# If not, navigate there:
cd C:\AutomationLearning\Testrepository\GTM_PS_BATCH13\Rohit\RAG_1

# Verify structure:
ls app/     # Should show: config, ingestion, llm, rag, utils, vectorstore
```

---

## 3. ❌ Command not found: pytest

### Cause
Virtual environment not activated, or pytest not installed

### ✅ Solution
```powershell
# Activate venv
venv\Scripts\Activate.ps1

# Check prompt should show (venv) at start
# Example: (venv) C:\path\RAG_1>

# Verify pytest installed
pytest --version

# If still missing, install:
pip install pytest pytest-cov pytest-mock
```

---

## 4. ❌ Tests report "Dependencies not installed"

### Example Output
```
SKIPPED (langchain and dependencies not installed. Run: pip install -r requirements.txt)
```

### ✅ Solution
```powershell
# Run the dependency checker to see what's missing
python check_dependencies.py

# Install missing packages
pip install -r requirements.txt

# Re-run tests
pytest tests/unit/ -v
```

---

## 5. ❌ OPENAI_API_KEY not found error when running main.py

### Cause
OpenAI API key not set in `.env` file

### ✅ Solution

**Step 1: Get your API key from OpenAI**
- Go to: https://platform.openai.com/account/api-keys
- Create new secret key
- Copy it (you can only see it once!)

**Step 2: Set the key in `.env`**
```powershell
# Edit `.env` in RAG_1 directory
code .env  # Opens in VS Code

# Add/update this line:
OPENAI_API_KEY=sk-your-actual-key-here
```

**Step 3: Verify it worked**
```powershell
# Run a test that uses LLM
pytest tests/llm/test_llm_response.py -v

# Or run main.py
python main.py
```

### Security Note
**Never commit `.env` to git!** It's already in `.gitignore`

---

## 6. ❌ FileNotFoundError: [Errno 2] No such file or directory: 'oopsque.docx'

### Cause
Word document not in correct location

### ✅ Solution
```powershell
# Check file exists
ls app/data/oopsque.docx

# If not found:
# 1. Copy the Word document into app/data/
# 2. Or update main.py with correct file path
# 3. Or disable Word loading in main.py temporarily
```

**In main.py, you can comment out Word document loading:**
```python
# Optional: Load Word document
# pipeline.ingest_documents("app/data/oopsque.docx")

# For now, just test the pipeline structure
print("Pipeline initialized successfully")
```

---

## 7. ❌ Error: "No such file or directory: '.env'"

### Cause
`.env` file not created yet

### ✅ Solution
```powershell
# The `.env.template` should exist, copy it:
cp .env.template .env

# Edit the copied .env file and add your API key:
code .env

# Update the OPENAI_API_KEY line with your actual key
OPENAI_API_KEY=sk-your-key-here
```

---

## 8. ⚠️ Warning: "python-docx not installed, skipping Word document loading"

### Cause
python-docx library missing (needed for .docx files)

### ✅ Solution
```powershell
# Install python-docx
pip install python-docx

# Or just reinstall all requirements
pip install -r requirements.txt

# Verify
python -c "import docx; print('✓ python-docx installed')"
```

---

## 9. ❌ Permission denied when trying to activate venv

### This happens on some Windows systems

### ✅ Solution
```powershell
# Method 1: Run PowerShell as Administrator
# Right-click PowerShell → Run as administrator

# Method 2: Change execution policy temporarily
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Method 3: Use cmd.exe instead of PowerShell
cmd /c venv\Scripts\activate.bat

# Method 4: Use Python to run scripts directly
python -m pytest tests/ -v
```

---

## 10. ❌ Error: "Circular import" or "ImportError" in app modules

### Cause
Import issues in app modules

### ✅ Solution

**Step 1: Check circular imports**
```powershell
# Try importing each module separately
python -c "from app.config import settings; print('✓')"
python -c "from app.ingestion import DocumentLoader; print('✓')"
python -c "from app.vectorstore import FAISSStore; print('✓')"
python -c "from app.llm import LLMClient; print('✓')"
python -c "from app.rag import RAGPipeline; print('✓')"
```

**Step 2: If import fails, check imports in that file**
```powershell
# Example: if DocumentLoader fails
code app/ingestion/document_loader.py

# Check the import statements at top
# They should use absolute imports:
# from app.config import settings  ✓
# from app.ingestion.text_splitter import TextSplitterService  ✓
```

**Step 3: Fix any circular imports**
- Don't import from parent modules in child modules
- Use absolute imports with full paths
- Avoid importing at module level inside functions (import inside function instead)

---

## 11. ❌ Tests pass but pipeline doesn't work with real data

### Cause
Tests use mocked data, real pipeline needs actual setup

### ✅ Solution

**Step 1: Check all prerequisites**
```powershell
# All these should return ✓
python check_dependencies.py

# API key should be set
$env:OPENAI_API_KEY  # Should show sk-... (not blank)
```

**Step 2: Test each component separately**
```powershell
# Test document loading
python -c "from app.ingestion import DocumentLoader; loader = DocumentLoader(); print(loader.load_text('app/data/sample.txt'))"

# Test embeddings
python -c "from app.ingestion import EmbeddingsService; svc = EmbeddingsService(); print(len(svc.embed_text('hello')))"

# Test LLM
python -c "from app.llm import LLMClient; llm = LLMClient(); print(llm.test_connection())"
```

**Step 3: Run main.py in debug mode**
```powershell
# Edit main.py and add debug prints
# Then run:
python main.py

# Check logs
tail -f logs/rag_pipeline.log  # Windows: Get-Content logs/rag_pipeline.log -Tail 20 -Wait
```

---

## 12. ❌ pip install fails with "error: Microsoft Visual C++ 14.0 or greater is required"

### This happens on Windows when installing certain packages

### ✅ Solution

**Option 1: Install Microsoft C++ Build Tools**
- Download from: https://visualstudio.microsoft.com/downloads/
- Select "Desktop development with C++"
- Install and restart

**Option 2: Use pre-built wheels**
```powershell
# Try upgrading pip first
python -m pip install --upgrade pip wheel setuptools

# Then try install again
pip install -r requirements.txt
```

**Option 3: Use conda instead**
```powershell
# If you have conda installed
conda create -n rag python=3.11
conda activate rag
pip install -r requirements.txt
```

---

## 13. ⏳ pip install takes very long

### Cause
Large packages like torch, tensorflow, or FAISS taking time to compile

### ✅ Solution

This is normal! It can take 5-15 minutes depending on:
- Internet speed
- Computer speed
- Package dependencies

**What to do:**
- Be patient, don't interrupt
- Check progress in terminal (should show percentage)
- If stuck > 15 mins, try Ctrl+C and run again

**To speed up:**
```powershell
# Use pre-built wheels (usually faster)
pip install --only-binary :all: -r requirements.txt

# Or install core packages first
pip install langchain langchain-core
pip install faiss-cpu
pip install openai
# ... etc
```

---

## 14. ❌ Error: "OPENAI_API_KEY invalid" or "401 Unauthorized"

### Cause
Invalid or expired API key

### ✅ Solution

**Step 1: Verify the key format**
```powershell
# Check if key is set and starts with 'sk-'
$env:OPENAI_API_KEY
# Should output something like: sk-proj-abc123...
```

**Step 2: Get a new key**
- Go to: https://platform.openai.com/account/api-keys
- Check if your key expired (they expire after 90 days)
- Create a new one
- Update `.env` file

**Step 3: Test the key**
```powershell
# Run this test
pytest tests/llm/test_llm_response.py::test_llm_connection -v

# Should pass if key is valid
```

---

## 15. ❌ Memory error or slow performance

### Cause
FAISS vectorstore getting too large or system memory low

### ✅ Solution

**Check system resources:**
```powershell
# Check available RAM
systeminfo | findstr "System Boot"
Get-WmiObject -Class Win32_ComputerSystem | Select-Object TotalPhysicalMemory
```

**Reduce dataset size:**
```python
# In main.py, limit documents:
pipeline.ingest_documents("app/data/oopsque.docx", max_documents=50)
```

**Use GPU acceleration (optional):**
```powershell
# Install GPU version of FAISS
pip install faiss-gpu

# Or use lighter vectorstore temporarily
# Use in-memory search instead of FAISS
```

---

## 🔍 Debug Commands

### Check Everything
```powershell
# Run full diagnostic
python check_dependencies.py
```

### Run Tests with Debug Output
```powershell
# Verbose output
pytest tests/unit/ -v -s

# Show print statements
pytest tests/unit/ -s

# Stop on first failure
pytest tests/unit/ -x

# Show local variables on failure
pytest tests/unit/ -l

# Generate HTML coverage report
pytest tests/ --cov=app --cov-report=html
# Then open: htmlcov/index.html
```

### Check Logs
```powershell
# Windows PowerShell
Get-Content logs/rag_pipeline.log -Tail 50

# Or watch in real-time
Get-Content logs/rag_pipeline.log -Tail 50 -Wait
```

### Test Individual Components
```powershell
# Document loading
python -c "from app.ingestion.document_loader import DocumentLoader; d = DocumentLoader(); print(d.load_text('README.md')[:100])"

# Text splitting
python -c "from app.ingestion.text_splitter import TextSplitterService; t = TextSplitterService(); docs = t.split_text('This is a test'); print(f'{len(docs)} chunks')"

# Vector store
python -c "from app.vectorstore.faiss_store import FAISSStore; print('✓ FAISSStore imports OK')"

# LLM connection
python -c "from app.llm.llm_client import LLMClient; llm = LLMClient(); print('LLM connected' if llm.test_connection() else 'Connection failed')"
```

### Run Specific Test
```powershell
# Run one test file
pytest tests/unit/test_loader.py -v

# Run specific test
pytest tests/unit/test_loader.py::test_load_text_files -v

# Run tests matching pattern
pytest tests/ -k "loader" -v

# Run with specific markers
pytest tests/ -m requires_deps -v
```

---

## 📞 Still Stuck?

### Collect Diagnostic Information
```powershell
# Run this and share output
python --version
pip --version
pip list | Select-Object -First 20
pytest --version
echo $env:OPENAI_API_KEY
cat .env | Select-String "OPENAI"
```

### Check Recent Errors
```powershell
# See last 100 lines of log
Get-Content logs/rag_pipeline.log -Tail 100

# Find error lines
Select-String "ERROR" logs/rag_pipeline.log
```

### Reset Environment (if all else fails)
```powershell
# Remove old environment
rm -r venv

# Create fresh environment
python -m venv venv
venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt

# Test again
python check_dependencies.py
pytest tests/unit/ -v
```

---

**Last Updated**: 2024
**Next Step**: Run `python check_dependencies.py` to verify your setup!
