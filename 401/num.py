def numText():
    try:
        # Get input from the user
        text = input("Enter some text: ")
        num_times = int(input("Enter the number of times to print the text: "))

        # Print the text the specified number of times
        for _ in range(num_times):
            print(text)

    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Call the function to execute the script
numText()
