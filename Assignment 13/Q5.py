# 5. Write a program which accepts marks and displays grade.
def DisplayGrade(marks):
    if marks >= 75:
        print("Distinction")
    elif marks >= 60:
        print("First Class")
    elif marks >= 50:
        print("Second Class")
    else:
        print("Fail")

marks = float(input())
DisplayGrade(marks)
