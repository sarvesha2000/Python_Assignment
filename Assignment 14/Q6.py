# 6. Write a lambda function which accepts one number and returns True if number is odd otherwise False.

is_odd = lambda x: True if x % 2 != 0 else False

if __name__ == "__main__":
    num = 5
    print(f"Is {num} odd? {is_odd(num)}")
