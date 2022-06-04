class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        l = len(secret)
        a = 0
        b = 0
        secret = list(secret)
        guess = list(guess)
        for i in range(l):
            if secret[i]==guess[i]:
                secret[i]='#'
                guess[i]='#'
                a+=1
        sample = Counter(secret)
        for i in range(l):
            if guess[i] in sample and sample[guess[i]]>0 and guess[i]!='#':
                sample[guess[i]]-=1
                b+=1
        return f"{a}A{b}B"