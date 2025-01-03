from typing import Dict

def combine_dicts(*args:Dict[str, int]) -> Dict[str, int]:
    """
    Combine multiple dictionaries by summing the values of identical keys.

    :param args: A variable number of dictionaries.
    :return: A single dictionary where values of identical keys are summed.
    """
    combined = {}
    
    for dictionary in args:
        for key, value in dictionary.items():
            if key in combined:
                combined[key] += value
            else:
                combined[key] = value
    
    return combined