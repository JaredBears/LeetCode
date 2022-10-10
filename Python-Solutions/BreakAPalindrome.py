# Given a palindromic string of lowercase English letters palindrome, replace
# exactly one character with any lowercase English letter so that the resulting
# string is not a palindrome and that it is the lexicographically smallest one
# possible.
#
# Return the resulting string. If there is no way to replace a character to make
# it not a palindrome, return an empty string.
#
# A string a is lexicographically smaller than a string b (of the same length)
# if in the first position where a and b differ, a has a character strictly
# smaller than the corresponding character in b. For example, "abcc" is
# lexicographically smaller than "abcd" because the first position they differ
# is at the fourth character, and 'c' is smaller than 'd'.

def breakPalindrome(palindrome: str) -> str:
    if len(palindrome) <= 1:
        return ""
    i = 0
    while i < (len(palindrome))//2:
        if(palindrome[i] != 'a'):
            return palindrome[:i] + 'a' + palindrome[i+1:]
        i += 1
    return palindrome[:-1] + 'b'

testOne = "abccba"
testTwo = "a"
testThree = "aa"
testFour = "aba"

print(breakPalindrome(testOne) == "aaccba")
print(breakPalindrome(testTwo) == "")
print(breakPalindrome(testThree) == "ab")
print(breakPalindrome(testFour) == "abb")
