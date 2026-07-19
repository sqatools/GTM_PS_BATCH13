"""
Framework Configuration
"""

import os

from dotenv import load_dotenv

load_dotenv()


class Config:

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    MODEL = os.getenv("MODEL")

    BASE_URL = os.getenv("BASE_URL")

    USERNAME = os.getenv("USERNAME")

    PASSWORD = os.getenv("PASSWORD")

    BROWSER = os.getenv("BROWSER")

    TIMEOUT = int(

        os.getenv(

            "TIMEOUT",

            20

        )

    )