# 3. Write a program which accepts one number and checks whether it is perfect number or not.
def CheckPerfect(no):
    sum_factors = 0
    for i in range(1, no):
        if no % i == 0:
            sum_factors += i
    if sum_factors == no:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")

no = int(input())
CheckPerfect(no)
