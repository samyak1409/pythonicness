# BEDMAS- openBracket Expo Div Multi Add Sub


# You can use the del statement to remove a variable, which means the reference from the name to the value is deleted, and trying to use the variable causes an error.
badminton = True
print(badminton)
del badminton
# print(badminton)


# in a string it compares the ASCII value for example:
print("abc" < "abd")  # True
# because ascii value of first 2 letters is same ,i.e., "ab", but then ascii value of "d" is greater than "c" and that's why it is true.
# so this is how it works in string.. hope it helps😅


# Remember! Python uses words for its Boolean operators, whereas most other languages use symbols such as '&&', '||' and '!'.


# '!=' is checking for values that are not equal, and 'not' just inverts the boolean result!! V.imp.


# '==' has a higher precedence than 'or'!


# Just take a look at operator precedence table in phone's gallery


# Lists of lists are often used to represent 2D grids, as Python lacks the multidimensional arrays that would be used for this in other languages.


# Lists and strings are similar in many ways - strings can be thought of as lists of characters that can't be changed.


# What is the difference between appending and concatenation?
# "Concatenate" joins two specific items together, whereas "append" adds(at the end) what you specify to whatever may already be there.


# list.count(obj): Returns a count of how many times an item occurs in a list


# Don't Repeat Yourself, or DRY- Bad, repetitive code is said to abide by the WET principle, which stands for Write Everything Twice, or We Enjoy Typing.


# Functions->
def firstFcn(var):
    print(var + '1')


def secondFcn(var):
    print(var + '2')


def thirdFcn(var):
    print(var + '3')


FcnList = [firstFcn, secondFcn, thirdFcn]
for fcn in FcnList:
    fcn('Hello')


# Functions can also be used as arguments of other functions.


# standard library, and contains many useful modules. Some of the standard library's useful modules include string, re, datetime, math, random, os, multiprocessing, subprocess, socket, email, json, doctest, unittest, pdb, argparse and sys.

# Tasks that can be done by the standard library include string parsing, data serialization, testing, debugging and manipulating dates, emails, command line arguments, and much more!

# Python's extensive standard library is one of its main strengths as a language.


t = tuple()
dir(t)   # gives all the methods of t!
print()

# Why is python slow?

# Because it is DYNAMICALLY-TYPED! Means, the type of the data is identified at the run-time! (Languages like C, C++, JAVA are statically-typed!)


'''
Artificial intelligence, sometimes called machine intelligence, is intelligence demonstrated by machines, 
unlike the natural intelligence displayed by humans and animals.

Machine learning is the study of computer algorithms that improve automatically through experience. 
It is seen as a subset of artificial intelligence.

Deep learning is part of a broader family of machine learning methods based on artificial neural networks with representation learning. 
Learning can be supervised, semi-supervised or unsupervised.
'''


# sorting dictionaries by value:
d = {'+': 1, '++': 2, '++++': 4, '--': -2, '-': -1}
print(d)

# print({k: v for k, v in sorted(d.items(), key=lambda x: x[1])}); exit()

di = d.items()
print(di)  # ; print(list(di))

l = sorted(di, key=lambda x: x[1])
print(l)

sd = {k: v for k, v in l}
# sd = dict(l)
print(sd)

"""
initializer = '''
x = {'+': 1, '++': 2, '++++': 4, '--': -2, '-': -1}
'''
code1 = '''
{k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
'''
code2 = '''
None
'''
from timeit import timeit
print(timeit(setup=initializer, stmt=code1, number=10000000))
print(timeit(setup=initializer, stmt=code2, number=10000000))
"""
