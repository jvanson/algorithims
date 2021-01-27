# Suppose we're given an array of numbers like the following:

# [4, 2, 4]

# Could you find the majority element? A majority is defined as "the greater part,
# or more than half, of the total. It is a subset of a set consisting of more than half of the set's elements."

# Let's assume that the array length is always at least one, and that there's always a majority element.

# In the example above, the majority element would be 4.

import math

def find_majority(a):
    print(a)
    majority_threshold = math.floor(len(a) / 2)
    print('threshold', majority_threshold)
    counter = {}


    for i in range(0, len(a)):
        print(a[i])

        temp = counter.get(a[i], 0)
        temp += 1
        counter.update({a[i]: temp})

    for key, value in counter.items():
        if value > majority_threshold:
            print('majority:', key)
            return key
    return 'no majority'


    print(counter)

# another way that is faster
# sort the array and find the middle
# if 0 to middle +1 are equal, then
# it's the majority
# [5,3,5,4,22,5,5]
# sorted [3,4,5,5,5,5,22]



result = find_majority([4, 2, 4, 2, 1, 1, 1, 1, 1])
1,1,1,1,2,2
print(result)
assert result == 1
