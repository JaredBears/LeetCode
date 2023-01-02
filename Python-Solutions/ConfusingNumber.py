class Solution:
    # The idea is to use a dictionary to map the confusing digits to their corresponding digits.
    # We iterate through the digits of the number and check if the digit is in the dictionary.
    # If the digit is not in the dictionary, we return False. If the digit is in the dictionary,
    # we add the corresponding digit to the output. We then check if the output is equal to the
    # input. If the output is equal to the input, we return False. If the output is not equal to
    # the input, we return True.
    # Time Complexity: O(L) where L is the number of digits in the input, since we are performing
    # a constant time operation on each digit. L = log(n) where n is the input.
    # Space Complexity: O(L) since we are storing the digits of the input in the output variable.
    def confusingNumber(self, n: int) -> bool:
        confusing_digits = {0:0, 1:1, 8:8, 6:9, 9:6}
        i = n
        output = 0
        while i > 0:
            i, digit = divmod(i, 10)
            if digit not in confusing_digits:
                return False 
            output = output * 10 + confusing_digits[digit]
        return output != n