#!/usr/bin/python3

# Script Name: scapyScanEnhanced.py
# Author: Michael Sineiro
# Date of latest revision: 1/24/2024
# Purpose: This script enhances the original network scanning tool by combining ICMP ping and port scanning functionalities.
#          It utilizes Scapy for network interactions, aiming for improved efficiency, modularity, and user experience.

import re
import threading
from concurrent.futures import ThreadPoolExecutor
from scapy.all import *
from ipaddress import ip_address

def validate_ip(ip):
    """Validate the given IP address to ensure it's in a proper IPv4 format."""
    try:
        ip_address(ip)  # Attempts to create an IPv4Address object from the provided IP.
        return True
    except ValueError:
        return False

def get_target_info():
    """Prompt the user for the target IP address and port range, ensuring the input is valid."""
    target_host = input("Enter the IP address of the target host: ")
    while not validate_ip(target_host):
        print("Invalid IP address format. Please try again.")
        target_host = input("Enter the IP address of the target host: ")

    start_port = input("Enter the starting port: ")
    end_port = input("Enter the ending port: ")
    if not start_port.isdigit() or not end_port.isdigit() or int(start_port) > int(end_port):
        print("Invalid port range. Using default range 1-1024.")
        start_port, end_port = 1, 1024  # Defaults to a common range if input is invalid.
    else:
        start_port, end_port = int(start_port), int(end_port)

    return target_host, start_port, end_port

def icmp_ping(target_host):
    """Check if the target host responds to ICMP echo requests (ping)."""
    pkt = IP(dst=target_host)/ICMP()
    resp = sr1(pkt, timeout=1, verbose=0)  # Sends a single ICMP echo request to the target.
    return resp is not None  # True if a response was received, indicating the host is up.

def scan_port(target_host, port, result_list):
    """Scan a specific TCP port on the target host and record if it's open."""
    pkt = IP(dst=target_host)/TCP(dport=port, flags='S')
    resp = sr1(pkt, timeout=1, verbose=0)  # Sends a SYN packet to initiate a TCP connection.
    if resp is not None and TCP in resp and resp[TCP].flags & 0x12:  # Checks for SYN/ACK response, indicating an open port.
        result_list.append(port)  # Adds the open port to the list.

def port_scan(target_host, start_port, end_port):
    """Perform a TCP port scan on the target host, using threading for efficiency."""
    print(f"Scanning {target_host} for open ports...")
    open_ports = []  # List to store open ports found during the scan.
    with ThreadPoolExecutor(max_workers=50) as executor:  # Utilizes a thread pool to manage concurrent scans efficiently.
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, target_host, port, open_ports)  # Submits port scan tasks to the thread pool.
    return sorted(open_ports)  # Returns a sorted list of open ports.

def main():
    """Main function to orchestrate the scanning process based on user input."""
    target_host, start_port, end_port = get_target_info()  # Retrieves target information from the user.
    if icmp_ping(target_host):
        print(f"Host {target_host} is up. Proceeding with port scan...")
        open_ports = port_scan(target_host, start_port, end_port)  # Conducts the port scan if the host is responsive.
        if open_ports:
            print("Open ports:")  # Lists open ports if any were found.
            for port in open_ports:
                print(f"Port {port}: Open")
        else:
            print("No open ports found.")  # Indicates no open ports were detected.
    else:
        print(f"Host {target_host} is down or not responding to ICMP echo requests.")  # Host did not respond to ping.

if __name__ == "__main__":
    main()
