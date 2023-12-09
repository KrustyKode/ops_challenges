import os


# Create a new file
with open("new_file.txt", "w") as f:
    # Append three lines
    f.write("A line\n")
    f.write("Another line\n")
    f.write("Last line\n")

# Open the file and read the first line
with open("new_file.txt", "r") as f:
    firstLine = f.readline()

# Print the first line
print(f"First line: {firstLine}")

# Delete the file
import os
os.remove("new_file.txt")

print("File deleted successfully.")
