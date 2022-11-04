class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        d = Counter(list(s))
        palindromeLength = 0
        single = False
        for char, count in d.items():
            if count % 2 == 0:
                palindromeLength += count
            else:
                palindromeLength += count - 1
                single = True
        if single:
            palindromeLength += 1
        return palindromeLength
