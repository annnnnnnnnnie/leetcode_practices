from typing import List


def move_zeros(nums):
    if len(nums) <= 1:
        return

    digit_pointer = 0

    while digit_pointer < len(nums):
        if nums[digit_pointer] == 0:
            digit_pointer = switch_this_zero_with_next_digit(digit_pointer, nums)
        else:
            digit_pointer += 1
    return


def switch_this_zero_with_next_digit(zero_pointer, nums):
    # if there is a non-zero digit, swap that with this zero. Then return zero pointer + 1
    for i in range(zero_pointer, len(nums)):
        if nums[i] != 0:
            nums[zero_pointer], nums[i] = nums[i], nums[zero_pointer]
            return zero_pointer + 1
    else:
        # if no non-zero digit is present between zero_pointer and len(nums), we are all done. return len(nums)
        return len(nums)


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        move_zeros(nums)
        """
        Do not return anything, modify nums in-place instead.
        """
