class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Super simple, just use a for loop to iterate through the numbers and add the previous two numbers
    # together
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        first = 0
        second = 1
        for i in range(2, n+1):
            temp = second
            second = first + second
            first = temp
        return second