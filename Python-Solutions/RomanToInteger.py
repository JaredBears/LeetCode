class Solution:
    # The idea is to use a dictionary to store the conversion of each roman numeral to its integer value.
    # Then, we iterate through the string, checking if the next two characters are in the dictionary.
    # If they are, we add the value of the two characters to the answer and increment i by 2.
    # If they are not, we add the value of the single character to the answer and increment i by 1.
    # We do this until we reach the end of the string, and then return the answer.
    # Time Complexity: O(n) where n is the length of the string.
    # Space Complexity: O(1) since the dictionary is constant size.
    def romanToInt(self, s: str) -> int:
        conversion = {
            'M': 1000,'CM': 900,
            'D': 500,'CD': 400,
            'C': 100,'XC': 90,
            'L': 50,'XL': 40,
            'X': 10,'IX': 9,
            'V': 5,'IV': 4,
            'I': 1
        }
        answer = 0
        i = 0
        while i < len(s):
            one = s[i]
            two = s[i:i+2]
            if two in conversion:
                answer += conversion[two]
                i += 2
            else:
                answer += conversion[one]
                i += 1
        return answer