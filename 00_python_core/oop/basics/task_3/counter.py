class Counter:
    def __init__(self, start=0, stop=None):
        """
        Initializes a counter with an optional start and stop value.

        :param start: The starting value of the counter, defaults to 0.
        :param stop: The stopping value of the counter, defaults to None (infinite).
        """
        self.current = start
        self.stop = stop

    def increment(self):
        """
        Increments the counter by 1. If the stop value is reached, prints a message.
        """
        if self.stop is not None and self.current >= self.stop:
            print("Maximal value is reached.")
        else:
            self.current += 1

    def get(self):
        """
        Returns the current value of the counter.

        :return: The current counter value.
        """
        return self.current