import copy
from itertools import dropwhile
from typing import List


# combination: [x,y,z]
def is_triangle(combination):
    x, y, z = sorted(combination)
    return x + y > z and x > 0 and y > 0 and z > 0


def triangle_number_comb(nums):
    if len(nums) < 3:
        return 0
    count = len([combination for combination in list_choose_r_fast(nums, 3) if is_triangle(combination)])
    return count


def list_choose_r_fast(ls, r):
    table = [[[] for i in range(r)] for j in range(len(ls))]
    return list_choose_r_dp(ls, r, 0, table)


# with a look-up table to cache the result
# returns the choices of ls[start:] choose r
# result stored in table[start][r-1]
def list_choose_r_dp(ls, r, start, table):
    assert r > 0

    # choose r elements from the list
    n = len(ls) - start
    if n < r:
        raise Exception("Cannot nCr when r > n")

    if n == r:
        result = [copy.deepcopy(ls[start:])]

    elif r == 1:
        result = [[x] for x in ls[start:]]

    else:
        result = []
        for i in range(start, len(ls) - r + 1):
            x = ls[i]
            new_start = i + 1
            if table[new_start][r - 2]:
                rest_choose = table[new_start][r - 2]
            else:
                rest_choose = list_choose_r_dp(ls, (r - 1), new_start, table)
                table[new_start][r - 2] = rest_choose
            for_this_x = [([x] + rc) for rc in rest_choose if rc]
            result.extend(for_this_x)

    table[start][r - 1] = result
    return result


def triangle_number_binary(nums):
    sorted_nums = list(dropwhile((lambda x: x <= 0), sorted(nums)))

    n = len(sorted_nums)
    count = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):

            max_length_exclusive = sorted_nums[i] + sorted_nums[j]

            if sorted_nums[j + 1] >= max_length_exclusive:
                # This means that this pair of i j ? will never work
                continue
            else:
                # use binary search to find the index that makes a triangle
                index = binary_search(sorted_nums, max_length_exclusive, j + 1, n)

                # shift the index to the right to account for duplicates
                while index + 1 < n and sorted_nums[index] == sorted_nums[index + 1]:
                    index += 1

                count += index - j

    return count


# returns the index i such that
# start <= i < end
# sorted_nums[i] < max_length_exclusive
def binary_search(sorted_nums, max_length_exclusive, start, end):
    if end - start == 1:
        return start
    else:
        middle = (start + end) // 2
        if sorted_nums[middle] < max_length_exclusive:
            return binary_search(sorted_nums, max_length_exclusive, middle, end)
        else:
            return binary_search(sorted_nums, max_length_exclusive, start, middle)


def triangle_number_loop(nums):
    if len(nums) < 10:
        return triangle_number_comb(nums)

    count = 0
    n = len(nums)
    sorted_nums = sorted(nums)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                edge_1 = sorted_nums[i]
                edge_2 = sorted_nums[j]
                edge_3 = sorted_nums[k]
                if is_triangle([edge_1, edge_2, edge_3]):
                    count += 1
                else:
                    break
    return count


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        return triangle_number_binary(nums)


# returns list of r-list-tuples
# e.g. [[1,2,3],[1,2,4],[1,3,4],[2,3,4]]
def list_choose_r(ls, r):
    assert r > 0

    # choose r elements from the list
    if len(ls) < r:
        return []
    elif len(ls) == r:
        return [copy.deepcopy(ls)]

    if r == 1:
        return [[x] for x in ls]
    else:
        result = []
        for i in range(0, len(ls) - r + 1):
            x = ls[i]
            rest = ls[(i + 1):]
            rest_choose = list_choose_r(rest, (r - 1))
            for_this_x = [([x] + rc) for rc in rest_choose if rc]
            result += for_this_x

        return result
