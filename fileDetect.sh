#!/bin/bash

# Script Name:                  fileDetect.sh
# Author:                       Michael Sineiro
# Date of latest revision:      10/30/2023
# Purpose:                      Check and/or create files/directories
# Execution:                    bash fileDetect.sh ./fileDetect.sh chmod -x fileDetect.sh


# Decleration of variables

# Decleration of functions

# Main
# making Dirs to stick in an array
mkdir dir1 dir2 
# I needed an array
newArray=("dir1" "dir2")

# Ask for user input to specify the file or directory name
read -p "Enter the name of the file or directory: " item

# Check if the file or directory exists
if [[ -e "$item" ]]; then
  echo "$item already exists."
else
  echo "$item File or Dir does not exist, creating now."
  # Create the file or directory
  mkdir -p "$item"
  echo "$item Successfully created."
fi


# End




