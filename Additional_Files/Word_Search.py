'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

'''
def Word_Search(board, word):
    # Dimensions of the board
    rows, cols = len(board), len(board[0])
    
    # Helper function for backtracking DFS
    def dfs(r, c, i, visited):
        # Base case: if we have matched the entire word
        if i == len(word):
            return True
        
        # Check for boundary conditions and if the current cell matches the word's character
        if (r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i] or (r, c) in visited):
            return False
        
        # Add the current cell to the visited set
        visited.add((r, c))
        
        # Explore neighbors (up, down, left, right)
        res = (dfs(r+1, c, i+1, visited) or  # Down
               dfs(r-1, c, i+1, visited) or  # Up
               dfs(r, c+1, i+1, visited) or  # Right
               dfs(r, c-1, i+1, visited))    # Left
        
        # Backtrack: Remove the cell from visited for other paths
        visited.remove((r, c))
        
        return res

    # Start DFS from each cell in the grid
    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0, set()):
                return True
    
    return False

# Example usage:
board = [
    ['a', 'b', 'c', 'e'],
    ['s', 'f', 'c', 's'],
    ['a', 'd', 'e', 'e']
]

word = "abcced"
print(Word_Search(board, word))  # Output: True
