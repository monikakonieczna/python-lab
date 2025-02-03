# Python Lab
This repository contains my progress and tasks completed during my Python Core Course. Below is a summary of the key tasks and concepts covered in the course.

## Introduction
This repository documents the tasks completed throughout my Python Core Course. The course covers basic to intermediate Python programming concepts, 
including data types, functions, control structures, modules, and object-oriented programming.

## Tasks and Exercises
Below is a list of the tasks and exercises completed during the course:

## Tasks and Exercises: Data Types

### Task 1: Data Types - Numbers
#### Rounding
Create a function with two parameters a and b. The function calculates the following expression:

(12 * a + 25 * b) / (1 + a**(2**b))	
and returns a result of the expression rounded up to the second decimal place.
### Task 2: Data Types - Strings
#### Get longest word
Implement a function get_longest_word(s: str) -> str which returns the longest word in the given string. The word can contain any symbols except whitespaces (' ', '\n', '\t' and so on). 
If there are multiple longest words in the string with the same length return the word that occurs first.

__Examples:__
```python 
>>> get_longest_word('Python is simple and effective!')
'effective!'
```
#### Replacer
Implement a function that receives a string and replaces all " symbols with ' and vice versa.

#### Fractions
Create a function that takes two parameters of string type which are fractions with the same denominator and returns a sum expression of these fractions and the sum result.

__Examples:__
```python 
>>> a_b = '1/3'
>>> c_b = '5/3'
>>> get_fractions(a_b, c_b)
'1/3 + 5/3 = 6/3'
```
#### Palindrome
Write a function that checks whether a string is a palindrome or not. The usage of any reversing functions is prohibited.

To check your implementation you can use strings from here

__Examples:__

```python 
A dog! A panic in a pagoda!
Do nine men Interpret? Nine men I nod
T. Eliot, top bard, notes putrid tang emanating, is sad; I'd assign it a name: gnat dirt upset on drab pot toilet.
A man, a plan, a canal — Panama!
```
### Task 3: Data Types - Lists
#### Sort unique elements
Write a Python program that accepts a sequence of words as input and prints the unique words in a sorted form.

__Examples:__

Input:
```python 
('red', 'white', 'black', 'red', 'green', 'black') 
```
Output: 
```python 
['black', 'green', 'red', 'white']
```
#### Fizzbuzz list
Update the __get_fizzbuzz_list__ function. The function has to generate and return a list with numbers from _1_ to _n_ inclusive where the _n_ is passed as a parameter to the function. 
But if the number is divided by _3_ the function puts a _Fizz_ word into the list, and if the number is divided by _5_ the function puts a _Buzz_ word into the list. 
If the number is divided by both _3_ and _5_ the function puts _FizzBuzz_ into the list.

#### Foo
Implement a function `foo(List[int]) -> List[int]` which, given a list of
integers, returns a new list such that each element at index `i` of the new list
is the product of all the numbers in the original array except the one at `i`.

__Example:__
```python
>>> foo([1, 2, 3, 4, 5])
[120, 60, 40, 30, 24]
>>>foo([3, 2, 1])
[2, 3, 6]
```

### Task 4: Data Types - Tuples
#### Get Tuple
Implement a function `get_tuple(num: int) -> Tuple[int]` which returns a tuple of a given integer's digits.

__Example:__
```python
>>> get_tuple(87178291199)
(8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)
```
#### Get pairs
Implement a function `get_pairs(lst: List) -> List[Tuple]` which returns a list
of tuples containing pairs of elements. The pairs should be formed as in the
example. If there is only one element in the list, return `[]` instead.

__Example:__
```python
>>> get_pairs([1, 2, 3, 8, 9])
[(1, 2), (2, 3), (3, 8), (8, 9)]
>>> get_pairs(['need', 'to', 'sleep', 'more'])
[('need', 'to'), ('to', 'sleep'), ('sleep', 'more')] 
>>> get_pairs([1])
[]
```
### Task 5: Data Types - Dictonaries

Write a Python program to count the frequency of each character in a string (ignore the case of letters).

__Example:__

Input: `'Oh, it is python'`

Output: `{" ": 3, ",": 1, "h": 2, "i": 2, "n": 1, "o": 2, "p": 1, "s": 1, "t": 2, "y": 1}`

### Data Types - Final Task 1

Write a Python program to print all the unique values of all the dictionaries in a list.

__Example__:
```
Input: [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
```

### Data Types - Final Task 2

Write a program which makes a pretty print of a part of the multiplication table.

__Example__:
```
Input:
row_start = 2
row_end = 4
column_start = 3
column_end = 7

Output: [[6, 8, 10, 12, 14], [9, 12, 15, 18, 21], [12, 16, 20, 24, 28]]
that is equal to the following multiplication table:

    3   4   5   6   7   
2   6   8   10  12  14  
3   9   12  15  18  21  
4   12  16  20  24  28

```

## Tasks and Exercises: Functions
### Task 1: Functions - Arguments
#### Generate squares
Implement a function that takes a number as an argument and returns a dictionary, where the key is a number and the value is the square of that number.

**Example:**
```python
>>> generate_squares(5)
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```
#### Filter
We have a list of dictionaries:
```python
friends = [
    {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'},
    {'name': 'Emily', 'gender': 'female', 'sport': 'volleyball'},
]
```
Create functions `query`, `select`, `field_filter` to work with lists similar to 
`friends`.
Stubs for these functions are already created.

Example:
```python
>>> result = query(
    friends,
    select('name', 'gender', 'sport'),
    field_filter('sport', *('Basketball', 'volleyball')),
    field_filter('gender', *('male',)),
)
>>> result
[{'gender': 'male', 'name': 'Sam', 'sport': 'Basketball'}]
```
These functions have to provide with possibility to select necessary columns
and make filtering by these columns

#### Union & intersect
Create generic `union` and `intersect` functions to work with sets.
The functions must accept an arbitrary number of arguments of different types: `list`, `tuple`, `set`.
Each function must return value of `set` type.
For example:
```python
>>> union(('S', 'A', 'M'), ['S', 'P', 'A', 'C'])
{'S', 'P', 'A', 'M', 'C'}

>>> intersect(('S', 'A', 'C'), ('P', 'C', 'S'), ('G', 'H', 'S', 'C'))
{'S', 'C'}
```
#### Combine dictionaries
Implement a function that receives a changeable number of dictionaries (keys - letters, values - numbers) and combines them into one dictionary. Dict values should be summarized in case of identical keys

```
def combine_dicts(*args):
    ...

dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

print(combine_dicts(dict_1, dict_2))
>>> {'a': 300, 'b': 200, 'c': 300}

print(combine_dicts(dict_1, dict_2, dict_3))
>>> {'a': 600, 'b': 200, 'c': 300, 'd': 100}
```

### Task 2: Functions - Recursions
#### Count the sum of elements
Define a function `seq_sum(sequence)` which allows to count sum of elements. Elements of all nested sequences should be included.

Example:
```python
def seq_sum(sequence):
    pass
  
sequence = [1,2,3,[4,5, (6,7)]]

>>> print(seq_sum(sequence))
28
```

#### Linear sequence
Define a function `linear_seq(sequence)` which converts a passed sequence to a sequence without nested sequences.

Example:
```python
def linear_seq(sequence):
    pass
  
sequence = [1,2,3,[4,5, (6,7)]]

>>> print(linear_seq(sequence))
[1,2,3,4,5,6,7]
```

### Task 3: Functions - Decorators
#### Time decorator
***
Create a decorator function `time_decorator` which has to calculate decorated function execution time
and put this time value to `execution_time` dictionary where `key` is 
decorated function name and `value` is this function execution time.
For example:
```python
@time_decorator
def func_add(a, b):
    sleep(0.2)
    return a + b

>>> func_add(10, 20)
30

>>> execution_time['func_add']
0.212341254
```

#### Decorator for additional information about calls of decorated function
Write a decorator which logs information about calls of decorated function,
values of its arguments, values of keyword arguments and execution time. Log
should be written to a file.

### Example of using
``` python
@log
def foo(a, b, c):
    ...

foo(1, 2, c=3)
```

### log.txt
```
...
foo; args: a=1, b=2; kwargs: c=3; execution time: 0.12 sec.
...
```

#### Decorator to validate arguments in other function
Create decorator `validate` which validates arguments in `set_pixel` function. All function parameters should be between 0(int) and 256(int) inclusive.

In case if all parameters are valid, `set_pixel` function should return _"Pixel created!"_ message. Otherwise, it should return _"Function call is not valid!"_ message.

Use `functools.wraps` where is it necessary.

Don't forget about doc stings.

__Examples__
```python
>>> set_pixel(0, 127, 300)
Function call is not valid!
>>> set_pixel(0,127,250)
Pixel created!
```

#### Decorators Factory

Create a decorators factory (decorator itself). The factory accepts a function (lambda) as an input and returns a decorator that will return the result of the function as the first argument, the result of the decorated function is passed. The function which the factory accepts (in the example below it is a lambda) can take one positional parameter only.

For example:
```python
>>> @decorator_apply(lambda user_id: user_id + 1)
>>> def return_user_id(num: int): 
        return num
>>> return_user_id(42) 
>>> 43
```
### Final Task: Functions - Decorators
#### Custom split function
Implement a function that works the same as `str.split` method
(without using `str.split` itself, ofcourse).
Pay attention to strings with multiple spaces. For example: '    Hi     Python    world!' 

Example:
```python
    def split(data: str, sep=None, maxsplit=-1):
        ...
```
#### Split by index
Implement a function `split_by_index(s: str, indexes: List[int]) -> List[str]`
which splits the `s` string by indexes specified in `indexes`. Wrong indexes
must be ignored.
Examples:
```python
>>> split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

>>> split_by_index("no luck", [42])
["no luck"]
```

## Tasks and Exercises: OOP in Python
### OOP Basics
#### Field Class
***

Develop a class `Field` with "full encapsulation", whose attributes are accessed and data changes are implemented through method calls.


In OOP, it is generally accepted to start the names of methods for extracting data with the word *"get"*,
and the names of the methods in which fields are equated to a certain value - *"set"*.

In this task, you need to implement `get_value` and `set_value` methods for `Field` class (`__value` property).

#### SchoolMember, Teacher, Student Classes
***
Create a class `SchoolMember` which represents any person in school.
Classes `Teacher` and `Student` are inherited from `SchoolMember`. 

Classes should have the same interface with the public `show ()` method.
`Teacher` accepts *name* (str), *age* (int), *salary* (int).
`Student` accepts *name* (str), *age* (int), *grades*.
Move the same logic of initialization to the class `SchoolMember`.

Method `show()` returns string (see string patters in *Example*).

Example
```
    >>> persons = [Teacher("Mr.Snape", 40, 3000), Student("Harry", 16, 75)]

    >>> for person in persons:
           print(person.show())

    "Name: Mr.Snape, Age: 40, Salary: 3000"
    "Name: Harry, Age: 16, Grades: 75"
 ```
#### Counter
Implement a Counter class that optionally accepts the start value and the counter stop value.
If the start value is not specified the counter should begin with 0.
If the stop value is not specified it should be counting up infinitely.
If the counter reaches the stop value, print "Maximal value is reached."

Implement two methods: "increment" and "get"

Example:
```python
>>> c = Counter(start=42)
>>> c.increment()
>>> c.get()
43

>>> c = Counter()
>>> c.increment()
>>> c.get()
1
>>> c.increment()
>>> c.get()
2

>>> c = Counter(start=42, stop=43)
>>> c.increment()
>>> c.get()
43
>>> c.increment()
Maximal value is reached.
>>> c.get()
43
```
#### History Dictionary
Implement a custom dictionary that will memorize the 5 latest changed keys.
Using method "get_history" return these keys.

Example:
```python
>>> d = HistoryDict({"foo": 42})
>>> d.set_value("bar", 43)
>>> d.get_history()

["bar"]
```
*After your own implementation of the class have a look at collections.deque https://docs.python.org/3/library/collections.html#collections.deque*

### Decorators
#### Vehicle
***
You need to create abstract class `Vehicle`. Classes `Car`, `Motorcycle`, `Truck`, `Bus` are inherited from `Vehicle` 
and already implemented. 

Class `Vehicle` accepts the following parameters:

- `brand_name` -> str (e.g. Honda)
- `year_of_issue` -> int (e.g. 2020)
- `base_price` -> int (e.g. 1_000_000)
- `mileage` -> int (e.g. 10_000)

The following methods should be implemented:

- `vehicle_type` - returns str - type of the vehicle in the following pattern *brand_name + name of the class*.
  For example: *Toyota Car*, *Suzuki Motorcycle*;
- `is_motorcycle` return boolean value depends on the amount of wheels (2 wheels -> motorcycle, so method should return *True*);
- `purchase_price` - returns the price of the vehicle: (`base_price - 0.1 * mileage`). If the result price is less than 100_000, 
method should return 100_000.

Put the following decorators where necessary and if it is necessary:

`abstractmethod`, `classmethod`, `staticmethod`, `property` and other decorators.

Example
```
    >>> vehicles = (
        Car(brand_name="Toyota", year_of_issue=2020, base_price=1_000_000, mileage=150_000),
        Motorcycle(brand_name="Suzuki", year_of_issue=2015, base_price=800_000, mileage=35_000),
        Truck(brand_name="Scania", year_of_issue=2018, base_price=15_000_000, mileage=850_000),
        Bus(brand_name="MAN", year_of_issue=2000, base_price=10_000_000, mileage=950_000)
    )
    
    >>> for vehicle in vehicles:
            print(
                f"Vehicle type={vehicle.vehicle_type()}\n"
                f"Is motorcycle={vehicle.is_motorcycle()}\n"
                f"Purchase price={vehicle.purchase_price}\n"
            )
    

    Vehicle type=Toyota Car
    Is motorcycle=False
    Purchase price=985000.0
    
    Vehicle type=Suzuki Motorcycle
    Is motorcycle=True
    Purchase price=796500.0
    
    Vehicle type=Scania Truck
    Is motorcycle=False
    Purchase price=14915000.0
    
    Vehicle type=MAN Bus
    Is motorcycle=False
    Purchase price=9905000.0
```

### Exceptions
#### Pagination
Implement a Pagination class helpful to arrange text on pages and list content on the given page. 
The class should take in a text and a positive integer which indicate how many symbols will be allowed per page (take spaces into account as well).

You need to be able to get the number of whole symbols in the text, get the number of pages that came out and the method that accepts the page number, and return the number of symbols on this page. If the provided number of the page is missing raise exception with message "Invalid index. Page is missing". 

Implement searching/filtering pages by symbols/words and displaying pages with all the symbols on it. If the provided symbols/words are missing raise exception with message "'<symbol/word>' is missing on the pages". 

If you're querying by symbol that appears on many pages or if you are querying by the word that is splitted in two return an array of all the occurences.

Pages indexing starts with 0.

Example:
```python
>>> pages = Pagination('Your beautiful text', 5)
>>> pages.page_count
4
>>> pages.item_count
19

>>> pages.count_items_on_page(0)
5
>>> pages.count_items_on_page(3)
4
>>> pages.count_items_on_page(4)
Exception: Invalid index. Page is missing.
>>> pages.find_page('Your')
[0]
>>> pages.find_page('e')
[1, 3]
>>> pages.find_page('beautiful')
[1, 2]
>>> pages.find_page('great')
Exception: 'great' is missing on the pages
>>> pages.display_page(0)
'Your '
```
#### Divide Function
Write a function `divide` which accepts a string that contains two integers, separated by **spaces** (integers can be separated by more than one space).
You have to perform the division operation (`a / b`) and return the result (float) or an error message.

The structure of the error message is the following: `Error code: {error message}`.

```
    >>> divide("4 2")
    2.0

    >>> divide("4 0")
    "Error code: division by zero"

    >>> divide("* 1")
    "Error code: invalid literal for int() with base 10: '*'"
```
### Magic Methods
#### Overload addition operator
You have to overload the addition operator in `Counter` class. Use the `__add__()` magic method to overload the addition.

For example, in case of *a + b*, *a* object should have `__add__()` which accepts *b* as a second parameter (`self` goes first).

In this case, `Counter` object accepts a list from int as a parameter. Object to summarize with will be a str object.
The result should be a list of strings which have the following pattern: `1 test` - one object from list and str separated by the whitespace.

#### Example

    >>> Counter([1, 2, 3]) + "mississippi"

    ["1 mississippi", "2 mississippi" , "3 mississippi"]

#### The hierarchy out of birds
Create a hierarchy out of birds. 
Implement 4 classes:
* class `Bird` with an attribute `name` and methods `fly` and `walk`.
* class `FlyingBird` with attributes `name`, `ration`, and with the same methods. `ration` must have a default value. 
Implement the method `eat` which will describe its typical ration.
* class `NonFlyingBird` with same characteristics but which obviously without attribute `fly`.
Add the same "eat" method but with other implementation regarding the swimming bird tastes.
* class `SuperBird` which can do all of it: walk, fly, swim and eat.
But be careful which "eat" method you inherit.

Implement str() function call for each class.

Example:
```python
>>> b = Bird("Any")
>>> b.walk()
"Any bird can walk"

p = NonFlyingBird("Penguin", "fish")
>> p.swim()
"Penguin bird can swim"
>>> p.fly()
AttributeError: 'Penguin' object has no attribute 'fly'
>>> p.eat()
"It eats mostly fish"

c = FlyingBird("Canary")
>>> str(c)
"Canary bird can walk and fly"
>>> c.eat()
"It eats mostly grains"

s = SuperBird("Gull")
>>> str(s)
"Gull bird can walk, swim and fly"
>>> s.eat()
"It eats mostly fish"
```
#### Book class with the attributes price, author, and name.

You have to implement class `Book` with attributes `price, author, name.`

- `author` and `name` fields have to be immutable;
- `price` field may be changes but has to be in `0 <= price <= 100` range.

If user tries to change `author` or `name` fields after
initialization or set price out of range, the `ValueError` should be raised.

Implement descriptors `PriceControl` and `NameControl` to validate parameters.

#### Example

    >>> b = Book("William Faulkner", "The Sound and the Fury", 12)
    >>> print(f"Author='{b.author}', Name='{b.name}', Price='{b.price}'")
    Author='William Faulkner', Name='The Sound and the Fury', Price='12'
    
    >>> b.price = 55
    >>> b.price
    55
    >>> b.price = -12  # => ValueError: Price must be between 0 and 100.
    >>> b.price = 101  # => ValueError: Price must be between 0 and 100.
    
    >>> b.author = "new author"  # => ValueError: Author can not be changed.
    >>> b.name = "new name"      # => ValueError: Name can not be changed.

#### Context manager 
Create a context manager `TempDir` (Use Context Manager protocol - methods `__enter__`, `__exit__`):
1. When entering the context, a new temporary directory is created with random, unique name.
   Use `os.mkdir` to create the directory.
2. Until exiting this context the new created directory becomes current one and all actions are executed 
   in scope of this new directory.
3. When exiting this context, the temporary directory is removed with all files in it.
   Use `rmtree` from `shutil` to remove whole directory.
4. The new working directory becomes the same as before entering context.