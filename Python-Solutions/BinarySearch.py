class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def helper(start, end):
            mid = start + (end - start)//2
            if start > end:
                return -1
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                return helper(start, mid-1)
            return helper(mid+1, end)
        return helper(0, len(nums) - 1)
