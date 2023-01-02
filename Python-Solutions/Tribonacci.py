class Solution:
    # The idea is to use a for loop to iterate through the first n numbers of the tribonacci sequence.
    # We use three variables to keep track of the first, second, and third numbers of the sequence.
    # We then iterate through the sequence and update the first, second, and third variables to the
    # second, third, and first + second + third numbers of the sequence.
    # We don't need to store the entire sequence since we only need the most recent three numbers to
    # calculate the next number in the sequence.
    # Time Complexity: O(n) where n is the number of tribonacci numbers to calculate
    # Space Complexity: O(1) since we only use three variables to keep track of the tribonacci numbers
    def tribonacci(self, n: int) -> int:
        first = 0
        second = 1
        third = 1
        if n <= 2:
            return min(1, n)
        for i in range(2, n): 
            first, second, third = second, third, first + second + third
        return third