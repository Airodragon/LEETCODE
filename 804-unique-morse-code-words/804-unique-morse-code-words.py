class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        temp = {'a':".-",
         'b':"-...",
         'c':"-.-.",
         'd':"-..",
         'e':".",
         'f':"..-.",
         'g':"--.",
         'h':"....",
         'i':"..",
         'j':".---",
         'k':"-.-",
         'l':".-..",
         'm':"--",
         'n':"-.",
         'o':"---",
         'p':".--.",
         'q':"--.-",
         'r':".-.",
         's':"...",
         't':"-",
         'u':"..-",
         'v':"...-",
         'w':".--",
         'x':"-..-",
         'y':"-.--",
         'z':"--.."}
        x = []
        for i in words:
            temp2 = ""
            for j in i:
                temp2+=temp[j]
            x.append(temp2)
        count = 0
        freq = Counter(x)
        # freq = sorted(freq)
        # print(freq)
        return len(freq)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        