from typing import List


def single_number(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        n = sum(set(nums)) * 2 - sum(nums)
        return n


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return single_number(nums)
