from typing import List, Tuple

def sort_unique_elements(str_list: Tuple[str]) -> List[str]:
    
    # Convert the tuple to a set to remove duplicates
    unique_words = set(str_list)
    
    # Sort the unique words
    sorted_unique_words = sorted(unique_words)
    
    # Print and return the sorted unique words
    print(sorted_unique_words)
    return sorted_unique_words