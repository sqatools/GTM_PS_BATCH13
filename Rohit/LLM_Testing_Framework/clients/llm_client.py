import requests
import os
from config.config import API_URL, HEADERS, MODEL, API_KEY

def send_prompt(prompt):
    # Skip validation if running in test mode or if API_KEY is explicitly set
    is_test_mode = os.getenv('TEST_MODE', 'false').lower() == 'true'
    
    if not is_test_mode and (API_KEY == "your_api_key" or not API_KEY):
        raise ValueError(
            "Error: API_KEY is not configured. "
            "Please set your OpenAI API key in config/config.py. "
            "Get your API key from: https://platform.openai.com/api-keys"
        )

    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)
    response_data = response.json()
    
    # Check if response contains an error
    if "error" in response_data:
        raise Exception(
            f"API Error: {response_data['error'].get('message', 'Unknown error')}. "
            f"Status Code: {response.status_code}"
        )
    
    # Check if response has the expected structure
    if "choices" not in response_data:
        raise KeyError(
            f"Unexpected API response format. Expected 'choices' key but got: {response_data}"
        )

    return response_data["choices"][0]["message"]["content"]