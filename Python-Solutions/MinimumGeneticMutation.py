class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        q = deque([(start, 0)])
        seen = {start}

        while q:
            node, steps = q.popleft()
            if node == end:
                return steps
            for c in "ACGT":
                for i in range(len(node)):
                    if node[i] != c:
                        neighbor = node[:i] + c + node[i+1:]
                        if neighbor not in seen and neighbor in bank:
                            q.append((neighbor, steps+1))
                            seen.add(neighbor)

        return -1
