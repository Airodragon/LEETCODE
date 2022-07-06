class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        temp = 0
        for i in operations:
            if '--' in i:
                temp-=1
            if '++' in i:
                temp+=1
        return temp