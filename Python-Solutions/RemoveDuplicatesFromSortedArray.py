from collections import List
class Solution:
    # The idea is simple: We'll use two nested while loops.  The outer loop will iterate through the array, 
    # and the inner loop will check for duplicate values.  If the two values are equal, we'll remove the 
    # second value. Once they are no longer equal, we'll increment the outer loop's index and repeat the 
    # process until we have reached the end of the array. Then we'll return the length of the array.

    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums) - 1:
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                nums.pop(i + 1)
            i += 1
        return len(nums)