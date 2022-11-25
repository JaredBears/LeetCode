# Runtime: 47 ms, faster than 68.09% of Python3 online submissions for
# Strobogrammatic Number.
# Memory Usage: 13.8 MB, less than 97.06% of Python3 online submissions for
# Strobogrammatic Number.

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        strog_match = {
            "0": "0",
            "1": "1",
            "6": "9",
            "8": "8",
            "9": "6"
        }
        length = len(num)
        for i in range(length):
            n = num[i]
            o = num[length - 1 - i]
            if n not in strog_match or strog_match[n] != o:
                return False
        return True
