class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ds = {}
        dt = {}
        for i in range(len(s)):
            if s[i] in ds:
                if t[i] != ds[s[i]]:
                    return False
            elif t[i] in dt:
                if s[i] != dt[t[i]]:
                    return False
            else:
                ds[s[i]] = t[i]
                dt[t[i]] = s[i]
        return True
