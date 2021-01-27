# In a given array of numbers, one element will show up once and the others will each show up twice. Can you find the number that only appears once in O(n) linear time? Bonus points if you can do it in O(1) space as well.

def lonely_number(numbers):
    counter = {}
    for i in range(0, len(numbers)):
        add_it = counter.get(numbers[i], 0)
        add_it += 1
        counter.update(
            {
                numbers[i]: add_it
            }
        )

    for key, value in counter.items():
        if value == 1:
            return key

def lonely_number_faster(numbers):
    appearances = {}

    for num in numbers:
        if num in appearances:
            del appearances[num]
        else:
            appearances[num] = True
    # appearances.keys() in python 3 returns an iterable but no indexable object
    # so use list to make it a list
    return list(appearances.keys())[0]






result = lonely_number([4, 4, 6, 1, 3, 1, 3])
print(result)

result = lonely_number_faster([4, 4, 6, 1, 3, 1, 3])
print(result)
