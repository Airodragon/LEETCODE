class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a = s[:len(s)//2]
        b = s[len(s)//2:]
        a_v = 0
        b_v = 0
        for i in a:
            i = i.lower()
            if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
                a_v +=1
        for i in b:
            i = i.lower()
            if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
                b_v +=1
        return a_v == b_v
    