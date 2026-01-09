# Write a program that takes a list of words and returns a dictionary that maps each
# word to its frequency in the list.
def word_frequency(words):
    frequency_dict = {}
    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1
    return frequency_dict
# Example usage:
words_list = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(word_frequency(words_list))