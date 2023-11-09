#!/bin/bash

# Script Name:                  logHist.sh
# Author:                       Michael Sineiro
# Date of latest revision:      10/25/2023
# Purpose:                      write a function that when called
                                # prints the compputers login history
# Execution:                    bash logHist.sh ./logHist.sh chmod -x logHist.sh


# Decleration of variables
# last - calls a list of the recent logins.
num=1

# Decleration of functions
userHistory () {
    last
}
# Main

for ((i=0; i<=3; i++)); do
    userHistory &
done

# End