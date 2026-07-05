# 1. Write a program which accepts one number and prints multiplication table of that number.
def DisplayTable(no):
    for i in range(1, 11):
        print(no * i, end=" ")
    print()

no = int(input())
DisplayTable(no)
