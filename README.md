# Python Lab
This repository contains my progress and tasks completed during my Python Core Course. Below is a summary of the key tasks and concepts covered in the course.

## Introduction
This repository documents the tasks completed throughout my Python Core Course. The course covers basic to intermediate Python programming concepts, 
including data types, functions, control structures, modules, and object-oriented programming.

## Tasks and Exercises
Below is a list of the tasks and exercises completed during the course:

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
### Task 4: Data Types - Dictonaries

Write a Python program to count the frequency of each character in a string (ignore the case of letters).

__Example:__

Input: `'Oh, it is python'`

Output: `{" ": 3, ",": 1, "h": 2, "i": 2, "n": 1, "o": 2, "p": 1, "s": 1, "t": 2, "y": 1}`
