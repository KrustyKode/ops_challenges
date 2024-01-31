#!/usr/bin/python3

# Script Name: scapyScan3.py
# Author: Michael Sineiro
# Date of latest revision: 1/24/2024
# Purpose: Enhanced network scanning tool with ICMP ping and port scanning functionalities using Scapy.
# This version includes improvements for user input validation, error handling, and feedback.


from concurrent.futures import ThreadPoolExecutor
from scapy.layers.inet import IP, ICMP, TCP
from scapy.sendrecv import sr1, send
from scapy.volatile import RandShort
from ipaddress import ip_address

def validate_ip(ip):
    """Validate the given IP address to ensure it's in a proper IPv4 format."""
    try:
        ip_address(ip)
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
    if not start_port.isdigit() or not end_port.isdigit():
        print("Ports must be numeric. Using default range 1-1024.")
        return target_host, 1, 1024
    start_port, end_port = int(start_port), int(end_port)
    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("Invalid port range. Using default range 1-1024.")
        return target_host, 1, 1024
    return target_host, start_port, end_port

def icmp_ping(target_host):
    """Check if the target host responds to ICMP echo requests (ping)."""
    try:
        pkt = IP(dst=target_host)/ICMP()
        resp = sr1(pkt, timeout=1, verbose=0)
        return resp is not None
    except Exception as e:
        print(f"Error during ICMP ping: {e}")
        return False

def scan_port(target_host, port, result_list):
    """Scan a specific TCP port on the target host and record if it's open."""
    src_port = RandShort()  # Generate a random source port
    try:
        response = sr1(IP(dst=target_host)/TCP(sport=src_port, dport=port, flags="S"), timeout=1, verbose=0)
        if response is not None and response.haslayer(TCP):
            if response[TCP].flags == 0x12:  # Check for SYN/ACK flags
                # Send a RST packet to close the connection
                send(IP(dst=target_host)/TCP(sport=src_port, dport=port, flags="R"), verbose=0)
                result_list.append(port)  # Port is open
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

def port_scan(target_host, start_port, end_port):
    """Perform a TCP port scan on the target host, using threading for efficiency."""
    print(f"Scanning {target_host} for open ports...")
    open_ports = []
    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = [executor.submit(scan_port, target_host, port, open_ports) for port in range(start_port, end_port + 1)]
    return sorted(open_ports)

def main():
    """Main function to orchestrate the scanning process based on user input."""
    target_host, start_port, end_port = get_target_info()
    if icmp_ping(target_host):
        print(f"Host {target_host} is up. Proceeding with port scan...")
        open_ports = port_scan(target_host, start_port, end_port)
        if open_ports:
            print("Open ports:")
            for port in open_ports:
                print(f"Port {port}: Open")
        else:
            print("No open ports found.")
    else:
        print(f"Host {target_host} is down or not responding to ICMP echo requests.")

if __name__ == "__main__":
    main()
