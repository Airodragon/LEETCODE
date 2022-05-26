class Solution:
    def hammingWeight(self, n: int) -> int:
        # print(n)
        n = "{0:b}".format(int(n))
        # print(n)
        return n.count('1')