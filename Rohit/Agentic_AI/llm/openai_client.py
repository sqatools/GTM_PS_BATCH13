import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

base_dir = Path(__file__).resolve().parents[1]
dotenv_path = base_dir / "config" / ".env"
load_dotenv(dotenv_path)


def get_openai_api_key():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or api_key.lower().startswith("your_openai_api_key"):
        raise EnvironmentError(
            "OPENAI_API_KEY is not configured. Add a valid key to config/.env or set the environment variable."
        )
    return api_key


def get_llm():
    return ChatOpenAI(
        model="gpt-4o",
        api_key=get_openai_api_key()
    )


def ask_llm(prompt):
    llm = get_llm()
    response = llm.invoke(prompt)
    return response.content