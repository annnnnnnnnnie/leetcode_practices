import math


class Solution:
    @staticmethod
    def rotate(nums, k):
        k = k % len(nums)
        if k == 0:
            return

        for i in range(math.gcd(len(nums), k)):
            Solution.rotate_one(k, nums, i)

    @staticmethod
    def rotate_one(k, nums, offset):
        read_position = 0 + offset
        write_position = k + offset

        temp = nums[write_position]
        while read_position != (k + offset):
            nums[write_position] = nums[read_position]
            write_position = read_position
            read_position = (read_position - k) % len(nums)
        nums[write_position] = temp
