from __future__ import annotations

import logging
import os
from datetime import datetime


class Logger:
    _instance = None
    _logger = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._setup_logger()
        return cls._instance

    @classmethod
    def _setup_logger(cls):
        # Create logs directory if it doesn't exist
        logs_dir = 'logs'
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)

        # Create logger
        cls._logger = logging.getLogger('hand_gestures')
        cls._logger.setLevel(logging.DEBUG)

        # Create formatters and handlers
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        )

        # File handler
        file_handler = logging.FileHandler(
            os.path.join(
                logs_dir, f'app_{
                    datetime.now().strftime("%Y%m%d")
                }.log',
            ),
        )
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)

        # Add handlers to logger
        cls._logger.addHandler(file_handler)
        cls._logger.addHandler(console_handler)

    @classmethod
    def debug(cls, message):
        if cls._logger is None:
            cls._setup_logger()
        cls._logger.debug(message)

    @classmethod
    def info(cls, message):
        if cls._logger is None:
            cls._setup_logger()
        cls._logger.info(message)

    @classmethod
    def warning(cls, message):
        if cls._logger is None:
            cls._setup_logger()
        cls._logger.warning(message)

    @classmethod
    def error(cls, message):
        if cls._logger is None:
            cls._setup_logger()
        cls._logger.error(message)

    @classmethod
    def critical(cls, message):
        if cls._logger is None:
            cls._setup_logger()
        cls._logger.critical(message)
