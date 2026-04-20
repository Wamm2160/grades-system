def add_grade(grades, grade):
    if grade < 0 or grade > 10: 
        raise ValueError("Grade must be between 0 and 10")
    grades.append(grade)
    return grades

def calculate_average(grades):
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)

grades = []

grades = add_grade(grades, 8)
grades = add_grade(grades, 10)

print("Average:", calculate_average(grades))
