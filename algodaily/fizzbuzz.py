"""Fizz Buzz is a classic interview question that apparently many engineering candidates can't solve! Let's cover it today.

We're given a number in the form of an integer n.
Write a function that returns the string representation of all numbers
to n based on the following rules:

If it's a multiple of 3, represent it as "fizz".
If it's a multiple of 5, represent it as "buzz".
If it's a multiple of both 3 and 5, represent it as "fizzbuzz".
If it 's neither, just return the number itself."""

def fizz_buzz(n):
    result = ''
    for x in range(1,n+1):
        if (x % 3 == 0) and (x % 5 == 0):
            result += 'fizzbuzz'
        elif x % 3 == 0:
            result += 'fizz'
        elif x % 5 == 0:
            result += 'buzz'
        else:
            result += f'{x}'


    return result

result = fizz_buzz(15)
print(result)
#fizz_buzz(10)
#fizz_buzz(31)
#fizz_buzz(15)
