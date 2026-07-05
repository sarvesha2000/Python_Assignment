# 3. Write a program which accepts one number and prints sum of digits.
def SumDigits(no):
    total = 0
    while no > 0:
        total += no % 10
        no = no // 10
    print(total)

no = int(input())
SumDigits(no)
