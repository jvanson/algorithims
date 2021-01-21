import re

def is_character(c):
    if re.match('[a-zA-Z]', c):
        return True
    return False

def swap_characters(myarray, start, end):
    temp = myarray[end]
    myarray[end] = myarray[start]
    myarray[start] = temp
    return myarray

def reverse_only_alpha(s):
    orig_array = list(s)
    start = 0
    end = len(orig_array) - 1

    while start < end:
        start_is_character = is_character(orig_array[start])
        end_is_character = is_character(orig_array[end])

        if start_is_character == False:
            start += 1
        elif end_is_character == False:
            end -= 1
        else:
            swap_characters(orig_array, start, end)
            start += 1
            end -= 1

    # convert list to string
    return ''.join(orig_array)

result = reverse_only_alpha('sea!$hells3')
print(result)


assert result == 'sll!$ehaes3'
