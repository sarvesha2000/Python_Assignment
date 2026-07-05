# 3. Write a program which accepts two numbers and prints addition, subtraction, multiplication and division.
def ArithmeticOperations(no1, no2):
    print(no1 + no2)
    print(no1 - no2)
    print(no1 * no2)
    if no2 != 0:
        print(no1 / no2)

no1 = int(input())
no2 = int(input())
ArithmeticOperations(no1, no2)
