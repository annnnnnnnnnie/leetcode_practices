# https://github.com/tianyicui/pack
# 背包问题
import numpy as np

"""
Zero-one knapsack problem. N items and a knapsack with size S. Each item :: (cost C, value V)
Find a way to maximize value.
"""


def zero_one_knapsack(items, knapsack_size):
    """
    Find the optimal way of filling backpack of size backpack_size
    :param items: [(cost, value)], denoted by Ci and Vi for the ith item
    :param knapsack_size: int
    :return: max value
    """
    n_items = len(items)

    # table: shape (n_items, backpack_size)
    # table[i][s] means that with a knapsack size s, one can achieve max value considering
    # the first i items (inclusive). i <- [0, n_items].
    # i == 0 means picking from first 0 items, which apparently leads to max value == 0.
    table = [[0 for _ in range(knapsack_size + 1)] for _ in range(n_items + 1)]

    # To reach state [i][s], we either come from [i-1][s] or [i-1][s-Ci]
    # if we come from the former, then table[i][s] == table[i-1][s]
    # if we come from the latter, table[i][s] == table[i-1][s-Ci] + Vi
    # Hence
    # table[i][s] = max(table[i - 1,s], table[i-1, s-Ci] + Vi)

    # start filling the table from table[0][?]
    for i, item in enumerate(items):
        i = i + 1
        Ci = item[0]
        Vi = item[1]
        # start from Ci because if s < Ci, we cannot take the current item
        # and this state will be not interesting.
        # TODO: Still confused here. Review it later.
        for s in range(Ci, knapsack_size + 1):
            table[i][s] = max(table[i - 1][s], table[i - 1][s - Ci] + Vi)
    table_for_debug = np.array(table)
    return table[n_items][knapsack_size]


def zero_one_knapsack_optimize_mem(items, knapsack_size):
    n_items = len(items)

    # Now table[s] will contain the max value after iteration i.
    table = [0 for _ in range(knapsack_size + 1)]

    for i, item in enumerate(items):
        i = i + 1
        Ci = item[0]
        Vi = item[1]
        # This loop is from S to Ci, because the lower part of the table would be
        # storing the result from previous iteration.
        for s in range(knapsack_size, Ci - 1, -1):
            table[s] = max(table[s], table[s - Ci] + Vi)

    table_for_debug = np.array(table)
    return table[knapsack_size]
