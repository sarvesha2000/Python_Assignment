# 4. Write a program which accepts one number and prints binary equivalent.
def BinaryEquivalent(no):
    print(bin(no).replace("0b", ""))

no = int(input())
BinaryEquivalent(no)
