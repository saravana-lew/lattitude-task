import os
import logging

DEFINED_LOG_LEVELS = {
    "CRITICAL": logging.CRITICAL,
    "ERROR": logging.ERROR,
    "WARNING": logging.WARNING,
    "INFO": logging.INFO,
    "DEBUG": logging.DEBUG,
    "DEFAULT": logging.INFO,
}


def get_logger():
    LOGGER = logging.getLogger()
    LOGLEVEL = os.getenv("LOGLEVEL", "DEFAULT")
    LOGGER.setLevel(DEFINED_LOG_LEVELS[LOGLEVEL])
    return LOGGER
