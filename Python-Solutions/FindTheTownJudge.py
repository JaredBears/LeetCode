from typing import List
from collections import Counter
class Solution:
    # We will use a dictionary to keep track of the number of times
    # a person is trusted. We will also use a set to eliminate people
    # who are not the judge. We will iterate through the trust list
    # and add the person who is trusted to the dictionary and add the
    # person who trusts to the set. We will then iterate through the
    # dictionary and check if the person is not in the set and if the
    # person is trusted by everyone else. If so, we will return the
    # person. If not, we will return -1.
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        trust_count = Counter()
        eliminated = set()
        for person1, person2 in trust:
            eliminated.add(person1)
            trust_count[person2] += 1
        for i in range(n + 1):
            if i not in eliminated and trust_count[i] == n - 1:
                return i
        return -1