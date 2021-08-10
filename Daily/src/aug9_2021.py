import math
from typing import List
import heapq


# No 313

class PotentialCombination:
    def __init__(self, result_position, sorted_primes, super_ugly_numbers):
        self.result_position = result_position
        self.sorted_primes = sorted_primes
        self.super_ugly_numbers = super_ugly_numbers

        self.n_sorted_primes = len(self.sorted_primes)
        self.sorted_primes_index = 0
        self.product = self.calculate_product()

    def next_comb(self):
        self.sorted_primes_index += 1
        if self.is_in_range():
            self.product = self.calculate_product()

    def calculate_product(self):
        return self.super_ugly_numbers[self.result_position] * self.sorted_primes[self.sorted_primes_index]

    def is_in_range(self):
        return self.sorted_primes_index < self.n_sorted_primes

    def __lt__(self, other):
        return self.product < other.product


def generate_super_ugly_sequence_heap(n, sorted_primes):
    # n_sorted_primes = len(sorted_primes)
    result = [0 for _ in range(n)]
    comb_heap = []  # entry: PotentialCombination

    result[0] = 1

    initial_comb = PotentialCombination(0, sorted_primes, result)

    heapq.heappush(comb_heap, initial_comb)

    for current_result_position in range(1, n):

        # Pops from the heap the smallest ones
        smallest_product = comb_heap[0].product
        all_smallest_combs = []
        while comb_heap and comb_heap[0].product == smallest_product:
            small_comb = heapq.heappop(comb_heap)
            all_smallest_combs.append(small_comb)

        # Update the result
        result[current_result_position] = smallest_product

        # Update the comb_heap
        # The used ones
        for comb in all_smallest_combs:
            comb.next_comb()
            if comb.is_in_range():
                heapq.heappush(comb_heap, comb)

        # The new one
        new_comb = PotentialCombination(current_result_position, sorted_primes, result)
        heapq.heappush(comb_heap, new_comb)

    return result


# List_A : sorted primes
# List_B : super ugly sequence
def generate_super_ugly_sequence(n, sorted_primes):
    n_sorted_primes = len(sorted_primes)
    result = [0 for _ in range(n)]
    current_comb_table = [(0, 0) for _ in range(n)]  # [(index of List_A, product)]

    current_result_position = 0
    result[current_result_position] = 1
    current_comb_table[0] = (0, sorted_primes[0])

    for current_result_position in range(1, n):

        # Find which one to be appended (the smallest one)
        smallest_comb_indices, smallest_comb_product = find_smallest_combs(current_comb_table, current_result_position,
                                                                           n_sorted_primes)

        # Update the result
        result[current_result_position] = smallest_comb_product

        # Update the current_comb_table
        # The used ones
        for s_index in smallest_comb_indices:
            (sorted_prime_index, smallest_comb_product) = current_comb_table[s_index]
            assert smallest_comb_product == sorted_primes[sorted_prime_index] * result[s_index]

            if sorted_prime_index + 1 < n_sorted_primes:
                new_product = result[s_index] * sorted_primes[sorted_prime_index + 1]
                current_comb_table[s_index] = (sorted_prime_index + 1, new_product)
            else:  # Index out of range is handled in the for loop already
                current_comb_table[s_index] = (sorted_prime_index + 1, 0)

        # The new one
        new_product = result[current_result_position] * sorted_primes[0]
        current_comb_table[current_result_position] = (0, new_product)

    return result


def find_smallest_combs(current_comb_table, current_result_position, n_sorted_primes):
    smallest_comb_indices = []
    smallest_comb_product = math.inf
    for i in range(current_result_position):
        (current_comb_choice, current_comb_product) = current_comb_table[i]

        if current_comb_choice == n_sorted_primes:
            continue

        if current_comb_product <= smallest_comb_product:
            if current_comb_product < smallest_comb_product:
                smallest_comb_indices = [i]
            else:
                smallest_comb_indices.append(i)
            smallest_comb_product = current_comb_product
    return smallest_comb_indices, smallest_comb_product


def nth_super_ugly_number(n, primes):
    super_ugly_sequence = generate_super_ugly_sequence_heap(n, sorted(primes))
    return super_ugly_sequence[n - 1]


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        return nth_super_ugly_number(n, primes)
