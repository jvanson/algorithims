# Can you write a function that reverses an inputted string without using the built-in Array#reverse method?

#Let's look at some examples. So, calling:

#reverseString("jake") should return "ekaj".

# Constraints
# Do not use the built-in #reverse() method or [::-1] if Python
# Ideal solution would run in O(n) time complexity and O(1) space complexity

def reverse_string(s):
    myarray = list(s)
    reversearray = []
    counter = len(myarray) - 1
    while counter > -1 :
        print(myarray[counter])
        reversearray.append(myarray[counter])
        counter -= 1
    return ''.join(reversearray)

# 2nd way that is faster using 2 pointer pattern
def reverse_string_two_pointer(s):
    my_array = list(s)
    start = 0
    end = len(my_array) - 1
    while start < end:
        swap_characters(my_array, start, end)
        print(my_array)
        start += 1
        end -= 1
    return ''.join(my_array)

def swap_characters(myarray, start, end):
    temp = myarray[start]
    myarray[start] = myarray[end]
    myarray[end] = temp

#result = reverse_string('reverseastring')
result = reverse_string_two_pointer('reverseastring')
print(result)

assert result == 'gnirtsaesrever'


