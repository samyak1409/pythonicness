# NOTE:
# if you want to use a variable or call a function using it's name (string), you can do:

var = 'Hello'


def func(): return 'World'


print(globals()['var'])
print(globals()['func']())


# and if the function is a method from some other module, then->
# Assuming module foo with method bar:

"""
import foo
print(getattr(foo, 'bar')())
"""
