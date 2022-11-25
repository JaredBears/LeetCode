# Runtime: 69 ms, faster than 9.06% of Python3 online submissions for Number of
# Steps to Reduce a Number to Zero.
# Memory Usage: 13.9 MB, less than 53.66% of Python3 online submissions for
# Number of Steps to Reduce a Number to Zero.
class SolutionRecursive:
    def numberOfSteps(self, num: int) -> int:
        def helper(n, steps):
            if n == 0:
                return steps
            if n % 2 > 0:
                return helper(n - 1, steps + 1)
            return helper(n//2, steps + 1)
        return helper(num, 0)

# Runtime: 62 ms, faster than 29.56% of Python3 online submissions for Number of
# Steps to Reduce a Number to Zero.
# Memory Usage: 14 MB, less than 8.53% of Python3 online submissions for Number
# of Steps to Reduce a Number to Zero.
class SolutionIterative:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num > 0:
            if num % 2 > 0:
                num -= 1
            else:
                num //= 2
            steps += 1
        return steps

# Runtime: 37 ms, faster than 85.90% of Python3 online submissions for Number of
# Steps to Reduce a Number to Zero.
# Memory Usage: 13.7 MB, less than 96.08% of Python3 online submissions for
# Number of Steps to Reduce a Number to Zero.
class SolutionBinary:
    def numberOfSteps(self, num: int) -> int:
        binary = bin(num)[2:]
        count = binary.count("1")
        return count + len(binary) - 1
