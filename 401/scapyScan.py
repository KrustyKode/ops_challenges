#!/usr/bin/python3

# Script Name:                  scapyScan.py
# Author:                       Michael Sineiro
# Date of latest revision:      1/22/2024
# Purpose:                      This script is a custom TCP port range scanner that uses the Scapy library
#########                       to test whether TCP ports are open or closed on a target host. 
#########                       I used chatgpt to help me write this
import re
import threading
from queue import Queue
from scapy.layers.inet import IP, TCP
from scapy.sendrecv import sr1, sr
from scapy.volatile import RandShort

# Validates the format of the given IP address to ensure it's a valid IPv4 address.
def validate_ip(ip):
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if re.match(pattern, ip):
        parts = ip.split('.')
        return all(0 <= int(part) <= 255 for part in parts)  # Each octet must be between 0 and 255
    return False

# Validates that the given port number is within the valid range of 1 to 65535.
def validate_port(port):
    try:
        port = int(port)
        return 1 <= port <= 65535
    except ValueError:
        return False

# Lock for synchronized output in multi-threading environment.
print_lock = threading.Lock()

# Scans a single port by sending a SYN packet and waiting for responses.
def scan_port(port):
    with print_lock:
        print(f"Scanning port {port}")
    src_port = RandShort()  # Use a random source port for scanning
    response = sr1(IP(dst=target_host)/TCP(sport=src_port, dport=port, flags="S"), timeout=1, verbose=0, retry=0)
    with print_lock:
        if response is not None and response.haslayer(TCP):
            if response[TCP].flags == 0x12:  # SYN-ACK indicates port is open
                # Send a RST packet to close the connection
                sr(IP(dst=target_host)/TCP(sport=src_port, dport=port, flags="R"), timeout=1, verbose=0, retry=0)
                open_ports.append(port)
                print(f"Port {port}: Open")
            elif response[TCP].flags == 0x14:  # RST-ACK indicates port is closed
                if verbose:
                    print(f"Port {port}: Closed")
        else:
            if verbose:
                print(f"Port {port}: Closed/Filtered")  # No response or other flags indicate filtering

# Worker thread that processes ports from the queue.
def worker():
    while not port_queue.empty():
        port = port_queue.get()
        try:
            scan_port(port)
        finally:
            port_queue.task_done()

# Main script execution starts here.
if __name__ == "__main__":
    target_host = input("Enter the IP address of the target host: ")
    # Keep prompting for IP until a valid format is entered
    while not validate_ip(target_host):
        print("Invalid IP address format. Please enter a valid IP address.")
        target_host = input("Enter the IP address of the target host: ")

    start_port = input("Enter the starting port: ")
    end_port = input("Enter the ending port: ")
    # Validate port range input
    while not (validate_port(start_port) and validate_port(end_port) and int(start_port) <= int(end_port)):
        print("Invalid port range. Ensure ports are between 1 and 65535 and start port is less than end port.")
        start_port = input("Enter the starting port: ")
        end_port = input("Enter the ending port: ")
    start_port, end_port = int(start_port), int(end_port)

    verbose = input("Enable verbose mode? (y/n): ").lower() == 'y'

    open_ports = []  # List to hold open ports
    port_queue = Queue()  # Queue to hold ports for scanning
    # Populate queue with port range
    for port in range(start_port, end_port + 1):
        port_queue.put(port)

    thread_list = []  # List to hold threads
    # Create and start threads
    for _ in range(10):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in thread_list:
        thread.join()

    # Output the results
    print("\nOpen ports:")
    for port in sorted(open_ports):
        print(f"Port {port}: Open")

    # Optionally, save the results to a file
    save_results = input("Save results to a file? (y/n): ").lower() == 'y'
    if save_results:
        with open("scan_results.txt", "w") as file:
            for port in sorted(open_ports):
                file.write(f"Port {port}: Open\n")
            print("Results saved to scan_results.txt.")
