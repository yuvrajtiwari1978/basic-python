# Demonstrating file handling and exception handling in Python

# File handling: writing to and reading from a file
filename = "example.txt"

# Writing to a file
try:
    file = open(filename, "w")
    file.write("Hello, this is a sample text.\n")
    file.write("This demonstrates file handling in Python.\n")
    file.close()
    print(f"Data written to {filename} successfully.")
except IOError:
    print("Error: Could not write to file.")

# Reading from a file
try:
    file = open(filename, "r")
    print(f"\nContents of {filename}:")
    for line in file:
        print(line, end="")
    file.close()
except IOError:
    print("Error: Could not read file.")
