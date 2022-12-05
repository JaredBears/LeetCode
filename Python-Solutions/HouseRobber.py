class Solution:
    def rob(self, nums: List[int]) -> int:
        theif1, theif2 = 0, 0
        for n in nums:
            temp = max(n + theif1, theif2)
            theif1 = theif2
            theif2 = temp
        return theif2
