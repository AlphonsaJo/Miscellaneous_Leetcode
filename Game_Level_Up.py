'''
A group of friends are playing a video game together. During the game, each player earns a number of points. At the end of a round, players
who achieve at least a certain rank get to "level up" their characters to gain increased abilities. Given the scores of the players at the end of a
round, how many players will be able to level up?

Note: Players with equal scores will have equal ranks, but the player with the next lower score will be ranked based on the position within the
list of all players' scores. For example, if there are four players, and three players tie for first place, their ranks are 1, 1, 1, and 4.
Note:  No player with a score of 0 can level up, regardless of rank.


Example
n = 4
k = 3
scores = [100, 50, 50, 25]
These players' ranks are [1, 2, 2, 4]. Because the players need to have a rank of at least 3 to level up, only the first three players qualify.
Therefore, the answer is 3.

 ## Function Description
Complete the function numPlayers in the editor below.
numPlayers has the following parameters:
    int k: an integer denoting the cutoff rank for leveling up a player's character
    int scores[n]: an array of integers denoting the scores of the players
Returns:
    int: the number of players who can level up after this round
Constraints
1 ≤ n ≤ 105
0 ≤ scores[i] ≤ 100
k ≤ n
Input Format For Custom Testing
Sample Case 0
Sample Input
STDIN Function
'''

def numPlayers(k, scores):
    # Sort the scores in descending order to rank players based on their scores.
    # Players with higher scores will be ranked first.
    scores.sort(reverse=True)

    # Initialize variables:
    # 'rank' will hold the current rank of players as we iterate through the scores.
    # 'num_level_up' will keep track of how many players can level up (i.e., are within the top k ranks).
    # 'previous_score' is used to compare the current player's score with the previous one, to manage rank ties.
    # We set 'previous_score' to -1 initially, which ensures it's different from any actual score.
    # 'same_rank_count' is used to count how many players have the same rank when there's a tie (optional, not used here).
    rank = 0
    num_level_up = 0
    previous_score = -1
    same_rank_count = 0
    
    # Loop through the list of scores, using 'enumerate' to get both the index 'i' and the corresponding 'score'.
    for i, score in enumerate(scores):
        # If the score is 0, break the loop, as players with a score of 0 cannot level up.
        if score == 0:
            break
        
        # Check if the current score is different from the previous score.
        # If it is, increment the rank. The rank is set to 'i + 1' because the index 'i' is 0-based.
        # This ensures that the first player gets rank 1, the second gets rank 2, and so on.
        if score != previous_score:
            rank = i + 1
        
        # If the current rank is less than or equal to 'k', this player qualifies for leveling up.
        # We increment the count of players who can level up.
        if rank <= k:
            num_level_up += 1
        else:
            # If the current rank exceeds 'k', we stop the loop because players ranked lower than 'k'
            # do not qualify for leveling up. There's no need to continue checking further.
            break
        
        # Update the 'previous_score' to the current score to handle the next iteration.
        previous_score = score
    
    # Return the total number of players who can level up.
    return num_level_up

# Sample input:
n = 4  # Total number of players
k = 3  # Players who need to be ranked in the top 'k' to level up
scores = [100, 50, 50, 25]  # List of player scores

# Call the function and store the result
result = numPlayers(k, scores)

# Print the result (which in this case should be 3, because the first 3 players can level up)
print(result)  # Output: 3



