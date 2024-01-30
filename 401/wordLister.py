# Script Name:                  wordLister.py
# Author:                       Michael Sineiro
# Date of latest revision:      1/29/2024
# Purpose:                      allows a user to iterate through a wordlist/
###############                 check if a string exists in a list/
###############                 checks password complexity.
###############                 I used chatGPT to help me write pieces of this script.

import time
import re
import os
import threading
from queue import Queue

def readWordList(filePath):
    """
    Reads a word list from a specified file path.
    Returns the list of words if the file is found, or None if the file is not found.
    """
    try:
        with open(filePath, 'r', encoding='utf-8', errors='ignore') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
        return None

def processWord(word, index, total, delay=0.5):
    """
    Process a single word with a delay.
    """
    print(f"Trying word {index}/{total}: {word}")
    time.sleep(delay)

def offensiveMode(filePath, num_threads=5):
    """
    Offensive Mode with threading: Processes words in the word list concurrently.
    """
    wordList = readWordList(filePath)
    if wordList is not None:
        # Create a queue to hold words and their indices
        wordQueue = Queue()
        for index, word in enumerate(wordList, start=1):
            wordQueue.put((word, index, len(wordList)))

        # Worker function for threads
        def worker():
            while not wordQueue.empty():
                word, index, total = wordQueue.get()
                processWord(word, index, total)
                wordQueue.task_done()

        # Create and start threads
        threads = []
        for _ in range(num_threads):
            thread = threading.Thread(target=worker)
            thread.start()
            threads.append(thread)

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

def defensiveMode(inputString, filePath):
    """
    Defensive Mode: Checks if a user input string is in the word list.
    """
    wordList = readWordList(filePath)
    if wordList:
        if inputString in wordList:
            print("The string is in the word list")
        else:
            print("The string is not in the word list")

def passwordComplexity(password):
    """
    Password Complexity Mode: Checks the complexity of a given password
    based on predetermined criteria.
    """
    # Password complexity criteria
    criteria = {
        'length': (8, '8 characters'),
        'uppercase': (1, '1 uppercase letter'),
        'digits': (1, '1 digit'),
        'symbols': (1, '1 symbol')
    }

    # Check if the password meets each criterion
    checks = {
        'length': len(password) >= criteria['length'][0],
        'uppercase': len(re.findall(r'[A-Z]', password)) >= criteria['uppercase'][0],
        'digits': len(re.findall(r'\d', password)) >= criteria['digits'][0],
        'symbols': len(re.findall(r'\W', password)) >= criteria['symbols'][0]
    }

    satisfied = all(checks.values())
    for key, value in checks.items():
        print(f"{criteria[key][1]} requirement {'met' if value else 'not met'}.")

    if satisfied:
        print("SUCCESS: All password complexity requirements satisfied.")
    else:
        print("Password does not meet all complexity requirements.")

def main():
    """
    Main function: Provides a menu for users to select a mode and 
    processes the user's choice.
    """
    while True:
        print("\nSelect mode:\n 1 - Offensive\n 2 - Defensive\n 3 - Password Complexity\n 4 - Exit")
        mode = input("Enter your choice: ")

        if mode == '1':
            filePath = input("Enter word list file path: ")
            if os.path.isfile(filePath):
                offensiveMode(filePath)
            else:
                print("Invalid file path. Please try again.")
        elif mode == '2':
            inputString = input("Enter a string to search for: ")
            filePath = input("Enter word list file path: ")
            if os.path.isfile(filePath):
                defensiveMode(inputString, filePath)
            else:
                print("Invalid file path. Please try again.")
        elif mode == '3':
            password = input("Enter a password to check for complexity: ")
            passwordComplexity(password)
        elif mode == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid mode selected. Please try again.")

if __name__ == "__main__":
    main()
