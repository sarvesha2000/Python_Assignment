# 7. Write a lambda function which accepts one number and returns True if divisible by 5.

is_divisible_by_5 = lambda x: True if x % 5 == 0 else False

if __name__ == "__main__":
    num = 15
    print(f"Is {num} divisible by 5? {is_divisible_by_5(num)}")
