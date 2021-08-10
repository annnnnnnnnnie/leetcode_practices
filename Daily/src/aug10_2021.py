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


def number_of_arithmetic_slices_fast(nums):
    # 作者：LeetCode - Solution
    # 链接：https://leetcode-cn.com/problems/arithmetic-slices/solution/deng-chai-shu-lie-hua-fen-by-leetcode-so-g7os/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    n = len(nums)
    if n == 1:
        return 0

    d, t = nums[0] - nums[1], 0
    ans = 0

    # 因为等差数列的长度至少为 3，所以可以从 i=2 开始枚举
    for i in range(2, n):
        if nums[i - 1] - nums[i] == d:
            t += 1
        else:
            d = nums[i - 1] - nums[i]
            t = 0
        ans += t

    return ans


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        return number_of_arithmetic_slices(nums)
