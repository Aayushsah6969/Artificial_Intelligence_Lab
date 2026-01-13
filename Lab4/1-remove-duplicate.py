# WAP that removes all duplicate elements from a list without using set() and
# preserves the original order. write code invery simpleandbginner friendly way.

def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    
    return unique_list  

original_list = [1, 2, 2, 3, 4, 4, 5, 1]
result = remove_duplicates(original_list)
print("Original List:", original_list)
print("List after removing duplicates:", result)

