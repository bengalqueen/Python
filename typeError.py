# Program to raise TypeError if inputs are not numerical

try:
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    # Check if inputs are digits
    if not (num1.isdigit() and num2.isdigit()):
        raise TypeError("Inputs must be numerical!")

    # Convert to integer
    num1 = int(num1)
    num2 = int(num2)

    print("Sum:", num1 + num2)

except TypeError as e:
    print("Error:", e)