"""
Logger Utility
Centralized logging configuration
"""

import os
import logging

# Gracefully handle missing config
try:
    from app.config.settings import Config
    from app.config.constants import LOG_LEVEL, LOG_FORMAT
except (ImportError, ModuleNotFoundError):
    # Fallback values when config modules are not available
    Config = type('Config', (), {'LOGS_PATH': 'logs'})
    LOG_LEVEL = 'INFO'
    LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'


def get_logger(name: str) -> logging.Logger:
    """Get logger instance"""
    logger = logging.getLogger(name)
    
    # Only configure if not already configured
    if not logger.handlers:
        try:
            logger.setLevel(getattr(logging, LOG_LEVEL))
            
            # Console handler
            console_handler = logging.StreamHandler()
            console_handler.setLevel(getattr(logging, LOG_LEVEL))
            
            # Formatter
            formatter = logging.Formatter(LOG_FORMAT)
            console_handler.setFormatter(formatter)
            
            logger.addHandler(console_handler)
            
            # File handler (if logs directory exists)
            logs_dir = Config.LOGS_PATH
            os.makedirs(logs_dir, exist_ok=True)
            
            file_handler = logging.FileHandler(
                os.path.join(logs_dir, "rag_pipeline.log")
            )
            file_handler.setLevel(getattr(logging, LOG_LEVEL))
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        except Exception:
            # If logging setup fails, at least basic logging should work
            logger.setLevel(logging.INFO)
    
    return logger
