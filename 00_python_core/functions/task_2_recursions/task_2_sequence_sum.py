from typing import List, Tuple, Union


def seq_sum(sequence: Union[List, Tuple]) -> int:
    sum = 0
    for element in sequence:
        if isinstance(element, (list, tuple)):
            sum += seq_sum(element)
        else:
             sum += element
    return sum