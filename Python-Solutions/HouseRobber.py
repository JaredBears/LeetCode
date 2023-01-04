from typing import List

class Solution:
    # Use dynamic programming to find the maximum amount of money that can be robbed
    # Imagine there are two theifs, one that robs every other house, and one that robs every other 
    # house starting at the second house.  The maximum amount of money that can be robbed is the
    # maximum of the two theifs
    # Time Complexity: O(n)
    def rob(self, nums: List[int]) -> int:
        theif1, theif2 = 0, 0
        for n in nums:
            theif1, theif2 = theif2, max(n + theif1, theif2)
        return theif2
