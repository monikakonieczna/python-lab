def decorator_apply(lambda_func):
    """
    A decorator factory that accepts a lambda function `lambda_func` which will
    modify the first argument of the decorated function.
    """
    def decorator(fn):
        def wrapper(*args, **kwargs):
            modified_args = (lambda_func(args[0]),) + args[1:]
            return fn(*modified_args, **kwargs)
        return wrapper
    return decorator


@decorator_apply(lambda user_id: user_id + 1)
def return_user_id(num: int) ->int:
    return num


print(return_user_id(42))