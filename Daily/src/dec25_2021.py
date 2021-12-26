import math
from typing import Optional


# No. 1609
# https://leetcode-cn.com/problems/even-odd-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


def convert_tree_to_list(root):
    result = []
    current_level = [root]
    result.append(current_level)
    while current_level:
        next_level = []
        for t in current_level:
            if t.left:
                next_level.append(t.left)
            if t.right:
                next_level.append(t.right)
        result.append(next_level)
        current_level = next_level
    return result[:-1]


def is_all_odd(ns):
    return all(map(lambda n: n % 2 == 1, ns))


def is_all_even(ns):
    return all(map(lambda n: n % 2 == 0, ns))


def is_increasing(ns):
    current = -math.inf
    for n in ns:
        if n <= current:
            return False
        else:
            current = n
    return True


def is_decreasing(ns):
    current = math.inf
    for n in ns:
        if n >= current:
            return False
        else:
            current = n
    return True


def is_odd_and_increasing(ts):
    ns = list(map(lambda t: t.val, ts))
    return is_increasing(ns) and is_all_odd(ns)


def is_even_and_decreasing(ts):
    ns = list(map(lambda t: t.val, ts))
    return is_decreasing(ns) and is_all_even(ns)


def is_even_odd_tree(root):
    assert root
    nodes = convert_tree_to_list(root)
    odd_layers = nodes[::2]
    even_layers = nodes[1::2]
    odd_layers_ok = all(map(lambda ts: is_odd_and_increasing(ts), odd_layers))
    even_layers_ok = all(map(lambda ts: is_even_and_decreasing(ts), even_layers))
    result = odd_layers_ok and even_layers_ok
    return result


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        return is_even_odd_tree(root)
