'''
Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to gain weight, so she visited a doctor.
The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while still following the doctor's advice.
Given the integer array candyType of length n, return the maximum number of different types of candies she can eat if she only eats n / 2 of them.

Approach
1) Find the 1/2th length of the given list of candies
2) Generate a new iterable using set to store 1 instance of each type of candy
3) Find th minimum between both and return the minimum value


'''

class Solution(object):
    def distributeCandies(self, candyType):
        types_of_candies = len(set(candyType))
        max_possible_to_eat = len(candyType) // 2

        min_candies = min(max_possible_to_eat, types_of_candies)
        return min_candies
