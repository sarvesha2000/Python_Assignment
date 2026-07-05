# 7. Write a lambda function using filter() which accepts a list of strings and returns a list of strings having length greater than 5.

if __name__ == "__main__":
    strings = ["apple", "banana", "kiwi", "orange", "pear", "strawberry"]
    long_strings = list(filter(lambda s: len(s) > 5, strings))
    print(f"Original list: {strings}")
    print(f"Strings with length > 5: {long_strings}")
