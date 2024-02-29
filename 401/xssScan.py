#!/usr/bin/env python3

# Author:      Abdou Rockikz
# Description: This script scans web pages for potential XSS and SQL Injection vulnerabilities
# Date:        2/28/24
# Modified by: Mike Sineiro

# Note: Install requests and bs4 before executing this in Python3
# pip install requests beautifulsoup4

# Import libraries

import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# Function to get all forms from the given URL
def get_all_forms(url):
    """Fetches and returns all forms from a given webpage URL."""
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

# Function to extract details from a form
def get_form_details(form):
    """Extracts and returns the details of a given form, including its action, method, and inputs."""
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

# Function to submit a form with given details
def submit_form(form_details, url, value):
    """Submits a form with the provided details and returns the response."""
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        # For SQLi scanning, we replace the payload with SQLi specific code
        input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value", "")
        if input_name:
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

# Function to scan for XSS vulnerabilities
def scan_xss(url):
    """Scans for XSS vulnerabilities by submitting forms with a JavaScript payload designed to test for XSS."""
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url} for XSS scanning.")
    # Malicious JavaScript code for testing XSS
    js_script = "<script>alert('XSS')</script>"
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = True
    return is_vulnerable

# Function to scan for SQL Injection vulnerabilities
def scan_sqli(url):
    """Scans for SQL Injection vulnerabilities by submitting forms with SQL error-inducing payloads."""
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url} for SQL Injection scanning.")
    sqli_payload = "' OR '1'='1"
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, sqli_payload).content.decode()
        error_messages = ["MySQL", "Warning: mysql", "Unclosed quotation mark", "Microsoft OLE DB Provider for SQL Server"]
        if any(error_message in content for error_message in error_messages):
            print(f"[+] SQL Injection Detected on {url}")
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = True
    return is_vulnerable

# Main function
if __name__ == "__main__":
    """Main function that prompts the user for a URL and scans the URL for XSS and SQL Injection vulnerabilities."""
    url = input("Enter a URL to test for vulnerabilities:") 
    print("Scanning for XSS vulnerabilities...")
    if scan_xss(url):
        print("XSS vulnerability detected.")
    else:
        print("No XSS vulnerability detected.")
    print("Scanning for SQL Injection vulnerabilities...")
    if scan_sqli(url):
        print("SQL Injection vulnerability detected.")
    else:
        print("No SQL Injection vulnerability detected.")


# Instructions for Web Security Dojo Testing:
# 1. Run this script and use the target URLs provided for positive and negative XSS detection.
# 2. For positive detection, use: https://xss-game.appspot.com/level1/frame
#    Expected output: Indication of XSS detection with form details.
# 3. For negative detection, use: http://dvwa.local/login.php
#    Expected output: Message indicating no XSS vulnerability detected.
