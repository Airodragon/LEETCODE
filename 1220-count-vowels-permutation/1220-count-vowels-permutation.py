class Solution:
    def countVowelPermutation(self, n: int) -> int:
        arr = [ [], [1,1,1,1,1] ]
        mod = (10**9 + 7)
        a,e,i,o,u = 0,1,2,3,4
        i = 2
        while i<=n:
            temp = [0]*5
            temp[0] = arr[i-1][1]%mod
            temp[1] = (arr[i-1][0] + arr[i-1][2])%mod
            temp[2] = (arr[i-1][0] + arr[i-1][1] + arr[i-1][3] + arr[i-1][4])%mod
            temp[3] = (arr[i-1][2] + arr[i-1][4])%mod
            temp[4] = (arr[i-1][0])%mod
            arr.append(temp)
            i+=1
        return sum(arr[-1])%mod