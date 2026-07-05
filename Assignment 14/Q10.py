# 10. Write a lambda function which accepts three numbers and returns largest number.

largest = lambda a, b, c: max(a, b, c)
# Alternatively without max: lambda a, b, c: a if (a >= b and a >= c) else (b if b >= c else c)

if __name__ == "__main__":
    num1, num2, num3 = 10, 25, 15
    print(f"The largest of {num1}, {num2}, and {num3} is {largest(num1, num2, num3)}")
