import logging
import sys
from os import getenv


def setup_logging():
    """
    Configure logging with different levels and formats
    """
    logging_level = getenv("LOGGING_LEVEL", "INFO").upper()
    logging_format = "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s"

    logger = logging.getLogger()
    logger.setLevel(logging_level)

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.addFilter(lambda record: record.levelno < logging.ERROR)
    stdout_handler.setFormatter(logging.Formatter(logging_format))

    stderr_handler = logging.StreamHandler(sys.stderr)
    stderr_handler.setLevel(logging.ERROR)
    stderr_handler.setFormatter(logging.Formatter(logging_format))

    logger.addHandler(stdout_handler)
    logger.addHandler(stderr_handler)

    logging.getLogger("aiogram").setLevel(logging_level)
    logging.getLogger("schedule").setLevel(logging_level)