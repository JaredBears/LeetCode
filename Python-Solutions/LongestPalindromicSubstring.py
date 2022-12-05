class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]
        answer = ""
        for i in range(len(s)):
            odd = helper(i, i)
            even = helper(i, i+1)
            if len(odd) > len(even) and len(odd) > len(answer):
                answer = odd
            elif len(even) > len(odd) and len(even) > len(answer):
                answer = even
        return answer
