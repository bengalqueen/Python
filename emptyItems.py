# Program to get the key, value and item in dictionary

# Given dictionary
input_dict = {1: 10, 2: 20, 3: None, 4: 40, 5: None, 6: 60}

# Create a new dictionary excluding None values
result = {}

for key, value in input_dict.items():
    if value is not None:
        result[key] = value

# Display result
print(result)