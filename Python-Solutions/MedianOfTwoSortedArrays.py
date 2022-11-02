class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        answer = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                answer.append(nums1[i])
                i += 1
            else:
                answer.append(nums2[j])
                j += 1
        if i < len(nums1):
            answer.extend(nums1[i:])
        elif j < len(nums2):
            answer.extend(nums2[j:])
        if len(answer) % 2 == 0:
            return (answer[(len(answer)//2)] + answer[(len(answer)//2) - 1])/2
        else:
            return answer[(len(answer)//2)]
