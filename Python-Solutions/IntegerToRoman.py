class Solution:
    # This is solved in O(1) time and O(1) space. The idea is to loop through the
    # integer and add the appropriate roman numeral to the string. We subtract the
    # integer by the value of the roman numeral we just added. We do this until
    # the integer is 0.
    # The only reason it is solved in O(1) time and O(1) space is because the
    # integer is guaranteed to be between 1 and 3999. If it wasn't, it would be
    # O(n) time and O(n) space for arbitrarily large integers.
    
    def intToRoman(self, num: int) -> str:
        romans = ""
        while num > 0:
            if num >= 1000:
                romans = romans + "M"
                num = num - 1000
            elif num >= 900:
                romans = romans + "CM"
                num = num - 900
            elif num >= 500:
                romans = romans + "D"
                num = num - 500
            elif num >= 400:
                romans = romans + "CD"
                num = num - 400
            elif num >= 100:
                romans = romans + "C"
                num = num - 100
            elif num >= 90:
                romans = romans + "XC"
                num = num - 90
            elif num >= 50:
                romans = romans + "L"
                num = num - 50
            elif num >= 40:
                romans = romans + "XL"
                num = num - 40
            elif num >= 10:
                romans = romans + "X"
                num = num - 10
            elif num == 9:
                romans = romans + "IX"
                num = 0
            elif num >= 5:
                romans = romans + "V"
                num = num - 5
            elif  num == 4:
                romans = romans + "IV"
                num = 0
            elif num >=1:
                romans = romans + "I"
                num = num - 1
        return romans;
