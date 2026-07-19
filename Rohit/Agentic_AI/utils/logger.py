"""
Centralized Logger
"""

import logging
import os


class Logger:

    @staticmethod
    def get_logger(name):

        if not os.path.exists("logs"):
            os.makedirs("logs")

        logger = logging.getLogger(name)

        logger.setLevel(logging.INFO)

        if not logger.handlers:

            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
            )

            file_handler = logging.FileHandler(
                "logs/telecom_ai.log"
            )

            file_handler.setFormatter(formatter)

            console_handler = logging.StreamHandler()

            console_handler.setFormatter(formatter)

            logger.addHandler(file_handler)

            logger.addHandler(console_handler)

        return logger