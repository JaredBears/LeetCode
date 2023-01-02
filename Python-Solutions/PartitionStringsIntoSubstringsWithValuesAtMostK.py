class Solution:
    # Time Limit Exceeded
    def minimumPartition(self, s: str, k: int) -> int:
        left = 0
        right = 1
        subs = set()
        while right < len(s) + 1:
            if int(s[left:right]) <= k:
                right += 1
            else:
                subs.add(s[left:right -1])
                left = right - 1
        if int(s[left:right]) <= k:
            subs.add(s[left:right])
        if subs:
            print(subs)
            return len(subs)
        return -1