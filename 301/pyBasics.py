import re
import os


def get_username():
    """
    Returns the currently logged-in username.
    """
    return os.popen("whoami").read().strip()


def get_ip_address():
  """
  Extracts and returns the IP address of the machine using regular expressions.
  """
  for line in os.popen("ifconfig").read().splitlines():
    match = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
    if match and not line.startswith("lo:"):
      return match.group(0)
  return None


def get_system_info():
    """
    Returns a summary of the system hardware using the "lshw" command.
    """
    return os.popen("lshw -short").read()


def display_system_details():
    """
    Prints the username, IP address, and system information.
    """
    username = get_username()
    ip_address = get_ip_address()
    system_info = get_system_info()

    if ip_address is None:
        print("Error: Unable to find IP address")
    else:
        print(f"Currently logged in user: {username}")
        print(f"IP address of the machine: {ip_address}")
        print("A summary of your system hardware:")
        print(system_info)

    print("Bash commands executed successfully!")

# Call the display function to execute everything
display_system_details()
