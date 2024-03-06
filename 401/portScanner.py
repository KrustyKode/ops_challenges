#!/usr/bin/python3

# Script Name:                  malwareScan.py
# Author:                       Michael Sineiro
# Date of latest revision:      2/20/2024
# Purpose:                      malware scanner that recursively scans a specified directory,

import socket

# Create a socket object
sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Set a timeout value
timeout = 10  # Example: 10 seconds
sockmod.settimeout(timeout)

# Collect a host IP from the user
hostip = input("Enter the host IP address: ")

# Collect a port number from the user, then convert it to an integer data type
portno = int(input("Enter the port number to scan: "))

def portScanner(port):
    try:
        # Try to connect to the port
        connection = sockmod.connect_ex((hostip, port))
        if connection == 0:
            print("Port", port, "is open")
        else:
            print("Port", port, "is closed")
    finally:
        # Ensures the socket is closed, which is good practice to free up resources
        sockmod.close()

portScanner(portno)
