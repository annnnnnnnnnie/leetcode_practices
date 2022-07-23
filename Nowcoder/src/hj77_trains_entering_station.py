import itertools
from typing import List


def is_valid_sequence(seq: List[int], trains: List[int]) -> bool:
    stack = []
    for out_train in seq:
        # try pop from stack
        if stack and stack[-1] == out_train:
            stack.pop()
        # else push trains into stack
        else:
            while trains:
                train = trains.pop(0)
                if train == out_train:
                    break
                else:
                    stack.append(train)
            else:
                return False
    return True


def all_permutations(trains: List[int]) -> List[List[int]]:
    itertools.permutations
    pass


def train_sequence(trains: List[int]) -> str:
    pass


def main():
    pass


if __name__ == '__main__':
    main()
