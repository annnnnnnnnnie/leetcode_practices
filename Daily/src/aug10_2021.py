from typing import List


# No 413

def number_of_arithmetic_slices_starting_from(n, nums):
    if len(nums) - n < 3:  # less than 3 elements left in the list (inclusive)
        return 0

    total_slices = 0
    d = nums[n + 1] - nums[n]
    for i in range(n + 2, len(nums)):
        if nums[i] - nums[i - 1] == d:
            total_slices += 1
        else:
            break
    return total_slices


def number_of_arithmetic_slices(nums):
    total_slices = 0
    for n in range(len(nums)):
        total_slices += number_of_arithmetic_slices_starting_from(n, nums)
    return total_slices


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        return number_of_arithmetic_slices(nums)
