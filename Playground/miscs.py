def partition(xs):
    result = []
    current_partitions = [([], xs)]
    result.extend(current_partitions)
    for i in range(len(xs) // 2):
        next_partitions = partition_helper(current_partitions)
        result.extend(next_partitions)
        current_partitions = next_partitions
    return result


def partition_helper(partitions):
    """
    Compute all the next partitions
    :param partitions: [(left, right), (left, right), ...]
    :return: all possible partitions one step after
    """
    result = []
    for p in partitions:
        result.extend(step(p[0], p[1]))
    return result


def step(left, right):
    return [(left + [x], right[:i] + right[(i + 1):]) for i, x in enumerate(right)]


def partition_using_binary(xs):

    pass
