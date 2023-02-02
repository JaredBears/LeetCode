from math import gcd

class Solution:
    # If the two strings have a common divisor, then str1 + str2 == str2 + str1
    # If they do not have a common divisor, we return an empty string.
    # If they do have a common divisor, we check for the length of the common divisor, which
    # is equal to the gcd of the lengths of the two strings.
    # We then return the substring of str1 from 0 to the length of the common divisor.
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        dLen = gcd(len(str1),len(str2))
        return str1[:dLen]