class Solution:
    # Check each digit of the number and see if it divides the number
    # If it does, increment the count
    # Return the count
    # Time Complexity: O(log n)
    def countDigits(self, num: int) -> int:
        copy = num
        count = 0
        while copy:
            copy, digit = divmod(copy, 10)
            if not num % digit:
                count += 1
        return count