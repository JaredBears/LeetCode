# Given two strings s and part, perform the following operation on s until all
# occurrences of the substring part are removed:
#
# * Find the leftmost occurrence of the substring part and remove it from s.
#
# Return s after removing all occurrences of part.
#
# A substring is a contiguous sequence of characters in a string.

def removeOccurrencesNative(s, part):
    """
    :type s: str
    :type part: str
    :rtype: str
    """
    while part in s:
        s = s.replace(part, "", 1)
    return s

def removeOccurrencesList(s, part):
    """
    :type s: str
    :type part: str
    :rtype: str
    """
    sList = [' '] * len(s)
    pList = list(part)

    i = 0
    j = len(pList)
    for c in s:
        sList[i] = c
        i += 1
        if i >= j and sList[i - j:i] == pList:
            i -= j
    return ''.join(sList[:i])

print(removeOccurrencesList("daabcbaabcbc", "abc") == "dab")
print(removeOccurrencesNative("daabcbaabcbc", "abc") == "dab")
print(removeOccurrencesList("axxxxyyyyb", "xy") == "ab")
print(removeOccurrencesNative("axxxxyyyyb", "xy") == "ab")
