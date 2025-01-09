class Solution(object):
    def countPrefixSuffixPairs(self, words):
        count = 0
        n = len(words)


        def isboth(str1, str2):
            return str2.startswith(str1) and str2.endswith(str1)

        for i in range(n):
            for j in range(i+1, n): # j is always j<i so no repetition
                if isboth(words[i], words[j]):
                    count+=1
        
        return count

            
        