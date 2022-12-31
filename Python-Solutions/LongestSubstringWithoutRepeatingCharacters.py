# Given a string s, find the length of the longest substring without repeating
# characters.

# This is solved in O(n) time and O(1) space. The idea is to keep a dictionary
# of the last seen index of each character. Then, we iterate through the string
# and keep track of the longest substring we've seen so far. If we see a
# character that we've seen before, we update the start of the substring to be
# the max of the last seen index of that character and the current start of the
# substring. This is because we don't want to include any characters that we've
# seen before in the substring. We also update the last seen index of the
# character to be the current index.
# Time Complexity: O(n) where n is the length of the string.
# Space Complexity: O(1) since the dictionary is at most 26 characters long.

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    N = len(s)
    if N <= 1:
        return N
    dict = {}
    maxSub = 0
    start = 0
    for i, c in enumerate(s):
        if c in dict:
            start = max(dict[c], start)
        maxSub = max(maxSub, i - start + 1)
        dict[c] = i + 1
    return maxSub

print(lengthOfLongestSubstring("abcabcbb") == 3)
print(lengthOfLongestSubstring("bbbbb") == 1)
print(lengthOfLongestSubstring("pwwkew") == 3)
print(lengthOfLongestSubstring("dvdf") == 3)
