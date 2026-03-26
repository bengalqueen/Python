# Program to remove items from set1 that are not common to both set1 and set2

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Keep only common elements in set1
set1.intersection_update(set2)

# Print updated set1
print(set1)