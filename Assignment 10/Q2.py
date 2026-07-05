# 2. Write a program which accepts one number and prints sum of first N natural numbers.
def SumNatural(no):
    total = 0
    for i in range(1, no + 1):
        total += i
    print(total)

no = int(input())
SumNatural(no)
