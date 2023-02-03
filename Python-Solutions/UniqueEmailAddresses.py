from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        validEmails = set()
        for email in emails:
            spl = email.split("@")
            if len(spl) > 2: continue
            try:
                local = spl[0].split("+")[0]
            except:
                local = spl[0]
            local = local.replace(".", "")
            domain = spl[1]
            validEmails.add((local, domain))
        return len(validEmails)
            