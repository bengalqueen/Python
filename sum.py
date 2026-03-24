# Program to calculate the sum of the numbers in a given tuple.

tuples_list = [(1,2),(3,4),(5,6)]
total = 0
for items in tuples_list:
    # using sum function
    total += sum(items) 

print("Sum of values in the tuples:", total)