class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combos = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        answers = []
        if len(digits) == 0: return []
        def helper(idx, word = ""):
            if idx >= len(digits):
                answers.append("".join(word))
                return
            n = int(digits[idx])
            if n < 2:
                helper(idx + 1, word)
            else:
                for c in combos[n]:
                    helper(idx + 1, word + c)
        helper(0)
        return answers
