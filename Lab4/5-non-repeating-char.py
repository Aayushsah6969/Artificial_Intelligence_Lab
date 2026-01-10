# WAP to find the first non-repeating character in a string. If all characters repeat,
# return “None”.

def first_non_repeating_char(input_string):
    # Create an empty dictionary to store character frequencies
    frequency_dict = {}
    
    # Loop through each character in the input string to count frequencies
    for char in input_string:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    
    # Loop through the input string again to find the first non-repeating character
    for char in input_string:
        if frequency_dict[char] == 1:
            return char
    
    # If no non-repeating character is found, return "None"
    return "None"

# Example usage
input_str = "aayush"
result = first_non_repeating_char(input_str)
print("First Non-Repeating Character:", result)