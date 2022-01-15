my_list = [0, 1, 2, 3, 4, ]


# Aam Zindagi-> Everything Normal (more lines of code, time and space complexity)
def square(list_):
    result = list()
    for x in list_:
        result.append(x*x)
    return result


nums = square(my_list)
print(f'\n{nums}\n')


# Type 1 Mentos Zindagi-> Using yield!
def square(list_):
    for x in list_:
        yield x*x  # yield makes a normal function-> a generator function!

# yield is a keyword in Python that is used to return from a function without destroying the states of its local variable
# and when the function is called, the execution starts from the last yield statement.
# Any function that contains a yield keyword is termed as generator.

# What is difference between yield and return in Python?
# 'return' sends a specified value back to its caller, whereas 'yield' can produce a sequence of values.
# We should use 'yield' when we want to iterate over a sequence but don't want to store the entire sequence in memory.
# 'yield' is used in Python generators.


nums = square(my_list)
print(nums)  # generator object
# print(next(nums), next(nums), next(nums), next(nums), next(nums))
# print(next(nums))  # traceback
# print(list(nums), '\n')  # if we'll do this, this will increase space complexity and using generators will be wasted (complexities will literally be the same as in Aam Zindagi)
# so do this->
for num in nums:
    print(num, end=' ')
print('\n')
# Generators are useful when we don't want the sequence to be saved, but to use it only once!


# Type 2 Mentos Zindagi-> List Comprehension!
nums = (num*num for num in my_list)
print(nums)  # generator object
for i in nums:
    print(i)

# print(list(nums))  # type-casting! (gen to list)
