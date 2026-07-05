# 4. Write a program which accepts one number and prints that many numbers starting from 1.
def PrintNumbers(no):
    for i in range(1, no + 1):
        print(i, end=" ")
    print()

no = int(input())
PrintNumbers(no)
