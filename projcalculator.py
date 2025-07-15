#Student Grade Calculator: Take marks and calculate average and grade.
def calculate_grade(marks):
    average = sum(marks) / len(marks)
    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return average, grade   
