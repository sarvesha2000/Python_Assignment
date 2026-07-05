# 5. Write a program which accepts one number and prints all odd numbers till that number.
def OddNumbers(no):
    for i in range(1, no + 1):
        if i % 2 != 0:
            print(i, end=" ")
    print()

no = int(input())
OddNumbers(no)
