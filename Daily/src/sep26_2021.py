# https://leetcode-cn.com/problems/sum-of-two-integers/
# No. 371

# a b are 32-bit signed integers
def get_sum(a, b):
    if a == 0:
        return b
    if b == 0:
        return a

    sign = 0  # 0 means positive, 1 means negative
    if a < 0:
        a *= -1  # Note that in two's complement, this is ~a + 1. Which involves addition
        sign ^= 1
    if b < 0:
        b *= -1
        sign ^= 1

    reversed_result = []
    carry = 0
    while a > 0 or b > 0 or carry > 0:
        last_bit_of_a = a % 2
        last_bit_of_b = b % 2
        sum_of_them = last_bit_of_a ^ last_bit_of_b ^ carry
        carry = ((last_bit_of_a ^ last_bit_of_b) & carry) | (last_bit_of_a & last_bit_of_b)
        a >>= 1
        b >>= 1
        reversed_result.append(sum_of_them)

    result = 0
    for bit in reversed_result:
        result <<= 1
        result |= bit

    if sign:  # if sign means negative (sign == 1)
        result *= -1

    return result


def add_binary(a, b):
    result = []

    return 0


def to_bits(n):
    bits = bin(n)[2:]
    return reversed(bits)


class Solution:
    def getSum(self, a: int, b: int) -> int:
        return get_sum(a, b)
