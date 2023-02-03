from collections import defaultdict
from typing import List

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_counter = defaultdict(int)
        for entry in cpdomains:
            split_entry = entry.split(" ")
            domain_split = split_entry[1].split(".")
            count = int(split_entry[0])
            for i in range(len(domain_split)):
                domain = ".".join(domain_split[i:])
                domain_counter[domain] += count
        return [str(count) + " " + domain for domain, count in domain_counter.items()]