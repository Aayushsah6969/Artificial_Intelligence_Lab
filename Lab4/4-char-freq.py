# WAP to count the frequency of each character in a given string and store the result in
# a dictionary.

def char_frequency(input_string):
    # Create an empty dictionary to store character frequencies
    frequency_dict = {}
    
    # Loop through each character in the input string
    for char in input_string:
        # If the character is already in the dictionary, increment its count
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            # If the character is not in the dictionary, add it with a count of 1
            frequency_dict[char] = 1
    
    return frequency_dict

# Example usage
input_str = "hello world computer lab"
result = char_frequency(input_str)
print("Character Frequencies:", result)