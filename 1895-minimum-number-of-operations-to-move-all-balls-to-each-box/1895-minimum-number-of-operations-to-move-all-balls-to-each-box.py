class Solution(object):
    def minOperations(self, boxes):
        res = []
        n = len(boxes)

        if n == 0:
            return []

        for i in range(n):
            op = 0
            for j in range(n):
                if boxes[j] == '1':  
                    op += abs(i - j)
            res.append(op)

        return res
