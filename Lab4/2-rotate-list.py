# WAP to rotate a list to the right by k positions, where k is an integer provided as input
# using list.

def rotate_list(input_list, k):
    n = len(input_list)
    k = k % n if n > 0 else 0
    rotated_list = input_list[-k:] + input_list[:-k]
    return rotated_list

original_list = [1, 2, 3, 4, 5]
k = 2
result = rotate_list(original_list, k)
print("Original List:", original_list)
print("List after rotating by", k, "positions:", result)
