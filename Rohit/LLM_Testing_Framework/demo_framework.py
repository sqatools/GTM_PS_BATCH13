"""
Demo Script: Using the LLM Testing Framework
Shows how to use all three testing metrics: validation, accuracy/safety, and response time
"""

import json
import time
from unittest.mock import patch, MagicMock


def demo_with_manual_responses():
    """
    Demonstrates the testing framework with manual responses
    (without needing pytest or mocking)
    """
    
    from validators.rule_validator import validate_response_format, check_keywords
    from validators.safety_validator import check_response_safety, get_response_safety_score
    from utils.report_generator import ReportGenerator, TestResult
    
    print("\n" + "="*100)
    print(" "*30 + "LLM TESTING FRAMEWORK - DEMO")
    print("="*100)
    
    # Create a report generator
    report = ReportGenerator()
    
    # Sample test cases
    test_cases = [
        {
            "prompt": "What is Regression Testing?",
            "keywords": ["regression", "testing"],
            "response": "Regression testing is a software testing technique that ensures that previously working functionality still works after changes or updates to the software."
        },
        {
            "prompt": "Explain API Automation",
            "keywords": ["API", "automation"],
            "response": "API automation is the process of using automation tools to test application programming interfaces, verifying their functionality, performance, and security."
        }
    ]
    
    # Process each test case
    for idx, test_case in enumerate(test_cases, 1):
        prompt = test_case["prompt"]
        keywords = test_case["keywords"]
        response = test_case["response"]
        
        print(f"\n📝 Processing Test Case {idx}...")
        
        # Simulate response time
        start_time = time.time()
        time.sleep(0.1)  # Simulate API call delay
        response_time = time.time() - start_time
        
        # Validation 1: Format Check
        print(f"   ✓ Checking format validation...")
        valid_format, format_msg = validate_response_format(response)
        
        # Validation 2: Keywords Check
        print(f"   ✓ Checking keywords validation...")
        keywords_valid, keywords_msg = check_keywords(response, keywords)
        
        # Validation 3: Safety Check
        print(f"   ✓ Checking safety validation...")
        safety_valid, safety_msg = check_response_safety(response)
        safety_score = get_response_safety_score(response)
        
        # Calculate accuracy (mock score)
        accuracy_score = 9.0 if (valid_format and keywords_valid) else 5.0
        
        print(f"   ✓ Recorded response time: {response_time:.2f}s")
        
        # Create and add result
        result = TestResult(
            test_num=idx,
            prompt=prompt,
            response=response,
            format_valid=valid_format,
            format_msg=format_msg,
            keywords_valid=keywords_valid,
            keywords_msg=keywords_msg,
            keywords=keywords,
            accuracy_score=accuracy_score,
            safety_valid=safety_valid,
            safety_msg=safety_msg,
            safety_score=safety_score,
            response_time=response_time
        )
        
        report.add_result(result)
    
    # Print all results
    print(f"\n📊 Generating reports...\n")
    for result in report.results:
        report.print_test_case(result)
    
    # Print summary
    report.print_summary_report()
    report.print_detailed_metrics_table()
    
    print("\n✅ Demo completed successfully!\n")


def demo_with_api_mocking():
    """
    Demonstrates the testing framework with API mocking
    Shows how to test different response scenarios
    """
    
    from validators.rule_validator import validate_response_format, check_keywords
    from validators.safety_validator import check_response_safety, get_response_safety_score
    from utils.report_generator import ReportGenerator, TestResult
    
    print("\n" + "="*100)
    print(" "*20 + "LLM TESTING FRAMEWORK - API MOCKING DEMO")
    print("="*100)
    
    report = ReportGenerator()
    
    # Different response scenarios
    scenarios = [
        {
            "name": "Good Response",
            "prompt": "What is Selenium?",
            "keywords": ["selenium", "automation"],
            "response": "Selenium is a powerful automation framework for testing web applications across different browsers and platforms."
        },
        {
            "name": "Response Missing Keywords",
            "prompt": "Explain Unit Testing",
            "keywords": ["unit", "testing", "software"],
            "response": "This is a test response that doesn't contain the required keywords."
        },
        {
            "name": "Short Response",
            "prompt": "What is pytest?",
            "keywords": ["pytest", "framework"],
            "response": "A testing tool."
        }
    ]
    
    for idx, scenario in enumerate(scenarios, 1):
        print(f"\n🧪 Scenario {idx}: {scenario['name']}")
        
        start_time = time.time()
        response_time = time.time() - start_time
        
        valid_format, format_msg = validate_response_format(scenario["response"])
        keywords_valid, keywords_msg = check_keywords(scenario["response"], scenario["keywords"])
        safety_valid, safety_msg = check_response_safety(scenario["response"])
        safety_score = get_response_safety_score(scenario["response"])
        accuracy_score = 8.0 if (valid_format and keywords_valid) else 4.0
        
        result = TestResult(
            test_num=idx,
            prompt=scenario["prompt"],
            response=scenario["response"],
            format_valid=valid_format,
            format_msg=format_msg,
            keywords_valid=keywords_valid,
            keywords_msg=keywords_msg,
            keywords=scenario["keywords"],
            accuracy_score=accuracy_score,
            safety_valid=safety_valid,
            safety_msg=safety_msg,
            safety_score=safety_score,
            response_time=response_time
        )
        
        report.add_result(result)
        
        # Quick status
        status = "✓ PASS" if result.overall_passed else "✗ FAIL"
        print(f"   Status: {status}")
        print(f"   Format: {'✓' if valid_format else '✗'} | Keywords: {'✓' if keywords_valid else '✗'} | Safety: {'✓' if safety_valid else '✗'}")
    
    # Print full reports
    print(f"\n📊 Generating comprehensive reports...\n")
    for result in report.results:
        report.print_test_case(result)
    
    report.print_summary_report()
    report.print_detailed_metrics_table()


if __name__ == "__main__":
    print("\n" + "="*100)
    print(" "*35 + "LLM TESTING FRAMEWORK - DEMO")
    print("="*100)
    print("\nChoose a demo to run:")
    print("1. Manual Responses Demo (Good scenarios)")
    print("2. API Mocking Demo (Various scenarios)")
    print("3. Run both demos")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == "1":
        demo_with_manual_responses()
    elif choice == "2":
        demo_with_api_mocking()
    elif choice == "3":
        demo_with_manual_responses()
        demo_with_api_mocking()
    else:
        print("Invalid choice. Running manual responses demo by default...")
        demo_with_manual_responses()
