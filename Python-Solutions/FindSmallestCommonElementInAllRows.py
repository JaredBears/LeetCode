class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        for i in range(len(mat[0])):
            num = mat[0][i]
            for j in range(1, len(mat)):
                if num not in mat[j]:
                    break
                if j == len(mat) - 1:
                    return num
        return -1
