#!/usr/bin/python3

# Script Name:                  pymap.py
# Author:                       Michael Sineiro
# Date of latest revision:      3/5/2024

import nmap

scanner = nmap.PortScanner()

print("Nmap Automation Tool")
print("--------------------")

ip_addr = input("IP address to scan: ")
print("The IP you entered is: ", ip_addr)

resp = input("""\nSelect scan to execute:
                1) SYN ACK Scan
                2) UDP Scan
                3) Comprehensive Scan\n""")
print("You have selected option: ", resp)

# Prompt the user for a port range
range = input("Enter the port range to scan (e.g., 1-1024): ")

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", list(scanner[ip_addr]['tcp'].keys()))
elif resp == '2':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sU')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    # UDP scan might not find all protocols, hence checking before printing
    if 'udp' in scanner[ip_addr].all_protocols():
        print("Open UDP Ports: ", list(scanner[ip_addr]['udp'].keys()))
    else:
        print("No UDP ports found or UDP scan not supported for this IP.")
elif resp == '3':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -A')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    # Comprehensive scan includes more than just TCP/UDP, so check each
    if 'tcp' in scanner[ip_addr].all_protocols():
        print("Open TCP Ports: ", list(scanner[ip_addr]['tcp'].keys()))
    if 'udp' in scanner[ip_addr].all_protocols():
        print("Open UDP Ports: ", list(scanner[ip_addr]['udp'].keys()))
else:
    print("Please enter a valid option")
