# Configuration File
# Project settings and configurations
import os
from pathlib import Path

# Test Mode - Set to True to run without a real API key
# This will use mock responses for testing/demonstration
TEST_MODE = True

# Try to load from .env file first
env_file = Path(__file__).parent / ".env"
if env_file.exists():
    from dotenv import load_dotenv
    load_dotenv(dotenv_path=env_file)

# Get API key from environment variable or .env file
API_KEY = os.getenv("OPENAI_API_KEY", "").strip()

# Check if API key is missing or is a placeholder
placeholder_values = [
    "",
    "your_actual_openai_api_key_here",
    "your_api_key",
    "your-api-key-here",
]

# Allow placeholder if in TEST_MODE
if (not API_KEY or API_KEY in placeholder_values) and not TEST_MODE:
    raise ValueError(
        "\n" + "="*60 + "\n"
        "❌ OPENAI_API_KEY is not configured!\n"
        "="*60 + "\n"
        "Please follow these steps:\n\n"
        "1. Get your API key from: https://platform.openai.com/account/api-keys\n\n"
        "2. Open the .env file in this project directory\n\n"
        "3. Replace the placeholder with your actual API key:\n"
        "   OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx\n\n"
        "4. Set TEST_MODE = False in config.py\n\n"
        "5. Save and run the script again\n"
        "="*60
    )
