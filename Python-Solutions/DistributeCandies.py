from typing import List
from collections import Counter
class Solution:
    # Time Complexity: O(n) where n is the number of candies
    # Space Complexity: O(k) where k is the number of unique candies
    # This is a pretty simple problem, just use a counter to count the number of each candy type
    # and then return the minimum of the number of candies divided by 2 and the number of unique
    # candies
    def distributeCandies(self, candyType: List[int]) -> int: 
        counts = Counter(candyType)
        return min(len(candyType)//2,len(counts))