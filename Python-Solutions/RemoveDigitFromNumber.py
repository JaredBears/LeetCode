class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        answers = []
        for i in range(len(number)):
            if number[i] == digit:
                num = int(number[:i] + number[i+1:])
                answers.append(num)
        return str(max(answers))
