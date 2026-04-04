# Program to handle FileNotFoundError

try:
    # Trying to open a file
    file = open("data.txt", "r")

    # Reading and printing file content
    content = file.read()
    print("File Content:\n", content)

    # Closing the file
    file.close()

# This block handles the error if file does not exist
except FileNotFoundError:
    print("Error: File not found. Please check the file name or path.")

# This block always executes
finally:
    print("Program executed.")