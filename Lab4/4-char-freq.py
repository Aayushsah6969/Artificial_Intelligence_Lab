# WAP to count the frequency of each character in a given string and store the result in
# a dictionary.

def char_frequency(input_string):
    frequency_dict = {}
    for char in input_string:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    
    return frequency_dict
input_str = "hello"
result = char_frequency(input_str)
print("Character Frequencies:", result)