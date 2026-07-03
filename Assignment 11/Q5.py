def CheckPalindrome(no):
    temp = no
    rev = 0
    while no > 0:
        rev = rev * 10 + (no % 10)
        no = no // 10
    if temp == rev:
        print("Palindrome")
    else:
        print("Not a Palindrome")

no = int(input())
CheckPalindrome(no)
