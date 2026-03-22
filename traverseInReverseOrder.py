# Program to traverse a given list in reverse order and print the elements with the original index

# Original list
colors = ['red', 'green', 'white', 'black']

# Traverse the list in reverse 
for i in range(len(colors) - 1, -1, -1):
    print(colors[i])