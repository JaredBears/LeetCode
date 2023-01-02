class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Super simple, just use a for loop and keep track of the previous two numbers in the sequence
    # to calculate the next number in the sequence. We don't need to store the entire sequence since
    # we only need the previous two numbers.  At each iteration, we update the first and second variables
    # to the second and first + second numbers of the sequence.
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        first = 1
        second = 1
        for i in range(2, n):
            first, second = second, first + second
        return second