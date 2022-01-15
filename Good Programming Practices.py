# TERNARY CONDITIONS/OPERATORS (for simple conditions (both if & else should be present))
condition = True
'''
if condition:
    x = 0
else:
    x = 1
'''
x = 0 if condition else 1
print(x)


# UNDERSCORE PLACEHOLDERS (for large numbers)
'''
num1 = 1000000000
num2 = 1000000
'''
num1 = 1_000_000_000  # (billion/ 100 crores)
num2 = 1_000_000  # (million/ 10 lakhs)
total = num1 + num2
'''
print(total)
'''
print(f'{total:,}')  # cool!


# CONTEXT MANAGERS (automatic resource management!)
'''
f_handle = open('imp stuff.py')  # (by default mode = 'r')
'''
with open('imp stuff.py') as f_handle:
    f_contents = f_handle.read()
'''
f_handle.close()
'''
list_of_words = f_contents.split()
word_count = len(list_of_words)
print(word_count)


# ENUMERATE
sports = ['Badminton', 'Cricket', 'Table Tennis', 'Swimming']
'''
num = 1
for sport in sports:
    print(num, sport)
    num += 1
'''
for num, sport in enumerate(sports, start=1):  # nice!
    print(num, sport)


# ZIP (to iterate parallelly)
names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
universes = ['Marvel', 'DC', 'Marvel', 'DC']
for name, hero, universe in zip(names, heroes, universes):  # (tuple-unpacking!)
    print(f'{name} is actually {hero} from {universe}.')
# or
for data in zip(names, heroes, universes):
    print(data)
# note that it will stop with the shortest iterator!, if you want to iterate till the longest iterator, use zip_longest() from itertools!


# UNPACKING
my_tuple = (1, 2, 4)
'''
a, b, c = my_tuple  # simply unpacking
print(a)  # let's say I just need a
'''
a, _, _ = my_tuple
print(a)  # interesting fact!-> underscores(_) can be used as variable names!, note that this is not only the reason why we used _ as a variable name of the values we don't need, but it(_) also tells the compiler to just ignore the unused vars!!(_)

# we can also do this!->
a, *b = my_tuple  # same as in function parameters!
print(a, b)

# so combining these two stuff, we can achieve->
a, *_ = my_tuple  # idc how many values are there in the tuple, I just want first.
print(a)
# note that I was just telling about the unpacking feature of tuples! we can always use this->
a = my_tuple[0]
print(a)

# advanced unpacking technique->
a, b, *c, d = (1, 2, 4, 8, 16, 32, 64, 128)
print(a, b, c, d)
# similarly->
a, b, *_, d = (1, 2, 4, 8, 16, 32, 64, 128)
print(a, b, d)
# that's all for tuple unpacking, not very important, but yeah can be useful sometimes.


# SETATTR & GETATTR (Python OOP stuff, so not interested in doing it now, here's the link if you want-> https://www.youtube.com/watch?v=C-gEQdGVXbk&list=WL&index=4&t=1148s)
class Person:
    pass


person = Person()


# GETPASS (hiding passwords)
username = input('Username: ')
'''
password = input('Password: ')
'''
from getpass import getpass
password = getpass('Password: ')  # either run this on terminal or edit config ('emulate terminal in output console' should be on)!
if password == 'pass':
    print(f'Welcome {username}!')
else:
    print('Wrong Password')


# -m  (in cmd / terminal-> 'python -m modules_name')
# what this do is just find {module_name} in sys.path and run it, it does not need to add .py to the module name!


# HELP & DIR (do try these on stuff to know about them!)
help(getpass)
"""
Calling help() at the Python prompt starts an interactive help session.
Calling help(thing) prints help for the python object 'thing'.
"""

dir(getpass)
"""
If called without an argument, return the names in the current scope.

Else, return an alphabetized list of names comprising (some of) the attributes
of the given object, and of attributes reachable from it.

for a module object: the module's attributes.
for a class object:  its attributes, and recursively the attributes of its bases.
for any other object: its attributes, its class's attributes, and recursively the attributes of its class's base classes.
"""
