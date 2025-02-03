import time
import datetime
from contextlib import ContextDecorator

class LogFile(ContextDecorator):
    def __init__(self, log_file_name):
        self.log_file_name = log_file_name

    def __enter__(self):
        # Record start time when entering the context
        self.start_time = time.time()
        self.start_datetime = datetime.datetime.now()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Calculate the execution time
        end_time = time.time()
        execution_time = end_time - self.start_time
        end_datetime = datetime.datetime.now()
        
        # Handle exception if there is one
        if exc_type:
            error_message = str(exc_value)
        else:
            error_message = "None"
        
        # Prepare the log line
        log_line = (
            f"Start: {self.start_datetime} | "
            f"Run: {str(datetime.timedelta(seconds=execution_time))} | "
            f"An error occurred: {error_message}\n"
        )

        # Write to log file in append mode
        with open(self.log_file_name, 'a') as log_file:
            log_file.write(log_line)

        # Reraise the exception if there was one
        if exc_type:
            raise exc_value

