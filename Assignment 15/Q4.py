# 4. Write a lambda function using reduce() which accepts a list of numbers and returns the addition of all elements.

from functools import reduce

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    total_sum = reduce(lambda a, b: a + b, numbers)
    print(f"Original list: {numbers}")
    print(f"Addition of all elements: {total_sum}")
