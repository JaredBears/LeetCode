from typing import List
class Solution:
    # Iterate through each column and check if the column is sorted
    # If it is not, increment the count
    # Return the count
    # Time Complexity: O(n) where n is the total number of characters in the array
    # Space Complexity: O(1)
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for j in range(len(strs[0])):
            prev = None
            for i in range(len(strs)):
                if not prev or strs[i][j] >= prev:
                    prev = strs[i][j]
                else:
                    count += 1
                    break
        return count