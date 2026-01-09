# Given a list of integers, write a Python program to find the longest increasing
# subsequence. The function should return the length of the subsequence and the
# subsequence itself. Ensure that the subsequence is a continuous subsequence (not
# necessarily unique).

def longest_increasing_subsequence(arr):
    max_length = 1
    current_length = 1
    start_index = 0
    max_start_index = 0

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
                max_start_index = start_index
            current_length = 1
            start_index = i

    # Final check at the end of the loop
    if current_length > max_length:
        max_length = current_length
        max_start_index = start_index

    longest_subseq = arr[max_start_index:max_start_index + max_length]
    return max_length, longest_subseq

# Example usage:
input_list = [10, 22, 9, 33, 21, 50, 41, 60, 80]
length, subsequence = longest_increasing_subsequence(input_list)
print("Length of longest increasing subsequence:", length)
print("Longest increasing subsequence:", subsequence)
