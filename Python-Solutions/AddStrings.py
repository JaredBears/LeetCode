class Solution:
    # Time Complexity: O(n) where n is the length of the longer string
    # Space Complexity: O(n) where n is the length of the longer string
    # With this one, we will need to iterate through the strings from the end and add the digits
    # together. If the sum is greater than 10, subtract 10 and add 1 to the carry else reset the carry to 0. 
    # If the carry is 1 at the end, add it to the beginning of the answer
    def addStrings(self, num1: str, num2: str) -> str:
        N1 = len(num1)
        N2 = len(num2)
        answer = ""
        if N2 > N1:
            num2, num1 = num1, num2
            N2, N1 = N1, N2
        carry = 0
        for i in range(-1, -(N1+1), -1):
            digit1 = int(num1[i])
            digit2 = 0
            if -i < N2+1:
                digit2 = int(num2[i])
            digit3 = digit1 + digit2 + carry
            if digit3 >= 10:
                digit3 -= 10
                carry = 1
            else: carry = 0
            answer = str(digit3) + answer
        if carry:
            answer = str(carry) + answer
        return answer