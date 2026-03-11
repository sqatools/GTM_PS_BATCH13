# LLM Testing Framework - Quick Start Guide

## 🎯 What This Framework Does

Tests LLM responses across **THREE KEY METRICS**:

1. ✅ **Validation** - Format, keywords, and safety checks
2. 🎯 **Accuracy & Safety** - Quality scores (0-100)
3. ⏱️ **Performance** - Response time measurement

---

## 🚀 Quick Start (5 minutes)

### 1. Install Dependencies
```powershell
cd LLM_Testing_Framework
pip install -r requirements.txt
```

### 2. View Demo (No Configuration Needed)
```powershell
python demo_framework.py
```
Shows sample output with all three metrics.

### 3. Run Actual Tests
```powershell
python -m pytest tests/test_llm_response.py -v -s
```

### 4. View Comprehensive Report
```powershell
python -m pytest tests/test_llm_response.py -v -s --html=report.html --self-contained-html
```

---

## 📊 Output Displays (All Three Metrics)

### Metric 1: Validating Responses ✅

```
📊 VALIDATION METRICS:
├─ [1] Format Validation: ✓ PASS - Valid response
├─ [2] Keywords Validation: ✓ PASS - Keywords found
└─ [3] Safety Validation: ✓ PASS - Safe response
```

### Metric 2: Accuracy & Safety 🎯

```
🎯 ACCURACY & SAFETY SCORES:
   Average Accuracy Score: 8.50/10
   Average Safety Score:   100.00/100
```

### Metric 3: Response Time ⏱️

```
⏱️  PERFORMANCE METRICS:
   Total Response Time:    0.70 seconds
   Average Response Time:  0.35 seconds
   Response Time: 0.35 seconds (per test)
```

---

## 📁 Project Structure

```
LLM_Testing_Framework/
├── tests/
│   └── test_llm_response.py          ← Main test file
├── validators/
│   ├── rule_validator.py             ← Format & keywords checks
│   ├── ai_evaluator.py               ← Accuracy scoring
│   └── safety_validator.py           ← Safety validation
├── utils/
│   └── report_generator.py           ← Report formatting
├── test_data/
│   └── prompts.json                  ← Test cases
├── demo_framework.py                 ← Interactive demo
├── TESTING_GUIDE.md                  ← Detailed guide
├── OUTPUT_GUIDE.md                   ← Output examples
└── requirements.txt                  ← Dependencies
```

---

## ✨ Key Features

| Feature | Details |
|---------|---------|
| **Format Validation** | Response not empty, min 10 chars |
| **Keyword Validation** | All required keywords present |
| **Safety Validation** | No unsafe content, complete response |
| **Accuracy Scoring** | AI evaluation 0-10 |
| **Safety Scoring** | Safety rating 0-100 |
| **Response Time** | Individual and aggregate timing |
| **Professional Reports** | Individual test, summary, and table views |

---

## 🔧 Common Commands

```powershell
# Install without running
pip install -r requirements.txt

# Run demo
python demo_framework.py

# Run tests (with full output)
python -m pytest tests/test_llm_response.py -v -s

# Run tests with coverage
python -m pytest tests/test_llm_response.py --cov=validators --cov=utils -v

# Generate HTML report
python -m pytest tests/test_llm_response.py --html=report.html --self-contained-html -v

# Run single test case
python -m pytest tests/test_llm_response.py::test_llm_responses -v -s
```

---

## 📝 Adding Test Cases

### Option 1: Add to prompts.json
Edit `test_data/prompts.json`:

```json
{
  "prompt": "Your question here?",
  "keywords": ["keyword1", "keyword2"]
}
```

### Option 2: Run Demo Script
```powershell
python demo_framework.py
```
Choose option 2 for interactive scenarios.

---

## 🎯 Understanding Reports

### TEST CASE REPORT
Shows one test with all validations:
```
[Test Case 1]
Prompt: Your prompt
Format Validation: ✓ PASS
Keywords Validation: ✓ PASS
Safety Validation: ✓ PASS
Accuracy: 8.5/10
Response Time: 0.35s
```

### SUMMARY REPORT
Shows overall statistics:
```
Total Tests: 2
Passed: 2 (100%)
Format Validation: 2/2 (100%)
Keywords Validation: 2/2 (100%)
Safety Validation: 2/2 (100%)
Avg Accuracy: 8.50/10
Avg Safety: 100.00/100
Avg Response Time: 0.35s
```

### METRICS TABLE
Shows all tests in one view:
```
Test | Prompt | Format | Keywords | Safety | Accuracy | Time
1    | ...    | ✓      | ✓        | ✓      | 8.5      | 0.35s
2    | ...    | ✓      | ✓        | ✓      | 8.5      | 0.35s
```

---

## ✅ All Three Metrics at a Glance

```
📊 COMPREHENSIVE TEST REPORT
════════════════════════════

✅ VALIDATING RESPONSES (Automation):
   Format:     2/2 ✓  (100%)
   Keywords:   2/2 ✓  (100%)
   Safety:     2/2 ✓  (100%)

🎯 ACCURACY & SAFETY:
   Accuracy Score:  8.50/10
   Safety Score:    100/100

⏱️  RESPONSE TIME:
   Average:     0.35s
   Min:         0.32s
   Max:         0.38s

📈 OVERALL: ALL TESTS PASSED ✓
════════════════════════════
```

---

## 🆘 Troubleshooting

**Q: Where is the output displayed?**
A: In the terminal when running with `-s` flag:
```powershell
python -m pytest tests/test_llm_response.py -v -s
```

**Q: How do I save the output/report?**
A: Generate HTML report:
```powershell
python -m pytest tests/test_llm_response.py --html=report.html --self-contained-html -v -s
```

**Q: Can I run without pytest?**
A: Yes, use the demo script:
```powershell
python demo_framework.py
```

**Q: How do I customize the output?**
A: Edit `utils/report_generator.py` methods:
- `print_test_case()` - Customize individual test display
- `print_summary_report()` - Customize summary format
- `print_detailed_metrics_table()` - Customize table view

---

## 📚 More Information

- **TESTING_GUIDE.md** - Complete testing guide with API setup
- **OUTPUT_GUIDE.md** - Detailed output examples and explanations
- **[validators/safety_validator.py](validators/safety_validator.py)** - Safety rules
- **[utils/report_generator.py](utils/report_generator.py)** - Report formatting

---

**Ready to test?** Run:
```powershell
python demo_framework.py
```
or
```powershell
python -m pytest tests/test_llm_response.py -v -s
```
