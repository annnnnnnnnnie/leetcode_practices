import collections

# If you need to import additional packages or classes, please import here.
from functools import reduce
from math import factorial


def compute_permutations(line):
    n_total = len(line)
    ctr = collections.Counter(line)
    n_total_factorial = factorial(n_total)
    denominator = reduce(lambda x, y: x * y, map(factorial, map(lambda item: item[1], ctr.items())))
    return n_total_factorial / denominator


def func():
    # please define the python3 input here. For example: a,b = map(int, input().strip().split())
    line = input().strip()
    # please finish the function body here.
    num_permutations = compute_permutations(line)
    # please define the python3 output here. For example: print().
    print(int(num_permutations))


if __name__ == "__main__":
    func()
