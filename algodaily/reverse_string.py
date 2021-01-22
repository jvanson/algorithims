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



result = reverse_string('reverseastring')
print(result)

assert result == 'gnirtsaesrever'


