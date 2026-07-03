def CheckVowel(ch):
    ch = ch.lower()
    if ch in ['a', 'e', 'i', 'o', 'u']:
        print("Vowel")
    else:
        print("Consonant")

ch = input()
CheckVowel(ch)
