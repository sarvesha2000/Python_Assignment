# 10. Write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers.

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_count = len(list(filter(lambda x: x % 2 == 0, numbers)))
    print(f"Original list: {numbers}")
    print(f"Count of even numbers: {even_count}")
