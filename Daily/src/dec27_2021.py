# No. 825
# https://leetcode-cn.com/problems/friends-of-appropriate-ages/
# TODO: wrong solution
from typing import List


def find_num_friend_requests_for(sorted_ages, this_index):
    n_friend_req = 0
    this_age = sorted_ages[this_index]
    other_index = this_index
    while other_index + 1 < len(sorted_ages) and sorted_ages[other_index + 1] == this_age:
        other_index += 1

    while 0 <= other_index:
        other_age = sorted_ages[other_index]
        if other_age > this_age:
            break

        if (other_age <= 100 or this_age >= 100) \
                and this_index != other_index \
                and other_age > 0.5 * this_age + 7:
            n_friend_req += 1

        other_index -= 1
    return n_friend_req


def num_friend_requests(ages):
    # cond_0 === window = (0.5 * this + 7, this]
    # cond_1 === other <= 100 or this >= 100
    # cond_2 === this > 14
    sorted_ages = sorted(ages)
    assert sorted_ages
    candidate_index = 0
    while sorted_ages[candidate_index] < 15 and candidate_index + 1 < len(sorted_ages):
        candidate_index += 1
    if sorted_ages[candidate_index] < 15:
        return 0

    total_num_friend_requests = 0
    while candidate_index < len(sorted_ages):
        num_friend_requests_for_this_candidate = find_num_friend_requests_for(sorted_ages, candidate_index)
        total_num_friend_requests += num_friend_requests_for_this_candidate
        candidate_index += 1

    return total_num_friend_requests


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        return num_friend_requests(ages)
