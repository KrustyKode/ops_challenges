#!/usr/bin/python3

# Script Name:                  fingerprint.py
# Author:                       Michael Sineiro
# Date of latest revision:      2/26/2024
# Purpose:                      Prompts the user for a URL or IP address. Prompts the user for a port number.
#########                       Performs banner grabbing using Netcat, Telnet, and Nmap against the target address and specified ports.
#########                       Prints the results of each tool to the screen.

import subprocess

def run_netcat(target, port):
    print("\n[+] Starting Netcat for banner grabbing...")
    try:
        # Netcat command for banner grabbing
        result = subprocess.check_output(['nc', '-vz', target, port], stderr=subprocess.STDOUT)
        print(result.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print("Netcat banner grabbing failed:", e.output.decode('utf-8'))

def run_telnet(target, port):
    print("\n[+] Starting Telnet for banner grabbing...")
    try:
        # Using 'echo' to quit telnet session after getting the banner
        result = subprocess.check_output(f'(echo quit; sleep 1) | telnet {target} {port}', shell=True, stderr=subprocess.STDOUT)
        print(result.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print("Telnet banner grabbing failed:", e.output.decode('utf-8'))

def run_nmap(target):
    print("\n[+] Starting Nmap for banner grabbing on well-known ports...")
    try:
        # Nmap command for banner grabbing on well-known ports
        result = subprocess.check_output(['nmap', '-sV', '--open', '-p-', target], stderr=subprocess.STDOUT)
        print(result.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print("Nmap banner grabbing failed:", e.output.decode('utf-8'))

if __name__ == "__main__":
    target = input("Enter the target URL or IP address: ")
    port = input("Enter the target port number: ")

    # Run banner grabbing using Netcat
    run_netcat(target, port)

    # Run banner grabbing using Telnet
    run_telnet(target, port)

    # Run banner grabbing using Nmap on all well-known ports
    run_nmap(target)
