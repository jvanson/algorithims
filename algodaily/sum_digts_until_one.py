# We're provided a positive integer num. Can you write a method to repeatedly add all of its digits until the result has only one digit?
#
# Here's an example: if the input was 49, we'd go through the following steps:
#
# SNIPPET
#
# // start with 49
#
# 4 + 9 = 13
#
# // move onto 13
#
# 1 + 3 = 4
# We would then return 4.


def sum_digits(num):
    split_nums = [int(x) for x in str(num)]
    print(split_nums)
    count = 0

    for i in split_nums:
        count += i
        print('here is count', count)

    if count < 10:
        return count
    else:
        print('if condition count', count)
        # return value of evaluating sum_digits(count)
        # otherwise if you just return count
        # it will return the previous value of count
        # when the function was last invoked

        return sum_digits(count)

result = sum_digits(49)
print(result)
