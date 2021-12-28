import collections


def binary_search_multiset(xs, y):
    result_index = search_in(xs, 0, len(xs), y)
    while result_index > 0 and xs[result_index - 1] == y:
        result_index -= 1
    return result_index


def binary_search(xs, y):
    return search_in(xs, 0, len(xs), y)


def search_in(xs, start_index, end_index, y):
    """
    search for y in xs, [s_i, e_i)
    :param xs: Sorted list
    :param start_index: s_i
    :param end_index: e_i
    :param y: target
    :return: i such that xs[i] == y
    :raise: Not found Exception
    """
    if end_index - start_index <= 1:
        assert end_index - start_index == 1
        if xs[start_index] == y:
            return start_index
        else:
            raise ValueError(str(y) + " not found in list")
    else:
        middle = (start_index + end_index) // 2
        if y < xs[middle]:
            return search_in(xs, start_index, middle, y)
        else:
            return search_in(xs, middle, end_index, y)


def collapse_list(xs):
    """
    Transforms [1,1,2,2,3,4] to [(1,2),(2,2),(3,1),(4,1)]
    which is [(e, n_occurrence)]
    :param xs: Sorted list
    :return: transformed list
    """
    result = []
    assert xs
    current = xs[0]
    count = 0
    for e in xs:
        if e == current:
            count += 1
        else:
            result.append((current, count))
            current = e
            count = 1
    if count > 0:
        result.append((current, count))
    return result


def collapse_list_with_counter(xs):
    return list(collections.Counter(xs).items())
