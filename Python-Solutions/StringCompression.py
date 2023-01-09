from typing import List
class Solution:
    # In order to solve for the length of the compressed string, we need to iterate through the
    # characters in the array.  We can use a sliding window approach to keep track of the current
    # character and the number of times it appears.  If the next character is the same as the current
    # character, we can increment the count.  If the next character is different, we can add the current
    # character to the compressed string.  If the count is greater than 1, we can add the count to the
    # compressed string.  We can then iterate through the compressed string and replace the characters
    # in the array with the characters in the compressed string.  We then return the length of the compressed
    # string.
    # Time Complexity: O(n) where n is the length of the array
    # Space Complexity: O(n)
    def compress(self, chars: List[str]) -> int:
        s = ""
        i = 0
        while i < len(chars):
            char = chars[i]
            count = 1
            while i < len(chars) - 1 and chars[i + 1] == char:
                i += 1
                count += 1
            s += char
            if count > 1:
                s += str(count)
            i += 1
        for j in range(len(s)):
            chars[j] = s[j]
        return len(s)