# 9. Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements.

from functools import reduce

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    product = reduce(lambda a, b: a * b, numbers)
    print(f"Original list: {numbers}")
    print(f"Product of all elements: {product}")
