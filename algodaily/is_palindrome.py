# Given a string str, can you write a method that will return True
# if is a palindrome and False if it is not?
# If you'll recall, a palindrome is defined as "a word, phrase, or sequence
# that reads the same backward as forward".
#
# For now, assume that we will not have input strings that contain special characters
# or spaces
import re


def is_palindrome(s):
    orig_str = s.lower()
    # re.sub(MATCH PATTERN, REPLACE STRING, STRING TO SEARCH)
    orig_str_alpha = re.sub('[\W]', '', orig_str)
    reverse_str = orig_str_alpha[::-1]
    return reverse_str == orig_str_alpha



result = is_palindrome('A Santa Lived As a Devil At NASA')
assert result == True
