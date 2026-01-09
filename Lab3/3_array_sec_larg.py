# Function to find the second largest number
def second_largest(numbers):
    
    numbers.sort()          # sort the array
    return numbers[-2]      # second last element


# Example
nums = [10, 5, 8, 20, 15]
print(second_largest(nums))
