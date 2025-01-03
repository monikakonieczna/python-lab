def union(*args) -> set:
    """
    Returns the union of all input iterables as a set.

    :param args: Iterable arguments (list, tuple, set, etc.)
    :return: A set containing all unique elements from the input iterables.
    """
    result = set()
    for arg in args:
        result.update(arg)
    return result


def intersect(*args) -> set:
    """
    Returns the intersection of all input iterables as a set.

    :param args: Iterable arguments (list, tuple, set, etc.)
    :return: A set containing only elements present in all input iterables.
    """
    if not args:
        return set()
    
    result = set(args[0])
    for arg in args[1:]:
        result.intersection_update(arg)
    return result