class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def helper(n):
            if n == 1 or n == 3:
                return True
            elif n < 3:
                return False
            if n % 9 == 0:
                return helper(n//9)
            if n % 3 == 0:
                return helper(n//3)
            return False
        return helper(n)
