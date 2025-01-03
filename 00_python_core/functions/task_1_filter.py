from typing import Dict, Any, Callable, Iterable

DataType = Iterable[Dict[str, Any]]
ModifierFunc = Callable[[DataType], DataType]


def query(data: DataType, selector: ModifierFunc,
          *filters: ModifierFunc) -> DataType:
    """
    Query data with column selection and filters

    :param data: List of dictionaries with columns and values
    :param selector: result of `select` function call
    :param filters: Any number of results of `field_filter` function calls
    :return: Filtered data
    """
    for filter_func in filters:
        data = filter_func(data)
    
    return selector(data)


def select(*columns: str) -> ModifierFunc:
    """
    Return a function that selects only specific columns from the dataset.
    
    :param columns: Column names to include in the result.
    :return: A function that applies column selection to the data.
    """
    def selector(data: DataType) -> DataType:
        return [{col: item[col] for col in columns if col in item} for item in data]

    return selector


def field_filter(column: str, *values: Any) -> ModifierFunc:
    """
    Return function that filters specific column to be one of `values`
    
    :param column: The column name to filter.
    :param values: Acceptable values for the column.
    :return: A function that applies the filter condition.
    """
    def filter_func(data: DataType) -> DataType:
        return [item for item in data if item.get(column) in values]

    return filter_func

def test_query():
    friends = [
        {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'}
    ]
    value = query(
        friends,
        select(*('name', 'gender', 'sport')),
        field_filter(*('sport', *('Basketball', 'volleyball'))),
        field_filter(*('gender', *('male',))),
    )
    assert [{'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'}] == value
    
if __name__ == "__main__":
    test_query()
