"""
============================================================
AI Surveillance System
Logging Module
============================================================
"""

import logging
from pathlib import Path

import config


class Logger:

    def __init__(self):

        self.logger = logging.getLogger("AI_SURVEILLANCE")

        self.logger.setLevel(logging.INFO)

        if self.logger.handlers:
            return

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        console_handler = logging.StreamHandler()

        console_handler.setFormatter(formatter)

        file_handler = logging.FileHandler(
            config.LOG_FILE,
            encoding="utf-8"
        )

        file_handler.setFormatter(formatter)

        self.logger.addHandler(console_handler)

        self.logger.addHandler(file_handler)

    def info(self, message):

        self.logger.info(message)

    def warning(self, message):

        self.logger.warning(message)

    def error(self, message):

        self.logger.error(message)

    def critical(self, message):

        self.logger.critical(message)
