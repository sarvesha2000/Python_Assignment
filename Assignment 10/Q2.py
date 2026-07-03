def SumNatural(no):
    total = 0
    for i in range(1, no + 1):
        total += i
    print(total)

no = int(input())
SumNatural(no)
