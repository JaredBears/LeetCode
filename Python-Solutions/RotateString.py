class Solution:
    # This is a brute force solution.
    # We iterate through the string and rotate it by one character.
    # If the rotated string is equal to the goal string, we return True.
    # If we iterate through the entire string and don't find a match, we return False.
    # Time Complexity: O(N) where N is the length of the string
    # Space Complexity: O(N) - we create a new string each time we rotate the string
    # because strings are immutable in Python
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            s = s[1:] + s[0]
            if s == goal: return True
        return False