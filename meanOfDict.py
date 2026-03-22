# Program to calculate mean of the given dictionary

# Given dictionary
test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}

# Calculate sum of values
total = sum(test_dict.values())

# Number of values
count = len(test_dict)

# Calculate mean
mean = total / count

print("Mean:", mean)