from typing import List


class Solution:
    @staticmethod
    def remove_duplicates(nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        write_position = 0
        read_position = 0
        while read_position < len(nums) - 1:
            read_position += 1
            if nums[read_position] != nums[write_position]:
                write_position += 1
                nums[write_position] = nums [read_position]
        return write_position + 1
