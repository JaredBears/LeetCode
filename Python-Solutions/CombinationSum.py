class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        answer = []
        candidates.sort()
        def checkSums(target, index=0, path = []):
            if target < 0:
                return
            elif target == 0:
                answer.append(path)
                return
            for i in range(index, len(candidates)):
                checkSums(target - candidates[i], i, path+[candidates[i]])
        checkSums(target)
        return answer
