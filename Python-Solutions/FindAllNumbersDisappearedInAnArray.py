# Runtime: 759 ms, faster than 59.98% of Python3 online submissions for Find All
# Numbers Disappeared in an Array.
# Memory Usage: 26.2 MB, less than 15.77% of Python3 online submissions for Find
# All Numbers Disappeared in an Array.

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        answer = set(range(1, len(nums) + 1))
        for num in nums:
            if num in answer:
                answer.remove(num)
        return answer
