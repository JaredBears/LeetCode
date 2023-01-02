import re

class Solution:
    # Use regular expressions to check if the word is all uppercase, all lowercase, or first letter uppercase
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def detectCapitalUse(self, word: str) -> bool:
        return re.match('^[A-Z]+$|^[A-Z][a-z]+$|^[a-z]+$', word)