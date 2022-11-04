class Solution:
    def average(self, salary: List[int]) -> float:
        maxim = 1000
        minum = 1000000
        summed = 0
        for s in salary:
            minum = min(minum, s)
            maxim = max(maxim, s)
            summed += s
        summed -= maxim + minum
        return summed / (len(salary) - 2)
