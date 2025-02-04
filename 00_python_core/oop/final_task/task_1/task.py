class Sun:
    _instance = None  # Class-level variable to hold the single instance
    
    @classmethod
    def inst(cls):
        # Check if the instance already exists
        if cls._instance is None:
            cls._instance = cls()  # If not, create the instance
        return cls._instance  # Return the existing instance

# Testing the Singleton behavior
p = Sun.inst()
f = Sun.inst()

print(p is f)  # This will print: True