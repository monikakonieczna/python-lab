class HistoryDict:
    def __init__(self, initial=None):
        """
        Initializes the custom dictionary with an optional initial dictionary.

        :param initial: An optional dictionary to initialize values.
        """
        self.data = initial or {}
        self.history = []

    def set_value(self, key, value):
        """
        Sets a key-value pair in the dictionary and updates the history.

        :param key: The key to set.
        :param value: The value to associate with the key.
        """
        self.data[key] = value
        if key not in self.history:
            self.history.append(key)
        else:
            self.history.remove(key)
            self.history.append(key)
        if len(self.history) > 5:
            self.history.pop(0)

    def get_history(self):
        """
        Returns the list of the last 5 changed keys.

        :return: A list of keys.
        """
        return self.history

    def get_value(self, key):
        """
        Gets the value associated with a key in the dictionary.

        :param key: The key to retrieve the value for.
        :return: The value associated with the key.
        """
        return self.data.get(key)