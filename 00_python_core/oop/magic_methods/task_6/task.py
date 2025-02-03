import os

class Cd:
    def __init__(self, target_dir):
        # Validate if the target directory exists and is indeed a directory
        if not os.path.isdir(target_dir):
            raise ValueError(f"{target_dir} is not a valid directory.")
        self.target_dir = target_dir

    def __enter__(self):
        # Save the current working directory
        self.original_dir = os.getcwd()

        # Change to the target directory
        os.chdir(self.target_dir)

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Restore the original directory when exiting the context
        os.chdir(self.original_dir)

        # If an exception occurred, it will be propagated
        if exc_type:
            return False  # Don't suppress the exception
        return True  # Suppress the exception (if any)
