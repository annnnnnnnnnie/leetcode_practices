import math
from typing import List


# No 313

# List_A : sorted primes
# List_B : super ugly sequence
def generate_super_ugly_sequence(n, sorted_primes):
    result = [0 for _ in range(n)]
    current_comb_table = [(0, 0) for _ in range(n)]  # [(index of List_A, product)]

    current_result_position = 0
    result[current_result_position] = 1
    current_comb_table[0] = (0, sorted_primes[0])

    while current_result_position < n - 1:
        current_result_position += 1

        # Find which one to be appended (the smallest one)
        smallest_comb_indices = []
        smallest_comb_product = math.inf
        for i in range(current_result_position):
            (current_comb_choice, current_comb_product) = current_comb_table[i]

            if current_comb_choice == len(sorted_primes):
                continue

            if current_comb_product <= smallest_comb_product:
                if current_comb_product < smallest_comb_product:
                    smallest_comb_indices = [i]
                else:
                    smallest_comb_indices.append(i)
                smallest_comb_product = current_comb_product

        # Update the result
        result[current_result_position] = smallest_comb_product

        # Update the current_comb_table
        # The used ones
        for s_index in smallest_comb_indices:
            (sorted_prime_index, smallest_comb_product) = current_comb_table[s_index]
            assert smallest_comb_product == sorted_primes[sorted_prime_index] * result[s_index]

            if sorted_prime_index + 1 < len(sorted_primes):
                new_product = result[s_index] * sorted_primes[sorted_prime_index + 1]
                current_comb_table[s_index] = (sorted_prime_index + 1, new_product)
            else:  # Index out of range is handled in the for loop already
                current_comb_table[s_index] = (sorted_prime_index + 1, 0)

        # The new one
        new_product = result[current_result_position] * sorted_primes[0]
        current_comb_table[current_result_position] = (0, new_product)

    return result


def nth_super_ugly_number(n, primes):
    super_ugly_sequence = generate_super_ugly_sequence(n, sorted(primes))
    return super_ugly_sequence[n - 1]


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        return nth_super_ugly_number(n, primes)
