class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        freq = []
        mod = 10**9 + 7
        for i in arr:
            freq.append([i,1])
        for i in range(1,len(freq)):
            total = freq[i][1]
            for j in range(0,i):
                if freq[i][0]%freq[j][0]==0 and freq[i][0]//freq[j][0] in arr:
                    index = arr.index(freq[i][0]//freq[j][0])
                    total+= (freq[j][1] * freq[index][1])%mod
            freq[i][1] = total%mod
        ans = 0
        for i,j in freq:
            ans+=j
        return ans%mod