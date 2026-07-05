# 6. Write a lambda function using reduce() which accepts a list of numbers and returns the minimum element.

from functools import reduce

if __name__ == "__main__":
    numbers = [15, 2, 34, 8, 21]
    min_element = reduce(lambda a, b: a if a < b else b, numbers)
    print(f"Original list: {numbers}")
    print(f"Minimum element: {min_element}")
