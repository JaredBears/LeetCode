class Solution:
    def reverseVowelsOriginal(self, s: str) -> str:
        vowels = set(['a','e','i', 'o', 'u','A','E','I','O','U'])
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] in vowels and s[j] in vowels:
                s = s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
                i += 1
                j -= 1
                continue
            if s[i] not in vowels:
                i += 1
            if s[j] not in vowels:
                j -= 1
        return s

    def reverseVowelsImproved(self, s: str) -> str:
        vowels = set(['a','e','i', 'o', 'u','A','E','I','O','U'])
        ls = [*s]
        i = 0
        j = len(ls) - 1
        while i < j:
            if ls[i] in vowels and ls[j] in vowels:
                ls[i], ls[j] = ls[j], ls[i]
                i += 1
                j -= 1
            else:
                if ls[i] not in vowels:
                    i += 1
                if ls[j] not in vowels:
                    j -= 1
        return "".join(ls)