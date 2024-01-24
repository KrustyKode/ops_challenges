#!/usr/bin/python3

# Script Name: scapyScan.py
# Author: Michael Sineiro
# Date of latest revision: 1/22/2024
# Purpose: This script is a custom TCP port range scanner and ICMP Ping Sweep tool
#          that uses the Scapy library to test network hosts and ports. It allows for scanning
#          TCP ports within a specified range on a target host and performing an ICMP ping sweep
#          to determine the live hosts in a network.

import re
import threading
from queue import Queue
from scapy.layers.inet import IP, ICMP, TCP
from scapy.sendrecv import sr1, sr
from scapy.volatile import RandShort
from ipaddress import ip_network

# Global variables for verbose mode and open ports list
verbose = False
open_ports = []

def validate_ip(ip):
    """Validate IPv4 address format."""
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if re.match(pattern, ip):
        parts = ip.split('.')
        return all(0 <= int(part) <= 255 for part in parts)
    return False

def validate_port(port):
    """Validate port number within the acceptable range."""
    try:
        port = int(port)
        return 1 <= port <= 65535
    except ValueError:
        return False

def validate_cidr(cidr):
    """Validate network address in CIDR notation."""
    try:
        ip_network(cidr, strict=False)
        return True
    except ValueError:
        return False

print_lock = threading.Lock()

def scan_port(port, target_host):
    """Scan a single TCP port for its status."""
    global verbose
    with print_lock:
        if verbose:
            print(f"Scanning port {port}")
    src_port = RandShort()
    try:
        response = sr1(IP(dst=target_host)/TCP(sport=src_port, dport=port, flags="S"), timeout=1, verbose=0)
        with print_lock:
            if response is not None and response.haslayer(TCP):
                if response[TCP].flags == 0x12:
                    sr(IP(dst=target_host)/TCP(sport=src_port, dport=port, flags="R"), timeout=1, verbose=0)
                    open_ports.append(port)
                    print(f"Port {port}: Open")
                elif verbose:
                    print(f"Port {port}: Closed")
            elif verbose:
                print(f"Port {port}: Closed/Filtered")
    except Exception as e:
        with print_lock:
            print(f"Error scanning port {port}: {e}")

def worker_tcp():
    """Thread worker for TCP port scanning."""
    while not port_queue.empty():
        port = port_queue.get()
        try:
            scan_port(port, target_host)
        finally:
            port_queue.task_done()

def icmp_ping_sweep(network):
    """Perform ICMP ping sweep on the specified network."""
    online_hosts = 0
    for host in ip_network(network).hosts():
        response = sr1(IP(dst=str(host))/ICMP(), timeout=1, verbose=0)
        if response is None:
            print(f"{host} is down or unresponsive.")
        elif response.haslayer(ICMP) and (response[ICMP].type == 3 and response[ICMP].code in [1, 2, 3, 9, 10, 13]):
            print(f"{host} is actively blocking ICMP traffic.")
        else:
            online_hosts += 1
            print(f"{host} is responding.")
    print(f"\nTotal online hosts: {online_hosts}")

if __name__ == "__main__":
    mode = input("Select mode - 1 for TCP Port Range Scanner, 2 for ICMP Ping Sweep: ")
    if mode == "1":
        target_host = input("Enter the IP address of the target host: ")
        while not validate_ip(target_host):
            print("Invalid IP address format. Please enter a valid IP address.")
            target_host = input("Enter the IP address of the target host: ")

        start_port, end_port = map(int, [input("Enter the starting port: "), input("Enter the ending port: ")])
        while not (validate_port(start_port) and validate_port(end_port) and start_port <= end_port):
            print("Invalid port range. Please enter valid starting and ending ports.")
            start_port, end_port = map(int, [input("Enter the starting port: "), input("Enter the ending port: ")])

        verbose = input("Enable verbose mode? (y/n): ").lower() == 'y'

        port_queue = Queue()
        for port in range(start_port, end_port + 1):
            port_queue.put(port)

        num_threads = min(port_queue.qsize(), 10)
        for _ in range(num_threads):
            thread = threading.Thread(target=worker_tcp)
            thread.start()
        for thread in threading.enumerate()[1:]:
            thread.join()

        print("\nOpen ports:")
        for port in sorted(open_ports):
            print(f"Port {port}: Open")

        save_results = input("Save results to a file? (y/n): ").lower() == 'y'
        if save_results:
            with open("scan_results.txt", "w") as file:
                for port in sorted(open_ports):
                    file.write(f"Port {port}: Open\n")
                print("Results saved to scan_results.txt.")

    elif mode == "2":
        network = input("Enter the network address in CIDR notation (e.g., 192.168.1.0/24): ")
        while not validate_cidr(network):
            print("Invalid CIDR notation. Please enter a valid network address in CIDR notation.")
            network = input("Enter the network address in CIDR notation (e.g., 192.168.1.0/24): ")

        icmp_ping_sweep(network)

    else:
        print("Invalid mode selected. Please restart the script and choose a valid mode.")
