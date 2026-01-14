# WAP to find the longest substring of a given string where all characters are unique.
# Return both the substring and its length.

def longest_unique_substring(input_string):
    start = 0
    max_length = 0
    longest_substr = ""
    char_index_map = {}
    
    for i, char in enumerate(input_string):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        char_index_map[char] = i
        current_length = i - start + 1
        
        if current_length > max_length:
            max_length = current_length
            longest_substr = input_string[start:i+1]
    
    return longest_substr, max_length

# Example usage
input_str = "abcabcbbuiwqyjbdfjsadgh"
result_substr, result_length = longest_unique_substring(input_str)
print("Longest Unique Substring:", result_substr)
print("Length of Longest Unique Substring:", result_length)