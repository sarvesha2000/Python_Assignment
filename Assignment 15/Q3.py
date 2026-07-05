# 3. Write a lambda function using filter() which accepts a list of numbers and returns a list of odd numbers.

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
    print(f"Original list: {numbers}")
    print(f"List of odd numbers: {odd_numbers}")
