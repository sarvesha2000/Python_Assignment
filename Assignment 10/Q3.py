# 3. Write a program which accepts one number and prints factorial of that number.
def Factorial(no):
    fact = 1
    for i in range(1, no + 1):
        fact *= i
    print(fact)

no = int(input())
Factorial(no)
