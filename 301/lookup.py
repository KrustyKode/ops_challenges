#!/usr/bin/env python3

# Import libraries
import os

# Script Name:                  lookup.py
# Author:                       Michael Sineiro
# Date of latest revision:      12/5/2023
# Purpose:                      print root, sub & files
# Execution:                    python3 lookup.py

# Declaration of variables

path = input("Enter the directory path: ")

# Declaration of functions

def dirContent(path):
    for (root, dirs, files) in os.walk(path):
        print("== Root Directory ==", root)
        print("== Subdirectories ==", dirs)
        print("== Files ==", files)

# Main

dirContent(path)

# End
