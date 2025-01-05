from functools import wraps


def validate(fn):
    """
    A decorator to validate arguments for the decorated function.
    Ensures all arguments are integers between 0 and 256 (inclusive).

    If validation passes, the function is called, and its return value is used.
    If validation fails, a specific error message is returned.
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
      if all(isinstance(arg, int) and 0 <= arg <= 256 for arg in args):
        return fn(*args, **kwargs) 
      else:
        return "Function call is not valid!" 
    return wrapper
  
  
@validate
def set_pixel(x: int, y: int, z: int) -> str:
  """
  Set a pixel with the given x, y, and z values.
  This function will only execute if the arguments are between 0 and 256 (inclusive).
  """
  return "Pixel created!"


print(set_pixel(0, 127, 300)) 
print(set_pixel(0, 127, 250)) 