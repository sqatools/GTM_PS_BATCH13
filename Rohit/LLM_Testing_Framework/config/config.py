API_URL = "https://api.openai.com/v1/chat/completions"
# TODO: Replace 'your_api_key' with your actual OpenAI API key from https://platform.openai.com/api-keys
API_KEY = "your_api_key"
MODEL = "gpt-4o-mini"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}