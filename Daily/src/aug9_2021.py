import copy
from typing import List


# combination: [x,y,z]
def is_triangle(combination):
    x, y, z = sorted(combination)
    return x + y > z and x > 0 and y > 0 and z > 0


def triangle_number(nums):
    if len(nums) < 3:
        return 0
    count = len([combination for combination in list_choose_r(nums, 3) if is_triangle(combination)])
    return count


# returns list of r-list-tuples
# e.g. [[1,2,3],[1,2,4],[1,3,4],[2,3,4]]
def list_choose_r(ls, r):
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


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        return triangle_number(nums)
