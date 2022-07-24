class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'}':'{',']':'[',')':'('}
        stack = []
        for i in s:
            if i=='(' or i=='[' or i=='{':
                stack.append(i)
            elif stack and dic[i]==stack[-1]:
                stack.pop()
            else:
                return False
        return len(stack)==0
                
                
                