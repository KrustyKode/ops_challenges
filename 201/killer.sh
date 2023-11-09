#!/bin/bash

# Script Name:                  killer.sh
# Author:                       Michael Sineiro
# Date of latest revision:      10/27/2023
# Purpose:                      kill processes 
# Execution:                    killer demo.sh ./killer.sh chmod -x killer.sh


# Decleration of variables

# Decleration of functions



### Uses a nested if else loop that continues to rerun if a blank statement is given
### and exits after a valid PID or CTRL+C is entered.
# Main

while true; do
    echo "Processes:"
    ps aux

    read -p "Enter a PID to kill OR Ctrl+C to exit: " pid

    if [ "$pid" == "" ]; then
        echo "Please enter a valid PID."
    else
        kill "$pid"
        echo "PID $pid killed."
    fi
done


# End