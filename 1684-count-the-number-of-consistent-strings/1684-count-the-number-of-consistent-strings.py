class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        count_keys = Counter(allowed).keys()
        for i in words:
            check =  all(item in count_keys for item in Counter(i).keys())
            if i in allowed or check:
                count+=1
        return count
            
                