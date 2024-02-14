#!/usr/bin/python3

# Script Name:                  logger.py
# Author:                       Michael Sineiro
# Date of latest revision:      1/22/2024
# Purpose:                      now uses RotatingFileHandler.
########                        The log will rotate when it reaches 10KB in size
########                        This process will repeat, maintaining a history of up to 5 old log files plus the current one.


import logging
from logging.handlers import RotatingFileHandler

# Function to configure logging with rotation
def configure_logging():
    """Configure logging to write to a file with rotation."""
    # Create a logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # Set the logging level to DEBUG
    
    # Create a handler for rotating log files
    handler = RotatingFileHandler(
        'app.log', 
        maxBytes=10000,  # Maximum file size in bytes before rotating (e.g., 10KB)
        backupCount=5    # Number of backup files to keep
    )
    
    # Set the format for the log messages
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    # Add the handler to the logger
    logger.addHandler(handler)

def log_error(error_message):
    """Logs an error message to the configured log file."""
    logging.error(error_message)

def log_info(info_message):
    """Logs an informational message to the configured log file."""
    logging.info(info_message)

def safe_input(prompt, data_type):
    """
    Safely prompts the user for input, attempting to convert it to a specified data type.
    If the conversion fails, it logs the error and prompts the user again.
    """
    while True:
        try:
            return data_type(input(prompt))
        except ValueError:
            log_error("Invalid input: Expected a number.")
            print("Invalid input. Please enter a number.")

def divide(a, b):
    """
    Performs division of a by b. Logs the operation and its result if successful.
    In case of a ZeroDivisionError, it logs the error and returns None.
    """
    try:
        result = a / b
        log_info(f"Division result: {a} / {b} = {result}")  # Log the successful division result
        return result
    except ZeroDivisionError:
        log_error("Division by zero error.")
        return None

def main():
    """Main function to execute the application logic."""
    configure_logging()  # Configure logging with rotation at the start
    log_info("Starting the application.")
    numerator = safe_input("Enter the numerator: ", float)  # Ensures input is converted to float
    denominator = safe_input("Enter the denominator: ", float)  # Ensures input is converted to float
    
    result = divide(numerator, denominator)  # Attempts to divide the numbers and logs the result
    if result is not None:
        print(f"The result of the division is: {result}")
    else:
        print("Error: Division by zero.")
    
    log_info("Application finished.")  # Logs the completion of the application's execution

if __name__ == "__main__":
    main()
