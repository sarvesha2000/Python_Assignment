# 5. Write a lambda function which accepts one number and returns True if number is even otherwise False.

is_even = lambda x: True if x % 2 == 0 else False

if __name__ == "__main__":
    num = 4
    print(f"Is {num} even? {is_even(num)}")
