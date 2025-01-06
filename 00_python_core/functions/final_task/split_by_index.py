from typing import List

def split_by_index(s: str, indexes: List[int]) -> List[str]:
    """
    Splits the string `s` at the given indexes.
    Ignores invalid indexes (those out of the string's bounds).
    
    Args:
    s (str): The string to split.
    indexes (List[int]): The list of indexes at which to split.
    
    Returns:
    List[str]: The list of substrings after splitting.
    """
    # Sort and filter out invalid indexes
    valid_indexes = sorted(idx for idx in indexes if 0 <= idx < len(s))

    # If there are no valid indexes, return the whole string as one element
    if not valid_indexes:
        return [s]

    # Start the split at index 0
    result = []
    start_idx = 0

    for idx in valid_indexes:
        # Append the substring from start_idx to idx
        result.append(s[start_idx:idx])
        start_idx = idx  # Update start_idx to the current split point

    # Add the remaining part of the string after the last valid index
    result.append(s[start_idx:])
    
    return result