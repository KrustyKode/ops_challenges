#!/bin/bash

# Script Name:                  conditionals.sh
# Author:                       Michael Sineiro
# Date of latest revision:      11/30/2023
# Purpose:                      Creates a menu and executes some basic commands.
# Execution:                    bash conditionals.sh ./conditionals.sh chmod -x conditionals.sh

# Decleration of variables

# Decleration of functions
function hello {
    echo "Hello world!"
    read -n1 -r -p "Press any key to continue..."
}

function loopback {
    ping -c 1 127.0.0.1
    read -n1 -r -p "Press any key to continue..."
}

function ip {
    ifconfig
    read -n1 -r -p "Press any key to continue..."
}

# Main


while true; do
    clear
    echo "Menu:"
    echo "1. Hello world"
    echo "2. Ping self"
    echo "3. IP info"
    echo "4. Exit"
    read -p "Enter your choice: " choice

    case $choice in
        1)
            hello
            ;;
        2)
            loopback
            ;;
        3)
            ip
            ;;
        4)
            echo "Exiting..."
            exit
            ;;
        *)
            echo "Invalid choice. Press any key to continue..."
            read -n1 -r
            ;;
    esac
done


# End