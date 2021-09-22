# https://leetcode-cn.com/problems/split-linked-list-in-parts/
# No. 725

from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def split_list_to_parts(head, k):
    result = []
    length = count(head)
    size = length // k
    remainder = length % k
    current = head
    tail = current
    for _ in range(k - 1):
        entry, tail = cut(current, size + (1 if remainder > 0 else 0))
        remainder -= 1
        current = tail
        result.append(entry)
    result.append(tail)
    return result


def count(head):
    current = head
    n = 0
    while current:
        n += 1
        current = current.next
    return n


def cut(head, n):
    if not head:
        return None, None
    else:
        current = head
        prev = current
        for _ in range(n):
            prev = current
            current = current.next
        prev.next = None
    return head, current


class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        return split_list_to_parts(head, k)
