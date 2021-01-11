# Given a string, return whether or not it forms a palindrome ignoring case and non-alphabetical characters.
# Note: a palindrome is a sequence of characters that reads the same forwards and backwards.
#
# Ex: Given the following strings...
#
# "level", return true
# "algorithm", return false
# "A man, a plan, a canal: Panama.", return true

import re
in_palindrome = input('Type some string: ')
lowercase = in_palindrome.lower()
# re.sub(MATCH PATTERN, REPLACE STRING, STRING TO SEARCH)
alpha_only = re.sub("[^a-zA-Z]+", "", lowercase)
reverse_it = alpha_only[::-1]

print(alpha_only == reverse_it)


