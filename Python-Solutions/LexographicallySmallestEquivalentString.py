class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # We will create a dictionary to hold the equivalency of each letter.
        # Initially, each letter will be equivvalent to itself.
        dictNode = {chr(ord('a') + i) : chr(ord('a') + i) for i in range(26)}
        n = len(s1)
        # We will iterate through the strings and update the equivalency of each letter.
        # We will use a for loop to iterate through the alphabet, and then a nested for loop
        # to iterate through the strings.
        for k in range(26):
            for i in range(n):
                if(dictNode[s2[i]] < dictNode[s1[i]]):
                    dictNode[s1[i]] = dictNode[s2[i]]
                if(dictNode[s1[i]] < dictNode[s2[i]]):
                    dictNode[s2[i]] = dictNode[s1[i]]
        output = []
        for s in baseStr:
            output.append(dictNode[s])
        return ''.join(output) 