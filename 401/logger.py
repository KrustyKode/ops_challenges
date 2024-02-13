#!/usr/bin/python3

# Script Name:                  scapyScan.py
# Author:                       Michael Sineiro
# Date of latest revision:      1/22/2024
# Purpose:                      This script is a custom TCP port range scanner that uses the Scapy library
#########                       to test whether TCP ports are open or closed on a target host. 
#########                       I used chatgpt to help me write this

import logging

# Configure logging
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def log_error(error_message):
    logging.error(error_message)

def log_info(info_message):
    logging.info(info_message)

def safe_input(prompt, data_type):
    while True:
        try:
            return data_type(input(prompt))
        except ValueError:
            log_error("Invalid input: Expected a number.")
            print("Invalid input. Please enter a number.")

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        log_error("Division by zero error.")
        return None

def main():
    log_info("Starting the application.")
    numerator = safe_input("Enter the numerator: ", float)
    denominator = safe_input("Enter the denominator: ", float)
    result = divide(numerator, denominator)

    if result is not None:
        print(f"The result of the division is: {result}")
    else:
        print("Error: Division by zero.")
    
    log_info("Application finished.")

if __name__ == "__main__":
    main()
