# This module sets up the logging configuration for the calculator application.
# It configures logging to include different severity levels, output formats, and destinations.

import logging
import os

def setup_logging():
    # Configures the logging settings based on environment variables.
    # Sets the log level and the format of log messages.
    log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
    logging.basicConfig(
        level=getattr(logging, log_level, logging.INFO),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    