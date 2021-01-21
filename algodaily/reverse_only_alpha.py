import re

def is_character(c):
    print('is_character', c)
    if re.match('[a-zA-Z]', c):
        return True
    return False

def swap_characters(myarray, start, end):
    print('swap characters orig array:', myarray)
    temp = myarray[end]
    myarray[end] = myarray[start]
    myarray[start] = temp
    print('swap characters orig array after swap:', myarray)
    return myarray

def reverse_only_alpha(s):
    orig_array = list(s)
    print(orig_array)
    start = 0
    end = len(orig_array) - 1
    copy_array = orig_array


    while start < end:
        start_is_character = is_character(orig_array[start])
        end_is_character = is_character(orig_array[end])

        print('start_is_character', start_is_character)
        print('end_is_character', end_is_character)

        if start_is_character and end_is_character:
            print('both are characters')
            swap_characters(orig_array, start, end)
            print('THIS IS ORIG ARRAY after swap:', orig_array)
            start += 1
            end -= 1

        elif start_is_character == False:
            print('start is NOT character')
            start += 1

        else:
            print('end is NOTT character')
            end -= 1

    # convert list to string
    return ''.join(orig_array)

result = reverse_only_alpha('sea!$hells3')
print(result)


assert result == 'sll!$ehaes3'
