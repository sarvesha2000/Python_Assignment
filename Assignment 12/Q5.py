# 5. Write a program which accepts one number and prints that many numbers in reverse order.
def PrintReverse(no):
    for i in range(no, 0, -1):
        print(i, end=" ")
    print()

no = int(input())
PrintReverse(no)
