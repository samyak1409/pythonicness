# https://youtu.be/jTYiNjvnHZY just watch at 2x


list1 = [1, 2, 3]

for i in list1:  # anything can be looped over is called an iterable (as the name suggests!), so we see list is an iterable
    print(i)
print()

# so what's iterator? ->

i_list1 = iter(list1)

print(next(i_list1))
print(next(i_list1))
print(next(i_list1))
# print(next(i_list1))  # StopIteration
print()

# what for loop does in the bg is:

list1 = [5, 4, 6]
i_list1 = iter(list1)

while True:
    try:
        print(next(i_list1))
    except StopIteration:
        break


# Question: https://youtu.be/C3Z9lJXI6Qw

# solution using gens!->
def sentence(s):
    for w in s.split():
        yield w


sentence1 = sentence('This is a test')
for word in sentence1:
    print(word)
