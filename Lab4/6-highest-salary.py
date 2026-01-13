# WAP that takes a dictionary where keys are employee names and values are their
# respective salaries. Return the top 3 employees with the highest salaries in
# descending order. If there are ties, sort by name alphabetically.

def tths(salary_dict):
    sorted_salaries = sorted(salary_dict.items(), key=lambda item: (-item[1], item[0]))
    top_three = sorted_salaries[:3]
    
    return top_three    
employee_salaries = {
    "Alice": 75000,
    "Bob": 82000,
    "Charlie": 82000,
    "David": 60000,
    "Eve": 75000
}

top_employees = tths(employee_salaries)
print("Top 3 Employees with Highest Salaries:", top_employees)