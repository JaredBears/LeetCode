from typing import List

class Solution:
    # In order to solve the max subarray, we will use Kadane's algorithm.
    # Kadane's algorithm works by keeping track of the current subarray and the max subarray.
    # We can initialize the current subarray and max subarray to the first element in the array.
    # We can then iterate through the array starting at the second element.  We can update the current
    # subarray by taking the max of the current element and the current element plus the current subarray.
    # In other words, if the current element is greater than the current subarray plus the current element,
    # we reset the subarray to the current element.  If the current element is less than the current subarray
    # plus the current element, we add the current element to the current subarray. 
    # We can then update the max subarray by taking the max of the current subarray and the max subarray.
    # We can then return the max subarray.
    # Time Complexity: O(n) where n is the length of the array
    # Space Complexity: O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        current_subarray = max_subarray = nums[0]
        for num in nums[1:]:
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)
        return max_subarray

    # This is a variation of the max subarray problem.  In this problem, the array is circular.  This means
    # that the problem can be split into two parts.  The first part is the normal max subarray problem.  The
    # second part requires us to calculate the prefix/head sum and the suffix/tail sum.  We can do this by
    # iterating through the array from the beginning and the end.  We can then calculate the prefix sum and
    # suffix sum.  We can then iterate through the array again and calculate the special sum.  The special sum
    # is the prefix sum plus the suffix sum.  We can then return the max of the normal max subarray and the
    # special sum.
    # Time Complexity: O(n) where n is the length of the array
    # Space Complexity: O(n)
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        N = len(nums)
        normal = self.maxSubArray(nums)
        right_max = [0] * N
        suffix_sum = right_max[-1] = nums[-1]
        for i in range(N-2, -1, -1):
            suffix_sum += nums[i]
            right_max[i] = max(suffix_sum, right_max[i+1])
        special_sum = nums[0]
        prefix_sum = 0
        for i in range(0, N-2):
            prefix_sum += nums[i]
            special_sum = max(special_sum, prefix_sum + right_max[i+1])
        return max(normal, special_sum)
        