# Program to get the largest and smallest number from a list without builtin functions

# List of numbers
numbers = [10, 25, 5, 40, 15]

# Assume first element is both smallest and largest
smallest = numbers[0]
largest = numbers[0]

# Traverse the list
for num in numbers:
    if num < smallest:
        smallest = num   # Update smallest
    
    if num > largest:
        largest = num    # Update largest

# Print results
print("Smallest number:", smallest)
print("Largest number:", largest)