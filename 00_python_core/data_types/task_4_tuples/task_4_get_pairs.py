from typing import Any, Tuple, List

def get_pairs(lst: List[Any]) -> List[Tuple[Any, Any]]:
    
    # If the list has fewer than two elements, return an empty list
    if len(lst) < 2 : 
        return []
    
    # Create a list of tuples containing pairs of consecutive elements
    return [(lst[i], lst[i+1]) for i in range(len(lst) - 1)]