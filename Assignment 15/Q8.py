# 8. Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.

if __name__ == "__main__":
    numbers = [10, 15, 20, 25, 30, 35, 45]
    divisible_by_3_and_5 = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, numbers))
    print(f"Original list: {numbers}")
    print(f"Numbers divisible by 3 and 5: {divisible_by_3_and_5}")
