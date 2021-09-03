"""给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。


示例1：

输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2cv1c/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。"""
from typing import List


def plus_one(digits):
    carry = 1
    i = len(digits) - 1
    while carry == 1:
        if digits[i] == 9:
            digits[i] = 0
            carry = 1
        else:
            digits[i] += 1
            carry = 0

        i -= 1

        if i < 0 and carry == 1:
            return [1] + digits
    return digits


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return plus_one(digits)
