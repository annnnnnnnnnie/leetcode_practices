# If you need to import additional packages or classes, please import here.
from functools import reduce


def format_vowels(c):
    vowels = "AEIOU"
    if c.upper() in vowels:
        return c.upper()
    else:
        return c.lower()


def func():
    # please define the python3 input here. For example: a,b = map(int, input().strip().split())
    line = input()
    # please finish the function body here.
    result = reduce(lambda c1, c2: c1 + c2, map(format_vowels, line))
    # please define the python3 output here. For example: print().
    print(result)


if __name__ == "__main__":
    func()
