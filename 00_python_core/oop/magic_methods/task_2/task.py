from typing import List


class Bird:
    def __init__(self, name: str):
        self.name = name
    
    def fly(self):
        return f"{self.name} bird can fly"
    
    def walk(self):
        return f"{self.name} bird can walk"
    
    def __str__(self):
        return f"{self.name} bird"
            


class FlyingBird(Bird):
    def __init__(self, name: str, ration: str = "grains"):
        super().__init__(name)
        self.ration = ration
    
    def eat(self):
        return f"It eats mostly {self.ration}"
    
    def __str__(self):
        return f"{self.name} bird can walk and fly"


class NonFlyingBird(Bird):
    def __init__(self, name: str, ration: str = "fish"):
        super().__init__(name)
        self.ration = ration
    
    def eat(self):
        return f"It eats mostly {self.ration}"
    
    def swim(self):
        return f"{self.name} bird can swim"
    
    def __str__(self):
        return f"{self.name} bird can walk and swim"
    
    from typing import List


class Counter:
    def __init__(self, values: List[int]):
        self.values = values
    
    def __add__(self, other: str):
        if isinstance(other, str):
            return [f"{value} {other}" for value in self.values]
        raise TypeError("Unsupported operand type for +: 'Counter' and '{}'".format(type(other).__name__))


class Bird:
    def __init__(self, name: str):
        self.name = name
    
    def fly(self):
        return f"{self.name} bird can fly"
    
    def walk(self):
        return f"{self.name} bird can walk"

    def __str__(self):
        return f"{self.name} bird"


class FlyingBird(Bird):
    def __init__(self, name: str, ration: str = "grains"):
        super().__init__(name)
        self.ration = ration
    
    def eat(self):
        return f"It eats mostly {self.ration}"
    
    def __str__(self):
        return f"{self.name} bird can walk and fly"


class NonFlyingBird(Bird):
    def __init__(self, name: str, ration: str = "fish"):
        super().__init__(name)
        self.ration = ration
    
    def eat(self):
        return f"It eats mostly {self.ration}"
    
    def swim(self):
        return f"{self.name} bird can swim"
    
    def fly(self):
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute 'fly'")
    
    def __str__(self):
        return f"{self.name} bird can walk and swim"


class SuperBird(FlyingBird, NonFlyingBird):
    def __init__(self, name: str):
        super().__init__(name)
    
    def __str__(self):
        return f"{self.name} bird can walk, swim and fly"


class SuperBird( NonFlyingBird, FlyingBird ):
    def __init__(self, name: str):
        super().__init__(name)
        
    def __str__(self):
        return f"{self.name} bird can walk, swim and fly"
