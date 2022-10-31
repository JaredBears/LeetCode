class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            answer[i] = answer[i-1] + nums[i]
        return answer
