# LLM Testing Framework - Comprehensive Guide

## Overview
This framework tests LLM responses through **three validation layers** to ensure quality and consistency.

---

## ✅ Three Levels of Validation

### 1. **Format Validation**
Checks if the response meets basic quality criteria:
- Not empty
- Minimum length (≥10 characters)
- Properly structured

**File:** `validators/rule_validator.py`

```python
validate_response_format(response)
# Returns: (bool, message)
# Example: (True, "Valid response")
```

---

### 2. **Keyword Validation**
Verifies that all required keywords appear in the response:
- Case-insensitive matching
- Ensures LLM covered expected topics

**File:** `validators/rule_validator.py`

```python
check_keywords(response, keywords)
# Returns: (bool, message)
# Example: (True, "Keywords found")
```

**Test Data Format:**
```json
{
  "prompt": "Explain API testing in one sentence",
  "keywords": ["API", "testing"]
}
```

---

### 3. **AI Evaluation**
Uses an LLM to score the answer's accuracy:
- Generates evaluation prompt
- Returns scoring feedback

**File:** `validators/ai_evaluator.py`

```python
evaluate_answer(question, answer)
# Returns: score/feedback from LLM
```

---

## 🚀 How to Run Tests

### Basic Test Run
```powershell
cd LLM_Testing_Framework
python -m pytest tests/test_llm_response.py -v
```

### Detailed Output (with validation checks)
```powershell
python -m pytest tests/test_llm_response.py -v -s
```

### Run with Coverage Report
```powershell
python -m pytest tests/test_llm_response.py --cov=validators --cov=clients
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

## 🐛 Troubleshooting

### Issue: "API_KEY is not configured"
**Solution:** Set API_KEY in `config/config.py` or keep TEST_MODE enabled

### Issue: "KeyError: 'choices'"
**Solution:** API response format error. Check:
- API key is valid
- API URL is correct
- Network connectivity

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

