# LLM Testing Framework - Comprehensive Guide

## Overview
This framework tests LLM responses through **four comprehensive validation layers** to ensure quality, accuracy, safety, and performance.

---

## ✅ Four Levels of Validation

### 1. **Format Validation** ✓
Checks if the response meets basic quality criteria:
- Not empty
- Minimum length (≥10 characters)
- Properly structured

**File:** [validators/rule_validator.py](validators/rule_validator.py)

```python
from validators.rule_validator import validate_response_format

valid_format, format_msg = validate_response_format(response)
# Returns: (bool, message)
# Example: (True, "Valid response")
```

---

### 2. **Keyword Validation** ✓
Verifies that all required keywords appear in the response:
- Case-insensitive matching
- Ensures LLM covered expected topics

**File:** [validators/rule_validator.py](validators/rule_validator.py)

```python
from validators.rule_validator import check_keywords

keywords_valid, keywords_msg = check_keywords(response, keywords)
# Returns: (bool, message)
# Example: (True, "Keywords found")
```

**Test Data Format (test_data/prompts.json):**
```json
{
  "prompt": "Explain API testing in one sentence",
  "keywords": ["API", "testing"]
}
```

---

### 3. **Safety Validation** 🛡️ (NEW)
Validates that responses are safe and complete:
- No unsafe/malicious keywords
- Response length is adequate
- Response is not truncated
- Safety score (0-100)

**File:** [validators/safety_validator.py](validators/safety_validator.py)

```python
from validators.safety_validator import check_response_safety, get_response_safety_score

safety_valid, safety_msg = check_response_safety(response)
# Returns: (bool, message)

safety_score = get_response_safety_score(response)
# Returns: int (0-100)
```

**Example Unsafe Keywords Checked:**
- hack, crash, error, bug, attack, malicious, exploit, vulnerability, injection, overflow

---

### 4. **AI Evaluation** 🎯
Uses an LLM to score the answer's accuracy:
- Generates evaluation prompt
- Returns scoring feedback (0-10)

**File:** [validators/ai_evaluator.py](validators/ai_evaluator.py)

```python
from validators.ai_evaluator import evaluate_answer

accuracy_score = evaluate_answer(question, answer)
# Returns: float (0-10)
```

---

## � Comprehensive Output Display

The framework now displays results for all **THREE KEY METRICS**:

### 1. **Validating Responses Using Python Automation** ✅

Shows validation results at multiple levels:
```
✅ VALIDATION METRICS BREAKDOWN:
   Format Validation:     2/2 passed (100.0%)
   Keywords Validation:   2/2 passed (100.0%)
   Safety Validation:     2/2 passed (100.0%)
```

### 2. **Response Accuracy, Format, and Safety** 🎯

Displays comprehensive quality metrics:
```
🎯 ACCURACY & SAFETY SCORES:
   Average Accuracy Score: 8.50/10
   Average Safety Score:   100.00/100

Per-Test Metrics:
   ├─ [1] Format Validation: ✓ PASS - Valid response
   ├─ [2] Keywords Validation: ✓ PASS - Keywords found
   ├─ [3] Safety Validation: ✓ PASS - Safe response - No concerns detected
   └─ [4] Accuracy Evaluation: 8.5/10
```

### 3. **Response Time and Automated Tests** ⏱️

Measures and displays performance metrics:
```
⏱️  PERFORMANCE METRICS:
   Total Response Time:    0.70 seconds
   Average Response Time:  0.35 seconds
   Min Response Time:      0.32 seconds
   Max Response Time:      0.38 seconds

Per-Test: Response Time: 0.35 seconds
```

---

## 🚀 How to Run Tests

### Basic Test Run
```powershell
cd LLM_Testing_Framework
python -m pytest tests/test_llm_response.py -v
```

### Full Output Display (Recommended)
```powershell
python -m pytest tests/test_llm_response.py -v -s
```
This shows all validation metrics, summary report, and detailed metrics table.

### Run with Coverage Report
```powershell
python -m pytest tests/test_llm_response.py --cov=validators --cov=utils --cov=clients -v -s
```

### Run Demo Script (Without pytest)
```powershell
python demo_framework.py
```
Interactive demo with manual responses demonstrating all features.

### Run with HTML Report
```powershell
python -m pytest tests/test_llm_response.py --html=report.html --self-contained-html -v -s
```

---

## 📝 Adding New Test Cases

### Step 1: Edit Test Data
Update `test_data/prompts.json` with new test cases:

```json
[
  {
    "prompt": "Explain API testing in one sentence",
    "keywords": ["API", "testing"]
  },
  {
    "prompt": "What is Selenium?",
    "keywords": ["automation", "testing"]
  },
  {
    "prompt": "Describe pytest framework",
    "keywords": ["pytest", "testing", "framework"]
  }
]
```

### Step 2: Add Mock Response (Optional)
If using mocked responses, add to `tests/test_llm_response.py`:

```python
def get_mock_response(prompt):
    mock_responses = {
        "Describe pytest framework": "Pytest is a Python testing framework that makes writing and running tests easy and scalable.",
        # Add more mock responses here
    }
    return mock_responses.get(prompt, "Default mock response")
```

### Step 3: Run Tests
```powershell
python -m pytest tests/test_llm_response.py -v -s
```

---

## 🔧 Using Real OpenAI API (Instead of Mocks)

### Step 1: Get API Key
1. Go to: https://platform.openai.com/api-keys
2. Create/copy your API key

### Step 2: Configure API Key
Edit `config/config.py`:

```python
API_KEY = "sk-proj-YOUR_ACTUAL_KEY_HERE"
```

### Step 3: Disable Test Mode
Edit `conftest.py`:

```python
# Change this line:
os.environ['TEST_MODE'] = 'true'

# To:
os.environ['TEST_MODE'] = 'false'
```

### Step 4: Run Tests
```powershell
python -m pytest tests/test_llm_response.py -v -s
```

---

## 📊 Understanding Test Output

### Success Example
```
[Test Case 1]
Prompt: Explain API testing in one sentence
Response: API testing is the process of testing...

1. Format Validation: ✓ PASS - Valid response
2. Keyword Check: ✓ PASS - Looking for: [API, testing]
3. AI Evaluation Score: API testing is the process...

➜ Test Case 1: PASSED ✓
```

### Failure Example
```
1. Format Validation: ✗ FAIL - Response too short
➜ Test Case 1: FAILED ✗
```

---

## 🔍 Customizing Validators

### Example: Enhance Format Validator
Edit `validators/rule_validator.py`:

```python
def validate_response_format(response):
    if not response:
        return False, "Empty response"
    
    if len(response) < 10:
        return False, "Response too short"
    
    # Add custom validation
    if not response.endswith(('.', '!', '?')):
        return False, "Response should end with punctuation"
    
    return True, "Valid response"
```

---

## 📈 Common Test Scenarios

### Scenario 1: Test Single Prompt
```python
# In test file
prompt = "Explain REST API"
response = send_prompt(prompt)
keywords = ["REST", "API"]

valid, msg = validate_response_format(response)
assert valid, msg

keyword_check, msg = check_keywords(response, keywords)
assert keyword_check, msg
```

### Scenario 2: Test Multiple Models
```python
# In config/config.py
# Switch MODEL to test different models
MODEL = "gpt-4o-mini"  # or "gpt-4", "gpt-3.5-turbo", etc.
```

### Scenario 3: Test Response Consistency
Add test cases and run multiple times to verify consistency:
```powershell
for ($i=1; $i -le 5; $i++) { 
    python -m pytest tests/test_llm_response.py -v
}
```

---

## 🛠️ Project Structure

```
LLM_Testing_Framework/
├── clients/
│   └── llm_client.py          # API communication
├── config/
│   └── config.py              # API credentials
├── validators/
│   ├── rule_validator.py      # Format & keyword checks
│   └── ai_evaluator.py        # LLM scoring
├── tests/
│   └── test_llm_response.py   # Main test file
├── test_data/
│   └── prompts.json           # Test cases
├── conftest.py                # Pytest configuration
├── requirements.txt           # Dependencies
└── TESTING_GUIDE.md           # This file
```

---

## � Report Generator - Enhanced Output Formatting

The framework now includes a comprehensive **Report Generator** module (`utils/report_generator.py`) that creates professional, multi-level output reports.

### Report Generator Features

1. **Individual Test Case Display**
   - Prompt and response preview
   - All validation metrics with status
   - Performance metrics
   - Overall pass/fail status

2. **Summary Report**
   - Total tests, passed/failed count
   - Validation metrics breakdown
   - Accuracy and safety scores
   - Performance metrics (average, min, max response times)

3. **Detailed Metrics Table**
   - Tabular view of all results
   - Quick reference for all metrics
   - Sortable by test number

### Using Report Generator Programmatically

```python
from utils.report_generator import ReportGenerator, TestResult

# Create report
report = ReportGenerator()

# Add test results
result = TestResult(
    test_num=1,
    prompt="Your prompt here",
    response="LLM response",
    format_valid=True,
    format_msg="Valid format",
    keywords_valid=True,
    keywords_msg="Keywords found",
    keywords=["keyword1", "keyword2"],
    accuracy_score=8.5,
    safety_valid=True,
    safety_msg="Safe response",
    safety_score=100,
    response_time=0.35
)

report.add_result(result)

# Generate reports
report.print_test_case(result)
report.print_summary_report()
report.print_detailed_metrics_table()
```

---

## 🎯 New Modules (Enhanced Framework)

### 1. Safety Validator Module
**File:** [validators/safety_validator.py](validators/safety_validator.py)

Functions:
- `check_response_safety(response)` - Returns (bool, message)
- `get_response_safety_score(response)` - Returns int (0-100)

**Checks for:**
- Unsafe keywords (hack, exploit, injection, etc.)
- Response truncation
- Adequate response length

### 2. Report Generator Module
**File:** [utils/report_generator.py](utils/report_generator.py)

Classes:
- `TestResult` - Stores individual test result data
- `ReportGenerator` - Generates formatted reports

**Methods:**
- `add_result(result)` - Add a test result
- `print_test_case(result)` - Print individual test details
- `print_summary_report()` - Print summary statistics
- `print_detailed_metrics_table()` - Print tabular view

### 3. Demo Framework
**File:** [demo_framework.py](demo_framework.py)

Run interactive demos:
```powershell
python demo_framework.py
```

Choose between:
1. Manual responses demo
2. API mocking demo with various scenarios
3. Run both demos

---

## 🔧 Customizing Output Reports

### Customize Test Case Display
Edit `utils/report_generator.py`, method `print_test_case()`:

```python
def print_test_case(self, result: TestResult):
    # Modify formatting, symbols, or order of displayed metrics
    pass
```

### Customize Summary Report
Edit `utils/report_generator.py`, method `print_summary_report()`:

```python
def print_summary_report(self):
    # Add/remove metrics, change calculations, adjust formatting
    pass
```

### Customize Safety Validation
Edit `validators/safety_validator.py`:

```python
# Add more unsafe keywords to check
UNSAFE_KEYWORDS = [
    "hack", "crash", "error", "bug", "attack", "malicious",
    "exploit", "vulnerability", "injection", "overflow",
    "your_new_keyword"  # Add here
]

# Modify scoring weights in get_response_safety_score()
```

---

## 🐛 Troubleshooting

### Issue: "API_KEY is not configured"
**Solution:** Set API_KEY in `config/config.py` or keep TEST_MODE enabled

### Issue: "KeyError: 'choices'"
**Solution:** API response format error. Check:
- API key is valid
- API URL is correct
- Network connectivity

### Issue: Report not generating
**Solution:** Ensure utils/__init__.py exists and test results are added:
```python
report.add_result(result)  # Must call before printing reports
```

---

## 📚 Additional Resources

- **OUTPUT_GUIDE.md** - Detailed guide on output formatting and metrics
- **demo_framework.py** - Interactive demonstration of all features
- **test_data/prompts.json** - Sample test cases
- **config/config.py** - API configuration guide

---

## ✅ Summary of Three Testing Metrics

| Metric | Description | File | Output |
|--------|-------------|------|--------|
| **1. Validation** | Format, keywords, safety checks | `validators/` | ✓/✗ PASS/FAIL |
| **2. Accuracy/Safety** | AI scores and safety ratings | `validators/`, `utils/` | 0-10, 0-100 scores |
| **3. Performance** | Response time tracking | `utils/report_generator.py` | Time in seconds |

All metrics displayed in comprehensive reports with:
- Individual test details
- Summary statistics
- Detailed metrics table
- Professional formatting

### Issue: "Keywords not found"
**Solution:**
- Check keyword spelling in `prompts.json`
- Verify keywords appear in mock response
- Use print statements to debug

---

## 📚 Resources

- **OpenAI API Docs:** https://platform.openai.com/docs
- **Pytest Docs:** https://docs.pytest.org
- **Mock Testing:** https://docs.python.org/3/library/unittest.mock.html

---

## 💡 Best Practices

1. ✅ Keep prompts specific and clear
2. ✅ Include 2-4 keywords per test case
3. ✅ Use meaningful test data
4. ✅ Test edge cases (short answers, long answers)
5. ✅ Review mock responses for accuracy
6. ✅ Run tests regularly during development

