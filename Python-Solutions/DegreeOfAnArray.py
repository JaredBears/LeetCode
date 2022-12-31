from typing import List
from collections import Counter

class Solution:
    # The idea is to use three dictionaries to store the leftmost index, rightmost index, and count
    # of each number in the array.
    # Then, we find the maximum degree of the array and iterate through the count dictionary to find
    # the numbers that have that degree.
    # For each number with the maximum degree, we find the length of the subarray that contains that
    # number by subtracting the leftmost index from the rightmost index and adding 1.
    # Time Complexity: O(n+k) where n is the length of the array and k is the number of unique numbers
    # Space Complexity: O(k)
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right, count = {}, {}, Counter(nums)
        for i, x in enumerate(nums):
            if x not in left: left[x] = i
            right[x] = i

        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)

        return ans