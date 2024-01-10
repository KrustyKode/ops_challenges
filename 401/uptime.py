# Script Name:                  lockScreen.ps1
# Author:                       Michael Sineiro
# Date of latest revision:      1/18/2024
# Purpose:                      configures auto-lock-screen, windows scans, and OS updates.


# Script Name:                  lockScreen.ps1
# Author:                       Michael Sineiro
# Date of latest revision:      1/18/2024
# Purpose:                      Configures auto-lock-screen, windows scans, and OS updates.

import os
import time
import subprocess

def ping(target_ip):
    """Sends a ping to the target IP and returns status."""
    # Run the ping command with subprocess and check the return code
    response = subprocess.run(["ping", "-c", "1", target_ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return response.returncode == 0

def main():
    """Main function to continuously monitor uptime."""
    # Get the target IP address from user input
    target_ip = input("Enter target IP address: ")
    
    # Open or create a log file in append mode
    log_file = open("ping_log.txt", "a")

    while True:
        # Get the current timestamp
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S.%f")

        # Check the status of the network by sending a ping
        status = "Active" if ping(target_ip) else "Inactive"

        # Print the status and timestamp to the console and log file
        print(f"{timestamp} Network {status} to {target_ip}")
        log_file.write(f"{timestamp} Network {status} to {target_ip}\n")

        # Ensure log data is written; sleep three seconds and repeat.
        log_file.flush()
        time.sleep(3)        

if __name__ == "__main__":
    try:
        # Call the main function
        main()
    except KeyboardInterrupt:
        # (Ctrl+C) to exit
        print("Exiting uptime sensor tool.")
