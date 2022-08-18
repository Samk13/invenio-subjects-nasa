"""Utils for logging info to console."""
import logging

logging.basicConfig(level=logging.INFO)


def logger(input_msg):
    """Log message level INFO."""
    logging.info(input_msg)
