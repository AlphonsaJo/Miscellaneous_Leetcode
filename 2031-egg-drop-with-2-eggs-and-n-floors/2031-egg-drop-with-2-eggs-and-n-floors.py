class Solution(object):
    def twoEggDrop(self, n):
    
        moves = 0
        current_sum = 0
        
        while current_sum < n:
            moves += 1
            current_sum += moves
        
        return moves
