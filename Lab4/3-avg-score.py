# Given a dictionary where the keys are student names and the values are lists of
# scores, WAP to calculate the average score for each student and return it as a
# dictionary.

def calculate_average_scores(scores_dict):
    # Create an empty dictionary to store average scores
    average_scores = {}
    
    # Loop through each student and their scores in the input dictionary
    for student, scores in scores_dict.items():
        # Calculate the average score
        if scores:  # Check if the list of scores is not empty
            average = sum(scores) / len(scores)
        else:
            average = 0  # If no scores, set average to 0
        
        # Store the average score in the new dictionary
        average_scores[student] = average
    
    return average_scores

# Example usage
student_scores = {
    "Alice": [85, 90, 78],
    "Bob": [92, 88, 95],
    "Charlie": [70, 75, 80],
    "David": []
}

average_scores = calculate_average_scores(student_scores)
print("Average Scores:", average_scores)