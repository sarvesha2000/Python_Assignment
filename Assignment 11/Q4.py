def ReverseNumber(no):
    rev = 0
    while no > 0:
        rev = rev * 10 + (no % 10)
        no = no // 10
    print(rev)

no = int(input())
ReverseNumber(no)
