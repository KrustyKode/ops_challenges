#!/bin/bash

# Script Name:                  logger.sh
# Author:                       Michael Sineiro
# Date of latest revision:      11/28/2023
# Purpose:                      copy syslogs to pwd and append with dateTime
# Execution:                    bash logger.sh ./logger.sh chmod -x logger.sh


# Decleration of variables

# Get the current date and time in YYYY-MM-DD format
dateTime=$(date +"%Y-%m-%d @ %H:%M:%S" )

# Decleration of functions

# Main

# Copy the syslog file to the current working directory
cp /var/log/syslog test.txt

# append the test.txt file with date and time.
echo "date: $dateTime" >> test.txt