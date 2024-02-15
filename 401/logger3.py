#!/usr/bin/python3

# Script Name:                  logger3.py
# Author:                       Michael Sineiro
# Date of latest revision:      2/14/2024
# Purpose:                      incorporates both StreamHandler for console output 
########                        and FileHandler for writing to a local file
########                        


import logging
from logging.handlers import RotatingFileHandler

def configure_logging():
    """Configure logging to write to a file with rotation and to the console."""
    # Create a logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # Set the logging level to DEBUG

    # Create a handler for rotating log files
    file_handler = RotatingFileHandler(
        'app.log', 
        maxBytes=10000,  # Maximum file size in bytes before rotating (e.g., 10KB)
        backupCount=5    # Number of backup files to keep
    )

    # Create a stream handler for console output
    stream_handler = logging.StreamHandler()

    # Set the format for the log messages
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)  # Using the same format for console output

    # Add both handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

def log_error(error_message):
    """Logs an error message to the configured log file and console."""
    logging.error(error_message)

def log_info(info_message):
    """Logs an informational message to the configured log file and console."""
    logging.info(info_message)

# The rest of your functions remain the same

def main():
    """Main function to execute the application logic."""
    configure_logging()  # Configure logging with rotation and console output at the start
    # The rest of your main function logic remains unchanged

if __name__ == "__main__":
    main()
