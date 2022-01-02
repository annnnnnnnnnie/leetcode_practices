import numpy as np

"""
N items and knapsack size S. item :: (cost C, value V).
Each item has infinite copies.
"""


def knapsack_complete(items, knapsack_size):
    return 0


def preprocess_item_list(items, knapsack_size):
    """
    Throws away items with C > knapsack_size.
    Throws away items i when there exists item j such that: Vi <= Vj and Ci == Cj
    Note: Does not throw away i when Ci > Cj and Vi <= Vj due to bad implementation
    :param items: [(cost, value)]
    :param knapsack_size: int
    :return: preprocessed item_list
    """
    result = {}  # key: cost, value: item value
    for item in items:
        cost = item[0]
        value = item[1]
        if cost > knapsack_size:
            continue
        elif cost in result:
            old_value = result[cost]
            if value > old_value:
                result[cost] = value
        else:
            result[cost] = value
    return list(result.items())
