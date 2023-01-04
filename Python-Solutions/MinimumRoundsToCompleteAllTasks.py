from typing import List
from collections import Counter
from math import ceil

class Solution:
    # Use a counter to count the number of times each task appears.  If a task appears
    # only once, then it is impossible to complete all tasks.  Otherwise, the number of
    # rounds is the number of times a task appears divided by 3, rounded up.

    def minimumRounds(self, tasks: List[int]) -> int:
        task_count = Counter(tasks)
        rounds = 0
        for task in task_count:
            count = task_count[task]
            if count == 1:
                return -1
            # -(count // -3) is the same as ceil(count / 3) but more precise
            rounds += -(count // -3)
        return rounds