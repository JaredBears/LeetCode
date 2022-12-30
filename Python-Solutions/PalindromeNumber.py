class Solution:
    # Time Complexity: O(log10(n)) where n is the number
    # Space Complexity: O(1)
    # This is a pretty simple problem, just reverse the number and compare it to the original number
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reverse = 0
        i = x
        while i > 0:
            reverse = (reverse * 10) + (i % 10)
            i //= 10
        return reverse == x