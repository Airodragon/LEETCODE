class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        l = len(secret)
        a,b = 0,0
        secret,guess = list(secret),list(guess)
        for i in range(l):
            if secret[i]==guess[i]:
                secret[i],guess[i]='#','#'
                a+=1
        secret = Counter(secret)
        for i in range(l):
            if guess[i] in secret and secret[guess[i]]>0 and guess[i]!='#':
                secret[guess[i]]-=1
                b+=1
        return f"{a}A{b}B"