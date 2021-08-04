import copy
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return Solution.product_except_self(nums)

    @staticmethod
    def product_except_self(nums):
        if len(nums) <= 2:
            result = copy.deepcopy(nums)
            result.reverse()
            return result

        # Use the product tree as the cache to calculate the result
        pt = Solution.generate_product_tree(nums)

        return [Solution.product_of_one(i, pt) for i in range(len(nums))]

    @staticmethod
    def product_of_one(index, pt):
        return Solution.product_of_one_helper(index, pt, 1)

    @staticmethod
    def product_of_one_helper(index, pt, acc):
        # very similar to binary search, recursively go down the tree to calculate
        if pt.is_singleton():
            return acc

        if index >= pt.middle_index:
            # grab what is on the left and go right
            product = pt.lt.product * acc
            return Solution.product_of_one_helper(index, pt.rt, product)
        else:
            # go left
            product = pt.rt.product * acc
            return Solution.product_of_one_helper(index, pt.lt, product)

    @staticmethod
    def generate_product_tree(nums):
        pts = [ProductTree.singleton(i, nums[i]) for i in range(len(nums))]
        pt = Solution.build_product_tree(pts)
        return pt[0]

    @staticmethod
    def build_product_tree(trees):
        # recursively build the product tree
        output = []
        for i in range(len(trees) // 2):
            output.append(ProductTree.from_lt_rt(trees[2 * i], trees[2 * i + 1]))
        if len(trees) % 2 == 1:
            output.append(trees[-1])

        if len(output) > 1:
            return Solution.build_product_tree(output)
        else:
            return output

    @staticmethod
    def generate_one_level(nums):
        output = []
        for i in range(len(nums) // 2):
            output.append(nums[2 * i] * nums[2 * i + 1])
        if len(nums) % 2 == 1:
            output.append(nums[-1])
        return output


class ProductTree:
    def __init__(self, product, middle_index, lt, rt, min_index):
        self.product = product  # product of all subtree
        self.middle_index = middle_index  # >= middle_index will be in rt
        self.lt = lt
        self.rt = rt
        self.min_index = min_index

    @classmethod
    def from_lt_rt(cls, lt, rt):
        product = lt.product * rt.product
        middle_index = rt.min_index
        min_index = lt.min_index
        return cls(product, middle_index, lt, rt, min_index)

    @classmethod
    def singleton(cls, index, number):
        return cls(number, index, None, None, index)

    def is_singleton(self):
        return not (self.lt and self.rt)

    def __str__(self):
        if self.lt and self.rt:
            return "{}- {} -{}".format(self.lt, self.product, self.rt)
        return "(Leaf {}: {})".format(self.middle_index, self.product)