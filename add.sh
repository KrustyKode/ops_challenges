#!/bin/bash

# Script Name:                  HDemo.sh
# Author:                       Michael Sineiro
# Date of latest revision:      10/25/2023
# Purpose:                      Demo variables / and functions
# Execution:                    bash add.sh ./add.sh chmod -x add.sh


# Decleration of variables
read -p "please type the first number: " num1
read -p "please type the second number: " num2


# Decleration of functions

add_two_numbers() {
    sum=$(($num1 + $num2))
    echo $sum
}


# Main

add_two_numbers



# End