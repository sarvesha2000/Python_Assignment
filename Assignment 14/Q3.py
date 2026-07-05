# 3. Write a lambda function which accepts two numbers and returns maximum number.

maximum = lambda a, b: a if a > b else b

if __name__ == "__main__":
    num1 = 10
    num2 = 20
    print(f"The maximum of {num1} and {num2} is {maximum(num1, num2)}")
