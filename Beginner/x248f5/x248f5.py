class Solution:
    @staticmethod
    def contains_duplicates(nums):
        all_unique_nums = {}
        for n in nums:
            if n in all_unique_nums:
                return True
            else:
                all_unique_nums[n] = True
        return False
