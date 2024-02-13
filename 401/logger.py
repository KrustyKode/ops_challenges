#!/usr/bin/python3

# Script Name:                  logger.py
# Author:                       Michael Sineiro
# Date of latest revision:      1/22/2024
# Purpose:                      simple script that gene

import logging

# Configuration for logging: sets up the log file, log level, and log message format
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def log_error(error_message):
    """Logs an error message to the configured log file."""
    logging.error(error_message)

def log_info(info_message):
    """Logs an informational message to the configured log file."""
    logging.info(info_message)

def safe_input(prompt, data_type):
    """
    Prompts the user for input, converting it to the specified data type.
    Repeats the prompt until valid input is received.
    """
    while True:
        try:
            return data_type(input(prompt))
        except ValueError:
            log_error("Invalid input: Expected a number.")
            print("Invalid input. Please enter a number.")

def divide(a, b):
    """
    Attempts to divide two numbers, a and b.
    Logs an error and returns None if division by zero is attempted.
    """
    try:
        return a / b
    except ZeroDivisionError:
        log_error("Division by zero error.")
        return None

def main():
    """Main function to run the application."""
    log_info("Starting the application.")
    # Prompt the user for numerator and denominator, ensuring input is converted to float
    numerator = safe_input("Enter the numerator: ", float)
    denominator = safe_input("Enter the denominator: ", float)
    
    # Perform the division operation
    result = divide(numerator, denominator)

    # Output the result or an error message, if division by zero occurred
    if result is not None:
        print(f"The result of the division is: {result}")
    else:
        print("Error: Division by zero.")
    
    log_info("Application finished.")

if __name__ == "__main__":
    main()
