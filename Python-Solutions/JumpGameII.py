from typing import List
class Solution:
    # Use dynamic programming to find the minimum number of jumps to reach the last index
    # Start at the end, and work backwards.  At each index, check to see which of the next
    # indices can reach the last index in the fewest number of jumps.  The current index
    # can reach the last index in the fewest number of jumps by taking the minimum of the
    # number of jumps from the next indices plus one.
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 1:
            return 0
        def checkRemaining(idx):
            if idx + nums[idx] >= N - 1:
                return 1
            minSteps = float('inf')
            for i in range(idx + 1, idx + nums[idx] + 1):
                minSteps = min(minSteps, 1 + dp[i])
            return minSteps
        dp = [0] * N
        dp[-2] = 1
        for i in range(N - 2, -1, -1):
            dp[i] = checkRemaining(i)
        return dp[0]