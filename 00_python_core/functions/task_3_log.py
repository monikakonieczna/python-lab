import time

def log(fn):
    """
    A decorator to log the details of the function call, including arguments,
    keyword arguments, and execution time, into a log file.
    """
    def wrapper(*args, **kwargs):
        # Execution Time
        start_time = time.time()  
        result = fn(*args, **kwargs)  
        end_time = time.time()  
        
        execution_time = end_time - start_time
        
        # Prepare Log Message
        args_str = ", ".join(f"{k}={v}" for k, v in zip(fn.__code__.co_varnames, args))
        kwargs_str = ", ".join(f"{k}={v}" for k, v in kwargs.items())
        log_message = (
            f"{fn.__name__}; args: {args_str}; kwargs: {kwargs_str}; "
            f"execution time: {execution_time:.2f} sec.\n"
        )
        
        # Write to log file
        with open("log.txt", "a") as log_file:
            log_file.write(log_message)
        
        return result
    
    return wrapper

@log
def foo(a, b, c):
    time.sleep(0.12)
    return a + b + c

foo(1, 2, c=3)