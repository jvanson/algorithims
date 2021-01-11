# Given a string, reverse all of its characters and return the resulting string.
#
# Ex: Given the following strings...
#
# “Cat”, return “taC”
# “The Daily Byte”, return "etyB yliaD ehT”
# “civic”, return “civic”

some_string = input('Type in something: ')
print(some_string)
my_array = some_string.split()

reverse_it = ''
for word in my_array:
    reverse_it += f'{word[::-1]} '
    #print(word[::-1])
    #print(f'here is {word}')
print(reverse_it)

