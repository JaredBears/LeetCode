class Solution:
    # This is a variation of the fibonacci sequence. The idea is to use a for loop to iterate through
    # the first n numbers of the fibonacci sequence. We use two variables to keep track of the first
    # and second numbers of the sequence. We then iterate through the sequence and update the first
    # and second variables to the second and first + second numbers of the sequence.
    # We don't need to store the entire sequence since we only need the most recent two numbers to
    # calculate the next number in the sequence.
    # Time Complexity: O(n) where n is the number of fibonacci numbers to calculate
    # Space Complexity: O(1) since we only use two variables to keep track of the fibonacci numbers
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        first = 1
        second = 2
        for i in range(2, n):
            first, second = second, first + second
        return second