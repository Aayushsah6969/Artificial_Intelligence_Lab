# WAP that removes all duplicate elements from a list without using set() and
# preserves the original order. write code invery simpleandbginner friendly way.

def remove_duplicates(input_list):
    # Create an empty list to store unique elements
    unique_list = []
    
    # Loop through each element in the input list
    for item in input_list:
        # If the item is not already in the unique list, add it
        if item not in unique_list:
            unique_list.append(item)
    
    return unique_list  

# Example usage
original_list = [1, 2, 2, 3, 4, 4, 5, 1]
result = remove_duplicates(original_list)
print("Original List:", original_list)
print("List after removing duplicates:", result)

