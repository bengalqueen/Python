# Program to find duplicate values from a list and display those

# List of numbers
numbers = [10, 20, 30, 20, 40, 10, 50]

# List to store duplicates
duplicates = []

# Traverse the list
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        # Check if elements are same and not already in duplicates list
        if numbers[i] == numbers[j] and numbers[i] not in duplicates:
            duplicates.append(numbers[i])

# Display duplicates
print("Duplicate values:", duplicates)