import requests

# Script Name:                  reqs.py
# Author:                       Michael Sineiro
# Date of latest revision:      12/13/2023
# Purpose:                      Creates a menu that executes requests methods
#########                       
# Execution:                    python3 reqs.py



class HttpRequester:
    """
    This class handles sending HTTP requests and analyzing the responses.
    """

    def __init__(self):
        """
        This method initializes the class with a dictionary of human-readable
        descriptions for common HTTP status codes.
        """
        self.statusCode = {
            200: "OK",
            404: "Site not found",
            401: "Unauthorized",
            403: "Forbidden",
            500: "Internal Server Error",
        }

    def send_request(self):
        """
        This method prompts the user for a URL, validates it, selects an HTTP method,
        sends the request, and displays the response.
        """
        url = ""
        isValid = False

        # Loop until a valid URL is entered
        while not isValid:
            url = input("Enter URL: ")
            if url.startswith("http") or url.startswith("https"):
                isValid = True
            else:
                print("Invalid URL format. Please try again.")

        # Define a dictionary mapping numbers to HTTP methods
        methMenu = {
            1: "GET",
            2: "POST",
            3: "PUT",
            4: "DELETE",
            5: "HEAD",
            6: "PATCH",
            7: "OPTIONS",
        }

        # Prompt the user to select an HTTP method
        print("Select HTTP Method:")
        for key, value in methMenu.items():
            print(f"{key}. {value}")

        choice = None
        while not choice:
            try:
                choice = int(input("Enter method number: "))
                if choice not in methMenu:
                    raise ValueError
            except ValueError:
                print("Invalid selection. Please enter a valid number.")

        # Get the chosen HTTP method from the dictionary
        method = methMenu[choice]

        # Print information about the request
        print(f"-- Sending {method.upper()} request to {url} --")

        try:
            # Send the request using the requests library
            response = requests.request(method, url)
        except Exception as error:
            # Handle any errors during the request
            print(f"Error: {error}")
            return

        # Print the response headers
        print("-- Response Headers --")
        for key, value in response.headers.items():
            print(f"{key}: {value}")

        # Print the status code and its human-readable description
        print(f"-- Status Code: {response.status_code}")
        print(f"({self.statusCode.get(response.status_code, 'Unknown code')}) --")


        # Check if the response contains text content
        if response.content:
            contentType = response.headers.get("Content-Type")
            if contentType and "text" in contentType:
                # Decode and formatting
                content = response.content.decode()
                print("\n-- Response Content --\n", content)
            else:
                print("-- Response content not text. Skipping display. --")

        # Print a completion message
        print("-- Request complete! --")


# Run the program to send a request
requester = HttpRequester()
requester.send_request()
