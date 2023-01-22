from typing import List
class Solution:
    # Dynamic Programming, depth first search
    # Time Complexity: O(n * 2^n) where n is the length of the string
    # Space Complexity: O(n^2)
    def partition(self, s: str) -> List[List[str]]:
        N = len(s)
        dp = [[False for _ in range(N)] for _ in range(N)]
        result = []
        def dfs(start: int, current: List[str]):
            if start >= N:
                result.append(current[:])
                return
            for end in range(start, N):
                if s[start] == s[end] and (end - start <= 2 or dp[start + 1][end - 1]):
                    dp[start][end] = True
                    current.append(s[start:end+1])
                    dfs(end + 1, current)
                    current.pop()
            
        dfs(0, [])
        return result