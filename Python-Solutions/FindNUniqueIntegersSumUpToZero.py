# Runtime: 41 ms, faster than 83.36% of Python3 online submissions for Find N
# Unique Integers Sum up to Zero.
# Memory Usage: 13.9 MB, less than 54.15% of Python3 online submissions for Find
# N Unique Integers Sum up to Zero.

class Solution:
    def sumZero(self, n: int) -> List[int]:
        answer = [0] * n
        if n == 1: return answer
        i = 0
        if n % 2 > 0:
            i += 1
            n -= 1
        while n > 0:
            answer[i] = i + 1
            answer[i + 1] = (i + 1) * -1
            i += 2
            n -= 2
        return answer
