from typing import List


def find_occurrences(text, first, second):
    text_list = text.split()
    result = []
    for i in range(len(text_list)):
        if text_list[i] == first:
            if (i + 2) in range(len(text_list)) and text_list[i + 1] == second:
                result.append(text_list[i + 2])
    return result


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        return find_occurrences(text, first, second)
