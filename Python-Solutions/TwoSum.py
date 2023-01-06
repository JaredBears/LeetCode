from collections import List, Counter
class Solution:
    # Use a hash map to store the number and its index.
    # Iterate through the list and check if the hash map contains the complement.
    # If it does, return the index of the current number and the index of the complement.
    # Time complexity: O(n)
    # Space complexity: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = Counter()
        for i, num in enumerate(nums):
            hm[num] = i
        for i, num in enumerate(nums):
            j = hm[target - num]
            if i != j and j:
                return [i, j]