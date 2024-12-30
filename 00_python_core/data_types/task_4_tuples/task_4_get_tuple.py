from typing import Tuple

def get_tuple(num: int) -> Tuple[int]:
    
    # Convert the number to a string, remove the negative sign if any
    num_str = str(abs(num))
    
    # Convert each character back to an integer and return as a tuple
    return tuple(int(digit) for digit in num_str)