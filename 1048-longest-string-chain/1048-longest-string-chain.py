class Solution:
    def longestStrChain(self, words: List[str]) -> int:     
        # define the dp with hash_map and initilize each word in words with possible longest string chain = 1 (itself)	
        dp = {}
        for word in words:
            if word not in dp:
                dp[word] = 1
        # sort the word and work from the shortest ones
        for word in sorted(words, key=len):
		    # get all possible substring (sub_word) of current word removing 1 letter
            for i in range(len(word)):
                s = word[:i] + word[i+1:]
				# if the sub_word in dp
                if s in dp:
                    dp[word] = max(dp[word], dp[s] + 1)
        return max(dp.values())