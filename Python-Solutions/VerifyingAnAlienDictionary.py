from typing import List

class Solution:
    # Time Complexity: O(n) where n is the length of the words
    # Space Complexity: O(1)
    # We will use a dictionary to map the characters of the order string to their indices.
    # We will iterate through the words and compare the characters of the current word to the next word.
    # If the characters are not equal, we will check if the character in the current word is greater 
    # than the character in the next word, if so, return false.
    # If the characters are equal, we will continue to the next character.
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {key:value for value, key in enumerate(order)}
        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i+1]): return False
                char1 = words[i][j]
                char2 = words[i+1][j]
                if char1 != char2:
                    if d[char1] > d[char2]: return False
                    break
        return True