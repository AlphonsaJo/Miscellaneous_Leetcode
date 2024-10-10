'''There is a hackathon organized by HackerRank which has 2 separate tracks, healthcare and e-commerce. For track 1, the
required team size is teamSize_1, while for track 2, the required team size is teamSize_2. The total number of participants is p.
Find the minimum number of teams into which the participants can be divided such that each participant belongs to exactly one team (either of track 1 or track 2), 
and each team has a size equal to either teamSize_1 or teamSize_2. If no division is possible, return -1.Tracks in HackathonThere is a hackathon organized by HackerRank 
which has 2 separate tracks, healthcare and e-commerce. For track 1, the required team size is teamSize_1, while for track 2, the required team size is teamSize_2. 
The total number of participants is p.Find the minimum number of teams into which the participants can be divided such that each participant belongs to exactly one
team (either of track 1 or track 2), and each team has a size equal to either teamSize_1 or teamSize_2. If no division is possible, return -1.
'''
def minimum_teams(p, teamSize_1, teamSize_2):
    # We're starting by forming as many teams of size 'teamSize_2' as possible.
    # The range() function will start at the maximum number of 'teamSize_2' teams that can be formed from 'p' participants.
    # It works by doing an integer division 'p // teamSize_2', which gives how many full teams of 'teamSize_2' we can form.
    # The loop will then try to reduce the number of 'teamSize_2' teams one by one (decreasing step), down to 0 teams.
    
    for teams2 in range(p // teamSize_2, -1, -1):
      '''
      range(p // teamSize_2, -1, -1): This means the loop will stop when teams2 reaches 0. The second -1 ensures the loop decreases step by step.
      '''
        # Now we calculate how many participants are left after forming 'teams2' teams of size 'teamSize_2'.
        # This is done by subtracting the participants used by the 'teamSize_2' teams from the total participants 'p'.
        # The total participants used by 'teams2' is teams2 * teamSize_2.
        remaining_participants = p - teams2 * teamSize_2
        
        # After forming the 'teams2' teams, we check if the remaining participants can be divided into full teams of size 'teamSize_1'.
        # This is done by checking if 'remaining_participants' is perfectly divisible by 'teamSize_1'.
        # The '%' (modulus) operator checks if there is no remainder when dividing by 'teamSize_1'.
        if remaining_participants % teamSize_1 == 0:
            # If the remaining participants can be divided into full teams of size 'teamSize_1', calculate how many such teams we can form.
            # This is done by integer division: 'remaining_participants // teamSize_1'.
            teams1 = remaining_participants // teamSize_1
            
            # Once we have both the number of 'teamSize_1' and 'teamSize_2' teams, return the total number of teams.
            # The total number of teams is simply the sum of 'teams1' and 'teams2'.
            return teams1 + teams2
    
    # If the loop finishes without finding a valid way to form all participants into teams, return -1.
    # This means it's not possible to divide the participants into teams with the given team sizes.
    return -1

# Example usage:
# Let's say we have 10 participants and we want to form teams of size 3 or 4.
# We can try to form as many teams of size 4 as possible, then see if the remaining participants can be grouped into teams of size 3.
p = 10
teamSize_1 = 3
teamSize_2 = 4
result = minimum_teams(p, teamSize_1, teamSize_2)
print(result)  # Output: 3 (2 teams of 3 and 1 team of 4)


