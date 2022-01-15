# https://youtu.be/D3JvDWO-BY4


# list
numbers = [7, 63, 426, 86, 222]
s_numbers = sorted(numbers, reverse=True)
numbers.sort(reverse=True)
print(s_numbers)
print(numbers)
print()


# tuples
# just note that class tuple don't have sort() method


# dictionary
# same for dictionary
di = {'name': 'Samyak', 'stream': 'CS', 'age': 20}
print(sorted(di))  # only returns sorted keys!
print()


# absolute sorting
nums = [-5, -4, -3, 0, 1, 2]
print(sorted(nums, key=abs))  # checkout! what it does is just pass every value into the key function before sorting!!!!
print()
