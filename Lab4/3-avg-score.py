# Given a dictionary where the keys are student names and the values are lists of
# scores, WAP to calculate the average score for each student and return it as a
# dictionary.

def cas(scores):
    average_scores = {}
    for student, scores in scores.items():
        if scores:  # Check if the list of scores is not empty
            average = sum(scores) / len(scores)
        else:
            average = 0  # If no scores, set average to 0
        average_scores[student] = average
    
    return average_scores

# Example usage
student_scores = {
    "Alice": [85, 90, 78],
    "Bob": [92, 88, 95],
    "Charlie": [70, 75, 80],
    "David": []
}

average_scores = cas(student_scores)
print("Average Scores:", average_scores)