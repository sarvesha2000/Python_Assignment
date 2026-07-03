def EvenNumbers(no):
    for i in range(1, no + 1):
        if i % 2 == 0:
            print(i, end=" ")
    print()

no = int(input())
EvenNumbers(no)
