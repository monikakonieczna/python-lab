from typing import List


class Counter:
    def __init__(self, values: List[int]):
        self.values = values
    
    def __add__(self, other: str):
        if isinstance(other, str):
            return [f"{value} {other}" for value in self.values]
        raise TypeError("Unsupported operand type for +: 'Counter' and '{}'".format(type(other).__name__))
