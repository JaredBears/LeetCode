from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(idx, edx):
            theif1, theif2 = 0, 0
            for i in range(idx, edx):
                temp = max(nums[i] + theif1, theif2)
                theif1 = theif2
                theif2 = temp
            return theif2
        n = len(nums)
        if n <= 3:
            return max(nums)
        return max(helper(0, n-1), helper(1, n))
