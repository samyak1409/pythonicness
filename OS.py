import os  # module which allow us to interact with underlying OS!


def print_(*xyz):  # (extension of print()), *xyz-> Tuple(any number...)  any no. of arguments can be passed!
    print(*xyz, '\n' + '-'*74)


print_('')
print_(dir(os))  # all attributes


print_(os.getcwd())  # cwd- current working directory


os.chdir('C:\\Users\\Samyak\\Desktop')  # '\\' or '/' ! :), changing directory
print_(os.getcwd())

print_(os.listdir())  # by default this FUNCTION will list the the contents of the cwd!, however, we can explicitly pass path to any dir!


# os.mkdir('New Folder!')  # creates a dir(folder!) in cwd
# os.makedirs('New Folder!\\Sub-Folder')  # super-mkdir!, mkdir() can't create folder with sub-folder(s), makedirs() can! :D, so will always use makedirs()!
# print_(os.listdir())


# os.rmdir('New Folder!')  # remove dir(note that dir should be empty!, if not we have to use removedirs() :), like mkdir()
# os.removedirs('New Folder!\\Sub-Folder')  # remove dirs, like makedirs()
# print_(os.listdir())


# os.rename(src='Minesweeper - Shortcut.lnk', dst='Minesweeper-Shortcut.lnk')  # renaming
# print_(os.listdir())


# stats = os.stat('Minesweeper (64-bit) - Shortcut.lnk')  # info
# print_(stats)
# from datetime import datetime  # :))
# print_(datetime.fromtimestamp(stats.st_mtime))  # time in readable form!


for path, dir_names, file_names in os.walk('C:\\Users\\Samyak\\Desktop'):  # cool
    print('Location:', path)
    print('Folders:', dir_names)
    print('Files:', file_names, '\n')
print_('')

for i, j in os.environ.items():
    if 'Samyak' in j:
        print(f'{i}- {j}')
print_('')

home = os.environ.get('HOMEPATH')
print_('HOMEPATH-', home)  # now this can be used in, for eg, I want to create shortcut of my app at user's desktop!

print_(os.path.join(home, 'new_file.txt'))  # join two paths, tc of the formatting!

sample_path = 'My Folder/file.extension'
print(sample_path)
print(os.path.basename(sample_path), ',', os.path.dirname(sample_path), ',', os.path.exists(sample_path))
print_(os.path.split(sample_path), ',', os.path.isdir(sample_path), ',', os.path.isfile(sample_path), ',', os.path.splitext(sample_path))

print_(dir(os.path))  # checkout!
