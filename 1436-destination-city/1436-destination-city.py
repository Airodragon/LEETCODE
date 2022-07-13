class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dic = dict()
        for i in paths:
            dic[i[0]] = i[1]
        initial_city = paths[0][0]
        while 1:
            try:
                final_city = dic[initial_city]
                initial_city = final_city
            except:
                break
        return final_city