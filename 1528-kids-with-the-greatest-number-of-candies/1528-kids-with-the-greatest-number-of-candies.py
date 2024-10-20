class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        bool_list = []
        max_candies = max(candies)
        n = len(candies)
        for i in range(0, n):
            if candies[i] + extraCandies >= max_candies:
                bool_list.append(True)
            else:
                bool_list.append(False)
        return bool_list
            