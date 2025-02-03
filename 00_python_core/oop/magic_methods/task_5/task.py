import os
import shutil
import random
import string

class TempDir:
    def __enter__(self):
        # Save the current working directory
        self.original_dir = os.getcwd()

        # Generate a unique name for the temporary directory
        random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        self.temp_dir = os.path.join(self.original_dir, f"temp_{random_str}")

        # Create the temporary directory
        os.mkdir(self.temp_dir)

        # Change the current working directory to the new temporary directory
        os.chdir(self.temp_dir)

        # Return the path of the temporary directory
        return self.temp_dir

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Change back to the original directory
        os.chdir(self.original_dir)

        # Remove the temporary directory and all its contents
        shutil.rmtree(self.temp_dir)

        # If an exception was raised inside the context, re-raise it
        if exc_type:
            return False  # Propagate the exception, if any
        return True  # Suppress the exception (if any)
