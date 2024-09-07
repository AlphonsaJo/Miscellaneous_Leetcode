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
STDIN Function'''

def numPlayers(k, scores):
    # Sort the scores in descending order
    scores.sort(reverse=True)
    
    # Initialize variables
    rank = 0
    num_level_up = 0
    previous_score = -1
    same_rank_count = 0
    
    for i, score in enumerate(scores):
        if score == 0:
            break  # No players with score 0 can level up
        
        # Only increment rank when score changes
        if score != previous_score:
            rank = i + 1
        
        # Check if the rank is within the top k
        if rank <= k:
            num_level_up += 1
        else:
            break  # No need to continue if rank exceeds k
        
        previous_score = score
    
    return num_level_up

# Sample input
n = 4
k = 3
scores = [100, 50, 50, 25]
result = numPlayers(k, scores)
print(result)  # Output: 3



