class Field:
    __value = None
    def __init__(self):
        self.__value = None
        
    def get_value(self):
        """
        Retrieves the value of the field.

        :return: The current value of the field.
        """
        return self.__value
    
    def set_value(self, value):
        """
        Sets a new value for the field.

        :param value: The new value to be set.
        """
        self.__value = value