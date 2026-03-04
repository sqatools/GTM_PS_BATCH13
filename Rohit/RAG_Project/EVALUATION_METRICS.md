# RAG System Evaluation Metrics Guide

## Overview

This guide explains how to test three critical metrics for RAG systems:
1. **Hallucination Rate** - How often the LLM generates false information
2. **Accuracy** - How correct the answers are
3. **Efficiency** - How fast and resource-efficient the system is

---

## 1. Hallucination Rate Testing

### What is Hallucination?
Hallucination occurs when the LLM generates information that is not present in the knowledge base.

### How to Test:

```bash
pytest tests/test_rag_metrics.py::TestHallucinationRate -v -s
```

### Key Tests:

| Test | Purpose | Example |
|------|---------|---------|
| `test_detect_hallucinated_content` | Detects false information | "What lunar benefits?" → Flagged as hallucinated |
| `test_grounded_answer_not_flagged` | Validates correct info | "What is the waiting period?" → Grounded ✓ |
| `test_hallucination_rate_calculation` | Calculates % of hallucinations | 1 out of 5 queries = 20% |

### Benchmark Targets:
- **Excellent**: < 5% hallucination rate
- **Good**: 5-10% hallucination rate
- **Acceptable**: 10-20% hallucination rate
- **Poor**: > 20% hallucination rate

---

## 2. Accuracy Testing

### What is Accuracy?
Accuracy measures if the answers are factually correct and relevant to the questions.

### How to Test:

```bash
pytest tests/test_rag_metrics.py::TestAccuracy -v -s
```

### Key Tests:

| Test | Purpose |
|------|---------|
| `test_keyword_accuracy` | Checks if answer contains required keywords |
| `test_source_grounding_accuracy` | Validates answer is supported by sources |
| `test_accuracy_score` | Calculates overall accuracy percentage |

### Accuracy Scoring Method:

```
For each query:
1. Run the query through RAG system
2. Check if expected keywords are in answer
3. Verify answer is supported by sources
4. Calculate percentage: (matched_keywords / total_keywords) * 100
5. Average across all queries
```

### Benchmark Targets:
- **Excellent**: ≥ 95% accuracy
- **Good**: 85-95% accuracy
- **Acceptable**: 75-85% accuracy
- **Poor**: < 75% accuracy

---

## 3. Efficiency Testing

### What is Efficiency?
Efficiency measures response speed, throughput, and resource usage.

### How to Test:

```bash
pytest tests/test_rag_metrics.py::TestEfficiency -v -s
```

### Key Tests:

| Test | Metric | Benchmark |
|------|--------|-----------|
| `test_response_time` | Latency per query | < 100ms |
| `test_throughput` | Queries per second | > 10 QPS |
| `test_memory_efficiency` | Memory per response | < 10MB |
| `test_latency_percentiles` | P50, P95, P99 latency | P99 < 500ms |

### Latency Percentiles Explained:
- **P50**: 50% of queries respond within this time (median)
- **P95**: 95% of queries respond within this time
- **P99**: 99% of queries respond within this time (worst case)

### Benchmark Targets:

**Response Time:**
- **Excellent**: < 50ms
- **Good**: 50-100ms
- **Acceptable**: 100-200ms
- **Poor**: > 200ms

**Throughput:**
- **Excellent**: > 100 QPS
- **Good**: 50-100 QPS
- **Acceptable**: 10-50 QPS
- **Poor**: < 10 QPS

---

## 4. Running All Metrics Tests

### Run All Metric Tests:

```bash
pytest tests/test_rag_metrics.py -v -s
```

### Run Specific Metric Type:

```bash
# Hallucination only
pytest tests/test_rag_metrics.py::TestHallucinationRate -v -s

# Accuracy only
pytest tests/test_rag_metrics.py::TestAccuracy -v -s

# Efficiency only
pytest tests/test_rag_metrics.py::TestEfficiency -v -s

# Comprehensive report
pytest tests/test_rag_metrics.py::TestComprehensiveMetrics -v -s
```

---

## 5. Comprehensive Metrics Report

The `TestComprehensiveMetrics` class generates a complete report:

```
============================================================
RAG SYSTEM PERFORMANCE METRICS REPORT
============================================================
Hallucination Rate:     10.0%
Accuracy Score:         95.0%
Avg Response Time:      0.45ms
Throughput:             2200.00 QPS
Total Queries Tested:   10
============================================================
```

---

## 6. Test Structure

### Test Categories:

```
tests/
├── test_rag_metrics.py
│   ├── TestHallucinationRate
│   │   ├── test_detect_hallucinated_content
│   │   ├── test_grounded_answer_not_flagged
│   │   └── test_hallucination_rate_calculation
│   ├── TestAccuracy
│   │   ├── test_keyword_accuracy
│   │   ├── test_source_grounding_accuracy
│   │   └── test_accuracy_score
│   ├── TestEfficiency
│   │   ├── test_response_time
│   │   ├── test_throughput
│   │   ├── test_memory_efficiency
│   │   └── test_latency_percentiles
│   └── TestComprehensiveMetrics
│       └── test_rag_metrics_report
```

---

## 7. Key Metrics Definitions

### Hallucination Rate Formula:
```
Hallucination Rate (%) = (Hallucinated Answers / Total Answers) × 100
```

### Accuracy Score Formula:
```
Accuracy (%) = (Correct Answers / Total Answers) × 100
```

### Throughput Formula:
```
Throughput (QPS) = Total Queries / Total Time (seconds)
```

### Average Response Time:
```
Avg Response Time (ms) = (Sum of All Response Times) / Number of Queries
```

---

## 8. Interpreting Results

### All Green (Passing):
✓ System is performing well across all metrics

### Some Red (Failing):
- **High Hallucination**: Improve knowledge base quality or use temperature tuning
- **Low Accuracy**: Check answer validation logic or improve prompts
- **Slow Response**: Optimize retrieval or use caching

### Example Interpretation:
```
✓ Hallucination Rate: 5% (GOOD)
✗ Accuracy Score: 72% (POOR) → Needs improvement
✓ Avg Response Time: 25ms (EXCELLENT)
✓ Throughput: 2000 QPS (EXCELLENT)

Action Items:
1. Improve accuracy by refining test expectations
2. Consider adding more comprehensive source validation
```

---

## 9. Best Practices

1. **Run tests regularly** - After each knowledge base update
2. **Track trends** - Monitor metrics over time
3. **Set thresholds** - Define acceptable ranges for your use case
4. **Benchmark competitors** - Compare against other RAG systems
5. **User feedback** - Correlate metrics with real user satisfaction

---

## 10. Example Usage

```python
# Run comprehensive report
pytest tests/test_rag_metrics.py::TestComprehensiveMetrics::test_rag_metrics_report -v -s

# Output:
# ============================================================
# RAG SYSTEM PERFORMANCE METRICS REPORT
# ============================================================
# Hallucination Rate:     10.0%      (Target: < 5%)
# Accuracy Score:         95.0%      (Target: > 90%)
# Avg Response Time:      0.45ms     (Target: < 100ms)
# Throughput:             2200 QPS   (Target: > 100 QPS)
# Total Queries Tested:   10
# ============================================================
```
