# Student Grade Calculator

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "Fail"

# Input
name = input("Enter student name: ")
marks = []

for i in range(5):
    mark = float(input(f"Enter mark {i+1}: "))
    marks.append(mark)

# Calculation
total = sum(marks)
average = total / len(marks)
grade = calculate_grade(average)

# Output
print("\n----- Result -----")
print("Name:", name)
print("Total Marks:", total)
print("Average:", average)
print("Grade:", grade)
