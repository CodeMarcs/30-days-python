# grade checker

def check_grade(grade):
    if grade >= 90:
        return "A"
    elif grade >= 86:
        return "B"
    elif grade >= 80:
        return "C"
    elif grade >= 78:
        return "D"
    else:
        return "F"
    
grade = float(input("Enter your grade: "))
print(f"Your grade is: {check_grade(grade)}")