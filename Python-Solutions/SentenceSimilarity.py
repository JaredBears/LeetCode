from typing import List
from collections import defaultdict

class Solution:
    # Time Complexity: O(n) where n is the length of the sentences
    # Space Complexity: O(n)
    # We will use a dictionary to map the words in the similarPairs to their similar words.
    # We will iterate through the sentences and compare the words.
    # If the words are not equal, we will check word2 is in the set of similar words of word1.
    # If not, return false.
    # If we reach the end of the loop, return true.
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        N = len(sentence1)
        if N != len(sentence2): return False

        pairMatch = defaultdict(set)
        for word1, word2 in similarPairs:
            pairMatch[word1].add(word2)
            pairMatch[word2].add(word1)
        for i in range(N):
            word1 = sentence1[i]
            word2 = sentence2[i]
            if word2 != word1 and word2 not in pairMatch[word1]:
                return False
        return True