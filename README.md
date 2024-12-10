# Python Lab
This repository contains my progress and tasks completed during my Python Core Course. Below is a summary of the key tasks and concepts covered in the course.

## Introduction
This repository documents the tasks completed throughout my Python Core Course. The course covers basic to intermediate Python programming concepts, including data types, functions, control structures, modules, and object-oriented programming.

## Tasks and Exercises
Below is a list of the tasks and exercises completed during the course:

### Task 1: Data Types - Numbers
#### Rounding
Create a function with two parameters a and b. The function calculates the following expression:

(12 * a + 25 * b) / (1 + a**(2**b))	
and returns a result of the expression rounded up to the second decimal place.
### Task 2: Data Types - Strings
#### Get longest word
Implement a function get_longest_word(s: str) -> str which returns the longest word in the given string. The word can contain any symbols except whitespaces (' ', '\n', '\t' and so on). If there are multiple longest words in the string with the same length return the word that occurs first.

Example:
```
>>> get_longest_word('Python is simple and effective!')
'effective!'
```
#### Replacer
Implement a function that receives a string and replaces all " symbols with ' and vice versa.

#### Fractions
Create a function that takes two parameters of string type which are fractions with the same denominator and returns a sum expression of these fractions and the sum result.

For example:
```
>>> a_b = '1/3'
>>> c_b = '5/3'
>>> get_fractions(a_b, c_b)
'1/3 + 5/3 = 6/3'
```
#### Palindrome
Write a function that checks whether a string is a palindrome or not. The usage of any reversing functions is prohibited.

To check your implementation you can use strings from here

Examples:
```
A dog! A panic in a pagoda!
Do nine men Interpret? Nine men I nod
T. Eliot, top bard, notes putrid tang emanating, is sad; I'd assign it a name: gnat dirt upset on drab pot toilet.
A man, a plan, a canal — Panama!
```