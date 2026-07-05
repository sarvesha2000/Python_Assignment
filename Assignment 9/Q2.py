# 2. Write a program which contains one function ChkGreater() that accepts two numbers and prints the greater number.
def ChkGreater(no1, no2):
    if no1 > no2:
        print(f"{no1} is greater")
    else:
        print(f"{no2} is greater")

no1 = int(input())
no2 = int(input())
ChkGreater(no1, no2)
