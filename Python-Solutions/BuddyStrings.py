from collections import Counter

class Solution:
    # First, we need to get a count of each letter in both strings.
    # If the counts are not the same, then we can return False, 
    # because there is no way to make the strings equal.
    # If the two strings are identical, the only way to make them
    # equal is to swap two identical letters. Return True if there
    # are at least two of the same letter and False otherwise.
    # If the two strings are not identical, we need to make sure
    # that there are exactly two letters that are different.
    # Iterate through the strings and count the number of differences.
    # Return True if there are exactly two differences and False otherwise.
    def buddyStrings(self, s: str, goal: str) -> bool:
        counts = Counter(s)
        countgoal = Counter(goal)
        if counts != countgoal:
            return False
        if s == goal:
            return max(counts.values()) > 1
        differences = 0
        for i in range(len(s)):
            if s[i] != goal[i]:
                differences += 1
        return differences == 2