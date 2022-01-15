print(f'\n{__name__}. I will always print!\n')  # special variable!


def func1():
    print('Ran the file directly!')


def func2():
    print('Imported!')  # on importing any module, it's executed!!!!


if __name__ == '__main__':
    func1()
else:
    func2()

# checkout-> "if name is main (2).py"
