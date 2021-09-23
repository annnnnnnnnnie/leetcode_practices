# https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence/
# No. 673
from itertools import filterfalse
from typing import List


class Entry:
    def __init__(self, start, end, size):
        self.start = start
        self.end = end
        self.size = size

    # return a new entry if can grow, None otherwise
    def grow(self, nums, idx):
        if nums[self.end] < nums[idx]:
            return Entry(self.start, idx, self.size + 1)
        else:
            return None

    def __str__(self):
        return f"[{self.start}, {self.end}] size: {self.size}"


# Only look at end = i
def remove_duplicate_entries(all_entries, i):
    entries_end_at_i = list(filter(lambda e: e.end == i, all_entries))
    others = list(filterfalse(lambda e: e.end == i, all_entries))
    result = others
    all_start_index = set(map(lambda e: e.start, entries_end_at_i))
    for start_index in all_start_index:
        candidates = list(filter(lambda e: e.start == start_index, entries_end_at_i))
        if len(candidates) == 1:
            result.extend(candidates)
        else:
            # keep only those with the greatest size
            greatest_size = max(map(lambda e: e.size, candidates))
            valid_candidates = list(filter(lambda e: e.size == greatest_size, candidates))
            result.extend(valid_candidates)
        pass
    return result


def find_number_of_lis(nums):
    assert nums
    if len(nums) <= 1:
        return len(nums)

    all_entries = []
    e = Entry(0, 0, 1)
    all_entries.append(e)

    for i in range(1, len(nums)):
        growth = list(filter(None, map(lambda entry: entry.grow(nums, i), all_entries)))
        all_entries.extend(growth)
        # if current can be appended do not add current
        # else add current
        if not growth:
            all_entries.append(Entry(i, i, 1))

        # if exists multiple entries that start = start, end = end, size < size then try remove
        all_entries = remove_duplicate_entries(all_entries, i)
    all_entries.sort(key=lambda entry: entry.size, reverse=True)

    count = 0
    max_size = all_entries[0].size
    while count < len(all_entries) and all_entries[count].size == max_size:
        count += 1
    return count


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        return find_number_of_lis(nums)
