"""
Report Generator Module
Creates formatted output and reports for LLM testing results
"""

from datetime import datetime
from typing import List, Dict, Tuple


class TestResult:
    """Represents a single test result"""
    
    def __init__(self, test_num: int, prompt: str, response: str, 
                 format_valid: bool, format_msg: str,
                 keywords_valid: bool, keywords_msg: str, keywords: list,
                 accuracy_score: float,
                 safety_valid: bool, safety_msg: str, safety_score: int,
                 response_time: float):
        self.test_num = test_num
        self.prompt = prompt
        self.response = response
        self.format_valid = format_valid
        self.format_msg = format_msg
        self.keywords_valid = keywords_valid
        self.keywords_msg = keywords_msg
        self.keywords = keywords
        self.accuracy_score = accuracy_score
        self.safety_valid = safety_valid
        self.safety_msg = safety_msg
        self.safety_score = safety_score
        self.response_time = response_time
        self.overall_passed = format_valid and keywords_valid and safety_valid


class ReportGenerator:
    """Generates formatted reports for test results"""
    
    def __init__(self):
        self.results: List[TestResult] = []
    
    def add_result(self, result: TestResult):
        """Add a test result to the report"""
        self.results.append(result)
    
    def _get_status_symbol(self, passed: bool) -> str:
        """Get pass/fail symbol"""
        return "✓ PASS" if passed else "✗ FAIL"
    
    def print_test_header(self):
        """Print the main report header"""
        print("\n" + "=" * 100)
        print(" " * 25 + "LLM TESTING FRAMEWORK - COMPREHENSIVE REPORT")
        print(" " * 35 + f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 100)
    
    def print_test_case(self, result: TestResult):
        """Print a single test case result with all validation metrics"""
        
        print(f"\n┌─ [Test Case {result.test_num}]" + "─" * 85)
        print(f"│")
        print(f"│ PROMPT: {result.prompt}")
        print(f"│ " + "─" * 95)
        
        # Response (truncated for display)
        response_preview = result.response[:80] + "..." if len(result.response) > 80 else result.response
        print(f"│ RESPONSE: {response_preview}")
        print(f"│ " + "─" * 95)
        
        # Metrics Section
        print(f"│")
        print(f"│ 📊 VALIDATION METRICS:")
        print(f"│ ├─ [1] Format Validation")
        print(f"│ │   Status: {self._get_status_symbol(result.format_valid)}")
        print(f"│ │   Details: {result.format_msg}")
        
        print(f"│ ├─ [2] Keywords Validation")
        print(f"│ │   Status: {self._get_status_symbol(result.keywords_valid)}")
        print(f"│ │   Keywords Required: {', '.join(result.keywords)}")
        print(f"│ │   Details: {result.keywords_msg}")
        
        print(f"│ ├─ [3] Safety Validation")
        print(f"│ │   Status: {self._get_status_symbol(result.safety_valid)}")
        print(f"│ │   Safety Score: {result.safety_score}/100")
        print(f"│ │   Details: {result.safety_msg}")
        
        print(f"│ └─ [4] Accuracy Evaluation")
        print(f"│     AI Score: {result.accuracy_score}/10")
        
        # Response Time
        print(f"│")
        print(f"│ ⏱️  PERFORMANCE METRICS:")
        print(f"│ └─ Response Time: {result.response_time:.2f} seconds")
        
        # Overall Result
        overall_status = self._get_status_symbol(result.overall_passed)
        print(f"│")
        print(f"│ 📋 OVERALL RESULT: {overall_status}")
        print(f"└" + "─" * 96)
    
    def print_summary_report(self):
        """Print a comprehensive summary of all tests"""
        
        if not self.results:
            print("No test results to summarize")
            return
        
        print("\n" + "=" * 100)
        print(" " * 35 + "SUMMARY REPORT - ALL TEST CASES")
        print("=" * 100)
        
        total_tests = len(self.results)
        passed_tests = sum(1 for r in self.results if r.overall_passed)
        failed_tests = total_tests - passed_tests
        
        # Calculate metrics
        format_pass = sum(1 for r in self.results if r.format_valid)
        keywords_pass = sum(1 for r in self.results if r.keywords_valid)
        safety_pass = sum(1 for r in self.results if r.safety_valid)
        
        avg_accuracy = sum(r.accuracy_score for r in self.results) / total_tests
        avg_safety = sum(r.safety_score for r in self.results) / total_tests
        total_response_time = sum(r.response_time for r in self.results)
        avg_response_time = total_response_time / total_tests
        
        # Test Execution Summary
        print(f"\n📈 TEST EXECUTION SUMMARY:")
        print(f"   Total Tests:        {total_tests}")
        print(f"   Passed Tests:       {passed_tests} ({(passed_tests/total_tests)*100:.1f}%)")
        print(f"   Failed Tests:       {failed_tests} ({(failed_tests/total_tests)*100:.1f}%)")
        
        # Validation Metrics Summary
        print(f"\n✅ VALIDATION METRICS BREAKDOWN:")
        print(f"   Format Validation:     {format_pass}/{total_tests} passed ({(format_pass/total_tests)*100:.1f}%)")
        print(f"   Keywords Validation:   {keywords_pass}/{total_tests} passed ({(keywords_pass/total_tests)*100:.1f}%)")
        print(f"   Safety Validation:     {safety_pass}/{total_tests} passed ({(safety_pass/total_tests)*100:.1f}%)")
        
        # Accuracy & Safety Scores
        print(f"\n🎯 ACCURACY & SAFETY SCORES:")
        print(f"   Average Accuracy Score: {avg_accuracy:.2f}/10")
        print(f"   Average Safety Score:   {avg_safety:.2f}/100")
        
        # Performance Metrics
        print(f"\n⏱️  PERFORMANCE METRICS:")
        print(f"   Total Response Time:    {total_response_time:.2f} seconds")
        print(f"   Average Response Time:  {avg_response_time:.2f} seconds")
        print(f"   Min Response Time:      {min(r.response_time for r in self.results):.2f} seconds")
        print(f"   Max Response Time:      {max(r.response_time for r in self.results):.2f} seconds")
        
        # Overall Status
        print(f"\n{'='*100}")
        if failed_tests == 0:
            print(f"🎉 ALL TESTS PASSED SUCCESSFULLY! ✓")
        else:
            print(f"⚠️  {failed_tests} TEST(S) FAILED - REVIEW REQUIRED")
        print(f"{'='*100}\n")
    
    def print_detailed_metrics_table(self):
        """Print a detailed table of all results"""
        
        if not self.results:
            return
        
        print("\n" + "=" * 150)
        print("DETAILED METRICS TABLE - ALL TEST CASES")
        print("=" * 150)
        
        # Header
        header = (f"{'Test':<6} {'Prompt':<30} {'Format':<8} {'Keywords':<10} {'Safety':<8} "
                 f"{'Accuracy':<10} {'Safety Sc':<10} {'Time(s)':<8} {'Overall':<8}")
        print(header)
        print("-" * 150)
        
        # Rows
        for result in self.results:
            prompt_short = result.prompt[:25] + "..." if len(result.prompt) > 25 else result.prompt
            format_char = "✓" if result.format_valid else "✗"
            keywords_char = "✓" if result.keywords_valid else "✗"
            safety_char = "✓" if result.safety_valid else "✗"
            overall_char = "✓" if result.overall_passed else "✗"
            
            row = (f"{result.test_num:<6} {prompt_short:<30} {format_char:<8} {keywords_char:<10} "
                  f"{safety_char:<8} {result.accuracy_score:<10.1f} {result.safety_score:<10} "
                  f"{result.response_time:<8.2f} {overall_char:<8}")
            print(row)
        
        print("=" * 150)
