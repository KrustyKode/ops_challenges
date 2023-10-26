#!/bin/bash

# Script Name:                  array.sh
# Author:                       Michael Sineiro
# Date of latest revision:      10/26/2023
# Purpose:                      Demo array
# Execution:                    bash array.sh ./array.sh chmod -x array.sh


# Decleration of variables

mkdir dir1
mkdir dir2
mkdir dir3
mkdir dir4

newDir=("dir1" "dir2" "dir3" "dir4")

# Decleration of functions
for i in "${!newDir[@]}"; do
  filename="test.txt"
  touch "${newDir[$i]}/$filename"
done



# Main


# End