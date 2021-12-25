import math
from typing import List


# No. 1705
# https://leetcode-cn.com/problems/maximum-number-of-eaten-apples/

def eaten_apples(apples, days):
    apple_shelf = AppleShelf(0)
    total_apple_count = 0
    for n_apple_today, keep_fresh_day in zip(apples, days):
        apple_shelf.batch_add_apple(n_apple_today, keep_fresh_day)

        apple = apple_shelf.try_get_one_apple()
        if apple:
            total_apple_count += 1

        apple_shelf.forward_one_day()
        pass
    return 0


class AppleShelf:
    def __init__(self, start_date):
        self.date = start_date
        self.apples = PriorityQueue()  # Priority tree based. Key = date. Value = apple count

    def batch_add_apple(self, apple_count, apple_fresh_for):
        """
        O(log n) insertion.
        :param apple_count: How many apples.
        :param apple_fresh_for: Apples expire in ? days.
        :return: None.
        """
        apple_best_until = self.date + apple_fresh_for
        self.apples.insert(apple_best_until, apple_count)

    def forward_one_day(self):
        """
        Increment date. Remove expired apples.
        :return: None.
        """
        self.date += 1
        # Throw away expired apples
        while self.apples.peek().key < self.date:
            self.apples.pop()

    def try_get_one_apple(self):
        """
        Try to get an apple closest to expiry.
        :return: 1 if successfully get, 0 if no apple is on the shelf.
        """
        return 0


class PriorityQueueNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value


def parent(i):
    return i // 2


def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


class PriorityQueue:
    """
    Minimum heap implementation as in CLRS (Introduction to Algorithms 3rd edition) Chapter 6.
    Alternatively, use Lib/queue.PriorityQueue or heapq.
    Min heap property: this.key = min(this.key, lt.key, rt.key).
    Full heap property: The heap is full on all levels except for the leaves.
    """

    def __init__(self):
        self.content: List[PriorityQueueNode] = []

    def heap_decrease_key(self, i, key):
        if key > self.content[i].key:
            raise Exception("New key is larger than current key.")

        self.content[i].key = key
        while i > 0 and self.content[parent(i)].key > self.content[i].key:
            self.content[i], self.content[parent(i)] = self.content[parent(i)], self.content[i]
            i = parent(i)

    def insert(self, key, value):
        self.content.append(PriorityQueueNode(math.inf, value))
        self.heap_decrease_key(len(self.content) - 1, key)

    def peek(self) -> PriorityQueueNode:
        if self.content:
            return self.content[0]
        else:
            raise Exception("Empty priority queue.")

    def min_heapify(self, start_index):
        l = left(start_index)
        r = right(start_index)

        if l < len(self.content) and self.content[l].key < self.content[start_index].key:
            smallest = l
        else:
            smallest = start_index
        if r < len(self.content) and self.content[r].key < self.content[smallest].key:
            smallest = r

        if smallest != start_index:
            self.content[start_index], self.content[smallest] = self.content[smallest], self.content[start_index]
            self.min_heapify(smallest)

    def pop(self) -> PriorityQueueNode:
        if self.content:
            min_element = self.content[0]
            self.content[0] = self.content[-1]
            del self.content[-1]
            self.min_heapify(0)
            return min_element
        else:
            raise Exception("Empty priority queue.")

    def is_empty(self):
        return not self.content


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        return eaten_apples(apples, days)
