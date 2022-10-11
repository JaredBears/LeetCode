# Given a string s, find the length of the longest substring without repeating
# characters.

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if(len(s) == 0):
        return 0
    maxLength = 1

    chars = []

    for c in s:
        if (len(chars) == 0) or not (c in chars):
            chars.append(c)
            if len(chars) > maxLength:
                maxLength = len(chars)
        else:
            chars = chars[chars.index(c)+1:]
            chars.append(c)

    return maxLength

print(lengthOfLongestSubstring("abcabcbb") == 3)
print(lengthOfLongestSubstring("bbbbb") == 1)
print(lengthOfLongestSubstring("pwwkew") == 3)
print(lengthOfLongestSubstring("dvdf") == 3)
