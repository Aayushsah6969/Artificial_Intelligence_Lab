# Write a Python program that takes two sets of integers as input and returns a new set
# containing all the elements that are common to both sets, but the common elements
# should be raised to the power of 2.

def common_elements_squared(set1, set2):
    common_elements = set1.intersection(set2)
    squared_elements = {x ** 2 for x in common_elements}
    return squared_elements
# Example usage:
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(common_elements_squared(set_a, set_b))
