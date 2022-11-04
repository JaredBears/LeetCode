class Solution:
    # brute force, times out for longer entries. O(n^3) where n is the number
    # of elements
    def longestPalindromeNaive(self, words: List[str]) -> int:
        palindromeLength = 0
        single = False #keeps track of if there's a single palindrome in the list
        while words: # O(n)
            curr = words.pop()
            reverse = curr[::-1]  # all words are same length, so constant O(2)
            if reverse in words: #slow! nested O(n)
                palindromeLength += 4
                words.remove(reverse) #slow! double nested O(n)
            elif curr == reverse and not single:
                palindromeLength += 2
                single = True
        return palindromeLength

    #Much faster, works in all cases. O(n)
    def longestPalindrome(self, words: List[str]) -> int:
        d = Counter(words) # builds a hashmap/dictionary of counts, O(n)
        palindromeLength = 0
        single = False
        for word in d: # O(n), but not nested
            reverse = word[::-1]
            if word == reverse:
                if d[word] % 2 == 0:
                    palindromeLength += 2 * d[word]
                else:
                    palindromeLength += 2 * (d[word] - 1)
                    single = True
            elif word[0] < word[1]: # only runs for the first half of the palin.
                                    # ("cl" will run but not "lc")
                palindromeLength += 4 * min(d[word], d[reverse])
        if single:
            palindromeLength += 2
        return palindromeLength
