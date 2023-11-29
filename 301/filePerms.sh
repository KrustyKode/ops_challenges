#!/bin/bash

# Script Name:                  filePerms.sh
# Author:                       Michael Sineiro
# Date of latest revision:      11/29/2023
# Purpose:                      prompt for dir path & user permissions
#                               then modifys and prints/appends
# Execution:                    bash filePerms.sh ./filePerms.sh chmod -x filePerms.sh


# Decleration of variables
# dirPath     holds user input for desired directory
# permNum     holds user input for desired user permissions

# while loop that runs until the user enters quit
# prints the echo and prompts for user input
while true; do
    echo "Please enter the directory path:" 
    read dirPath

    # checks if the user wants to quit
    if [ "$dirPath" == "quit" ]; then
        break
    fi
    # prints the echo and prompts for user input
    echo "Please enter the permissions number"
    read permNum
    
    # change dir to users input finds only files and executes
    # the permission changes stored in $permNum using chmod
    cd $dirPath
    find . -type f -exec chmod $permNum {} \;

    # Print directory -l flag shows relevent info
    ls -l

    # print results and append log file.
    echo "The permissions for '$dirPath' have been changed to '$permNum'" >> permChanges.txt
done