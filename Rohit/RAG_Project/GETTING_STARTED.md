# RAG Project - Getting Started Guide for Beginners

## 🎯 What is This Project About?

**Simple Explanation**: 
- You have a document (insurance policy)
- You ask it questions
- It answers based ONLY on that document (no hallucinations)
- It shows you where it found the answer (source document)

---

## 📦 **Step 1: Install Everything**

### Requirements File Already Created
The `requirements.txt` already has all libraries needed.

### Install Command
```bash
pip install -r requirements.txt
```

### What Gets Installed?
```
✓ langchain          - RAG framework
✓ faiss-cpu          - Search engine for documents
✓ openai             - AI model (ChatGPT)
✓ pytest             - Testing tool
✓ python-dotenv      - API key management
```

---

## 🔑 **Step 2: Setup OpenAI API Key**

### Why Needed?
- To use ChatGPT for answering questions
- You need an OpenAI account

### Get Your Key
1. Go to https://platform.openai.com
2. Click "API keys"
3. Create new secret key
4. Copy it

### Set Environment Variable (Windows PowerShell)
```powershell
$env:OPENAI_API_KEY = "sk-your-key-here"
```

### Verify It Works
```powershell
echo $env:OPENAI_API_KEY
# Should print: sk-xxx...
```

---

## 📚 **Step 3: Understand the Documents**

### What Document Are We Using?
`Data/insurance_policy.txt` - Contains insurance policy information

### Quick Preview
```
WAITING PERIODS
- Standard: 30 days
- Emergency: No waiting period
- Planned surgery: 90 days

COVERAGE
- Hospitalization: $100,000
- Out-patient: $10,000
- Dental: $5,000
```

---

## 🚀 **Step 4: Run Your First Test**

### Quick Test (No API Key Needed!)
This test uses mock data, so you don't need OpenAI API:

```powershell
cd C:\AutomationLearning\Testrepository\GTM_PS_BATCH13\Rohit\RAG_Project
pytest tests/test_mock_qa.py -v
```

### Expected Output
```
tests/test_mock_qa.py::TestMockQASystem::test_waiting_period_query PASSED
tests/test_mock_qa.py::TestMockQASystem::test_exclusions_query PASSED
tests/test_mock_qa.py::TestMockQASystem::test_coverage_query PASSED
...
========================= 7 passed in 0.45s ==========================
```

✅ **Success!** This proves tests work correctly.

---

## 💬 **Step 5: Manual Test - Ask Questions Yourself**

### Run the Main Demo
```powershell
python main.py
```

### What You'll See
```
Initializing RAG Q&A System...
✓ RAG Chain initialized successfully

================================================================================
Testing RAG System with Sample Questions
================================================================================

Question 1: What is the waiting period for health insurance?
--------------------------------------------------------------------------------
Answer: The waiting period for health insurance is 30 days from the date of 
policy issuance. However, for emergency medical conditions, no waiting period 
applies, and for planned surgeries, there is a 90-day waiting period.

Sources (3 found):
  Source 1: WAITING PERIODS
The waiting period for health insurance is defined as follows:
- Standard waiting period: 30 days from the date of policy issuance
...

================================================================================
```

### What This Shows
```
✓ Question: User's input
✓ Answer: AI's response (grounded in document)
✓ Sources: Where answer came from (proof)
```

---

## 🧪 **Step 6: Run All Tests**

### Test Suite Overview
```
test_rag_answers.py       → Basic Q&A works
test_qa_system.py         → All policy questions answerable
test_llm_integration.py   → LLM output format correct
test_mock_qa.py           → Mock behavior correct
test_rag_metrics.py       → Quality metrics (hallucination, accuracy)
```

### Run All Tests
```powershell
pytest tests/ -v
```

### Run Specific Test File
```powershell
# Test basic RAG functionality
pytest tests/test_rag_answers.py -v

# Test QA system with classes
pytest tests/test_qa_system.py -v

# Test mock (no API needed)
pytest tests/test_mock_qa.py -v

# Test metrics (advanced)
pytest tests/test_rag_metrics.py -v
```

---

## 📊 **Step 7: Understand Test Results**

### What PASSED Means
```
✓ test_waiting_period_query PASSED
  = The RAG system correctly answered the question
  = Answer contains expected keywords
  = Source documents were provided
```

### What FAILED Means
```
✗ test_waiting_period_query FAILED
  = Something went wrong
  = Check: API key, document file, dependencies
```

### View Detailed Test Output
```powershell
pytest tests/test_qa_system.py -v -s
# -v = Verbose (show all tests)
# -s = Show print statements
```

---

## 🔍 **Step 8: Run Specific Test Methods**

### Test One Question at a Time
```powershell
# Test waiting period
pytest tests/test_qa_system.py::TestQASystem::test_waiting_period_query -v

# Test coverage
pytest tests/test_qa_system.py::TestQASystem::test_coverage_query -v

# Test claim settlement
pytest tests/test_qa_system.py::TestQASystem::test_claim_settlement_query -v

# Test exclusions
pytest tests/test_qa_system.py::TestQASystem::test_exclusions_query -v

# Test premium
pytest tests/test_qa_system.py::TestQASystem::test_premium_query -v
```

---

## 📈 **Step 9: Check Quality Metrics**

### Hallucination Test (Detects False Information)
```powershell
pytest tests/test_rag_metrics.py::TestHallucinationRate -v -s
```

**What It Measures**:
- Does AI make up information? (hallucinate)
- Benchmark: < 5% is excellent

**Example Output**:
```
Hallucination Rate: 20.0%
Hallucinated: 1/5
# 1 out of 5 queries generated false info
```

---

### Accuracy Test (Is Answer Correct?)
```powershell
pytest tests/test_rag_metrics.py::TestAccuracy -v -s
```

**What It Measures**:
- Are answers factually correct?
- Benchmark: ≥ 95% is excellent

**Example Output**:
```
Overall Accuracy Score: 95.00%
# 95% of answers were correct
```

---

### Efficiency Test (Is It Fast?)
```powershell
pytest tests/test_rag_metrics.py::TestEfficiency -v -s
```

**What It Measures**:
- Response time per query
- Queries processed per second
- Memory usage

**Example Output**:
```
Response Time: 2.50ms
Throughput: 200.00 queries/second
Latency Percentiles (ms):
  P50: 1.20ms
  P95: 3.50ms
  P99: 5.10ms
```

---

## 🎓 **How RAG Works - Simple Explanation**

### Step-by-Step Process

```
1. USER QUESTION
   "What is the waiting period?"
           ↓
2. SEARCH IN DOCUMENT
   Find similar text in insurance_policy.txt
   Found: "Standard waiting period: 30 days"
           ↓
3. PASS TO AI (ChatGPT)
   AI reads found text + question
   AI generates answer based on text
           ↓
4. RETURN ANSWER + SOURCE
   Answer: "The waiting period is 30 days..."
   Source: [location in document]
           ↓
5. USER SEES PROOF
   Answer with evidence (no hallucination!)
```

---

## 🐛 **Troubleshooting**

### Problem: "ModuleNotFoundError: No module named 'langchain'"
**Solution**:
```powershell
pip install -r requirements.txt
```

---

### Problem: "openai.AuthenticationError: Invalid API key"
**Solution**:
1. Check API key is correct
2. Set environment variable:
   ```powershell
   $env:OPENAI_API_KEY = "sk-your-key-here"
   ```
3. Verify:
   ```powershell
   echo $env:OPENAI_API_KEY
   ```

---

### Problem: "FileNotFoundError: Data/insurance_policy.txt"
**Solution**:
1. Check file exists: `ls Data/`
2. Run pytest from project root:
   ```powershell
   cd C:\...\RAG_Project
   pytest tests/ -v
   ```

---

### Problem: Tests Pass But main.py Fails
**Solution**:
- main.py requires OpenAI API key
- test_mock_qa.py works without API key
- Start with: `pytest tests/test_mock_qa.py -v`

---

## 📝 **Next Steps**

### For Beginners:
1. ✅ Run `pytest tests/test_mock_qa.py -v` (no API needed)
2. ✅ Understand test output
3. ✅ Read SIMPLE_EXPLANATION.md
4. ✅ Try modifying questions in test files

### For Advanced Users:
1. ✅ Add your own documents to `Data/` folder
2. ✅ Create custom questions in test files
3. ✅ Analyze metrics in test_rag_metrics.py
4. ✅ Improve prompts in qa_engine.py

---

## 📚 **File Guide**

```
Data/insurance_policy.txt
  → The document RAG system uses
  
main.py
  → Demo script (requires API key)
  
rag/loader.py
  → Loads and chunks documents
  
rag/retriever.py
  → Searches for relevant text
  
rag/qa_engine.py
  → Main RAG pipeline
  
tests/test_mock_qa.py
  → Tests without API key (START HERE!)
  
tests/test_rag_metrics.py
  → Quality measurements
```

---

## ✅ Quick Checklist

- [ ] Install: `pip install -r requirements.txt`
- [ ] Setup API key: `$env:OPENAI_API_KEY = "..."`
- [ ] Run mock tests: `pytest tests/test_mock_qa.py -v`
- [ ] Read output
- [ ] Run main demo: `python main.py`
- [ ] Run all tests: `pytest tests/ -v`
- [ ] Celebrate! 🎉

---

**You're ready! Start with `pytest tests/test_mock_qa.py -v` 🚀**
