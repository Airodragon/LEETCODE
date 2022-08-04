class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dic = {i:0 for i in 'balloon'}
        for i in text:
            if i in dic:
                dic[i] += 1
        l1 = [(dic['b'],1),(dic['a'],1),(dic['l'],2),(dic['o'],2),(dic['n'],1)]
        l2 = list(map(lambda x:x[0]//x[1],l1))
        return min(l2)