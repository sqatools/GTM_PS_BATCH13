import json
from unittest.mock import patch, MagicMock
from clients.llm_client import send_prompt
from validators.rule_validator import validate_response_format, check_keywords
from validators.ai_evaluator import evaluate_answer


def get_mock_response(prompt):
    """Generate a mock response based on the prompt"""
    mock_responses = {
        "Explain Regression testing in one sentence": "API testing is the process of testing application programming interfaces to verify they function correctly and securely.",
        "What is AI Testing?": "Selenium is an automation framework used for testing web applications across different browsers and platforms."
    }
    return mock_responses.get(prompt, "This is a test response from a mocked LLM.")


@patch('clients.llm_client.requests.post')
def test_llm_responses(mock_post):
    """Test LLM responses with mocked API calls and detailed validation"""
    
    # Configure mock response
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "choices": [{"message": {"content": ""}}]
    }
    mock_post.return_value = mock_response

    with open("test_data/prompts.json") as f:
        data = json.load(f)

    print("\n" + "="*80)
    print("LLM RESPONSE VERIFICATION REPORT")
    print("="*80)
    
    all_passed = True
    
    for idx, item in enumerate(data, 1):
        prompt = item["prompt"]
        keywords = item["keywords"]

        # Set mock response content based on prompt
        mock_response_text = get_mock_response(prompt)
        mock_response.json.return_value = {
            "choices": [{"message": {"content": mock_response_text}}]
        }
        
        print(f"\n[Test Case {idx}]")
        print(f"Prompt: {prompt}")
        print("-" * 80)
        
        # Get response
        response = send_prompt(prompt)
        print(f"Response: {response[:100]}..." if len(response) > 100 else f"Response: {response}")
        
        # Validation 1: Format Check
        valid_format, format_msg = validate_response_format(response)
        status1 = "✓ PASS" if valid_format else "✗ FAIL"
        print(f"\n1. Format Validation: {status1} - {format_msg}")
        
        # Validation 2: Keyword Check
        keyword_check, keyword_msg = check_keywords(response, keywords)
        status2 = "✓ PASS" if keyword_check else "✗ FAIL"
        keywords_str = ", ".join(keywords)
        print(f"2. Keyword Check: {status2} - Looking for: [{keywords_str}]")
        print(f"   Result: {keyword_msg}")
        
        # Validation 3: AI Evaluation
        score = evaluate_answer(prompt, response)
        print(f"3. AI Evaluation Score: {score}")
        
        # Assertion checks
        try:
            assert valid_format, f"Format validation failed: {format_msg}"
            assert keyword_check, f"Keyword check failed: {keyword_msg}"
            print(f"\n➜ Test Case {idx}: PASSED ✓")
        except AssertionError as e:
            print(f"\n➜ Test Case {idx}: FAILED ✗")
            print(f"   Error: {str(e)}")
            all_passed = False
    
    print("\n" + "="*80)
    print(f"Overall Result: {'ALL TESTS PASSED ✓' if all_passed else 'SOME TESTS FAILED ✗'}")
    print("="*80 + "\n")
    
    assert all_passed, "Some test cases failed"