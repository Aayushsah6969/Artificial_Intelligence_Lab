# WAP to rotate a list to the right by k positions, where k is an integer provided as input
# using list.

def rotate_list(input_list, k):
    # Get the length of the list
    n = len(input_list)
    
    # Handle cases where k is greater than the length of the list
    k = k % n if n > 0 else 0
    
    # Rotate the list by slicing
    rotated_list = input_list[-k:] + input_list[:-k]
    
    return rotated_list

# Example usage
original_list = [1, 2, 3, 4, 5]
k = 2
result = rotate_list(original_list, k)
print("Original List:", original_list)
print("List after rotating by", k, "positions:", result)
