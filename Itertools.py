# https://youtu.be/Qu3dThVy6KQ, https://docs.python.org/3/library/itertools.html


import itertools


# count():
counter = itertools.count()

print(next(counter))
print(next(counter))
print(next(counter))
'''
for i in counter:  # infinite loop
    print(i)
'''
print()

# Use-case 1: table
num = 5  # int(input('Enter a no.: '))
counter = itertools.count(start=num, step=num)
for i in range(10):
    print(next(counter))
print()

# Use-case 2:
data = [100, 200, 300, 500]
daily_data = list(zip(itertools.count(), data))
print(daily_data)
print()


# zip_longest():
# zip stops with shortest iterable, if want to stop with longest -> use itertools.zip_longest()
data = [100, 200, 300, 500]
daily_data = list(itertools.zip_longest(range(10), data))
print(daily_data)
print()


# cycle():
switch = ['On', 'Off']
cycle_ = itertools.cycle(switch)
print(next(cycle_))
print(next(cycle_))
print(next(cycle_))
print(next(cycle_))
print()


# repeat():
counter = itertools.repeat(2, times=3)
print(next(counter))
print(next(counter))
print(next(counter))
# print(next(counter))  # StopIteration

# Use-case:
# squares = list(map(pow, range(1, 101), [2 for i in range(100)]))
squares = list(map(pow, range(1, 101), itertools.repeat(2)))
print(squares)
print()


# starmap():
print(list(itertools.starmap(pow, [(2, 5), (3, 2), (10, 3)])))  # --> 32 9 1000
print()


# combinations():  (order does not matter + repetition is not allowed)
letters = ['a', 'b']
print('combinations():')
for i in itertools.combinations(letters, len(letters)):
    print(i)
print()


# combinations_with_replacement():  (order does not matter + repetition is allowed)
print('combinations_with_replacement():')
for i in itertools.combinations_with_replacement(letters, len(letters)):
    print(i)
print()


# permutations():  (order does matter + repetition is not allowed)
print('permutations():')
for i in itertools.permutations(letters, len(letters)):
    print(i)
print()


# product():  (order does matter + repetition is allowed) cartesian product
print('product():')
for i in itertools.product(letters, repeat=len(letters)):
    print(i)
print()


# chain():
list1 = [8, 73, 74]
list2 = ['a', 'f', 'q']
list3 = [0, 0]

# now if one wants to loop over these all the iterables one after one! naive approach->
# list4 = list1+list2+list3  # taking extra space
for i in list1+list2+list3:
    print(i)
print()

# expert approach:
list4 = itertools.chain(list1, list2, list3)
print(list4)  # coz as you can see it's not holding all the values at the same time in the memory
for i in list4:
    print(i)
print()


# itertools.islice()  # iterator slicing! just that don't load all the data of iterable, but just the data that is sliced!
# like slice()


# itertools.compress()  # (similar to filter())


# filterfalse(): (opposite of filter())


# dropwhile(), takewhile():


# accumulate():
print(list(itertools.accumulate([0, 1, 2, 3, 4, 5])))  # by default it sums, but we can perform other ops too
from operator import mul
print(list(itertools.accumulate([1, 2, 3, 4, 5, 0], mul)))
print()


# groupby():
