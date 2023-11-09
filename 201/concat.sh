#!/bin/bash

# Script Name:                  concat.sh
# Author:                       Michael Sineiro
# Date of latest revision:      10/26/2023
# Purpose:                      Demo concatination
# Execution:                    bash concat.sh ./concat.sh chmod -x concat.sh


# Decleration of variables
firstName="Mike"
lastName="Sineiro"

fullName=$firstName$lastName
# fullName=$firstName" "lastName

echo $fullName

concatTwoStrings () {
    string1=$1"  "$2
    echo $string1
}

concatTwoStrings $firstName $lastName
# Decleration of functions

# Main


# End