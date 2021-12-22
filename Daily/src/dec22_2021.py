# https://leetcode-cn.com/problems/repeated-string-match/
# No. 686
import math


def is_substring(a: str, b: str, i: int):
    """
    Return whether a[i] onwards (inclusive) is b
    :param a: String that would contain b at i
    :param b: String
    :param i: Index
    :return: True if a[i] onwards (inclusive) is b, False otherwise
    """
    return all([c1 == c2 for (c1, c2) in zip(a[i:], b)])


def index_of_slow(a, b):
    """
    Find the smallest index i such that a[i] onwards (inclusive) is b
    This naiive implementation is too slow!
    :param a: String that would contain b
    :param b: String
    :return: i if found, else -1
    """
    assert len(a) >= len(b)
    assert len(b) > 0

    # Search range is range(0, len(a) - len(b) + 1)
    for i in range(len(a) - len(b) + 1):
        if is_substring(a, b, i):
            return i

    return -1


def index_of_fast(a, b):
    # The library function uses The Boyer-Moore-Horspool Algorithm, which is fast
    # https://www.encora.com/insights/the-boyer-moore-horspool-algorithm
    # CPython source: https://github.com/python/cpython/blob/main/Objects/stringlib/fastsearch.h
    return a.find(b)


def repeated_string_match(a, b):
    # Max number of repetition of a would be N + 1, where N * len(a) >= len(b).
    # Min number of repetition would be N, where N * len(a) >= len(b)
    N = math.ceil(len(b) / len(a))

    a_with_n_replicates = a * N
    if index_of_fast(a_with_n_replicates, b) >= 0:
        return N

    a_with_n_plus_one_replicates = a * (N + 1)
    if index_of_fast(a_with_n_plus_one_replicates, b) >= 0:
        return N + 1

    return -1


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        return repeated_string_match(a, b)
