from typing import List


# No 581

def find_mono_increasing(nums):
    # pre: len(nums) > 0
    i = 0
    while i < len(nums) - 1 and nums[i] <= nums[i + 1]:
        i += 1
    return i


def find_front_max(nums):
    # first find the index of the end of the first monotonic increasing series
    front_max = find_mono_increasing(nums)
    min_thereafter = min(nums[front_max:])
    while front_max >= 0 and nums[front_max] > min_thereafter:
        front_max -= 1

    return front_max


def find_back_min(nums):
    # reverse, * (-1), then find front max
    reversed_flipped = [i * (-1) for i in reversed(nums)]
    reversed_front_max = find_front_max(reversed_flipped)
    back_min = len(nums) - 1 - reversed_front_max
    return back_min


def find_unsorted_subarray(nums):
    if len(nums) <= 1:
        return 0

    front_max = find_front_max(nums)
    back_min = find_back_min(nums)

    return max(0, back_min - front_max - 1)


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        return find_unsorted_subarray(nums)
