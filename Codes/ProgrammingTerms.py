# https://youtube.com/playlist?list=PL-osiE80TeTsnP0Nl1UDY8VZAlHu1m_MQ


# String Interpolation:
name = 'Samyak Jain'
print(f'My name is {name}.')
print()


# DRY: (You already know.)


# Idempotence: if f(f(x)) == f(x)!


# PnC:
# P: All the ways in which you can group something where the order does matter!
# C: All the ways in which you can group something where the order does NOT matter!
# Examples:
from itertools import combinations, permutations

my_list = [1, 2, 3, 4, 5, 6]
combinations = combinations(my_list, 3)
# permutations = permutations(my_list, 3)
print([result for result in combinations if sum(result) == 10])
# print([result for result in permutations if sum(result) == 10])
print()

word = 'sample'
my_letters = 'aelmps'
# combinations = combinations(my_letters, 6)
permutations = permutations(my_letters, 6)
for p in permutations:
    # print(p)
    if ''.join(p) == word:  # join()-> sexy 👏
        print('Match!')
        break
else:
    print('No Match!')


# Memoization: In computing, memoization or memoisation is an optimization technique used primarily to speed up
#              computer programs by storing the results of expensive function calls and returning the cached result
#              when the same inputs occur again. Wikipedia


# Mutable vs Immutable: https://youtu.be/5qQQ3yzbKp8 just watch at 2x.
