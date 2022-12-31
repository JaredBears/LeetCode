from typing import List
class Solution:
    # Find the longest consecutive subsequence in the array
    # We can use a set to store the numbers in the array and a set to store the numbers we have visited
    # We can iterate through the numbers in the array and check if the number is in the visited set
    # If the number is not in the visited set, we can initialize the start and end of the sequence 
    # to the current number and decrement the start and increment the end until we reach a number that
    # is not in the set
    # We can then update the max sequence length and add the numbers in the sequence to the visited set
    # to make sure we don't visit them again
    # We can then return the max sequence length
    # Time complexity: O(n) where n is number of unique numbers in the array
    # Space complexity: O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        visited = set()
        maxSeq = 0
        for num in nums:
            if num not in visited:
                visited.add(num)
                start = end = num
                while start-1 in nums:
                    start -= 1
                    visited.add(start)
                while end+1 in nums:
                    end += 1
                    visited.add(end)
                maxSeq = max(maxSeq, end - start + 1)
        return maxSeq