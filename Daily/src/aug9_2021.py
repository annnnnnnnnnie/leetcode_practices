import copy
from typing import List


# combination: [x,y,z]
def is_triangle(combination):
    x, y, z = sorted(combination)
    return x + y > z and x > 0 and y > 0 and z > 0


def triangle_number(nums):
    if len(nums) < 3:
        return 0
    count = len([combination for combination in list_choose_r_fast(nums, 3) if is_triangle(combination)])
    return count


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


def list_choose_r_fast(ls, r):
    table = [[[] for i in range(r)] for j in range(len(ls))]
    return list_choose_r_dp(ls, r, 0, table)


# with a look-up table to cache the result
# ls[start:] choose r
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


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        return triangle_number(nums)
