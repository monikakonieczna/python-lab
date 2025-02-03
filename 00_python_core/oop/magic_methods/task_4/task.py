class PriceControl:
    """
    Descriptor which doesn't allow to set price
    less than 0 and more than 100 included.
    """
    def __get__(self, instance, owner):
        return instance._price

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError("Price must be between 0 and 100.")
        instance._price = value


class NameControl:
    """
    Descriptor which doesn't allow to change field value after initialization.
    """
    def __get__(self, instance, owner):
        return instance._name if instance is not None else None

    def __set__(self, instance, value):
        raise ValueError("Name can not be changed.")


class Book:
    author = NameControl()
    name = NameControl()
    price = PriceControl()

    def __init__(self, author, name, price):
        self._author = author
        self._name = name
        self._price = price

    @property
    def author(self):
        return self._author

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @author.setter
    def author(self, value):
        raise ValueError("Author can not be changed.")

    @name.setter
    def name(self, value):
        raise ValueError("Name can not be changed.")

    @price.setter
    def price(self, value):
        if not (0 <= value <= 100):
            raise ValueError("Price must be between 0 and 100.")
        self._price = value
