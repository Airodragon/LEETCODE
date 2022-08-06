class Solution:
    def poorPigs(self, buckets: int, mD: int, mT: int) -> int:
        pigs = 0
        while (mT/ mD + 1) ** pigs < buckets:
            pigs +=1
        return pigs