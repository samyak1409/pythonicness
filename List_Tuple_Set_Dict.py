lis = [1, 2, 'Samyak']
lis2 = [3, 4, 'Jain']
lis.extend(lis2)
print(lis)


lis = ['Sam', 'j']
lis_str = ', '.join(lis)  # note-> all elements in lis must be of type str
print(lis_str)


l1 = [1, 2]
l2 = l1
l1[-1] = 100
print(l2)  # waah :|


# creating an empty set->
# set1 = {}  # wrong, making dict
set1 = set()  # correct


list1 = ['a', 'b', 'c']
popped = list1.pop()
print(popped)


dict1 = {1: '1', 2: '2', 3: '3'}
del dict1[2]  # :
print(dict1)
dict1.update({1: '10', 2: '20', 3: '30'})
print(dict1)
