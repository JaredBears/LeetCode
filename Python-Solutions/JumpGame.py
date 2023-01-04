from typing import List
class Solution:
    # Use dynamic programming to find if the last index can be reached
    # Start at the end, and work backwards.  If the current index can reach another good index, then
    # it is a good index. If the first index is a good index, then it can reach the last index
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        dp = [False] * N
        dp[-1] = True
        # check if the current index can reach another good index
        def checkGood(idx):
            if idx + nums[idx] >= N - 1:
                return True
            for i in range(idx + 1, idx + nums[idx] + 1):
                if dp[i]: return True
            return False
        for i in range(N-2, -1, -1):
            dp[i] = checkGood(i)
        return dp[0]