# Script Name:                  uptime2.py
# Author:                       Michael Sineiro
# Date of latest revision:      1/10/2024
# Purpose:                      pings a target host and returns "Active" or "Nonactive"
###############                 continues until told to stop. Sends an email with the first pings status 
###############                 & if network status changes.

import os
import time
import subprocess
import smtplib
from email.mime.text import MIMEText

def ping(target_ip):
    """Sends a ping to the target IP and returns status."""
    response = subprocess.run(["ping", "-c", "1", target_ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return response.returncode == 0

def send_email(sender_email, password, receiver_email, message):
    """Send an email notification using SMTP."""
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    server.quit()

def main():
    """Main function to continuously monitor uptime and send email notifications on status change."""
    target_ip = input("Enter target IP address: ")
    sender_email = "realjohnhalo117@gmail.com"
    password = input("Enter your email password: ")
    receiver_email = sender_email  

    log_file = open("ping_log.txt", "a")
    previous_status = None

    while True:
        # making timestamp and pinging
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        current_status = "Active" if ping(target_ip) else "Inactive"

        # Send an email if this is the first ping or if there's a status change
        if previous_status is None or current_status != previous_status:
            status_change = "Initial Ping" if previous_status is None else f"Changed from {previous_status} to"
            message = f"Subject: Host Status Update\n\nStatus of {target_ip} {status_change} {current_status} at {timestamp}"
            send_email(sender_email, password, receiver_email, message)

        # Print the status and timestamp to the console and log file
        print(f"{timestamp} Network {current_status} to {target_ip}")
        log_file.write(f"{timestamp} Network {current_status} to {target_ip}\n")

        # Ensure log data is written; sleep three seconds and repeat.
        log_file.flush()
        time.sleep(3)
        previous_status = current_status       

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting uptime sensor tool.")
