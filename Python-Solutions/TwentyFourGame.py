class Solution(object):
    def judgePoint24(self, cards):
        """
        :type cards: List[int]
        :rtype: bool
        """
        def generateResults(a, b):
            res = [a + b, a - b, b - a, a * b]
            if a:
                res.append(b/a)
            if b:
                res.append(a/b)
            return res

        def checkResults(cards):
            if len(cards) == 1:
                return abs(cards[0] - 24) <= 0.1
            for i in range(len(cards)):
                for j in range(i+1, len(cards)):
                    newList = [number for k, number in enumerate(cards) if (k != i and k != j)]
                    for res in generateResults(float(cards[i]), float(cards[j])):
                        newList.append(res)
                        if checkResults(newList):
                            return True
                        newList.pop()
            return False
        return checkResults(cards)
