"""
两个数组的交集 II
给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]

说明:

输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
我们可以不考虑输出结果的顺序。
进阶:

如果给定的数组已经排好序呢？你将如何优化你的算法？
如果nums1的大小比nums2小很多，哪种方法更优？
如果nums2的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2y0c2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
from typing import List


def intersection(nums1, nums2):
    if len(nums1) < len(nums2):
        short_nums = nums1
        long_nums = nums2
    else:
        short_nums = nums2
        long_nums = nums1

    verify_dict = {}
    for e in short_nums:
        verify_dict[e] = verify_dict.setdefault(e, 0) + 1

    result = []

    for e in long_nums:
        if e in verify_dict:
            verify_dict[e] -= 1
            if verify_dict[e] == 0:
                del verify_dict[e]
            result.append(e)
    return result


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return intersection(nums1, nums2)
