import re
import os

# Script Name:                  pyBasics.py
# Author:                       Michael Sineiro
# Date of latest revision:      12/4/2023
# Purpose:                      Get current user, IP & system info
# Execution:                    python3 pyBasics.py


def getUser():
    """
    Returns the currently logged-in username.
    """
    return os.popen("whoami").read().strip()


def getIP():
  """
  Extracts and returns the IP address of the machine using regular expressions.
  """
  for line in os.popen("ifconfig").read().splitlines():
    match = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
    if match and not line.startswith("lo:"):
      return match.group(0)
  return None


def getInfo():
    """
    Returns a summary of the system hardware using the "lshw" command.
    """
    return os.popen("lshw -short").read()


def details():
    """
    Prints the username, IP address, and system information.
    """
    username = getUser()
    urIP = getIP()
    sysInfo = getInfo()

    if urIP is None:
        print("Error: Unable to find IP address")
    else:
        print(f"Currently logged in user: {username}")
        print(f"IP address of the machine: {urIP}")
        print("A summary of your system hardware:")
        print(sysInfo)

    print("Bash commands executed successfully!")

# Call the display function to execute everything
details()
