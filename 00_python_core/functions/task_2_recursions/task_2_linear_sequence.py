from typing import Any, List

def linear_seq(sequence: List[Any]) -> List[Any]:
    linear_sequence = []
    for element in sequence:
        if isinstance(element, (list, tuple)):
            linear_sequence.extend(linear_seq(element))
        else:
             linear_sequence.append(element)
    return linear_sequence