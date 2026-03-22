# Program to split a given list into two parts

# Original list
numbers = [1, 1, 2, 3, 4, 4, 5, 1]

# Length of first part
k = 3

# Split the list
first_part = numbers[:k]   # First 3 elements
second_part = numbers[k:]  # Remaining elements

# Display results
print((first_part, second_part))