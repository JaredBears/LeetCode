from typing import List

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # We will use a dictionary to map the values of nums2 to their indices. 
    # We will then iterate through nums1 and return a list of the matching indices of nums2.
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapper = {x: i for i, x in enumerate(nums2)}
        return [mapper[nums1[i]] for i in range(len(nums1))]


    # Time Complexity: O(n^2) where n is the length of the arrays
    # Space Complexity: O(n)
    # We will use a set to store the indices of nums2.  
    # We will iterate through nums1 and for each element, we will iterate through the set.
    # If the element in nums1 is equal to the element in nums2, we will remove the index from the set.
    # We will then add the index to the output list in the ith position.
    # We will return the output list.
    def oldAnagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        N = len(nums1)
        output = [0] * N
        index = set(range(N))
        for i in range(N):
            for j in list(index):
                if nums1[i] == nums2[j]:
                    index.remove(j)
                    output[i] = j
                    break
        return output