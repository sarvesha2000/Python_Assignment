# 2. Write a program which accepts one number and prints count of digits in that number.
def CountDigits(no):
    count = 0
    while no > 0:
        count += 1
        no = no // 10
    print(count)

no = int(input())
CountDigits(no)
