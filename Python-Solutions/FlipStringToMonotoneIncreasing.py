from collections import Counter
class Solution:
    # This is a greedy problem. 
    # First, use a Counter() map to obtain the number of Os and 1s present in 
    # the string and initialize the answer to the count of 0s.
    # Then, use a for loop to iterate through the string.
    # At each character, check if it's a zero. If it is, simulate changing it to 
    # a zero. If it is not, simulate changing it to a one. At each step, reset 
    # the answer to the minimum of the current answer, or the current count of "0s"
    def minFlipsMonoIncr(self, s: str) -> int:
        count = Counter(s)
        answer = count["0"]
        for char in s:
            if char == "0":
                count["0"] -= 1
            else:
                count["0"] += 1
            answer = min(answer, count["0"])

        return answer