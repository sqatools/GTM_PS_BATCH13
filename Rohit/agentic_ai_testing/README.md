# Agentic AI Testing Framework

This is an AI-powered test automation framework that uses agents to analyze requirements, generate test cases, and create automation scripts.

## Project Structure

```
agentic_ai_testing/
├── agents/                 # AI agents for different tasks
│   ├── requirement_agent.py
│   ├── testcase_agent.py
│   ├── script_agent.py
│   ├── debug_agent.py
│   └── report_agent.py
├── automation/             # Automation framework
│   ├── pages/             # Page Object Models
│   └── tests/             # Test files
├── prompts/               # Prompt templates
├── utils/                 # Utility modules
│   └── llm.py            # LLM interactions
├── config.py              # Configuration
├── conftest.py            # Pytest configuration
├── run_agent.py           # Main entry point
└── .env                  # Environment variables
```

## Setup Instructions

### 1. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 2. Configure API Key

1. Get your OpenAI API key from: https://platform.openai.com/account/api-keys
2. Open `.env` file in this directory
3. Replace `your_actual_openai_api_key_here` with your actual API key
4. Save the file

### 3. Run the Project

```powershell
python run_agent.py
```

## How It Works

1. **Requirement Agent**: Analyzes test requirements from `prompts/prompt.txt`
2. **Test Case Agent**: Generates detailed test cases based on requirements
3. **Script Agent**: Creates automation scripts for the test cases
4. **Output**: Prints generated automation script

## Security Notes

- ⚠️ Never commit `.env` file to version control
- Keep your API key confidential
- `.env` is listed in `.gitignore` for protection

## Configuration

All settings can be modified in `config.py`.

## Requirements

- Python 3.7+
- OpenAI API key
- pip packages (see requirements.txt)

## Troubleshooting

**ImportError: No module named 'openai'**
```powershell
pip install openai python-dotenv
```

**ValueError: OPENAI_API_KEY is not configured**
- Make sure you've set the API key in `.env` file
- Restart your terminal after updating `.env`

**Authentication Error**
- Verify your API key is correct
- Check your OpenAI account has available credits
