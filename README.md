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

def combine_dicts(*args):
    ...

dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

print(combine_dicts(dict_1, dict_2))
>>> {'a': 300, 'b': 200, 'c': 300}

print(combine_dicts(dict_1, dict_2, dict_3))
>>> {'a': 600, 'b': 200, 'c': 300, 'd': 100}