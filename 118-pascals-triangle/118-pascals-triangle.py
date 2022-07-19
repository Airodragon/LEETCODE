class Solution:
    def generate(self, n: int) -> List[List[int]]:
        ans = []
        for i in range(0,n):
            icj=1;
            x = []
            for j in range(0,i+1):
                x.append(int(icj))
                icj = (icj * (i - j)) / (j + 1);
            ans.append(x)
        return ans
            