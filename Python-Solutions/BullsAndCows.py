from collections import defaultdict
class Solution:
    # We can solve this problem using two passes over the strings.  In the first pass, 
    # we check for the number of bulls. If a character is not a bull, we add it to a
    # dictionary and increment it's count, and then add it to a list of unmatched characters.
    # In the second pass, we check through all of the unmatched characters in the guess.
    # If the character is in the dictionary, we increment the number of cows and decrement
    # the count in the dictionary.  We then return the number of bulls and cows.
    # Time Complexity: O(N) where N is the length of the strings
    # Space Complexity: O(N)
    def getHint(self, secret: str, guess: str) -> str:
        N = len(secret)
        count = defaultdict(int)
        cows = 0
        bulls = 0
        unmatched = []
        for i in range(N):
            a = secret[i]
            b = guess[i]
            if a == b:
                bulls += 1
            else:
                count[a] += 1
                unmatched.append(i)
        for i in unmatched:
            b = guess[i]
            if count[b] > 0:
                cows += 1
                count[b] -= 1
        return "{}A{}B".format(bulls,cows)