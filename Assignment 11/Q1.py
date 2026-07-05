# 1. Write a program which accepts one number and checks whether it is prime or not.
def CheckPrime(no):
    if no <= 1:
        print("Not a Prime Number")
        return
    for i in range(2, no):
        if no % i == 0:
            print("Not a Prime Number")
            return
    print("Prime Number")

no = int(input())
CheckPrime(no)
