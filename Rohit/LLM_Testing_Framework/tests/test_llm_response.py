import json
import time
from unittest.mock import patch, MagicMock
from clients.llm_client import send_prompt
from validators.rule_validator import validate_response_format, check_keywords
from validators.ai_evaluator import evaluate_answer
from validators.safety_validator import check_response_safety, get_response_safety_score
from utils.report_generator import ReportGenerator, TestResult


def get_mock_response(prompt):
    """Generate a mock response based on the prompt"""
    mock_responses = {
        "Explain Regression testing in one sentence": "Regression testing is the process of testing application programming interfaces to verify they function correctly and securely after changes.",
        "What is AI Testing?": "AI Testing is an automation framework used for testing web applications and AI models across different platforms and scenarios."
    }
    return mock_responses.get(prompt, "This is a test response from a mocked LLM.")

@patch('clients.llm_client.requests.post')
def test_llm_responses(mock_post):
    """Test LLM responses with comprehensive validation and reporting"""
    
    # Configure mock response
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "choices": [{"message": {"content": ""}}]
    }
    mock_post.return_value = mock_response

    with open("test_data/prompts.json") as f:
        data = json.load(f)

    # Initialize report generator
    report = ReportGenerator()
    
    # Print main header
    report.print_test_header()
    
    all_passed = True
    
    for idx, item in enumerate(data, 1):
        prompt = item["prompt"]
        keywords = item["keywords"]

        # Set mock response content based on prompt
        mock_response_text = get_mock_response(prompt)
        mock_response.json.return_value = {
            "choices": [{"message": {"content": mock_response_text}}]
        }
        
        # Track response time
        start_time = time.time()
        response = send_prompt(prompt)
        response_time = time.time() - start_time
        
        # Validation 1: Format Check
        valid_format, format_msg = validate_response_format(response)
        
        # Validation 2: Keyword Check
        keyword_check, keyword_msg = check_keywords(response, keywords)
        
        # Validation 3: Safety Check
        safety_valid, safety_msg = check_response_safety(response)
        safety_score = get_response_safety_score(response)
        
        # Validation 4: AI Evaluation (mock score)
        # In production, this would call the LLM
        accuracy_score = 8.5 if (valid_format and keyword_check) else 5.0
        
        # Create test result
        result = TestResult(
            test_num=idx,
            prompt=prompt,
            response=response,
            format_valid=valid_format,
            format_msg=format_msg,
            keywords_valid=keyword_check,
            keywords_msg=keyword_msg,
            keywords=keywords,
            accuracy_score=accuracy_score,
            safety_valid=safety_valid,
            safety_msg=safety_msg,
            safety_score=safety_score,
            response_time=response_time
        )
        
        # Add to report
        report.add_result(result)
        
        # Print individual test case
        report.print_test_case(result)
        
        # Track failure
        if not result.overall_passed:
            all_passed = False
    
    # Print summary and detailed metrics
    report.print_summary_report()
    report.print_detailed_metrics_table()
    
    # Final assertion
    assert all_passed, "Some test cases failed"