class Solution:
    def numUniqueEmails(self, email: List[str]) -> int:
        a = []
        for emails in email:
            idx = emails.index("@")
            local_name = emails[:idx]
            domain_name = emails[idx:]
            local_name = local_name.replace(".","")
            if '+' in local_name:
                temp = local_name.index("+")
                local_name = local_name[:temp]
            final_email = local_name+domain_name
            if final_email not in a:
                a.append(final_email)
        return len(a)