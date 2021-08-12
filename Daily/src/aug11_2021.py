# No 446
import itertools
import math
import operator
from functools import reduce
from typing import List


# distance_matrix[i][j] will contain nums[j] - nums[i]
# j > i
def generate_forward_distance_matrix(nums):
    # Initialize to -1 such that d == 0 will not match the invalid parts of the matrix
    result = [[nums[j] - nums[i] if j > i else -1 for j in range(len(nums))] for i in range(len(nums))]
    return result


def number_of_arithmetic_slices(nums):
    if len(nums) <= 2:
        return 0

    # key: (start, d)
    # value: the index of elements of this slice
    arithmetic_slices_table = find_all_long_slices(nums)

    total_number_of_slices = 0
    for ((_, _), sls) in arithmetic_slices_table.items():
        total_number_of_slices += len(sls)
    return total_number_of_slices


def number_of_slices_in_all_same_seq_with_length(n_ss):
    n = 0
    for i in range(3, n_ss + 1):
        n += math.comb(n_ss, i)
    return n


def number_of_possible_slices_in_seq_with_length(n_ss):
    return n_ss - 2


# returns True if and only if (_, d) is the key and first is in any of the value
def already_considered(first, d, arithmetic_slices_table):
    sss = [slices for ((_, dist), slices) in arithmetic_slices_table.items() if d == dist]
    if sss:
        ss = reduce(operator.add, sss)
        return any(first in s for s in ss)
    else:
        return False


# key: (start, d)
# value: the list of (indices of elements of one slice)
def find_all_long_slices(nums):
    distance_matrix = generate_forward_distance_matrix(nums)
    arithmetic_slices_table = {}
    for first in range(len(nums)):
        for second in range(first + 1, len(nums)):
            d = distance_matrix[first][second]

            # Find the longest possible slice whose first two terms are num[first] and num[second]
            current_slices = find_longest_slices(distance_matrix, first, second)

            # Record that in the arithmetic_slices_table
            current_slices = list(filter(lambda s: len(s) > 2, current_slices))
            if current_slices:
                arithmetic_slices_table[(first, d)] = \
                    arithmetic_slices_table.setdefault((first, d), []) + current_slices
    return arithmetic_slices_table


def find_longest_slices(distance_matrix, first, second):
    d = distance_matrix[first][second]

    current_node_index = second

    potential_tails = dfs_to_find_longest_slices(current_node_index, distance_matrix, d)
    result = list(map(lambda xs: [first] + xs, potential_tails))
    return result


# returns [[ , , ], [ , , ], [ , , ], [a long slice with d starting at node] ...]
def dfs_to_find_longest_slices(node_index, distance_matrix, d):
    next_nodes = [idx for (idx, dist) in enumerate(distance_matrix[node_index]) if dist == d]
    potential_tails = []
    for next_node in next_nodes:
        potential_tails_for_this_node = dfs_to_find_longest_slices(next_node, distance_matrix, d)
        potential_tails.extend(potential_tails_for_this_node)

    if potential_tails:
        result = list(map(lambda xs: [node_index] + xs, potential_tails)) + [[]]  # if anyone wishes to early terminate
    else:
        result = [[node_index]] + [[]]
    return result


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        return number_of_arithmetic_slices(nums)
