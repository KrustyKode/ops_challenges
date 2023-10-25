#!/bin/bash

# Script Name:                  logHist.sh
# Author:                       Michael Sineiro
# Date of latest revision:      10/25/2023
# Purpose:                      write a function that when called
                                # prints the compputers login history
# Execution:                    bash logHist.sh ./logHist.sh chmod -x logHist.sh


# Decleration of variables
last
# Decleration of functions

# Main
userHistory () {
    last
}

userHistory
# End