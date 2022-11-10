class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        last = False
        zero = False
        for i in nums:
            if abs(i) == len(nums):
                last = True
            else:
                nums[abs(i)] = -1 * nums[abs(i)]
        if not last:
            return len(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                return i
            if nums[i] == 0:
                zero = i
        return zero
