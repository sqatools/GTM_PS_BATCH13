"""
Demo Testing Script - Shows practical testing examples
Run: python test_demo.py
"""

import json
from unittest.mock import patch, MagicMock
from clients.llm_client import send_prompt
from validators.rule_validator import validate_response_format, check_keywords
from validators.ai_evaluator import evaluate_answer

# Mock responses for testing
MOCK_RESPONSES = {
    "Explain Regression testing in one sentence": "API testing is the process of testing application programming interfaces to verify they function correctly and securely.",
    "What is AI Testing?": "Selenium is an automation framework used for testing web applications across different browsers and platforms.",
}

def demo_test_single_prompt():
    """Demonstrate testing a single prompt"""
    prompt = "Explain API testing in one sentence"
    keywords = ["Regression", "testing"]
    
    with patch('clients.llm_client.requests.post') as mock_post:
        # Setup mock
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "choices": [{"message": {"content": MOCK_RESPONSES[prompt]}}]
        }
        mock_post.return_value = mock_response
        
        print("\n" + "="*80)
        print("DEMO: Testing Single Prompt")
        print("="*80)
        print(f"\nPrompt: {prompt}")
        print(f"Keywords: {', '.join(keywords)}")
        print("-"*80)
        
        response = send_prompt(prompt)
        print(f"\nResponse:\n{response}")
        
        # Validation checks
        valid_format, format_msg = validate_response_format(response)
        keyword_check, keyword_msg = check_keywords(response, keywords)
        
        print(f"\n✓ Format Check: {format_msg}")
        print(f"✓ Keywords Found: {keyword_msg}")
        print("\n" + "="*80 + "\n")

def demo_test_bulk_prompts():
    """Demonstrate testing multiple prompts"""
    
    with patch('clients.llm_client.requests.post') as mock_post:
        with open("test_data/prompts.json") as f:
            test_cases = json.load(f)
        
        mock_response = MagicMock()
        mock_post.return_value = mock_response
        
        print("\n" + "="*80)
        print("DEMO: Testing Multiple Prompts")
        print("="*80)
        
        for idx, test_case in enumerate(test_cases, 1):
            prompt = test_case["prompt"]
            keywords = test_case["keywords"]
            
            mock_response.json.return_value = {
                "choices": [{"message": {"content": MOCK_RESPONSES.get(prompt, "Mock response")}}]
            }
            
            response = send_prompt(prompt)
            valid_format, _ = validate_response_format(response)
            keyword_check, _ = check_keywords(response, keywords)
            
            status = "✓ PASS" if (valid_format and keyword_check) else "✗ FAIL"
            print(f"\n[{idx}] {status} - {prompt}")
        
        print("\n" + "="*80 + "\n")

def demo_validation_checks():
    """Demonstrate validation checks"""
    print("\n" + "="*80)
    print("DEMO: Validation Checks")
    print("="*80)
    
    # Test 1: Valid format
    response1 = "API testing is the process of testing application programming interfaces."
    valid, msg = validate_response_format(response1)
    print(f"\nTest 1: {msg}")
    print(f"Response: '{response1}'")
    print(f"Result: {'✓ PASS' if valid else '✗ FAIL'}")
    
    # Test 2: Invalid format (too short)
    response2 = "API"
    valid, msg = validate_response_format(response2)
    print(f"\nTest 2: {msg}")
    print(f"Response: '{response2}'")
    print(f"Result: {'✓ PASS' if valid else '✗ FAIL'}")
    
    # Test 3: Keywords present
    response3 = "API testing is important for quality assurance in software development."
    keywords = ["API", "testing"]
    found, msg = check_keywords(response3, keywords)
    print(f"\nTest 3: {msg}")
    print(f"Response: '{response3}'")
    print(f"Looking for: {keywords}")
    print(f"Result: {'✓ PASS' if found else '✗ FAIL'}")
    
    # Test 4: Keywords missing
    response4 = "Unit testing is a development practice that ensures code quality."
    keywords = ["API", "testing"]
    found, msg = check_keywords(response4, keywords)
    print(f"\nTest 4: {msg}")
    print(f"Response: '{response4}'")
    print(f"Looking for: {keywords}")
    print(f"Result: {'✓ PASS' if found else '✗ FAIL'}")
    
    print("\n" + "="*80 + "\n")

if __name__ == "__main__":
    print("\n" + "="*80)
    print("LLM TESTING FRAMEWORK - Demo")
    print("="*80)
    
    # Run demos
    demo_validation_checks()
    demo_test_single_prompt()
    demo_test_bulk_prompts()
    
    print("="*80)
    print("Demo Complete!")
    print("="*80)
