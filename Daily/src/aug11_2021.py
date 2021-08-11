# No 446
import math
from functools import reduce
from typing import List


# distance_matrix[i][j] will contain nums[j] - nums[i]
# j > i
def generate_forward_distance_matrix(nums):
    result = [[nums[j] - nums[i] if j > i else 0 for j in range(len(nums))] for i in range(len(nums))]
    return result


def number_of_arithmetic_slices(nums):
    if len(nums) <= 2:
        return 0

    # key: (start, d)
    # value: the index of elements of this slice
    arithmetic_slices_table = find_all_long_slices(nums)

    total_number_of_slices = 0
    for (fst, d) in arithmetic_slices_table:
        n_ss = len(arithmetic_slices_table[(fst, d)])
        if d == 0:
            total_number_of_slices += number_of_slices_in_all_same_seq_with_length(n_ss)
        else:
            total_number_of_slices += number_of_possible_slices_in_seq_with_length(n_ss)
    return total_number_of_slices


def number_of_slices_in_all_same_seq_with_length(n_ss):
    n = 0
    for i in range(3, n_ss + 1):
        n += math.comb(n_ss, i)
    return n


def number_of_possible_slices_in_seq_with_length(n_ss):
    return sum([n_ss - i + 1 for i in range(3, n_ss + 1)])


# returns True if and only if (_, d) is the key and first is in the value
def already_considered(first, d, arithmetic_slices_table):
    ss = [arithmetic_slices_table[(fst, dist)] for (fst, dist) in arithmetic_slices_table if d == dist]
    if ss:
        potential_matches = reduce(lambda l1, l2: l1 + l2, ss)
        return first in potential_matches
    else:
        return False


# key: (start, d)
# value: the index of elements of this slice
def find_all_long_slices(nums):
    distance_matrix = generate_forward_distance_matrix(nums)
    arithmetic_slices_table = {}
    for first in range(len(nums)):
        for second in range(first + 1, len(nums)):
            d = distance_matrix[first][second]

            # This means that we have already considered the slice with d that contains this point
            if already_considered(first, d, arithmetic_slices_table):
                continue

            # Find the longest possible slice whose first two terms are num[first] and num[second]
            current_slice = find_longest_slice(distance_matrix, first, second)

            # Record that in the arithmetic_slices_table
            if len(current_slice) > 2:
                arithmetic_slices_table[(first, d)] = current_slice
    return arithmetic_slices_table


def find_longest_slice(distance_matrix, first, second):
    d = distance_matrix[first][second]
    current_slice = [first, second]
    current_index = second

    # only [current_index + 1:] part is valid
    while d in distance_matrix[current_index][current_index + 1:]:
        next_index = distance_matrix[current_index].index(d, current_index + 1)
        current_slice.append(next_index)
        current_index = next_index
    return current_slice


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        return number_of_arithmetic_slices(nums)
