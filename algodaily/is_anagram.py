# Here's the definition of an anagram: a word, phrase, or name formed by
# rearranging the letters of another: such as cinema, formed from iceman.

# We are given two strings like "cinema" and "iceman" as inputs.
# Can you write a method isAnagram(str1, str2) that will return true or false
# depending on whether the strings are anagrams of each other?

def is_anagram(str1, str2):
    ## fill this in
    sort_str1 = ''.join(sorted(str1.lower()))
    sort_str2 = ''.join(sorted(str2.lower()))
    print(sort_str1)
    print(sort_str2)
    return sort_str1 == sort_str2


result = is_anagram('Mary', 'Army')
assert result == True
