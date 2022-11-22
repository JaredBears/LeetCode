class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0
        max_left = [height[0]] * len(height)
        max_right = [height[-1]] * len(height)
        for i in range(1, len(height)):
            max_left[i] = max(height[i], max_left[i-1])
            max_right[-(i+1)] = max(height[-(i+1)], max_right[-i])
        for i in range(len(height)):
            answer += min(max_left[i], max_right[i]) - height[i]
        return answer