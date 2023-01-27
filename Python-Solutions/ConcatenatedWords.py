from typing import List
from functools import cache

class Solution:
    # This is a memoized recursive solution.
    # First, we create a set of all of the words for fast lookup.
    # Then, we create a recursive function that takes a word as input.
    # In the recursive function, we iterate through the word and split the
    # word into a prefix and a suffix. 
    # If the prefix and suffix are both in the set, then we return True. 
    # Same if the prefix is in the set and the suffix is a concatenation of other words.
    # Same if the suffix is in the set and the prefix is a concatenation of other words 
    # If none of these conditions are met, we return False.
    # We use the @cache decorator to memoize the recursive function and improve performance
    # Finally, we iterate through the list of words and return the words that are 
    # concatenations of other words.
    def findAllConcatenatedWordsInADict(self, words: 'List[str]') -> 'List[str]':
        wordset = set(words)
        @cache
        def dfs(word):
            N = len(word)
            for i in range(1, N):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in wordset and suffix in wordset:
                    return True
                if prefix in wordset and dfs(suffix):
                    return True
                if suffix in wordset and dfs(prefix):
                    return True
            return False
        return [word for word in words if dfs(word)] 