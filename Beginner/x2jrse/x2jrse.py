from typing import List


def two_sum(nums, target):
    all_nums = set(nums)

    # Check if two equal entries will add up to the target
    if target % 2 == 0:
        half = target / 2
        if half in all_nums:
            try:
                first_index = nums.index(half)
                second_index = nums.index(half, first_index+1)
                return [first_index, second_index]
            except ValueError as e:
                pass

    # Use two different numbers to add up to the target
    for n in all_nums:
        look_for = target - n
        if look_for in all_nums:
            first_index = nums.index(n)
            second_index = nums.index(look_for)
            return [first_index, second_index]
    raise Exception("Not found")


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return two_sum(nums, target)
