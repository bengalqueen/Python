# Program to check if input is a valid integer

# Taking input from user
num = input("Enter an integer: ")
try:
    # Checking and converting input to integer
    # if input is not a number
    if not num.isdigit():   
        raise ValueError("Invalid input! Not an integer.")

    num = int(num)

    # If valid, print the number
    print("You entered:", num)

# Handling ValueError
except ValueError as e:
    print("Error:", e)