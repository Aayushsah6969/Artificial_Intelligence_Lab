# WAP to find the longest substring of a given string where all characters are unique.
# Return both the substring and its length.

def longest_unique_substring(input_string):
    start = 0
    max_length = 0
    longest_substr = ""
    char_index_map = {}
    
    for i, char in enumerate(input_string):
        # If the character is already in the map and its index is within the current window
        if char in char_index_map and char_index_map[char] >= start:
            # Move the start to the next position after the last occurrence of the character
            start = char_index_map[char] + 1
        
        # Update the character's latest index
        char_index_map[char] = i
        
        # Calculate the length of the current substring
        current_length = i - start + 1
        
        # Update max_length and longest_substr if we found a longer substring
        if current_length > max_length:
            max_length = current_length
            longest_substr = input_string[start:i+1]
    
    return longest_substr, max_length

# Example usage
input_str = "abcabcbbuiwqyjbdfjsadgh"
result_substr, result_length = longest_unique_substring(input_str)
print("Longest Unique Substring:", result_substr)
print("Length of Longest Unique Substring:", result_length)