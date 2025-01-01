from typing import Dict


def get_dict(s: str) -> Dict[str, int]:
    # Convert to lowercase to ignore case
    s = s.lower()
    # Initialize empty dictionary
    frequency = {}
    # Iterate over each character in the string
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency