import enum


class ListRepresentation:
    """
    The list is represented as (start, end, step)
    [start,
     start + step,
     start + 2 * step,
     ...,
     end]
    """

    def __init__(self, start, end, step):
        self.start = start  # inclusive
        self.end = end  # inclusive
        self.step = step
        assert (end - start) % step == 0

    def count(self):
        assert self.end >= self.start and (self.end - self.start) % self.step == 0
        return 1 + ((self.end - self.start) // self.step)

    def forward_pass(self):
        if self.count() % 2 != 0:
            self.end = self.end - self.step
        self.start = self.start + self.step
        self.step *= 2

    def backward_pass(self):
        if self.count() % 2 != 0:
            self.start = self.start + self.step
        self.end = self.end - self.step
        self.step *= 2

    def is_singleton(self):
        return self.start == self.end

    def get_result(self):
        assert self.is_singleton()
        return self.start

    def __str__(self):
        return f"[{self.start},{self.end},step={self.step}]"


class Direction(enum.Enum):
    FORWARD = 0
    BACKWARD = 1


def last_remaining(n):
    ls = ListRepresentation(1, n, 1)
    direction = Direction.FORWARD
    while not ls.is_singleton():
        if direction == Direction.FORWARD:
            ls.forward_pass()
            direction = Direction.BACKWARD
        elif direction == Direction.BACKWARD:
            ls.backward_pass()
            direction = Direction.FORWARD
        else:
            raise Exception("Invalid direction encountered")
    result = ls.get_result()
    return result


def last_remaining_slow(n):
    original = [i + 1 for i in range(n)]
    while len(original) > 1:
        next_ls = original[1::2]
        original = list(reversed(next_ls))
    return original[0]


class Solution:
    def lastRemaining(self, n: int) -> int:
        return last_remaining(n)


# if __name__ == '__main__':
#     print([last_remaining_slow(n) for n in range(1, 100)])
