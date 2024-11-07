class Solution(object):
    def uniqueOccurrences(self, arr):
        unique_arr = set(arr)
        n = len(arr)-1
        occur = []
        for i in unique_arr:
            count_i = arr.count(i)
            occur.append(count_i)   

        return len(occur) == len(set(occur))
        