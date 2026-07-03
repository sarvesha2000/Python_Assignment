def PrintFactors(no):
    for i in range(1, no + 1):
        if no % i == 0:
            print(i, end=" ")
    print()

no = int(input())
PrintFactors(no)
