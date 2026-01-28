# WAP to find the first non-repeating character in a string. If all characters repeat,
# return “None”.

def first_non_repeating_char(input_string):
    frequency_dict = {}
    for char in input_string:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    for char in input_string:
        if frequency_dict[char] == 1:
            return char
    return "None"

input_str = "aayush"
result = first_non_repeating_char(input_str)
print("First Non-Repeating Character:", result)